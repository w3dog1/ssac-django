from collections import namedtuple
from django.urls import path
from . import views

urlpatterns = [
    path('join', views.join),
    path('joined', views.joined),
    path('home', views.home),
    path('login', views.login),
    path('logined', views.logined),
    path('logined', views.check_logined),
    path('signout', views.signout),
    path('change', views.change),
    path('changed', views.changed),
    path('list', views.list),
    path('create', views.create, name='book-create'),
    path('', views.IndexView.as_view(), name="index"),
    path('reviews/<int:review_id>',
         views.ReviewDetailView.as_view(), name="review-detail"),
    path('reviews/new/', views.ReviewCreateView.as_view(), name="review--create"),
    path('reviews/<int:review_id>/edit/', views.ReviewUpdateView.as_view(), name="review-update"),
    path('books/<int:id>/', views.detail, name='book-detail'),
    path('books/<int:book_id>/review/create',
         views.review_create, name='review-create'),
    path('books/<int:book_id>/review/delete/<int:review_id>',
         views.review_delete, name='review-delete'),
    path('review/list', views.review_list, name="review-list"),
]
