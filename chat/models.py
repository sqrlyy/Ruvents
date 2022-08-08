from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Chat(models.Model):
    first_user = models.IntegerField()
    second_user = models.IntegerField()


class ChatMessage(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    message_object = GenericForeignKey('content_type', 'object_id')


class AbstractMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    sender = models.IntegerField()
    receiver = models.IntegerField()
    sended_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    chat_message = GenericRelation(ChatMessage)

    class Meta:
        abstract = True


class TextMessage(AbstractMessage):
    text = models.CharField(max_length=255)


class ImageMessage(AbstractMessage):
    image = models.ImageField()






