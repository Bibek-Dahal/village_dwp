from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import Bill, Employee, PaymentReceipt
from django.contrib import admin
from .models import MeterReading
from django.utils.translation import gettext_lazy as _

class ReportView(View):
    def get(self,request):
        app_list = admin.site.get_app_list(request)
        queryset = Bill.objects.filter(is_paid=True)
        amount_collected = sum([bill.total for bill in queryset])
        amount_remaining = amount_collected - sum(payment.received_amount for payment in PaymentReceipt.objects.all())
        
        print(queryset)
        context = {
            'has_permission': True, 
            'user': request.user,
            'is_popup':False,
            'is_nav_sidebar_enabled':True,
            'available_apps':app_list,
            'site_title':'DWP admin site',
            'title':'View Report',
            'site_header':_('Aangal Drinking Water Administration'),
            'amount_collected':amount_collected,
            'amount_remaining':amount_remaining
            }

        return render(request,'dwp/report.html',context)

