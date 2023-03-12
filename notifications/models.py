from django.db import models
from django.utils import timezone

class Notification(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
