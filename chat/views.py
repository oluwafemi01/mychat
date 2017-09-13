from django.shortcuts import render
from .models import Chat
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatSerializer
# Create your views here.

class ChatListView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDetailView(generics.RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
