from django.db import models
from django.conf import settings
from users.models import User


class Task(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    header = models.TextField(max_length=50, blank=False)
    text = models.TextField(max_length=100, blank=False)
    liable = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(verbose_name='image', upload_to='media/', blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_time']
