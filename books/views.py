import datetime
import random

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models

def book_detail_view(request, id):
    if request.method == 'GET':
        bl_id = get_object_or_404(models.book, id=id)
        return render(
            request,
            template_name='book/book_detail.html',
            context={
                'book_id': bl_id,
            }
        )

def book_list_view(request):
    if request.method == 'GET':
        queryset = models.Book_list.objects.filter().order_by('-id')
        return render(
            request,
            template_name='book/book_list.html',
            context={
                'bl': queryset
            }
        )



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



