from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    birthday = models.DateField()

    def __str__(self):
        return f'{self.user.username}'


