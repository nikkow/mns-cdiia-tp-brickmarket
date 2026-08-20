from django.shortcuts import render

def bot_view(request):
  return render(request, 'bot/conversation.html')