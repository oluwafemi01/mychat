from django.db import models
from django.contrib.auth.models import User
from post.models import post

# Create your models here.
class Chat(models.Model):
    chatmessage = models.TextField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    chatdate = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.chatmessage

    class Meta:
        ordering = ["-chatdate"]
