from django.contrib import admin
from .models import Userprofile

class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = Userprofile
        
admin.site.register(Userprofile,profileAdmin)

# Register your models here.

