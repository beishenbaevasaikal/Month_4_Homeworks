from django.urls import path
from books import views

urlpatterns = [
    path('kids/', views.kids_tags_view),
    path('fairy_tale/', views.fairy_tale_tags_view),
    path('love_story/', views.love_story_tags_view),
    path('all_types/', views.all_types),
    path('book/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:id>/', views.BookDetailView.as_view()),
    path('create_book/', views.CreateBookView.as_view()),
    path('book/<int:id>/delete/', views.DeleteBookView.as_view()),
    path('book/<int:id>/update/', views.EditBookView.as_view()),
    path('search/', views.SearchView.as_view(), name='search_book'),




    path('myself/', views.myself_view),
    path('hobby/', views.hobby_view),
    path('get_current_time/', views.get_current_time_view),
    path('random_number/', views.random_number_view),
]