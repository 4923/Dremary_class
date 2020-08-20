from django.urls import path
from . import views

# 이제부터 app에 있는 url은 page 앱의 urls.py에서 관리하니까 project에서는 각각의 앱을 연결만 하면 됨
urlpatterns = [  # 아니 뭔데 대문자로 쓰니까 circular import error 뜨는데 Url -> url로 고치니까 해결됨
  path('',views.home, name = "home"),
  path('introduce/', views.introduce, name = "introduce"),
  path('profile/<int:designer_id>',views.detail, name="detail"),
 ]