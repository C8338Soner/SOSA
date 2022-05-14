from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import RegistrationSerializer , UserSerializer , TokenSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Create your views here.
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
         password = serializer.validated_data.get('password')
         serializer.validated_data['password'] = make_password(password)         
         user = serializer.save()
         token, _  = Token.objects.get_or_create(user=user)               
         data = serializer.data
         data['token'] = token.key
        else:
            data = serializer.errors
        return Response(data)
@api_view(['POST'])
def logout_view(request):
 if request.method == 'POST':
  request.user.auth_token.delete()
  data = {
   'message': 'logout'
  }
  
  return Response(data)
@api_view(['GET'])
def allUsers(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def currentuser(request,token):
    if request.method == 'GET':
        user = Token.objects.filter(key=token)
        print(user)
        serialzer = TokenSerializer(user,many=True)
        return Response(serialzer.data)

