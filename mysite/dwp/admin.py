from django.contrib import admin

from .forms import BillCreationForm, MeterReadingForm
from .models import *
@admin.register(WaterMeter)
class WaterMeterAdmin(admin.ModelAdmin):
    list_display = ('user','meter_num')
    

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id','user','water_meter','fine','total')
    form = BillCreationForm
    list_filter = ('is_paid',)
    
@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    form = MeterReadingForm
    list_display = ('id','water_meter','current_reading','previous_reading','water_consumed','minimum_charge','extra_consumption_charge','total','read_by','date')
    search_fields = ('water_meter__meter_num',)

