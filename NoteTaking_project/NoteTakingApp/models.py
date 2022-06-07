from django.db import models
from django.contrib.auth.models import User 

class Note(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)