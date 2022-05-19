from django.db import models

#FUNCTIONS
def deleted_user():
  from user.models import User #circular import avoided
  return User.objects.get_or_create(username="Deleted", is_active=False, id=0)[0]

#MODELS
class Post(models.Model):
  title=models.CharField(max_length=100)
  content=models.TextField(max_length=100000)
  image=models.URLField(blank=True, null=True, max_length=10000) 
  post_date=models.DateTimeField(auto_now_add=True)
  views=models.IntegerField(default=0)
  likes=models.ManyToManyField('user.User', blank=True, related_name='post_likes')
  publisher = models.ForeignKey('user.User',on_delete=models.SET_DEFAULT, default=deleted_user, related_name='post_publisher')
  status=models.CharField(max_length=30, 
    choices=(("draft","Draft"),("published","Published")),default=("draft","Draft"))

  def __str__(self):
    return f"{self.title} -- id: {self.id}"