"""qawebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homeFeed.views import homeFeedView,addQuestion,addAnswer,answerFeedView,logoutUser
from signUpFeed.views import signUpFeedView,createUser
from loginPage.views import loginPageView,loginUser
from leaderBoard.views import leaderBoardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homeFeed/',homeFeedView),
    path('addQuestion/',addQuestion),
    path('addAnswer/<int:question_id>',addAnswer),
    path('answerFeedView/<int:question_id>',answerFeedView),
    path('signUp/',signUpFeedView),
    path('createUser/',createUser),
    path('login/',loginPageView),
    path('loginUser/',loginUser),
    path('logoutUser/',logoutUser),
    path('leaderBoard/',leaderBoardView)
]
