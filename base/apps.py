from django.apps import AppConfig
from django.db.models.signals import post_migrate

def build_settings(sender, **kwargs):
    from django.contrib.sites.models import Site
    from .models import Settings
    if Settings.objects.count() < 1:
        Settings.objects.create(site_ptr=Site.objects.first())

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self) -> None:
        post_migrate.connect(build_settings, sender=self)