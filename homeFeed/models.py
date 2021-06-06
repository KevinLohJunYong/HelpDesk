import datetime

from django.db import models

class Question(models.Model):
    question_name = models.CharField(max_length=100)
    def __str__(self):
        return "Question " + self.question_name

