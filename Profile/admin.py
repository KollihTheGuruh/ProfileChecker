from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_url')
 
    
# Register your models here.
admin.site.register(models.User, UserAdmin)
