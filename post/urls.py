from django.urls import path
from .views import PostCRUD, PostView, PostLike, PostSave

urlpatterns = [
  path('', PostView.as_view()),
  path('<int:pk>/', PostCRUD.as_view()),
  path('<int:pk>/like/', PostLike, name="like"),
  path('<int:pk>/save/', PostSave, name="save"),
]