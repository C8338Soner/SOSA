from user.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers

class PublicUserSerializer(serializers.ModelSerializer):
 class Meta:
  model = User
  exclude = ['password', 'first_name', 'last_name', 'last_login']

class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = User
  fields = '__all__'
  
class TokenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Token
    fields = ['user']
