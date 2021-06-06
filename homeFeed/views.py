import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answer
from django.shortcuts import render

def homeFeedView(request):
    return render(request,'homeFeed.html')

def addQuestion(request):
    new_question = Question(question_name = request.POST['question_name'],created_at = datetime.now())
    new_question.save()
    return HttpResponseRedirect('/homeFeed/')

def addAnswer(request):
    new_answer = Answer(answer_content = request.POST['answer_content'],created_at = datetime.now())
    new_answer.save()
    return HttpResponseRedirect('/homeFeed/')