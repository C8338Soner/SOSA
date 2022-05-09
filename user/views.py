from user.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer, PublicUserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from .permissions import IsAddedByUser

class UserView(APIView):
  def get(self, request):
    if request.user.is_staff:
      users=User.objects.all()
      serializer=PublicUserSerializer(users, many=True)
      return Response(serializer.data)
    return Response(status=status.HTTP_403_FORBIDDEN)

  def post(self,request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():

      # hash password manually
      password=serializer.validated_data.get('password')
      serializer.validated_data['password']=make_password(password)

      # token for new user
      user= serializer.save()
      token, _=Token.objects.get_or_create(user=user)
      data =serializer.data
      data['token']=token.key
      return Response(data)
    else:
      return Response(serializer.errors)

@api_view(['POST'])
def logout_view(request):
 if request.method == 'POST':
  request.user.auth_token.delete()
  data = {
   'message': 'logout successful!'
  }
  return Response(data)

class UserCRUD(APIView):
  permission_classes = [IsAddedByUser]
  
  def get_object(self, pk):
    return get_object_or_404(User, pk=pk)

  def get(self, request, pk):
    user=self.get_object(pk)
    serializer=UserSerializer(user)
    return Response(serializer.data)

  def put(self, request, pk):
    user=self.get_object(pk)
    serializer=UserSerializer(user, data=request.data)
    if serializer.is_valid():
      password=serializer.validated_data.get('password')
      serializer.validated_data['password']=make_password(password)
      serializer.save()
      serializer.data["success"]="User successfully updated"
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    user=self.get_object(pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)