from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey (User , on_delete=models.CASCADE)
