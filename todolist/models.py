from datetime import datetime
from email.policy import default
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class todolist(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models .CASCADE,
    )
    title = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    description = models.TextField()