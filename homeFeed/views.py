import datetime
from django.http import HttpResponse, HttpResponseRedirect,Http404
from .models import Question, Answer
from django.shortcuts import render
from django.contrib.auth import logout
from User.models import BaseUser

def isLoggedIn(request):
    return request.user.is_authenticated

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/login')

def homeFeedView(request):
    is_authenticated = False
    if isLoggedIn(request):
        is_authenticated = True
    all_questions = Question.objects.all()
    return render(request,'homeFeed.html',{'all_questions_list':all_questions,'is_authenticated':is_authenticated})

def addQuestion(request):
    if isLoggedIn(request):
      new_question = Question(question_name=request.POST['question_name'])
      new_question.save()
      return HttpResponseRedirect('/homeFeed/')
    else:
      is_authenticated = False
      is_question = True
      return render(request,'signUpFeed.html',{'is_authenticated':is_authenticated,'is_question':is_question})

def addAnswer(request,question_id):
    corresponding_question = Question.objects.get(id=question_id)
    answer_content = request.user.username + " replies: " + request.POST['answer_content']
    answer = Answer(question=corresponding_question,answer_content=answer_content)
    answer.save()
    return HttpResponseRedirect('/answerFeedView/%d' % question_id)

def answerFeedView(request,question_id):
    if isLoggedIn(request):
      corresponding_question = Question.objects.get(id=question_id)
      all_answers_for_question = Answer.objects.filter(question=corresponding_question)
      return render(request,
                  'answerFeed.html',
                  {'all_answers_for_question':all_answers_for_question,
                   'question':Question.objects.get(id=question_id),
                   }
                  )
    else:
        is_authenticated = False
        is_answer = True
        return render(request, 'answerFeed.html', {'is_authenticated': is_authenticated, 'is_question': is_answer})

def upvoteUser(request,username):
    base_user = BaseUser.objects.get(username=username)
    base_user.manage_upvote
