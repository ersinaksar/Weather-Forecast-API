# forecasts/api/views.py

import csv
import os
from datetime import timedelta

from django.utils.dateparse import parse_datetime
from rest_framework.response import Response
from rest_framework.views import APIView


class ForecastListView(APIView):
    def get(self, request, format=None):
        now_param = request.query_params.get("now")
        then_param = request.query_params.get("then")

        if not now_param or not then_param:
            return Response(
                {"detail": "'now' and 'then' paramaters needed."},
                status=400,
            )

        now = parse_datetime(now_param)
        then = parse_datetime(then_param)

        if now is None or then is None:
            return Response(
                {
                    "detail": "'now' and 'then' paramaters should be valid datetime format.",
                },
                status=400,
            )

        # Determine CSV file path
        csv_file_path = os.path.join("data", "weather.csv")

        if not os.path.isfile(csv_file_path):
            return Response(
                {"detail": f"CSV file '{csv_file_path}' could not find."},
                status=500,
            )

        forecasts = []

        with open(csv_file_path) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                try:
                    event_start_str = row["event_start"]
                    event_start = parse_datetime(event_start_str)
                    belief_horizon_in_sec = int(row["belief_horizon_in_sec"])
                    event_value = float(row["event_value"])
                    sensor = row["sensor"]
                    unit = row["unit"]

                    # Convert negative values to positive values
                    belief_horizon_in_sec = abs(belief_horizon_in_sec)

                    # calculate belief_time
                    belief_time = event_start - timedelta(seconds=belief_horizon_in_sec)
                    created_at = belief_time

                    # apply 'now' and 'then' filters
                    if event_start == then and created_at <= now:
                        forecast = {
                            "sensor": sensor,
                            "event_start": event_start_str,
                            "belief_horizon_in_seconds": belief_horizon_in_sec,
                            "event_value": event_value,
                            "unit": unit,
                        }
                        forecasts.append(forecast)
                except Exception as e:
                    # log the errors
                    print(f"Error row skipped: {e}")
                    continue

        # Select the newest forecast depends on sensors
        latest_forecasts = []
        sensors = ["temperature", "wind speed", "irradiance"]

        for sensor in sensors:
            sensor_forecasts = [f for f in forecasts if f["sensor"] == sensor]
            if sensor_forecasts:
                # select the nevest forecast depends on belief_horizon_in_seconds
                forecast = sorted(
                    sensor_forecasts,
                    key=lambda x: x["belief_horizon_in_seconds"],
                )[0]
                latest_forecasts.append(forecast)

        print(sensors)
        return Response(latest_forecasts)
