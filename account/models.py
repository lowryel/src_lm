# from typing import Any
from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from django.conf import settings
# from django.contrib.auth.models import BaseUserManager


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not password:
#             raise ValueError("Users must have a password")
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.staff = is_staff
#         user.admin = is_admin
#         user.active = is_active
#         user.save(using=self._db)
#         return user

#     def create_staffuser(self, email, password=None):
#         user = self.create_user(email, password=password, is_staff=True)
#         return user

#     def create_superuser(self, email, password=None):
#         user = self.create_user(email, password=password, is_staff=True, is_admin=True)
#         return user


# # Create your models here.
# class Agency(AbstractBaseUser):
#     agency_name = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False)
#     admin = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     objects = UserManager()
#     USERNAME_FIELD = 'email'

#     REQUIRED_FIELDS=[]

#     def __str__(self):
#         return self.email
    
#     def get_full_name(self):
#         return self.email
    
#     def get_short_name(self):
#         return self.email
    
#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True
    
#     @property
#     def is_staff(self):
#         return self.staff
    
#     @property
#     def is_admin(self):
#         return self.admin

#     @property
#     def is_active(self):
#         return self.active

