from django.contrib import admin
from .models import Comment , DirectMessage, Post
# Register your models here.
admin.site.register(Comment)
admin.site.register(DirectMessage)
admin.site.register(Post)