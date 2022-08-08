from django.urls import path

from chat import views

urlpatterns = [
    path('chat_messages/<int:chat_id>', views.GetAllChatMessages.as_view()),
    path('send_message_to_chat/<int:chat_id>', views.SendMessageToChat.as_view()),
    ]