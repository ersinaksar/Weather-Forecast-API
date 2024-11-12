# forecasts/management/commands/import_forecasts.py

import csv
import os
from datetime import timedelta

from dateutil.parser import parse as dateutil_parse
from django.core.management.base import BaseCommand

from weather_api.forecasts.models import Forecast


class Command(BaseCommand):
    help = "Import forecast data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]

        if not os.path.isfile(csv_file_path):
            self.stdout.write(
                self.style.ERROR(f"File '{csv_file_path}' does not exist"),
            )
            return

        with open(csv_file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            forecasts = []

            # for row in reader:
            #     event_start = parse_datetime(row['event_start'])
            #     belief_horizon_in_sec = int(row['belief_horizon_in_sec'])
            #     event_value = float(row['event_value'])
            #     sensor = row['sensor']
            #     unit = row['unit']
            #
            #     # belief_time hesaplayın
            #     belief_time = event_start - timedelta(seconds=belief_horizon_in_sec)
            #
            #     forecast = Forecast(
            #         event_start=event_start,
            #         belief_horizon_in_seconds=belief_horizon_in_sec,
            #         event_value=event_value,
            #         sensor=sensor,
            #         unit=unit,
            #         created_at=belief_time
            #     )
            #     forecasts.append(forecast)
            for i, row in enumerate(reader):
                try:
                    event_start_str = row["event_start"]
                    event_start = dateutil_parse(event_start_str)
                    if event_start is None:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Invalid event_start at line {i + 2}: {event_start_str}",
                            ),
                        )
                        continue

                    belief_horizon_in_sec_str = row["belief_horizon_in_sec"]
                    belief_horizon_in_sec = int(belief_horizon_in_sec_str)

                    event_value = float(row["event_value"])
                    sensor = row["sensor"]
                    unit = row["unit"]

                    # belief_time hesaplayın
                    if belief_horizon_in_sec < 0:
                        self.stdout.write(
                            self.style.WARNING(
                                f"Negative belief_horizon_in_sec at line {i + 2}: {belief_horizon_in_sec}. Using positive value for calculation.",
                            ),
                        )
                        belief_time = event_start + timedelta(
                            seconds=abs(belief_horizon_in_sec),
                        )
                        belief_horizon_in_sec = abs(belief_horizon_in_sec)
                    else:
                        belief_time = event_start - timedelta(
                            seconds=belief_horizon_in_sec,
                        )

                    forecast = Forecast(
                        event_start=event_start,
                        belief_horizon_in_seconds=belief_horizon_in_sec,
                        event_value=event_value,
                        sensor=sensor,
                        unit=unit,
                        created_at=belief_time,
                    )
                    forecasts.append(forecast)
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error processing line {i + 2}: {e}"),
                    )
                    continue
            # Verileri veritabanına kaydedin
            if forecasts:
                # Verileri veritabanına kaydedin
                Forecast.objects.bulk_create(forecasts)
                self.stdout.write(
                    self.style.SUCCESS(f"Imported {len(forecasts)} forecasts"),
                )
            else:
                self.stdout.write(self.style.WARNING("No forecasts were imported."))
