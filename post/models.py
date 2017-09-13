from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    channelname = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    
    def __str__(self):
        return self.channelname

    class Meta:
        ordering = ["-updated"]
