from django.db import models
from django.utils import timezone


class Inquirer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=12)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    date_generated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
