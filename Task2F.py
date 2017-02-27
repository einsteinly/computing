# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:59:02 2017

@author: Shengyuan
"""

import floodsystem.flood as flood
import floodsystem.plot as plot
import floodsystem.datafetcher as datafetcher
import floodsystem.stationdata as stationdata
import datetime

def run():
    # Build station list
    stations = stationdata.build_station_list();

    #create the list of stations of 10 highest level

    stations = flood.stations_highest_rel_level(stations, 10)

    for station in stations:
        dates, levels = datafetcher.fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=2))
        plot.plot_water_level_with_fit(station, dates, levels, 4)
    
    
if __name__ == "__main__":
    print("*** Task 2\f: CUED Part IA Flood Warning System ***")

    run()
    
