from django.db import models
from django.conf import settings

class ChatBot(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Using settings.AUTH_USER_MODEL instead of direct reference
        on_delete=models.CASCADE, 
        related_name="chatbots", 
        null=True
    )
    text_input = models.CharField(max_length=500)
    gemini_output = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_input
