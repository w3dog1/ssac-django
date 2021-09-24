from django.shortcuts import render
from .models import Page

# Create your views here.

# report list page
def page_list(req):
    object_list = Page.objects.all()
    return render(req, 'diary/page_list.html', {'object_list': object_list})

# report detail page
def page_detail(req, page_id):
    object = Page.objects.get(id=page_id)
    return render(req, 'diary/page_detail.html', {'object': object})

# report infomation page
def info(req):
    return render(req, 'diary/info.html')