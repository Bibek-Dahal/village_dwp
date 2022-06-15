from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class DwpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dwp'
    verbose_name = _("Drinking Water Project")
    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals
