import os
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from .models import User, Book, Review
from django.core.paginator import Paginator
from member.forms import BookForm, ReviewForm
from django.http import HttpResponseRedirect, request
from django.db.models import Count, Avg
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.


class IndexView(ListView):
    model = Review
    template_name = "bookcha/index.html"
    context_object_name = "reviews"
    paginate_by = 4
    ordering = ["created_at"]


class ReviewDetailView(DetailView):
    model = Review
    template_name = "bookcha/review_detail.html"
    pk_url_kwarg = "review_id"


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "bookcha/review_form.html"

    def form_vaild(self, form):  # 입력받은 데이터가 유효할 때 데이터로 채워진 모델 오브젝트 만들고 저장.
        # 현재 form instance에 author 필드 정의
        form.instance.author = self.request.user
        return super().form_vaild(form)
    # super는 review class의 상위 클래스
    # 원래는 req가 view 파라미터로 전달되지만 -> class형 view에서는 self.request로 접근해야 됨
    # form instance에 author(user)를 추가해 주고 그 form을 CreateView의 form_vaild method에 넣음

    def get_success_url(self):
        return reverse("review-detail", kwargs=({"review_id": self.object.id}))


# 리뷰 삭제 (close 버튼)

# 홈 화면

def home(req):
    return render(req, 'home.html')

# 회원가입 창 띄우기


def join(req):
    return render(req, 'join.html')

# 회원가입 완료 창


def joined(req):
    newmember = User.objects.filter(
        userid=req.POST.get('id'))  # User.objects.get?

    if newmember:
        return render(req, 'join.html', {'err': "이미 존재하는 아이디입니다."})
    else:
        newmember = User(userid=req.POST.get('id'), username=req.POST.get(
            'name'), password=req.POST.get('pw'))
        newmember.save()  # 회원가입 저장
        return render(req, 'joined.html')
# err가 안 먹는데 가입이 되지는 않음 alert 창 어떻게 제대로 띄우는지!
# messages.error로 보내 보기 contrib에서 import도 해야 함


# 로그인 창
def login(req):
    return render(req, 'login.html')

# 로그인 작동


def logined(req):
    logmember = User.objects.filter(
        userid=req.POST.get('id'), password=req.POST.get('pw'))

    # 로그인 성공 {'id':req.POST.get('id')}
    if logmember:
        req.session['userid'] = req.POST.get('id')
        return render(req, 'logined.html', {'total_member': logmember, 'id': req.POST.get('id')})
    else:
        return render(req, 'login.html', {'failId': "아이디와 비밀번호를 확인해 주세요"})
# failId도 확인해야 함

# 세션 로그인 확인


def check_logined(req):
    if req.session.get('userid'):
        return render(req, 'logined.html', {'id': req.session.get('userid')})
    else:
        return render(req, 'login.html')

# 비밀번호 변경창


def change(req):
    return render(req, 'updatePw.html')

# 비밀번호 변경 동작


def changed(req):
    changepw = User.objects.get(
        userid=req.POST.get('id')
    )
    print(changepw)
    changepw.password = req.POST.get('newpw')
    changepw.save()

    return render(req, 'changed.html',  {'info1': req.POST.get('id')})

# 로그아웃 창


def signout(req):
    return render(req, 'signout.html')
# 로그아웃 동작
# 로그아웃 시 session도 pop


# 책 list


def list(req):
    books = Book.objects.all().annotate(reviews_count=Count(
        'review')).annotate(average_point=Avg('review__point'))
    paginator = Paginator(books, 4)

    page = req.GET.get('page')
    items = paginator.get_page(page)
    context = {
        'books': items
    }
    return render(req, 'list.html', context)

# 책 추가


def create(req):
    if req.method == 'POST':  # 만약 받아오는 방식이 POST라면
        form = BookForm(req.POST)  # form.py의 BookForm 쓸 건데
        if form.is_valid:  # 그 form이 유효하다면
            new_item = form.save()  # 새 아이템들을 form에 저장할 거다
        # 그런데다들HttpResponseRedirect(reverse(''))의 형태던데..
        return HttpResponseRedirect('/member/list')
    form = BookForm()  # 새 아이템들이 담긴 form이 form.py에 있는 BookForm이다
    # create urls로 들어오면 create.html로 간다
    return render(req, 'create.html', {'form': form})

# 책 더보기


def detail(req, id):
    if id is not None:  # id가 없자나 그런데?
        # item에 import한 Model Book의 pk값 넣거나 없으면404 띄워
        item = get_object_or_404(Book, pk=id)
        # reviews에는 Model Review에서 싹 검색해
        reviews = Review.objects.filter(book=item).all()
        # 그리고 detail.html에 아까 담은 Model Book pk값, Review에 있던 값 파라미터로 보내
        return render(req, 'detail.html', {'item': item, 'reviews': reviews})
    # HttpResponseRedirect 내가 적어 둔 url로 연결해
    return render(req, 'list.html')

# 책 리뷰 남기기


def review_create(req, book_id):
    if req.method == 'POST':
        form = ReviewForm(req.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('book-detail', id=book_id)

    item = get_object_or_404(Book, pk=book_id)
    form = ReviewForm(initial={'book': item})
    return render(req, 'review_create.html', {'form': form, 'item': item})

# 리뷰 삭제 (close 버튼)


def review_delete(req, book_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()

    return redirect('book-detail', id=book_id)

# 리뷰 리스트 (작성순)


def review_list(req):
    reviews = Review.objects.all().order_by('-created_at')
    paginator = Paginator(reviews, 5)

    page = req.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'reviews': items
    }
    return render(req, 'review_list.html', context)


# def naver_login(req):
#     return render(req, 'naver_login.html')
# 이 새끼.. 쓸모 없음 지금 콜백 home으로 돌려둬서 저기 들어가지도 않음 ㅡㅡ
