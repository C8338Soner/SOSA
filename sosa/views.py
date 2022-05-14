from django.core.checks import messages
from .serializers import CommentSerializer, DirectMessageSerializer
from .models import Comment , DirectMessage
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q

# Create your views here.
class CommentViews(APIView):
    
    def get(self, request , pk):
        comments = Comment.objects.filter(post_id=pk).order_by('-time_stamp')
        serializer = CommentSerializer(comments, many=True)
        print(request.user)
        return Response(serializer.data)
    
        # NOT -- Asagida get metodunu post gibi kullanarak, client tarafindan json data gönderdik. bunu request.data olarak kullandik. Bu datanin icindeki post_id kullanarak filtreleme yaptik. --
        # serializer = CommentSerializer(data=request.data)
        # id = request.data['post_id'] 
        # comments = Comment.objects.filter(post_id=id).order_by('-time_stamp')
        # serializer = CommentSerializer(comments, many=True)
        # return Response(serializer.data)
    
    def post(self,request,pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request ,pk):
        comment_item = Comment.objects.filter(id=pk)
        comment_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DirectMessageViews(APIView):
    
    def get(self, request , recipient_id, sender_id):
        if recipient_id==sender_id:
            # kendine kendisine mesaj atanlar icin. gönderici ve alici ayni olanlar
            messages = DirectMessage.objects.filter(sender_id=sender_id,recipient_id=sender_id).order_by('time_stamp')
            print("calisti")
        
        else:
            # Eger gönderici ve alici farkli ise bu kod calisir
            messages = DirectMessage.objects.filter((Q(recipient_id=recipient_id) | Q(recipient_id=sender_id)),(Q(sender_id=recipient_id) | Q(sender_id=sender_id))).exclude(sender_id=sender_id , recipient_id=sender_id).exclude(sender_id=recipient_id , recipient_id=recipient_id).order_by('time_stamp')
            print("else calisti")
        serializer = DirectMessageSerializer(messages, many=True)
        
        return Response(serializer.data)
    
    def post(self,request, recipient_id, sender_id):
        serializer = DirectMessageSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request ,recipient_id, sender_id):
        message_item = DirectMessage.objects.filter(id=sender_id)
        message_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      