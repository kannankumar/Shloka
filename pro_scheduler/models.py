from django.db import models

#Create your models here.
class process_question(models.Model):
	TECHNIQUE_CHOICES = (('SJF','Shortest Job First'),('FCFS','First Come First Serve'));
	name = models.CharField('Question',max_length=400,help_text='The unique name of the question',unique=True);
        process1 = models.IntegerField('Process 1',help_text='The burst time for process 1');
        process2 = models.IntegerField('Process 2',help_text='The burst time for process 2');
        process3 = models.IntegerField('Process 3',help_text='The burst time for process 3');
        technique = models.CharField('Scheduling technique',max_length=50,choices=TECHNIQUE_CHOICES);

        def __unicode__(self):
                return self.name;

