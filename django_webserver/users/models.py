from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 한계정의 사용자를 가져옴
    mickname = models.CharField(max_length=40)
    profile_photo = models.ImageField(blank=True)

