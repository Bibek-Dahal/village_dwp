from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from .customUserManager import CustomUserManager
from django.utils import timezone
from django.contrib.auth.models import User


class MyUser(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(_('first name'),max_length=50)
    middle_name = models.CharField(_('middle name'),max_length=50,blank=True)
    last_name = models.CharField(_('last name'),max_length=50)
    email = models.EmailField(_('email address'),max_length=100,unique=True)
    municipality = models.CharField(_('municipality'),default='Banepa',max_length=40)
    ward_no = models.PositiveSmallIntegerField(_('ward number'),default=4)
    tole = models.CharField(_('tole'),default='Aangal',max_length=40)
    phone_num = models.CharField(_('phone number'),blank=True,null=True,max_length=10)
    date_joined = models.DateTimeField(_('date joiner'),default= timezone.now)
    is_staff = models.BooleanField(_('is staff'),default=False)
    is_active = models.BooleanField(_('is active'),default=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # @property
    # def get_full_name(self):
    #     return f"{self.first_name} {self.middle_name} {self.last_name}"  
    
    # x = property(get_full_name) 
    
