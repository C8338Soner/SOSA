from rest_framework import serializers
from .models import Comment, DirectMessage

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    post = serializers.StringRelatedField()
    post_id = serializers.IntegerField()
    class Meta:
        model = Comment
        fields = ('id','user','user_id','post','post_id','time_stamp','content')

class DirectMessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    sender_id = serializers.IntegerField()
    recipient = serializers.StringRelatedField()
    recipient_id = serializers.IntegerField()
    class Meta:
        model = DirectMessage
        fields = ('id','sender','sender_id','recipient','recipient_id','message','time_stamp')
        
        
      