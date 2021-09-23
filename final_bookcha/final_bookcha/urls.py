"""final_bookcha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('books/', include('books.urls')),
    path('', include('member.urls')),
    path('', include('allauth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='social_app/index.html')),
]

# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 미디어파일 요청 들어오면 미디어 루트 안의 미디어 파일을 돌려라
