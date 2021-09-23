from django.urls import path
from . import views

urlpatterns = [
    path('fav_book', views.fav_book),
    ]
