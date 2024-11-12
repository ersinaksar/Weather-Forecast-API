# weather_api/tomorrow/api/views.py
import csv
import os
from datetime import timedelta

from django.utils.dateparse import parse_datetime
from rest_framework.response import Response
from rest_framework.views import APIView


class TomorrowView(APIView):
    def get(self, request, format=None):
        now_param = request.query_params.get("now")

        if not now_param:
            return Response(
                {"detail": "'now' paramater needed."},
                status=400,
            )

        now = parse_datetime(now_param)

        if now is None:
            return Response(
                {"detail": "'now' pparamater should be valid datetime format."},
                status=400,
            )

        # Determine CSV file path
        csv_file_path = os.path.join("data", "weather.csv")

        if not os.path.isfile(csv_file_path):
            return Response(
                {"detail": f"CSV file '{csv_file_path}' could not find."},
                status=500,
            )

        # Threshold values
        temp_threshold = 20  # °C, example value
        wind_threshold = 10  # m/s, example value
        irradiance_threshold = 5  # W/m², example value

        # Flags for determine boolean values
        is_warm = False
        is_sunny = False
        is_windy = False

        # Determine next days start and end
        tomorrow_start = now + timedelta(days=1)
        tomorrow_end = tomorrow_start + timedelta(days=1)

        with open(csv_file_path) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                try:
                    event_start_str = row["event_start"]
                    event_start = parse_datetime(event_start_str)
                    event_value = float(row["event_value"])
                    sensor = row["sensor"]

                    # Check for tomoorrow data is exist
                    if tomorrow_start <= event_start < tomorrow_end:
                        # Set the boolean flags depends on thresholds
                        if sensor == "temperature" and event_value >= temp_threshold:
                            is_warm = True
                        elif sensor == "wind speed" and event_value >= wind_threshold:
                            is_windy = True
                        elif (
                            sensor == "irradiance"
                            and event_value >= irradiance_threshold
                        ):
                            is_sunny = True

                except Exception as e:
                    print(f"Error row skipped: {e}") # log the errors
                    continue

        return Response(
            {
                "is_warm": is_warm,
                "is_sunny": is_sunny,
                "is_windy": is_windy,
            },
        )
