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
    stationdata.update_water_levels(stations);

    #create the list of stations of 10 highest level
    stations = flood.stations_highest_rel_level(stations, 5)
    

    for station in stations:
        dates=[]
        levels=[]
        temp_dates=[]
        temp_levels=[]
        temp_dates, temp_levels = datafetcher.fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=2))
        for date in temp_dates:
            now = datetime.datetime.utcnow()
            date = (date.replace(tzinfo=None) - now).seconds
            dates.append(date)
        for level in temp_levels:
            levels.append(level)
        if dates != []:
            plot.plot_water_level_with_fit(station, dates, levels, 4)
        


    
    
if __name__ == "__main__":
    print("*** Task 2\f: CUED Part IA Flood Warning System ***")

    run()
    
