from django.shortcuts import render

# Create your views here.
def home(request):
  return render (request, 'home.html')
  # request가 들어오면 home 함수에서는 user가 보낸 요청(request)와 함께 home.html이라는 template를 return한다.

def introduce(request):
  return render (request, 'introduce.html')
