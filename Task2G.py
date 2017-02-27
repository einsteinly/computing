# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:41:04 2017

@author: Shengyuan
"""
import floodsystem.geo as geo
import floodsystem.flood as flood
import floodsystem.stationdata as stationdata


# Build station list
stations = stationdata.build_station_list();
# Update water levels
stationdata.update_water_levels(stations);

def run():
    """Requirements for Task 2G"""

    # Build list of stations
    result = flood.stations_highest_rel_level(stations, 30);

    # print result
    for item in result:
        if item.relative_water_level() > 10 and item.town != None:
            print(item.town  + '  severe risk')
        elif item.relative_water_level() > 1.5 and item.town != None:
            print(item.town + '  high risk')
        elif item.relative_water_level() > 1 and item.town != None:
            print(item.town  + ' moderate risk')
        elif item.town != None:
            print(item.town + '  low risk')

    


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
