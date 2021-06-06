from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def mainPageView(request):
    return render(request, 'mainPage.html')


