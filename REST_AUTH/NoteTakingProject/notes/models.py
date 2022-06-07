from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=520)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

