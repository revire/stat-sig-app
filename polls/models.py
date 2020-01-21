from django.db import models
import datetime
from django.utils import timezone



class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Data(models.Model):
    def __str__(self):
        return self.post
    post = models.CharField(max_length=500)


class DataFile(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='')
    pub_date = models.DateTimeField(auto_now_add=True)


