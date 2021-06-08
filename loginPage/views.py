from django.shortcuts import render
from django.contrib.auth import authenticate, login
from homeFeed.views import homeFeedView

def loginPageView(request):
    return render(request,'loginPage.html')

def loginUser(request):
    typed_username = request.POST['username']
    typed_password = request.POST['password']
    user = authenticate(request,username=typed_username,password=typed_password)
    if user is not None:
        login(request,user)
        return homeFeedView(request)
    else:
        invalid_credentials = True
        return render(request,'loginPage.html',{'invalid_credentials':invalid_credentials})



