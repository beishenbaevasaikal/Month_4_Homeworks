from django.urls import path
from books import views

urlpatterns = [
    path('myself/', views.myself_view),
    path('hobby/', views.hobby_view),
    path('get_current_time/', views.get_current_time_view),
    path('random_number/', views.random_number_view),
]