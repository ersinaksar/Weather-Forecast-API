# weather_api/forecasts/apps.py

from django.apps import AppConfig


class TomorrowConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "weather_api.tomorrow"
