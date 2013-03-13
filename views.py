from django.template import RequestContext, Context, loader
from django.http import HttpResponse,HttpResponseNotFound

from django.shortcuts import render_to_response
def home_page(request):
	hello="Hello World!"
        t = loader.get_template('home.html');
        c = RequestContext(request,
	{
	     'hello':hello
	});
        return HttpResponse(t.render(c));

def subject_page(request,subject_code):
        t = loader.get_template(subject_code + '.html');
        c = RequestContext(request,
        {
             'subject':subject_code
        });
        return HttpResponse(t.render(c));

def gate_page(request,gate):
	t = loader.get_template(gate + '.html');
	c = RequestContext(request,
	{
		'gate':gate
	});
	return HttpResponse(t.render(c));

def and_gate(request):
	gate ="and"
        t = loader.get_template('and.html');
        c = RequestContext(request,
        {
             'gate':gate
        });
        return HttpResponse(t.render(c));

def or_gate(request):
        gate ="or"
        t = loader.get_template('or.html');
        c = RequestContext(request,
        {
             'gate':gate
        });
        return HttpResponse(t.render(c));

def not_gate(request):
        gate ="not"
        t = loader.get_template('not.html');
        c = RequestContext(request,
        {
             'gate':gate
        });
        return HttpResponse(t.render(c));

def xor_gate(request):
        gate ="xor"
        t = loader.get_template('xor.html');
        c = RequestContext(request,
        {
             'gate':gate
        });
        return HttpResponse(t.render(c));



def show_all_quiz(request):
	username="xyz"
        t = loader.get_template('quiz.html');
        c = RequestContext(request,
        {
             'username':username
        });
        return HttpResponse(t.render(c));

def show_all_video(request):
	username="xyz"
        t = loader.get_template('video.html');
        c = RequestContext(request,
        {
             'username':username
        });
        return HttpResponse(t.render(c));

def show_process_states(request):
        username="xyz"
        t = loader.get_template('interactive_process_states.html');
        c = RequestContext(request,
        {
             'username':username
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



