from django.shortcuts import render, redirect
from ollama import chat, ChatResponse

def bot_view(request):
  conversation = request.session.get('conversation', [])
  conversation = [msg for msg in conversation if msg['role'] != 'system']

  return render(request, 'bot/conversation.html', {'conversation': conversation})

def bot_action(request):
  conversation = request.session.get('conversation')
  if not conversation:
    conversation = [{
      "role": "system",
      "content": "Tu es un bot d'aide sur une boutique LEGO. Tu t'appelles BrickBot. réponds de façon CONCISE mais FRIENDLY à l'utilisateur uniquement sur le thème des LEGO et refuse la question s'il dévie de ce thème. Ta réponse devra être en texte brut, sans AUCUN formatage."
    }] # Liste qui va contenir les échanges bot<>user

  user_request = request.POST.get("prompt", "").strip()
  if not user_request:
    return redirect("bot:view")

  user_prompt = {
    "role": "user",
    "content": user_request
  }

  conversation.append(user_prompt)

  response: ChatResponse = chat(
    model='gemma3:4b',
    messages=conversation
  )

  request.session['conversation'] = conversation + [{
    "role": "assistant",
    "content": response.message.content
  }]

  return redirect("bot:view")
  