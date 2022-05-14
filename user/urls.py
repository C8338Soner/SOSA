from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserView, logout_view, UserCRUD, currentUser

urlpatterns = [
 path('login/', obtain_auth_token, name='login'),
 path('register/', UserView.as_view()),
 path('<int:pk>/', UserCRUD.as_view()),
 path('logout/', logout_view, name='logout'),
 path('allusers/', allUsers, name='allusers'),
 path('currentuser/<str:token>', currentUser, name='currentuser'),
 
]