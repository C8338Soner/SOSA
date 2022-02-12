from django.urls import path
from .views import PostCRUD, PostView

urlpatterns = [
  path('posts/', PostView.as_view()),
  path('posts/<int:pk>/', PostCRUD.as_view()),
]