from django.shortcuts import render
from User.models import BaseUser

def leaderBoardView(request):
    num_users = BaseUser.objects.all().count()
    usernames = []
    points = []
    for i in range(num_users):
      usernames.insert(len(usernames),BaseUser.objects.get(id=i+1).base_user.username)
      points.insert(len(points),BaseUser.objects.get(id=i+1).points)
    user_data = zip(usernames,points)
    return render(request,'leaderBoard.html',{'num_users':num_users,'user_data_list':user_data})
