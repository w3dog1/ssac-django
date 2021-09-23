from django.urls import path
from . import views

urlpatterns = [
    path('ajax_test', views.ajax_test),
    path('ajax_login', views.ajax_login),
    path('join', views.join),
    path('joined', views.joined),
    path('signout', views.signout),
    path('userdelete', views.userdelete),
    path('resetpw', views.change),
    path('changed', views.changed),
    path('login', views.login),
    path('logined', views.logined),
    path('check_logined', views.check_logined),
    path('logout', views.logout),
    path('receive', views.rec),
    path('send', views.send),
    path('static', views.statictest),
    path('novel/<int:chapter>/<str:player1>/<str:player2>', views.novel)
]
