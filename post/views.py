from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import PostSerializer,PostSerializerAll
from .models import Post
from rest_framework import status
from rest_framework.response import Response

class PostView(APIView):

  def get(self, request):
    post=Post.objects.all().filter(status="2")
    if request.user.is_authenticated:
      draft=Post.objects.all().filter(publisher=request.user).filter(status="1")
      post = post | draft
    serializer=PostSerializer(post, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self,request):
    if request.user.is_authenticated:
      serializer = PostSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save(publisher=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

class PostCRUD(APIView):
  permission_classes = [IsAuthenticated]

  def get_object(self, pk):
    return get_object_or_404(Post, pk=pk)

  def get(self, request, pk):
    post=self.get_object(pk)
    if post.status == "1" and request.user == post.publisher.id:
      serializer=PostSerializerAll(post)
      return Response(serializer.data)
    return Response(status=status.HTTP_403_FORBIDDEN)

  def put(self, request, pk):
    post=self.get_object(pk)
    if request.user == post.publisher.id:
      serializer=PostSerializerAll(instance=post, data=request.data)
      if serializer.is_valid():
        post.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

  def delete(self, request, pk):
    post=self.get_object(pk)
    if request.user == post.publisher.id:
      post.delete()
      return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_401_UNAUTHORIZED)