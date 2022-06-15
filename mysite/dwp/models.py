from django.db import models
from user_account.models import MyUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import date,timedelta,datetime


class WaterMeter(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    meter_num = models.CharField(_('meter number'),max_length=20,primary_key=True)

    def __str__(self):
        return self.meter_num

class MeterReading(models.Model):
    water_meter = models.ForeignKey(WaterMeter,verbose_name=_('water meter'),on_delete=models.PROTECT)
    current_reading = models.PositiveSmallIntegerField(_('current reading'),)
    previous_reading = models.PositiveSmallIntegerField(_('previous reading'),)
    minimum_charge = models.PositiveSmallIntegerField(_('minimum charge'),)
    extra_consumption_charge = models.PositiveSmallIntegerField(_('extra consumption charge'),default=0)
    total = models.PositiveSmallIntegerField(_('meter number'),)
    read_by = models.ForeignKey(MyUser,on_delete=models.PROTECT,verbose_name=_('read by'))
    date = models.DateField(_('date'),)
    

    def __str__(self):
        return f"{self.water_meter.meter_num}   {self.date}"

    @property
    def water_consumed(self):
        # print(type(self.current_reading-self.previous_reading))
        return self.current_reading-self.previous_reading
    
    


class Bill(models.Model):
    water_meter = models.OneToOneField(MeterReading,on_delete=models.PROTECT,verbose_name=_('water meter'))
    water_charge = models.PositiveSmallIntegerField(_('water charge'))
    late_fine = models.PositiveSmallIntegerField(_('late fine'),null=True,blank=True)
    maintainance_charge = models.PositiveSmallIntegerField(_('maintainance charge'),null=True,blank=True)
    new_meter_cost = models.PositiveSmallIntegerField(_('new meter cost'),null=True,blank=True)
    extra_fees = models.PositiveSmallIntegerField(_('extra fees'),null=True,blank=True)
    discount = models.PositiveSmallIntegerField(_('discount'),null=True,blank=True)
    total = models.PositiveSmallIntegerField(_('total'),null=True,blank=True)
    entered_by = models.ForeignKey(MyUser,on_delete=models.PROTECT,verbose_name=_('entered by'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False,verbose_name=_('is_paid'))

    def __str__(self):
        return self.water_meter.water_meter.user.first_name
    
    class Meta:
        verbose_name = _('bill')
        verbose_name_plural = _('bills')
    
    @property
    def user(self):
        user_obj = self.water_meter.water_meter.user
        return f"{user_obj.first_name} {user_obj.middle_name} {user_obj.last_name}"
    
    def days_passed(self):
        print(print(self.created_at.tzinfo))
        ellapsed_days = (timezone.now()-self.created_at).days
        # return ellapsed_days
        return 6
    
    @property
    def fine(self):
        initial_fine=0
        if self.days_passed()-5 < 0:
            return initial_fine 
        else:
            initial_fine = (self.days_passed()-5)*10
            return initial_fine







