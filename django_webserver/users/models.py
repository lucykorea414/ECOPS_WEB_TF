from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.urls import reverse_lazy, reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 한계정의 사용자를 가져옴
    nickname = models.CharField(max_length=40)
    profile_photo = models.ImageField(blank=True)
    note = models.TextField(blank=True, help_text="자기소개를 작성해보세요!", editable=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def get_absolute_url(self):
        return reverse('users:profile', args=[self.pk])
    

# class Comment(models.Model):
#     to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     writer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     text = models.TextField(max_length=200)
#     created_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.text