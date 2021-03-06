from django.forms import ModelForm
from django import forms
from .models import User
from member.models import Book, Review
from django.utils.translation import ugettext_lazy

REVIEW_POINT_CHOICES = (
    ('1', "★"),
    ('2', "★★"),
    ('3', "★★★"),
    ('4', "★★★★"),
    ('5', "★★★★★")
)


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]

    def signup(self, req, user):
        # cleaned_data로 form date 들고 오는 듯
        user.nickname = self.cleaned_data['nickname']
        user.save()


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'book']
        labels = {'point': ('평점'), 'comment': ('코멘트')}
        widgets = {
            'book': forms.HiddenInput(),
            'author': forms.HiddenInput(),
            'point': forms.RadioSelect(),
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'writer', 'bookcovers']
        labels = {'name': ('책 제목'), 'writer': ('작가'),
                  'bookcovers': ('이미지 url')}
        help_texts = {'name': ('책 제목을 입력해 주세여'), 'writer': (
            '작가도 입력해 주세여'), 'bookcovers': ('이미지 주소 복사해서 입력하세요')}
        error_messages = {
            'name': {
                'max_length': ('책 제목이 너무 길어요. 줄여 보세요')
            }
        }
