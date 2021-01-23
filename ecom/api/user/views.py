from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
import re
import random
# Create your views here.


def generate_session_token(lenght = 10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)]+[str(i) for i in range(10)]) for _ in range(lenght))

def singin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'send a post request'})