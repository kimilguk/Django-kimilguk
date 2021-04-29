from django.db import models
from django.utils import timezone
import datetime

class Career(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images')
    post = models.CharField(max_length=500)
    career_date = models.DateField('Career_Date')
    pub_date = models.DateTimeField('date published')
    #votes = models.IntegerField(default=0)
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
    	return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Award(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50)
	award_date = models.DateField('Award_Date')
	pub_date = models.DateTimeField('date published')