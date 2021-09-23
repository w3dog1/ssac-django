from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# ORM의 역할: SQL을 직접 작성하지 않아도 데이터베이스로 접근해 CRUD가 가능하게 해줌
# 멤버라는 앱에 user라는 테이블을 만들 거야
# User라는 클래스가 models에 있는 Model이다라고 알려 줌

# AbstractUser -> User에 비해 상속받아서 쓸 수 있고 기본 제공하는 것도 다양한 편인 듯?


class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        error_messages={'unique': '이미 사용 중인 닉네임 입니다!'},)

    def __str__(self):
        return self.email


class Book(models.Model):
    name = models.CharField(max_length=25, verbose_name='제목')
    writer = models.CharField(max_length=15, verbose_name='저자')
    bookcovers = models.CharField(max_length=500, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


REVIEW_POINT_CHOICES = (
    ('1', "★"),
    ('2', "★★"),
    ('3', "★★★"),
    ('4', "★★★★"),
    ('5', "★★★★★")
)


class Review(models.Model):
    point = models.IntegerField(choices=REVIEW_POINT_CHOICES, default=None)
    comment = models.CharField(max_length=500)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        auto_now_add=True)  # 모델이 생성된 시간을 자동으로 필드에 넣어
    updated_at = models.DateTimeField(auto_now=True)
