from django.db import models
from subjects.models import subject, chapter
# Create your models here.
class quiz(models.Model):
	name = models.CharField('Quiz Name',max_length=100,help_text='An identifier for internal usage',unique=True);
        text = models.CharField('Quiz Text',max_length=200,help_text='The actual name of the quiz');
	url = models.URLField("URL of Video",help_text='The url link for the video');
	source = models.CharField("Source of Video",max_length=40,choices =());
	#subject = models.CharField('Subject',max_length=100,choices=());
        subject = models.ForeignKey(subject);
        chapter = models.ForeignKey(chapter);

	def __unicode__(self):
		return self.name;

class timestop(models.Model):
	time = models.DecimalField('Time to stop for Pop-Quiz',max_digits=5,decimal_places=2,help_text='Add time stop in mm.ss format');
        question = models.CharField('Question',max_length=500,help_text='The question to be asked at this timestop');
	option1 = models.CharField('Option 1',max_length=300,help_text='1st option for the question at this timestop');
	option2 = models.CharField('Option 2',max_length=300,help_text='2nd option for the question at this timestop');
	option3 = models.CharField('Option 3',max_length=300,help_text='3rd option for the question at this timestop');
	option4 = models.CharField('Option 4',max_length=300,help_text='4th option for the question at this timestop');
	answer = models.CharField('Answer',max_length=300,help_text='The correct option form the choices');
	explanation = models.CharField('Explanation',max_length=500,help_text='The footnote explanation for the particular answer');
	quiz = models.ForeignKey(quiz);
	
	def __unicode__(self):
		return u'%s %s' %(self.time, self.question);

