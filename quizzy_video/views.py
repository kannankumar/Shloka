# Create your views here.
from django.template import RequestContext, Context, loader
from django.http import HttpResponse,HttpResponseNotFound
from quizzy_video.models import quiz,timestop
from django.shortcuts import render_to_response

def quizzy_video(request,quizid):
	q = quiz.objects.get(id=quizid);
	timestops = timestop.objects.filter(quiz=q);
	video_url = q.url;
        t = loader.get_template('quizzydeo.html');
        c = RequestContext(request, #we use RequestContext to automagically prevent CSRF
        {
	     'videourl':video_url,
             'timestops':timestops
        }
        );
        return HttpResponse(t.render(c));



