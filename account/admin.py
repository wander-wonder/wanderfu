from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    list_filter = ("phone",)



admin.site.register(UserProfile, UserProileAdmin)