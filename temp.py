import pytest
from floodsystem.station import MonitoringStation
import floodsystem.stationdata as stationdata
import floodsystem.plot as plot
import floodsystem.datafetcher as datafetcher
import datetime

# Build station list
stations = stationdata.build_station_list();
# Update water levels
stationdata.update_water_levels(stations);

# Find station 'Cam'
for station in stations:
    if station.name == 'Bedford':
        station_cam = station
        break

# Fetch data over past 10 days
dt = 10
dates, levels = datafetcher.fetch_measure_levels(station_cam.measure_id,
                                     dt=datetime.timedelta(days=dt))

if __name__ == "__main__":
	plot.plot_water_levels(station_cam, dates, levels);