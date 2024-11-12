# weather_api/forecasts/models.py

from django.db import models


class Forecast(models.Model):
    SENSOR_CHOICES = [
        ("temperature", "Temperature"),
        ("wind_speed", "Wind Speed"),
        ("irradiance", "Irradiance"),
    ]

    event_start = models.DateTimeField()
    belief_horizon_in_seconds = models.IntegerField()
    event_value = models.FloatField()
    sensor = models.CharField(max_length=20, choices=SENSOR_CHOICES)
    unit = models.CharField(max_length=10)
    created_at = models.DateTimeField()

    class Meta:
        ordering = ["-event_start", "belief_horizon_in_seconds"]

    def __str__(self):
        return f"{self.sensor} forecast for {self.event_start}"
