from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
    user_follow = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    user_followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
