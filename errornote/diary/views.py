from django.shortcuts import render, redirect
from .models import Page
from .forms import PageForm

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

def page_create(request):
    if request.method == 'POST': # 만약 요청 방식이 POST라면
        form = PageForm(request.POST) # page_form과 PageForm, 데이터와 폼을 바인딩
        if form.is_valid():
            new_page = form.save() # new_page라는 변수에 바인딩된 내용(page_form)을 저장
            return redirect('page-detail', page_id=new_page.id) # 상세 일기 보기 페이지로 안내합니다.
    else: # 만약 요청 방식이 GET이라면(입력 폼 요청할 때임)
        form = PageForm # 이 form은 비어 있음 폼 요청할 때라 전송한 게 아님
    return render(request, 'diary/page_form.html', {'form': form}) 
    # 템플릿으로 보내 렌더해서 결과로 돌려줍니다.

