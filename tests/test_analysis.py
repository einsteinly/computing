# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:36:11 2017

@author: Shengyuan
"""
import floodsystem.flood as flood
import floodsystem.plot as plot
import floodsystem.datafetcher as datafetcher
import floodsystem.stationdata as stationdata
import datetime
import floodsystem.analysis as analysis
import numpy
import pytest

def test_polyfit():
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
            assert type(analysis.polyfit(dates, levels, 4)) == numpy.poly1d

   