from django.db import models

class subject(models.Model):
        name = models.CharField('Subject Name',max_length=100,help_text='The subject name in full');
        code = models.CharField('Subject Code',max_length=200,help_text='The lowercase code of the subject -Example: Subject code for Digital Electronics will be de',unique=True);

        def __unicode__(self):
                return u'%s %s' %(self.code, self.name);

class chapter(models.Model):
        number = models.IntegerField('Chapter Number',help_text='Chapter number starting from 1');
       	name = models.CharField('Chapter Name',max_length=100,help_text='Chapter name in full');
        subject = models.ForeignKey(subject);
        description = models.CharField('Description',max_length=500,help_text='The description of the details of this chapter aka syllabus');

        def __unicode__(self):
                return u'%s : %d - %s' %(self.subject.code, self.number, self.name);

class resource(models.Model):
	name = models.CharField('Resource Name',max_length=100, help_text='Name of resource to display');
	url = models.CharField("URL of Resource",max_length=500, help_text='As of now you have to provide relative address of HTML file/ controller address');
	subject = models.ForeignKey(subject);
	chapter = models.ForeignKey(chapter);

	def __unicode__(self):
		return u'%s: %d %s' %(self.subject.code, self.chapter.number, self.name);

# Create your models here.
