from datetime import datetime
from django.db import models
from django.conf import settings


class TodoItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ". " + self.title
