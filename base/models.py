from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240, blank=True)
    due = models.DateField(blank=True, null=True)
    due_time = models.TimeField(blank=True, null=True)
    progress = models.IntegerField(default=0)
    color = models.CharField(max_length=9, default="#aa00ff")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

