from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notes (models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.title