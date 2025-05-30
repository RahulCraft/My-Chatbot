# from django.db import models

# # Create your models here.

# class ChatMessage(models.Model):
#     user_message = models.TextField()
#     bot_response = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user_message[:30]}... -> {self.bot_response[:30]}..."

# This code defines a Django model for storing chat messages in a MongoDB database using MongoEngine.
from mongoengine import Document, StringField, DateTimeField
import datetime

class ChatbotApp(Document):
    user_message = StringField(required=True)
    bot_response = StringField(required=True)
    timestamp = DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return f"{self.user_message[:30]}... -> {self.bot_response[:30]}..."

