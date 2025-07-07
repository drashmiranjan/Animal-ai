from django.urls import path
from chat.views import *
urlpatterns = [
    path('', ChatForm, name='ChatForm'),
] 
