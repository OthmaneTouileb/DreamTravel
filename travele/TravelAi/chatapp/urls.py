from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('ask_question/', views.ask_question, name='ask_question'),
]
