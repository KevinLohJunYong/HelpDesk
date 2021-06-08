from django.shortcuts import render
from django.contrib.auth.models import User
from homeFeed.views import homeFeedView
from django.http import HttpResponse, HttpResponseRedirect,Http404

def signUpFeedView(request):
    return render(request,'signUpFeed.html')

def createUser(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    if password == confirm_password:
        user = User.objects.create_user(username,email,password)
        user.save()
        return homeFeedView(request)
    else:
        has_error = True
        return render(request,'signUpFeed.html',{'error':has_error})

