from django.template import RequestContext, Context, loader
from django.http import HttpResponse,HttpResponseNotFound
from subjects.models import subject, chapter, resource
from django.shortcuts import render_to_response
def home_page(request):
	hello="Hello World!"
        sub = subject.objects.all();
	t = loader.get_template('home.html');
        c = RequestContext(request,
	{
	     'subject':sub,
	     'hello':hello
	});
        return HttpResponse(t.render(c));

def gate_page(request,gate):
        sub = subject.objects.all();
	t = loader.get_template(gate + '.html');
	c = RequestContext(request,
	{
	     'subject':sub,
	     'gate':gate
	});
	return HttpResponse(t.render(c));


def show_all_quiz(request):
        sub = subject.objects.all();
        t = loader.get_template('quiz.html');
        c = RequestContext(request,
        {
             'subject':sub
        });
        return HttpResponse(t.render(c));

def show_all_video(request):
        sub = subject.objects.all();
        t = loader.get_template('video.html');
        c = RequestContext(request,
        {
             'subject':sub
        });
        return HttpResponse(t.render(c));

def show_process_states(request):
        sub = subject.objects.all();
        t = loader.get_template('interactive_process_states.html');
        c = RequestContext(request,
        {
             'subject':sub
        });
        return HttpResponse(t.render(c));



def hello(request):
        t = loader.get_template('quizzydeo.html');
        c = RequestContext(request, #we use RequestContext to automagically prevent CSRF
	{
             'timestops':timestops
	}	
	);
	return HttpResponse(t.render(c));

#	return render_to_response('quizzydeo.html',{'timestops':timestops})



