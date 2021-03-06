from django.urls import path

from . import views

app_name = 'homeFeed'
urlpatterns = [
    path('', views.homeFeedView, name='homeFeedView'),
    path('addQuestion/', views.addQuestion, name='addQuestion'),
    path('answerFeedView/<int:question_id>', views.answerFeedView,name='addAnswer')
]