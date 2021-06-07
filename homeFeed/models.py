import datetime

from django.db import models

class Question(models.Model):
    question_name = models.CharField(max_length=100)
    def __str__(self):
        return "Question " + self.question_name

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_content = models.CharField(max_length=1000)
    def __str__(self):
        return "Answer " + self.answer_content

