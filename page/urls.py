from django.urls import path
from . import views

# 이제부터 app에 있는 url은 page 앱의 urls.py에서 관리하니까 project에서는 각각의 앱을 연결만 하면 됨
Urlpatterns = [ 
    path('',views.home, name = "home"),
    path('introduce/', views.introduce, name = "introduce"),
    path('profile/<int:designer_id>',views.detail, name="detail"),
 ]