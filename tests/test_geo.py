"""Unit test for geo module"""

import pytest
import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    
    cam_coor = (52.2053, 0.1218);

    stations = build_station_list();
    sorted_stations = geo.stations_by_distance(stations, cam_coor);

    #Test that the function stations_by_distance runs
    assert sorted_stations;

    #Test that a list is returned
    assert  isinstance(sorted_stations, list);

    #Test that stations_within_radius function runs without error
    assert geo.stations_within_radius(stations, cam_coor, 10);

    #Test that stations_within_radius function returns a list
    assert  isinstance(geo.stations_within_radius(stations, cam_coor, 10), list);
    