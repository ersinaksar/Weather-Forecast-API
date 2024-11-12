# weather_api/forecasts/api/urls.py

from django.urls import path

from weather_api.forecasts.api.views import ForecastListView

urlpatterns = [
    path("forecasts/", ForecastListView.as_view(), name="forecast-list"),
]
