from django.db import models
from django.conf import settings

class UserProfile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
  password = models.CharField(max_length=20)
  nickname = models.CharField(max_length=30, blank=True, null=True)
  profile_img = models.ImageField(upload_to='profile_img/', blank=True, null=True)

  # 관리자페이지에서 user의 이름 그대를 불러온다.
  def __str__(self):
    return f'{self.user.username} Profile'