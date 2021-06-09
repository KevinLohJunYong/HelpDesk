from django.db import models
from django.contrib.auth.models import User

class BaseUser(models.Model):
    base_user = models.OneToOneField(User,on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
