import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.shortcuts import render

def homeFeedView(request):
    all_questions = Question.objects.all()
    return render(request,'homeFeed.html',{'all_questions_list':all_questions})

def addQuestion(request):
    new_question = Question(question_name=request.POST['question_name'])
    new_question.save()
    return HttpResponseRedirect('/homeFeed/')
