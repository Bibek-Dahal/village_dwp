from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('admin/', admin.site.urls),
]
admin.site.site_header = _('Aangal Drinking Water Administration')