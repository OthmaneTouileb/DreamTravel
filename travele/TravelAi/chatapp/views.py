from multiprocessing import context
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import ChatBot
from userauths.models import User  # Import the custom User model
import google.generativeai as genai

# Set up API key
genai.configure(api_key="YOUR_API_KEY_HERE")  # Replace "YOUR_API_KEY_HERE" with your actual API key

# Model configuration
generation_config = {
    "temperature": 0.7,  # Adjust temperature based on desired response creativity
    "max_tokens": 150,  # Limit response length
    "top_p": 0.9,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

system_instruction = "You are a chatbot for a travel agency in Morocco. You provide recommendations."

# Instantiate the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=system_instruction,
    safety_settings=safety_settings
)

@login_required

def ask_question(request):
    if request.method == "POST":
        text = request.POST.get("text")
        response = model.start_chat().send_message(text)
        user = request.user
        ChatBot.objects.create(text_input=text, gemini_output=response.text, user=user)
        response_data = {"text": response.text}
        return render(request, 'chatbot.html', context)
    else:
        return HttpResponseRedirect(reverse("chat"))

@login_required
def chat(request):
    user = request.user
    chats = ChatBot.objects.filter(user=user)
    return render(request, "chatdossier/chatbot.html", {"chats": chats})
