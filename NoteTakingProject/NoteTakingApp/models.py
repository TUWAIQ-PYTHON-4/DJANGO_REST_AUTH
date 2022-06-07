from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=400)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
