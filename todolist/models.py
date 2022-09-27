from django.db import models
from django.conf import settings

# Create your models here.
class todolist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.TextField()
    title = models.TextField()
    description = models.TextField()