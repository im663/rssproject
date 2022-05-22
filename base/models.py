from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django import forms
from django.contrib.sites.models import Site
import datetime


class Settings(Site):
    poll_interval = models.PositiveIntegerField(
        default=10, validators=[MinValueValidator(1), MaxValueValidator(255)]
    )
    description = models.CharField(
        max_length=150, default="Change Me!", null=False, blank=False
    )

    class Meta:
        verbose_name_plural = "settings"
        db_table = "settings"

    def __str__(self) -> str:
        return "Settings"
