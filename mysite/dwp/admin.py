from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .forms import BillCreationForm, MeterReadingForm
from .models import *
@admin.register(WaterMeter)
class WaterMeterAdmin(admin.ModelAdmin):
    list_display = ('user','meter_num')
    

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id','user','water_meter','fine','total','is_paid')
    form = BillCreationForm
    list_filter = ('is_paid','created_at')
    search_fields = ('water_meter__water_meter__user__first_name',)
    
@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    form = MeterReadingForm
    list_display = ('id','water_meter','get_full_name','current_reading','previous_reading','water_consumed','minimum_charge','extra_consumption_charge','total','read_by','date')
    search_fields = ('water_meter__meter_num',)
    list_filter = ('date',)

    def get_full_name(self , obj):
        return f"{obj.water_meter.user.first_name} {obj.water_meter.user.middle_name} {obj.water_meter.user.last_name} "
    get_full_name.short_description = _('full name')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','user','salary','type_of_employee',)
    search_fields = ('user__first_name',)

@admin.register(PaymentReceipt)
class PaymentReceiptAdmin(admin.ModelAdmin):
    list_display = ('id','employee','received_amount','date')
    fields = ('employee',)
    list_filter = ('date',)