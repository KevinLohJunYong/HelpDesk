from django.db import models
from django.contrib.auth.models import User
from homeFeed.models import Question, Answer

class BaseUser(models.Model):
    base_user = models.OneToOneField(User,on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
