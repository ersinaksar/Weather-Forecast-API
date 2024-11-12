# weather_api/forecasts/api/serializers.py

from rest_framework import serializers

from weather_api.forecasts.models import Forecast


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = [
            "sensor",
            "event_start",
            "belief_horizon_in_seconds",
            "event_value",
            "unit",
        ]
