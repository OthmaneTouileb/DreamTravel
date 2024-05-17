from multiprocessing import context
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .models import ChatBot
from userauths.models import User  # Import the custom User model
import google.generativeai as genai

# Set up API key
genai.configure(api_key="AIzaSyDe_DLQj_7YuKzw8mB7siAJSzcWvLmIiws")  # Replace with your actual API key

# Model configuration
generation_config = {
    "temperature": 0.7,  # Adjust temperature based on desired response creativity
    "top_p": 0.9,
    # Removed "max_tokens" since it was causing issues
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
Model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=system_instruction,
    safety_settings=safety_settings
)

@login_required
def ask_question(request):
    if request.method == "POST":
        text = request.POST.get("text")
        try:
            chat = Model.start_chat()
            response = chat.send_message(text)
            
            user = request.user
            ChatBot.objects.create(text_input=text, gemini_output=response.text, user=user)
            response_data = {"text": response.text}
            return JsonResponse({"response": response_data})
        except Exception as e:
            # Log the error for debugging purposes
            print(f"Error: {e}")
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponseRedirect(reverse("chat"))

@login_required
def chat(request):
    user = request.user
    chats = ChatBot.objects.filter(user=user)
    return render(request, "chatdossier/chatbot.html", {"chats": chats})
