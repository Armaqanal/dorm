from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(User):
    ...


class Manager(User):
    def save(self, *args, **kwargs):
        self.is_superuser = True
        super().save()
