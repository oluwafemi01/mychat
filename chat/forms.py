from django import forms
from .models import Chat
from django.contrib.auth.models import User


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = [
            'chatmessage'
        ]

    def clean_chatmessage(self):
        chatmessage = self.cleaned_data.get('chatmessage')
        return chatmessage