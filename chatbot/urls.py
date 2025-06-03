from django.urls import path
from .views import chat_view, ask_gpt

urlpatterns = [
    path('', chat_view, name='chat'),
    path('ask/', ask_gpt, name='ask_gpt'),
]
