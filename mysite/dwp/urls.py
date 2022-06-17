from django.urls import path,include
from . import views
app_name = 'dwp'
urlpatterns = [
    path('view-report/',views.ReportView.as_view(),name='report'),
]