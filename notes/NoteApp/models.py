from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
