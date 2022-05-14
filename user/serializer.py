
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
 class Meta:
  model = User
  fields = ['username', 'email', 'password','first_name']
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name']
        
class TokenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Token
    fields = ['user']