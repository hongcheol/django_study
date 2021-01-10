"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
#from django.conf.urls.static import static
#from django.conf import settings
from mysite.views import UserCreateView, UserCreateDoneTV

from mysite.views import HomeView
#다음은 APP_URLCONF로 이동
#from bookmark.views import BookmarkLV, BookmarkDV #뷰 모듈과 관련된 클래스를 임포트
#from bookmark.view import * 와 같이 일괄처리도 가능

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register/',UserCreateView.as_view(), name='register'),
    path('accounts/register/done/',UserCreateDoneTV.as_view(),name='register_done'),
    
    path('',HomeView.as_view(),name='home'),
    path('bookmark/',include('bookmark.urls')),
    path('blog/',include('blog.urls')),
    path('photo/',include('photo.urls'))
    #move to APP_URLCONF
    #class-based views
    #path('bookmark/',BookmarkLV.as_view(),name='index'),
    #path('bookmark/<int:pk>/',BookmarkDV.as_view(),name='detail'),
]#+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
