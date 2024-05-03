from django.contrib import admin
from .models import ChatBot

# Register your models here.

@admin.register(ChatBot)
class ChatBotAdmin(admin.ModelAdmin):
    list_display = ('text_input', 'gemini_output', 'user', 'date')
    search_fields = ('text_input', 'gemini_output', 'user__username')  # Add user__username to search by username
    list_filter = ('user', 'date')
