from django.contrib import admin
from .models import Comment , DirectMessage

# Register your models here.
admin.site.register(Comment)
admin.site.register(DirectMessage)