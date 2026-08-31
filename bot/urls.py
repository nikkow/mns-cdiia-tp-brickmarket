from django.urls import path
from . import views

app_name = "bot"

urlpatterns = [
  path('', views.bot_view, name="view"),
  path('send', views.bot_action, name="send")
]