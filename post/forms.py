from django import forms
from .models import post
from django.contrib.auth.models import User

class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = [
                'channelname'
            ]
        
