"""Unit test for geo module"""

import pytest
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    
    cam_coor = (52.2053, 0.1218);

    stations = build_station_list();
    sorted_stations = stations_by_distance(stations, cam_coor);

    #Test that the function stations_by_distance runs
    assert sorted_stations;

    #Test that a list is returned
    assert 	isinstance(sorted_stations, list);