from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MeterReading,Bill


@receiver(post_save, sender=MeterReading)
def my_handler(sender,instance,created, **kwargs):
    if created:
        late_fine=0
        # if instance.days_passed-5 < 0:
        #     late_fine = 0
        # else:
        #     late_fine = (instance.days_passed-5)*10

        Bill.objects.create(water_meter=instance,water_charge=instance.total,late_fine=late_fine,entered_by=instance.read_by,total=instance.total)