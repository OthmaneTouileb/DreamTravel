from django.apps import AppConfig


# chatapp/apps.py
from django.apps import AppConfig

class ChatAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatapp'
