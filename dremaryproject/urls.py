"""dremaryproject URL Configuration

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
from django.urls import path
from page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = "home"),
    path('introduce/', views.introduce, name = "introduce"),
    # path를 생성해서 url을 얼마든지 만들 수 있다.
    # url과 path 이름을 같게 지정하는게 편함
]
