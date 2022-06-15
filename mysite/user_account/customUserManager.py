from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUserManager(BaseUserManager):

    def create_user(self,email,first_name,last_name,password,**extra_fields):
        if not email:
            raise ValueError(_('Email must be set'))
        if not first_name:
            raise ValueError(_('first name must be set'))
        if not last_name:
            raise ValueError(_('last name must be set'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,first_name,last_name,password,**extra_fields):
        print('hello create_superuser called')

        user =  self.create_user( email,first_name,last_name,password,**extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user