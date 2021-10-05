from django import forms
from .models import Page

from django_summernote.widgets import SummernoteWidget

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'score']
        widgets = {
            'content': SummernoteWidget(),
        }
