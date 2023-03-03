from flask import Flask
from flask import request
from flask import jsonify
from django.shortcuts import render
from django.http import *
from .models import *
from .forms import *
from beauty.templates import *
import requests
import re
import telegram
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.conf import settings


my_token = '6164077746:AAGg1iQrX9zGh3wNZZPbTKGkV7pTbBxkveU'
my_chat_id = '197670320'
URL = 'https://api.telegram.org/bot' + my_token + '/'


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj,dict):
            return str(obj)
        return super().default(obj)

def send_message(chat_id, text = 'ну ты чел'):
    url = URL + 'sendMessage'
    answer = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.post(url, json=answer)
    return r.json()

def home(request):
    send_message(my_chat_id, text = 'Привет')
    return render(request,'home.html')