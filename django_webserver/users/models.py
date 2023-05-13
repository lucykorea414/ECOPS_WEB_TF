from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'