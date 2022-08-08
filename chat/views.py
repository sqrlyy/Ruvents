import json

from django.contrib.contenttypes.models import ContentType
from rest_framework import views, status
from rest_framework.response import Response

from chat.models import ChatMessage, TextMessage, Chat
from chat.serializers import ChatMessagesSerializer, TextMessageSerializer, ImageMessageSerializer


class GetAllChatMessages(views.APIView):

    def get(self, request, chat_id):
        qs = ChatMessage.objects.filter(chat_id=chat_id)
        serializer = ChatMessagesSerializer(qs, many=True)
        data = {
            'chat_id': chat_id,
            'chat_messages': serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )


class SendMessageToChat(views.APIView):
    def get_serializer_class(self, type):
        serializers = {
            'TextMessage': TextMessageSerializer,
            'ImageMessage': ImageMessageSerializer
        }
        return serializers.get(type, None)

    def post(self, request, chat_id):
        message_type = request.query_params.get('type')
        message_serializer = self.get_serializer_class(message_type)
        message = message_serializer(data=request.data)
        message.is_valid(raise_exception=True)
        chat_message = ChatMessage(message_object=message.save(), chat_id=Chat.objects.get(id=chat_id))
        chat_message.save()
        return Response(status=status.HTTP_200_OK)
