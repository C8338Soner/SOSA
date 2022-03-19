from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from user.models import User
from rest_framework import status
from rest_framework.response import Response

class PostView(APIView):

  def get(self, request):
    post=Post.objects.filter(status="published")
    if request.user.is_authenticated:
      draft=Post.objects.filter(publisher=request.user).filter(status="draft")
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

  def get_object(self, pk):
    return get_object_or_404(Post, pk=pk)

  def get(self, request, pk):
    post=self.get_object(pk)

    # if draft doesn't belong to request.user
    if post.status == "draft" and request.user != post.publisher and not request.user.is_staff:
      return Response(status=status.HTTP_403_FORBIDDEN)
    
    # add post to user history
    
    serializer=PostSerializer(post)
    return Response(serializer.data)
    

  def put(self, request, pk):
    post=self.get_object(pk)
    if request.user == post.publisher.id and request.user.is_authenticated or request.user.is_staff:
      serializer=PostSerializer(instance=post, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

  def delete(self, request, pk):
    post=self.get_object(pk)
    if request.user == post.publisher.id and request.user.is_authenticated or request.user.is_staff:
      post.delete()
      return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_401_UNAUTHORIZED)