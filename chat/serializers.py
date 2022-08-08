from generic_relations.relations import GenericRelatedField
from rest_framework import serializers

from chat.models import TextMessage, ImageMessage, ChatMessage


class TextMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextMessage
        fields = '__all__'


class ImageMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageMessage
        fields = '__all__'


class ChatMessagesSerializer(serializers.ModelSerializer):
    message_object = GenericRelatedField({
        TextMessage: TextMessageSerializer(),
        ImageMessage: ImageMessageSerializer()
    })

    class Meta:
        model = ChatMessage
        fields = ('message_object', )
