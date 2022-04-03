from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserView, logout_view, UserCRUD

urlpatterns = [
 path('login/', obtain_auth_token, name='login'),
 path('register/', UserView.as_view()),
 path('<int:pk>/', UserCRUD.as_view()),
 path('logout/', logout_view, name='logout'),
]