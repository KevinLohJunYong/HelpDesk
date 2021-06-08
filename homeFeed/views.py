import datetime
from django.http import HttpResponse, HttpResponseRedirect,Http404
from .models import Question, Answer
from django.shortcuts import render
from django.contrib import messages

def homeFeedView(request):
    all_questions = Question.objects.all()
    return render(request,'homeFeed.html',{'all_questions_list':all_questions})

def addQuestion(request):
    new_question = Question(question_name=request.POST['question_name'])
    new_question.save()
    return HttpResponseRedirect('/homeFeed/')

def answerFeedView(request,question_id):
    corresponding_question = Question.objects.get(id=question_id)
    new_answer = Answer(answer_content=request.POST['answer_content'],question=corresponding_question)
    new_answer.save()
    all_answers_for_question = Answer.objects.filter(question=corresponding_question)
    return render(request,
                  'answerFeed.html',
                  {'all_answers_for_question':all_answers_for_question,'question':Question.objects.get(id=question_id)}
                  )