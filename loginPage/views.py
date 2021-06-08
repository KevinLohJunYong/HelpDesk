from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.contrib.auth import authenticate

def loginPageView(request):
    return render(request,'loginPage.html')

def loginUser(request):
    typed_username = request.POST['username']
    typed_password = request.POST['password']
    user = authenticate(username=typed_username,password=typed_password)
    #to be done
    return render(request,'loginPage.html')



