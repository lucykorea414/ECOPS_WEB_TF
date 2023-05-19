from django.db import models
from django.conf import settings

# Create your models here.

class Guestbook(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    contents = models.TextField()
    reg_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Guestbook({self.contents}, {self.reg_date}'