from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    j_username = models.CharField(max_length=200)
    j_password = models.CharField(max_length=200)

admin.site.register(User)