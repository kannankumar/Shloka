# Create your views here.
from django.template import RequestContext, Context, loader
from django.http import HttpResponse,HttpResponseNotFound
from pro_scheduler.models import process_question
from django.shortcuts import render_to_response
from subjects.models import subject

def set_scheduling_question(request,questionid):
        question = process_question.objects.get(id=questionid);
        sub = subject.objects.all();
        t = loader.get_template('process_scheduling.html');
        c = RequestContext(request, #we use RequestContext to automagically prevent CSRF
        {
             'question':question,
	     'subject':sub
        }
        );
        return HttpResponse(t.render(c));



