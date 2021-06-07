import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answer
from django.shortcuts import render

def homeFeedView(request):
    all_questions = Question.objects.all()
    return render(request,'homeFeed.html',{'all_questions_list':all_questions})

def addQuestion(request):
    new_question = Question(question_name=request.POST['question_name'])
    new_question.save()
    return HttpResponseRedirect('/homeFeed/')

def answerFeedView(request,question_id):
    try:
        all_answers_for_question = Answer.objects.get(id=question_id)
    except Answer.DoesNotExist:
        all_answers_for_question = None
    return render(request,'answerFeed.html',{'all_answers_for_question':all_answers_for_question})