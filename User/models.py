from django.db import models
from django.contrib.auth.models import User

class BaseUser(models.Model):
    base_user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.TextField()
    password = models.TextField()
    points = models.IntegerField(default=0)
    upvoted_by_users_set = {}

    def manage_upvote(self,upvoted_by_username,answer_id):
       self.points = self.points + 1
       upvoted_hash = "upvoted by: " + upvoted_by_username + " with answer_id: " + answer_id
       if upvoted_hash not in self.upvoted_by_users_set:
           self.upvoted_by_users_set.add(upvoted_hash)
           self.points += 1

