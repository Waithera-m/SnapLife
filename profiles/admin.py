from django.contrib import admin
from .models import Profile, Image

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    fields = ['image_name', 'image_caption', 'profile', 'likes', 'comments']
    list_display = ('image_name', 'pub_date')
    list_filter = ['pub_date']

admin.site.register(Profile)
admin.site.register(Image, ImageAdmin)
