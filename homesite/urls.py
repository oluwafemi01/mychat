"""seed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views
app_name = "homesite"
urlpatterns = [
    
    url(r'^$', views.index, name = 'home'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^add/$', views.add_post, name = 'addPost'),
    url(r'^list/$', views.list_post, name = 'listPost'),
    url(r'^list_all/$', views.list_all, name = 'listAll'),
    url(r'^chat/$', views.chat, name = 'chat'),
    url(r'^channel/(\d+)/$', views.chatChannel, name = 'chat'),
]

