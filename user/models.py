from django.db import models
from django.contrib.auth.models import AbstractUser
from post.models import Post

class User(AbstractUser):
  profile_pic=models.URLField(max_length=1000, blank=True)
  date_joined = models.DateTimeField(auto_now_add=True)
  bio = models.TextField(max_length=2000, default="My bio")
  saved_posts = models.ManyToManyField(Post, blank=True, related_name='user_saved')
  history = models.ManyToManyField(Post, blank=True, related_name='user_history')

  def __str__(self):
    return f"{self.username} -- id: {self.id}"
