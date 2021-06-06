import datetime

from django.db import models

class Question(models.Model):
    question_name = models.CharField(max_length=100)
    created_at = models.DateTimeField('date published')
    def __str__(self):
        return "Question " + self.question_name + " is created at " + self.created_at

class Answer(models.Model):
    answer_content = models.CharField(max_length=1000)
    created_at = models.DateTimeField('date published')
    def __str__(self):
        return "Answer " + self.answer_content + " is created at " + self.created_at
