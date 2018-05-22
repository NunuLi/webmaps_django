from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class App(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app_text = models.CharField(max_length=200)

    def __str__(self):
        return self.app_text