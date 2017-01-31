"""Unit test for geo module"""

import pytest
import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
import floodsystem.map


cam_coor = (52.2053, 0.1218);
stations = build_station_list();

def test_plot_map_with_MornitoringStations():
    
    #Test that the function stations_by_distance runs
    assert floodsystem.map.plot_map_with_MornitoringStations(stations, _plot = False);
