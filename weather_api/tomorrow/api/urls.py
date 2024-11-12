# weather_api/tomorrow/api/urls.py

from django.urls import path

from weather_api.tomorrow.api.views import TomorrowView

urlpatterns = [
    path("tomorrow/", TomorrowView.as_view(), name="tomorrow"),
]
