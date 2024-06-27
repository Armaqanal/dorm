from django.contrib.auth.hashers import is_password_usable, make_password
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# class Customer(User):
#     ...
#
#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         if not is_password_usable(self.password) or not self.password.startswith('pbkdf2_sha256$'):
#             # if self.pk is None:
#             # if not is_password_usable(self.password):
#             '''age password hash nashode bia hash kon'''
#             self.password = make_password(self.password)
#         super().save(force_insert, force_update, using, update_fields)
#
#
# class Manager(User):
#     def save(self, *args, **kwargs):
#         self.is_superuser = True
#         super().save()

