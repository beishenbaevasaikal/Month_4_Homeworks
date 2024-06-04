import datetime
import random

from django.http import HttpResponse
from django.shortcuts import render

def myself_view(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовут Сайкал, моя фамилия Бейшенбаева. Мне 30 лет')

def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('В данный момент мое хобби - это изучение языков программирования')

def get_current_time_view(request):
    if request.method == 'GET':
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return HttpResponse(f'Текущее время: {current_time}')

def random_number_view(request):
    if request.method == 'GET':
        random_number = random.randint(1, 100)
        return HttpResponse(f'Случайное число: {random_number}')



