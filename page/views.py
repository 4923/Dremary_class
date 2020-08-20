from django.shortcuts import render, get_object_or_404
from .models import Designer
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


def detail(request, designer_id): # 인자에 request, pk 로 적으면 안됨. urls.py에서 정한 pk 이름을 적어야함
  designer = get_object_or_404(Designer, pk = designer_id)
  # object가 있으면 그게 내려갈거고 (리턴값으로?) 없으면 404가 내려감
  # get_object_or_404에서 객체를 찾아서 designer라는 변수에 넣어준 다음에 -> detail.html로 보냄
  return render(request, 'detail.html',{'designer':designer})
  # 'designer'라는 이름으로 변수 designer를 보냄