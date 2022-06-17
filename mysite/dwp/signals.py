from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Employee, MeterReading,Bill, PaymentReceipt,MyUser
from datetime import timedelta
from django.utils import timezone

@receiver(post_save, sender=MeterReading)
def my_handler(sender,instance,created, **kwargs):
    if created:
        late_fine=0
        # if instance.days_passed-5 < 0:
        #     late_fine = 0
        # else:
        #     late_fine = (instance.days_passed-5)*10

        Bill.objects.create(water_meter=instance,water_charge=instance.total,late_fine=late_fine,entered_by=instance.read_by,total=instance.total)


@receiver(pre_save,sender=MeterReading)        
def check_meter_reading(sender,instance,**kwargs):
    queryset = MeterReading.objects.filter(water_meter=instance.water_meter).order_by('-date').first()
    # print(queryset)
    """
    If the insertion is first and user has no meter reading then the previous meter reading will be set to zero
    If user has previous reading then the value of current reading of query set will be set to previous reading of new instance

    """
    if queryset:
        print(queryset)
        instance.previous_reading = queryset.current_reading
        pass
    else:
        instance.previous_reading = 0

@receiver(pre_save,sender=PaymentReceipt)
def check_salary(sender,instance,**kwargs):
    
    instance.received_amount = instance.employee.salary

@receiver(pre_save, sender=Bill)
def on_change(sender, instance,**kwargs):
    """
    if bill is created and made is paid to true there may be chance that it will be updated as is_paid == False
    so to restrict this situation this signal is created
    """
    if instance.id:
        previous = Bill.objects.get(id=instance.id)
        if previous.is_paid != instance.is_paid: 
            #is_paid value has been modified
            instance.is_paid = True