from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from .models import Page
from .forms import PageForm

# Create your views here.


# home
def index(request):
    return render(request, 'diary/index.html')


# report list page
class PageListView(ListView):
    model = Page
    ordering = ['-dt_created']
    paginate_by = 8


# report detail page
class PageDetailView(DetailView):
    model = Page


# report infomation page
def info(req):
    return render(req, 'diary/info.html')


# Mixin만으로 Login된 유저만 리뷰 작성할 수 있음
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('page-detail', kwargs={'pk': self.object.id})


# report modify
class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page
    form_class = PageForm

    def get_success_url(self):
        return reverse('page-detail', kwargs={'pk': self.object.id})

    def test_func(self, user):
        page = self.get_object()# 뷰가 다루는 오브젝트(게시글) 접근
        return page.author == user


# report delete
class PageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Page

    def get_success_url(self):
        return reverse('page-list')

    def test_func(self, user):
        page = self.get_object()
        return page.author == user