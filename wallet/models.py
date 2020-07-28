from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    portfolio = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add = True,editable=True)
    joker = models.CharField(max_length=100,blank = True)
    def __str__(self):
        return self.user.username
