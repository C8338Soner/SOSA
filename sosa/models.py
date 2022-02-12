from django.db import models
from django.contrib.auth.models import User
from post.models import Post


# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300)
    
    def __str__(self):
        return f'commentator {self.user} - post '  
    
class DirectMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    message = models.CharField(max_length=250, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'sender {self.sender} - recipient- message {self.message}'