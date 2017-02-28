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
    if station.name == 'Cam':
        station_cam = station
        break

# Fetch data over past 10 days
dt = 10
dates, levels = datafetcher.fetch_measure_levels(station_cam.measure_id,
                                     dt=datetime.timedelta(days=dt))
p=4

def test_plot_water_levels():
	#Test that the function runs without error to give the required plot for a single function
	assert plot.plot_water_levels(station_cam, dates, levels);

def test_plot_water_level_with_fit():
      #Test that the function runs without error to give the required plot for a single function
      assert plot.plot_water_level_with_fit(station_cam, p)