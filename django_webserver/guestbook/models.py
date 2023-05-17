from django.db import models
from django.conf import settings

# Create your models here.

class Guestbook(models.Model):
    user = models(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 한계정의 사용자를 가져옴
    writer = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    contents = models.TextField()
    reg_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Guestbook({self.name}, {self.password}. {self.contents}, {self.reg_date}'