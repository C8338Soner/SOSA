from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import registration_view, logout_view , allUsers , currentuser

urlpatterns = [
 path('login/', obtain_auth_token, name='login'),
 path('register/', registration_view, name='register'),
 path('logout/', logout_view, name='logout'),
 path('allusers/', allUsers, name='allusers'),
 path('currentuser/<str:token>', currentuser, name='currentuser'),
 
]