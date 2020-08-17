from django.db import models

# Create your models here.
class Designer(models.Model):  # models.Model은 고정
  image = models.ImageField(upload_to = 'images/')
    # settings.py에서 static 할 때 media는 유저들이 올리는 파일이고
    # 이 파일을 media로 보낸다고 했었음.
    # models.py에서 media의 images로 보내겠다고 선언함
  name = models.CharField(max_length = 50)
  address = models.CharField(max_length = 255)
  description = models.TextField()
  
  '''
  # 서버 켜기 전에 DB가 알아들을 수 있게 migration 하는거 잊지 말기

    # 근데 왜 에러가 나지
    ERRORS:
    page.Designer.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
      HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
      => 해결방법. pip install Pillow
      Pillow: py에서 이미지를 다루기 위해 사용하는 패키지
        # 번역한 후에 DB에 적용
  '''

  def __str__(self): # 들여쓰기 주의
    return self.name