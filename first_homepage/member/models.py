from django.db import models

# Create your models here.
# ORM의 역할: SQL을 직접 작성하지 않아도 데이터베이스로 접근해 CRUD가 가능하게 해줌

# 멤버라는 앱에 user라는 테이블을 만들 거야

# User라는 클래스가 models에 있는 Model이다라고 알려 줌


class User(models.Model):
    userid = models.CharField(max_length=64, verbose_name='아이디')
    # 장고에서의 컬럼, CharField는 문자열 필드
    # userid 칼럼은 장고 관리 페이지에서 '아이디'라는 이름으로 나올 거다
    # 그런 별칭을 지정해 주는 게 verbose_name
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    bio = models.TextField(null=True, verbose_name='소개')
    registered = models.DateTimeField(auto_now_add=True, verbose_name='등록')
    # DateTimeField auto_now_add=True? add할 당시의 현재 시간을 자동으로 넣어 준다
    # registered라는 컬럼 이름, models에 들었고, 데이터 타입은 DateTime이고, verbose
    # 로 별칭을 정해 줍니다
    GENDERS = (('M', '남성(Man)'), ('W', '여성(Woman)'))
    # 배열을 선언
    # 그 배열이 CharField의 속성으로 들어가게 됩니다?
    gender = models.CharField(
        max_length=1, verbose_name='성별', choices=GENDERS, default='W')
