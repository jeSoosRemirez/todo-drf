from django.utils import timezone
from django.db import models
from users.models import User


class Task(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    header = models.TextField(max_length=50, blank=False)
    text = models.TextField(max_length=100, blank=False)
    liable = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(verbose_name='image', upload_to='media/', blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_time']

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.created_time = self.created_time

    def save(self, *args, **kwargs):
        if not self.created_time and self.created_time:
            self.edited_date = timezone.now()
        super(Task, self).save(*args, **kwargs)
