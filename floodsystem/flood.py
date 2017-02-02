'''
    Flood module that provides functionality related to the analysis of flood risks
'''

def stations_level_over_threshold(stations, tol):
    '''
        returns a sorted list of tuples, that hold (1) station at which the latest relative water level is over tol and (2) the relative water level at the station
    '''
    # initialise an empty list
    result = [];

    for station in stations:
        #first check that the data exists
        if station.relative_water_level() != None:
            if station.relative_water_level() > tol:
                # append a tuple to the list
                result.append( (station, station.relative_water_level()) ) ;

    #sort the result in reverse order
    return sorted(result, key = lambda result_element: result_element[1], reverse = True);


def stations_highest_rel_level(stations, N):
    '''
        returns a sorted list (descending order) of the N stations at which the water level, relative to the typical range, is highest
    '''

    station_with_rel_level = [(station, station.relative_water_level()) for station in stations];

    #sort the stations in reverse order by water level
    station_with_rel_level = sorted(station_with_rel_level, key = lambda elem: elem[1], reverse = True);

    result = [];
    #Build the required list with only station as the list elements
    for tup in station_with_rel_level:
        result.append(tup[0]);

    # return required N elements in the list
    return result[:N];