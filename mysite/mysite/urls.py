from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.urls import path,include
from dwp import views
urlpatterns = [
    path('admin/',include('dwp.urls',namespace='dwp')),
    path('admin/', admin.site.urls),
]
admin.site.site_header = _('Aangal Drinking Water Administration')
admin.site.site_title = _('ADWP admin site')