from rest_framework import serializers
from .models import Post, Image

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model=Image
    fields='__all__'
    
class PostSerializer(serializers.ModelSerializer):
  images=ImageSerializer(read_only=True, many=True)
  class Meta:
    model=Post
    fields='__all__'
