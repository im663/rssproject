from django.contrib import admin
from .models import Site
from . import models

admin.site.unregister(Site)


@admin.register(models.Settings)
class SettingAdminModel(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request) -> bool:
        return False
