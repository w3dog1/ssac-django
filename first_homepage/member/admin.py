from django.contrib import admin
from .models import User

# Register your models here.

admin.site.register(User)
# admin 관리자 사이트에 User라는 (아까 만든 클래스)함수를 등록하겠다.
