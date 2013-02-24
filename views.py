from django.template import RequestContext, Context, loader
from django.http import HttpResponse,HttpResponseNotFound

from django.shortcuts import render_to_response

def hello(request):
	quiz=[{
		id:1,
		'url':'https://youtube.com',
		'source':'Youtube',
		'name':'FlipFlops'
		},
		{
		id:2,
		'url':'https://popcorn.com',
                'source':'PopCorn',
                'name':'Transistors'
		}]
	timestops = [{
		'time':2,
		'question':"Whats my name?",
		'options':["Kanan","Canon","Nikon","Kannan"],
		'answer':"Kannan",
		'extra':'Additional info goes here'
		},
		{
		'time':4,
                'question':'Where do i stay?',
                'options':['Mumbai','Delhi','Pune','Kolkata'],
                'answer':"Pune",
                'extra':'Extra info goes here'
		}
]
        t = loader.get_template('quizzydeo.html');
        c = RequestContext(request, #we use RequestContext to automagically prevent CSRF
	{
             'timestops':timestops
	}	
	);
	return HttpResponse(t.render(c));

#	return render_to_response('quizzydeo.html',{'timestops':timestops})



