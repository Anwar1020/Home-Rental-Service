from django.contrib import admin
from .models import Profile, Post, PostAddress, PostDetail

admin.site.register(Profile)

admin.site.register(Post)
admin.site.register(PostAddress)
admin.site.register(PostDetail)
