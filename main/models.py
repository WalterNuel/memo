from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.utils import timezone
# Create your models here.

User = get_user_model()

class Profile(models.Model):
  username = models.ForeignKey(User, on_delete=models.CASCADE)
  user_img = models.ImageField(upload_to='user_images', default='memo-black-bg.png')

  def name(self):
    return self.username


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    note_text = models.TextField(null=True, blank=True,)
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.entry_date >= timezone.now() - datetime.timedelta(days=1)

    def time_written(self):
        ago = self.entry_date
        hours = ago



class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(null=False, max_length=70)
    description = models.TextField(null=True, blank=True,)
    completed = models.BooleanField(default=False)
    create = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

    class Meta:
        ordering = ['time']