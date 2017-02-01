"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key
from haversine import haversine

def stations_by_distance(stations, p):
    """This function takes two arguments: a list of stations and a coordinate p,
    and returns a sorted list of (station, distance) tuples, 
    where distance (float) is the distance of the station (MonitoringStation) from the coordinate p
    """
    sorted_stations = [];

    for station in stations:
        sorted_stations.append( (station, haversine(p, station.coord)) );

    return sorted_by_key(sorted_stations,1);


def stations_within_radius(stations, centre, radius):
    """
        Arguments: list of stations, coordinate of the centre - a tuple (x,y), and the required radius in km
        This function returns a list of stations that are within a radius 'radius' from coordinate 'centre'
    """

    sorted_stations = [];

    # get a list of stations with their respective stations from the centre
    sorted_stations = stations_by_distance(stations, centre);

    return [ station[0] for station in sorted_stations if station[1] <= radius ];

def rivers_with_station(stations):
    """
        returns a set of rivers that have at least one monitoring station
    """
    return { station.river for station in stations };

def stations_by_river(stations):
    """
        returns a dictionary that maps river names to a LIST of stations
    """
    dictionary = {};
    rivers = rivers_with_station(stations);
    for river in rivers:
        #initialise list for storing the stations
        dictionary[river] = [];
        for station in stations:
            #when the station's river matches, push into list
            if station.river == river:
                dictionary[river].append(station);

    return dictionary;