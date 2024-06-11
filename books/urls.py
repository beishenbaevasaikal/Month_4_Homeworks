from django.urls import path
from books import views

urlpatterns = [
    path('kids/', views.kids_tags_view),
    path('all_types/', views.all_types),
    path('book/', views.book_list_view),
    path('book/<int:id>/', views.book_detail_view),



    path('myself/', views.myself_view),
    path('hobby/', views.hobby_view),
    path('get_current_time/', views.get_current_time_view),
    path('random_number/', views.random_number_view),
]