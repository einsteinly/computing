import datetime
import plotly
import plotly.graph_objs as go
import floodsystem.analysis as analysis
import matplotlib.pyplot as plt
import numpy as np
import floodsystem.stationdata as stationdata
import floodsystem.datafetcher as datafetcher



def plot_water_levels(stations, dates, levels):
    '''
        displays a plot of the water level data against time for a station, and include on the plot lines for the typical low and high levels
        arguments: list of stations, dates: list of arrays of date objects, levels: list of arrays of water levels

        if a single set of station, dates and levels are passed into the function, it will plot only that station and its ranges
    '''
    data = [];

    #Default file name
    filename = "water levels plot.html";

    if type(stations) == list:
        # if the input parameters include more than one set of data

        for key, station in enumerate(stations):
            data.append(go.Scatter(x=dates[key],y=levels[key], name=station.name) );

    else:
        # Otherwise plot only one station and its ranges
        data.append(go.Scatter(x=dates,y=levels, name=stations.name));
        #Plot the ranges if they are defined
        if stations.typical_range != None:
            data.append(go.Scatter(x=dates,y=[stations.typical_range[0]]*len(dates), name="Typical low range") );
            data.append(go.Scatter(x=dates,y=[stations.typical_range[1]]*len(dates), name="Typical high range") );

        #name the file the name of the station
        filename = stations.name;

    layout = dict( title = 'Water Levels Plot',
        xaxis = dict(title='Dates'),
        yaxis = dict(title='Water level'),
        showlegend = True);
    
    return plotly.offline.plot(dict(data=data,layout=layout), filename=filename);

def plot_water_level_with_fit(station, p):
    stationdata.update_water_levels([station])
    dates=[]
    levels=[]
    temp_dates=[]
    temp_levels=[]
    temp_dates, temp_levels = datafetcher.fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=2))
    for date in temp_dates:
        now = datetime.datetime.utcnow()
        date = (date.replace(tzinfo=None) - now).total_seconds()
        dates.append(date)
    for level in temp_levels:
            levels.append(level)
    if dates != []:
        poly = analysis.polyfit(dates, levels, p)
    
    
    
        plt.plot(dates, poly(dates))
        plt.plot(dates,levels)

    # Display plot
        plt.show()
    return True
    
