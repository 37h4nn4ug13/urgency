from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    due = models.DateField(blank=True, null=True)
    due_time = models.TimeField(blank=True, null=True)
    progress = models.IntegerField(default=0)
    red = models.IntegerField(default=255)
    green = models.IntegerField(default=255)
    blue = models.IntegerField(default=255)

    def __str__(self):
        return self.title

