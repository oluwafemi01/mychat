
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views
app_name = "chat"
urlpatterns = [
    url(r'^chatlistview/$', views.ChatListView.as_view(), name="chatList"),
    url(r'^chatlistview/(?P<pk>\d+)/$', views.ChatDetailView.as_view(), name="ChatDetails"),
]

urlpatterns = format_suffix_patterns(urlpatterns)