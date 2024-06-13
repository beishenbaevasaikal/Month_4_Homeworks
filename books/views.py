import datetime
import random

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

def edit_books_view(request, id):
    book_id = get_object_or_404(models.Book_list, id=id)
    if request.method == 'POST':
        form = forms.BooksForm(request.POST, instance=book_id)
        form.save()
        return HttpResponse('<h3>Book successfully edited!</h3>'
                            '<a href="/book/">Список книг</a>')
    else:
        form = forms.BooksForm(instance=book_id)
        return render(
            request,
            template_name='book/edit_books.html',
            context={'form': form,
                     'book_id': book_id
            }
        )

def drop_books_view(request, id):
    book_id = get_object_or_404(models.Book_list, id=id)
    book_id.delete()
    return HttpResponse('<h3>Book Deleted</h3>'
                        '<a href="/book/">Список книг</a>')

def create_book_view(request):
    if request.method == 'POST':
        form = forms.BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3> Book Created! </h3>'
                                '<a href="/book/">Список книг</a>')
    else:
        form = forms.BooksForm()
        return render(
            request,
            template_name='book/create_books.html',
            context={'form': form}
        )

def kids_tags_view(request):
    if request.method == 'GET':
        kids_tags = models.Types.objects.filter(tags__name='Детские книги').order_by('-id')
        return render(request,
                      template_name='types/kids_tags.html',
                      context={'kids_tags': kids_tags}
                      )

def fairy_tale_tags_view(request):
    if request.method == 'GET':
        fairy_tale_tags = models.Types.objects.filter(tags__name='Сказки').order_by('-id')
        return render(
            request,
            template_name='types/fairy_tale_tags.html',
            context={'fairy_tale_tags': fairy_tale_tags}
        )

def love_story_tags_view(request):
    if request.method == 'GET':
        love_story_tags = models.Types.objects.filter(tags__name='Любовная литература').order_by('-id')
        return render(
            request,
            template_name='types/love_story_tags.html',
            context={'love_story_tags': love_story_tags}
        )


def all_types(request):
    if request.method == 'GET':
        types = models.Types.objects.filter().order_by('-id')
        return render(
            request,
            template_name='types/all_types.html',
            context={
                'types': types
            }
        )

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book_list, id=id)
        return render(
            request,
            template_name='book/book_detail.html',
            context={
                'book_id': book_id,
            }
        )

def book_list_view(request):
    if request.method == 'GET':
        queryset = models.Book_list.objects.all().order_by('-id')
        return render(
            request,
            template_name='book/book_list.html',
            context={
                'book_list': queryset
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



