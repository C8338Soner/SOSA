from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import PostSerializer, ImageSerializer
from .models import Post, Image
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
      #DATA 1 -> URLs
      for i in list(request.data[1].values())[0]:
        serializer = ImageSerializer(data={"URL": str(i)})
        if serializer.is_valid(): serializer.save()
        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      #DATA 0 -> Serializer
      serializer = PostSerializer(data=request.data[0])
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
    image = Image.objects.filter(id__in=post.images.all()) # use .all() to open QuerySet
    images = list(map(lambda img: {f'img {img.id}': f'{img}'}, image))

    # if draft doesn't belong to request.user
    if post.status == "draft" and request.user != post.publisher and not request.user.is_staff:
      return Response(status=status.HTTP_403_FORBIDDEN)

    post.views=post.views+1
    if request.user.is_authenticated:
      request.user.history.add(post)
    post.save()

    serializer=PostSerializer(post)
    return Response(data=[serializer.data, {"URLs": images}])

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
def PostSave(request, pk):
  if request.method=='POST' and request.user.is_authenticated:
    post = get_object_or_404(Post, pk=pk)
    try:
      request.user.saved_posts.get(id = post.id)
      request.user.saved_posts.remove(post)
      return Response(data={"message": "Post Unsaved"})
    except:
      request.user.saved_posts.add(post)
      return Response(data={"message": "Post Saved"})
  else:
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def PostLike(request, pk):
  if request.method=='POST' and request.user.is_authenticated:
    post = get_object_or_404(Post, pk=pk)
    try:
      post.likes.get(id=request.user.id)
      post.likes.remove(request.user)
      return Response(data={"message": "Like Deleted"})
    except:
      post.likes.add(request.user)
      return Response(data={"message": "Like Added"})
  else:
    return Response(status=status.HTTP_401_UNAUTHORIZED)