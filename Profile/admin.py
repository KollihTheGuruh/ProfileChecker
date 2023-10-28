from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_url')
 
class TraitAdmin(admin.ModelAdmin):
    list_display = ('height', 'age', 'gender', 'weight')
    
# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Trait, TraitAdmin)