from django.shortcuts import render, get_object_or_404, redirect
from .models import Designer
# [QuerySet] Model의 존재 알려주기

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

def new(request):
  return render(request, 'new.html')

def create(request):
  # 객체 생성
  # method가 POST일때만 작동
  if request.method == 'POST':
    post = Designer()
    # 파일이 진짜 있는지 체크
    if 'image' in request.FILES:
      post.image = request.FILES['image']
    post.name = request.POST['name']
    post.address = request.POST['address']
    post.description = request.POST['description']

    post.save()

  return redirect('detail',post.id)  # 이게 django reference 표준
  # return redirect('profile/' + str(post.id))

# Advanced code
# create에서 method 두개로 나눴는데, 굳이 그래야하나?
def update(request, designer_id):
  post = get_object_or_404(Designer, pk = designer_id)

  if request.method == 'POST':
    if 'image' in request.FILES:
      post.image = request.FILES['image']
      post.name = request.POST['name']
      post.address = request.POST['address']
      post.description = request.POST['description']
      
      post.save()

      # 수정된 결과 바로 확인하기 위해 redirect
      # 여기서 detail: path 이름
      return redirect('detail', post.id)

  else: # GET일때
    return render(request, 'update.html', {'designer' : post})
    # desitner : post인 이유 > 미리 띄워놓기 위해
    # update는 기존에 입력된 값을 띄워놓고 수정할 예정이기 때문


def delete(request, designer_id):
  # 어떤게 제거가 필요한 객체인지 찾아야 한다
  post = get_object_or_404(Designer, pk=designer_id)
  post.delete()

  return redirect('home') 