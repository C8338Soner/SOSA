from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  title=models.CharField(max_length=100)
  content=models.TextField(max_length=100000)
  image=models.URLField(blank=True, null=True, max_length=10000) 
  post_date=models.DateTimeField(auto_now_add=True)
  views=models.IntegerField(default=0)
  likes=models.ManyToManyField(User, blank=True)
  publisher = models.ForeignKey(User,on_delete=models.SET_DEFAULT, default="Deleted", related_name="userNpost")
  status=models.CharField(max_length=30, choices=(("1","Draft"),("2","Published")),default=("1","Draft"))

  def __str__(self):
    return f"{self.title} -- id: {self.id}"