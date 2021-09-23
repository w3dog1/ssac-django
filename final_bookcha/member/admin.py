from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, User, Review

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Book)
admin.site.register(Review)

# 유저모델 추가 필드
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname",)}),)

# UserAdmin -> User 모델에 대해 특별한 인터페이스 제공한대서 써 봤는데
# 원래 쓰던 User에 비해 컬럼 많아서 정보가 여러 개 한꺼번에 보임
