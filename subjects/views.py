# Create your views here.
from django.template import RequestContext, Context, loader
from django.http import HttpResponse,HttpResponseNotFound
from subjects.models import subject, chapter, resource
from quizzy_video.models import quiz
from django.shortcuts import render_to_response

def subject_page(request,subjectcode):
        thissubject = subject.objects.get(code=subjectcode);
        sub = subject.objects.all();
	chap = chapter.objects.all();
	res = resource.objects.filter(subject__code=subjectcode);
	q = quiz.objects.all();
        t = loader.get_template('subject.html');
        c = RequestContext(request, #we use RequestContext to automagically prevent CSRF
        {
             'subject':sub,
             'chapter':chap,
	     'thissubject':thissubject,
	     'resource':res,
	     'quiz':q
        }
        );
        return HttpResponse(t.render(c));



