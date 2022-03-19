from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
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

    #increase view
    post.views=post.views+1
    post.save()

    # add post to user history
    if request.user.is_authenticated:
      request.user.history.add(post)
 
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

@api_view(['POST'])
def get_object(self, pk):
  return get_object_or_404(Post, pk=pk)

def PostSave(request, pk):
  if request.method=='POST' and request.user.is_authenticated:
    post = get_object(pk)
    try:
      request.user.saved_posts.get(post)
      request.user.saved_posts.remove(post)
      return Response(data="Post Unsaved")
    except:
      request.user.saved_posts.add(post)
      return Response(data="Post Saved")

def PostLike(request, pk):
  if request.method=='POST' and request.user.is_authenticated:
    post = get_object(pk)
    try:
      post.likes.get(request.user)
      post.likes.remove(request.user)
      return Response(data="Like Removed")
    except:
      request.user.saved_posts.add(post)
      return Response(data="Like Added")