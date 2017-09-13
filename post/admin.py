from django.contrib import admin
from .models import post

class postAdmin(admin.ModelAdmin):
    class Meta:
        model = post
        
admin.site.register(post,postAdmin)
