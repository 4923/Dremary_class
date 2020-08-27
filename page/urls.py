from django.urls import path
from . import views

# 이제부터 app에 있는 url은 page 앱의 urls.py에서 관리하니까 project에서는 각각의 앱을 연결만 하면 됨
urlpatterns = [
  path('',views.home, name = "home"),
  path('introduce/', views.introduce, name = "introduce"),
  path('profile/<int:designer_id>/',views.detail, name="detail"),
  # url에 페이지가 있다고 해서 무조건 사용해야하는건 아니다 (?)
  path('new/',views.new, name="new"),
  path('create/',views.create, name="create"),
  path('update/<int:designer_id>/', views.update, name = "update"),
  path('delete/<int:designer_id>/', views.delete, name="delete"),
 ]