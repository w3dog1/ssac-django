from django.shortcuts import render
import random

# Create your views here.

# 회원가입 창 띄우기


def fav_book(req):
    return render(req, 'fav_book.html')
