from django.shortcuts import render
from .models import designer
# [QuerySet] Model의 존재 알려주기

# Create your views here.
def home(request):
  designers = Designer.objects.all()
  # [QuerySet] QuerySet을 Templates로 보내기: 지금까지 만들어진 객체를 Designers에 한번에 넣기 (.all())
  return render (request, 'home.html',{'designers': designers})
  # request가 들어오면 home 함수에서는 user가 보낸 요청(request)와 함께 home.html이라는 template를 return한다.
  # return의 인자는 최대 세개 (필수 두개: request, template), 마지막 하나는 template에 넘겨줄 값을 dict처럼
def introduce(request):
  return render (request, 'introduce.html')
