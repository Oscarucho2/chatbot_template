from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .gpt_client import ask_gpt_api

def chat_view(request):
    return render(request, '../chatbot/templates/chatbot/chat.html')

def ask_gpt(request):
    if request.method == 'POST':
        user_input = request.POST.get('message', '')
        response = ask_gpt_api(user_input)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)