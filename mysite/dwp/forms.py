from django import forms
from .models import Bill, MeterReading
from django.utils.translation import gettext_lazy as _

class BillCreationForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ("__all__")

    def save(self,commit=True):
        bill = super().save(commit=False)
        arr = [bill.water_charge,bill.late_fine,bill.maintainance_charge,bill.new_meter_cost,bill.extra_fees]
        before_sum = [attr for attr in arr if attr is not None]
        
        bill.total = sum(before_sum)
        if bill.discount:
            bill.total = bill.total-bill.discount
        if commit:
            bill.save()
        return bill 

class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ('__all__')
        exclude = ('total','previous_reading')
    def save(self,commit=True):
        meter_reading = super().save(commit=False)
        arr = [meter_reading.minimum_charge,meter_reading.extra_consumption_charge,]
        before_sum = [attr for attr in arr if attr is not None]
        meter_reading.total = sum(before_sum)

        if commit:
            meter_reading.save()
        return meter_reading

    # def clean(self):
    #     cleaned_data = super().clean()
    #     print(cleaned_data)
    #     print(cleaned_data.get('current_reading'))
    #     print(cleaned_data.get('previous_reading'))
    #     if cleaned_data.get('current_reading') < cleaned_data.get('previous_reading'):
    #         raise forms.ValidationError(_('current reading cannot be less then previous reading'))
    #     return cleaned_data



    