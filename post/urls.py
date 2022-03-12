from django.urls import path
from .views import PostCRUD, PostView

urlpatterns = [
  path('', PostView.as_view()),
  path('<int:pk>/', PostCRUD.as_view()),
]