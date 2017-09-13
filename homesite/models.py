from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def upload_location(user,filename):
    return "%s/%s" %(user.username,filename)

class Userprofile(models.Model):
    user = models.OneToOneField(User)
    #image = models.ImageField(upload_to =upload_location,null = True,blank = True)
    city = models.CharField(max_length=20)
    def __str__(self):
        return self.user.username
