from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from post.forms import postForm
from post.models import post
from chat.models import Chat
from chat.forms import ChatForm


# Create your views here.

def index(request):
    if request.user.is_authenticated():
        user_home = request.user.username," WELCOME PAGE"
        return render (request, 'homesite/main_account.html',{"title":"Homepage","error":""})
    else :
        user_home = "WELCOME PAGE"
        return render (request, 'homesite/home.html',{"title":user_home,"error":""})


def register(request):
    if request.user.is_authenticated():
        account = request.user.username
        return render (request, 'homesite/main_account.html',{"title": account})
    else :
        return render (request, 'homesite/register.html')

@login_required
def list_post(request):
    show_post = post.objects.filter(user=request.user)
    return render(request,"homesite/list_post.html",{"title":"Your Categories","post":show_post})

@login_required
def list_all(request):
    show_post = post.objects.all()
    return render(request,"homesite/list_all.html",{"title":"All Categories","post":show_post})

@login_required
def add_post(request):
    mess = ""
    if request.method == "POST" :
        mess = "Invalid Input"
        form = postForm(request.POST)
        if form.is_valid():
            mess = "created successfully"
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
    return render(request,"homesite/add_post.html",{"title":"Add channel","message":mess})


@login_required
def chat(request):
     mess = ""
     if request.method == "POST" :
        mess = "Invalid Input"
        form = ChatForm(request.POST)
        if form.is_valid():
            mess = "created successfully"
            instance = form.save(commit = False)
            instance.user = request.user
            instance.post_id = request.POST["channel"]
            instance.save()
     return render(request, "homesite/chat.html", {"title": "Post to channel", "message": mess,"channel":post.objects.all()})

@login_required
def chatChannel(request,channelId):
     mess = ""
     channel = post.objects.get(id=channelId)
     listChat = Chat.objects.filter(post=channel)
     if request.method == "POST" :
        mess = "Invalid Input"
        form = ChatForm(request.POST)
        if form.is_valid():
            mess = "Post successfully"
            instance = form.save(commit = False)
            instance.user = request.user
            instance.post_id = request.POST["channel"]
            instance.save()
     return render(request, "homesite/channel_room.html", {"title": channel.channelname, "message": mess,"chat":listChat, "chanId":channelId})

