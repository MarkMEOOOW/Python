from django.shortcuts import render, redirect
from markapp.models import Food, Consume
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, 'index.html')


def say_hello(request):
    return HttpResponse('Привет, Мир!')
