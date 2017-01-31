"""
    This module provides functionality for map-related functions, eg. plotting stations on a map.
"""
import plotly
from . import geo
from . import stationdata

def plot_map_with_MornitoringStations(stations):
    # scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
    #     [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

    # Build map data for use

    map_data = dict(longitude=[], lattitude=[], text=[]);
    for station in stations:
        map_data["longitude"].append(station.coord[0]);
        map_data["lattitude"].append(station.coord[1]);
        map_data["text"].append(station.name);

    # print(map_data);
    data = [ dict(
            type = 'scattergeo',
            # locationmode = 'UK',
            lat = map_data["longitude"],
            lon = map_data['lattitude'],
            text = map_data['text'],
            mode = 'markers',
            marker = dict( 
                size = 3, 
                opacity = 0.8,
                reversescale = True,
                autocolorscale = False,
                symbol = 'square',
                color='#2391fe'
            ))]

    layout = dict(
            title = 'Water level monitoring stations in the UK',
            colorbar = True,   
            geo = dict(
                scope='europe',

                showland = True,
                showrivers = True,
                showocean = True,
                showlakes = True,
                showsubunits = True,
                showcountries = True,
                showcoastlines = True,

                oceancolor = "#afd3ed",
                landcolor = "rgb(212, 212, 212)",
                subunitcolor = "rgb(255, 255, 255)",
                countrycolor = "rgb(255, 255, 255)",
                lakecolor = "#dbf0ff",
                resolution = 50,
                lonaxis = dict(
                    range = [-6,2],
                    showgrid = True,
                    dtick = 2.0
                    ),
                lataxis = dict(
                    range = [50,59],
                    showgrid = True,
                    dtick = 2.0
                    )
            ),
        )

    fig = dict( data=data, layout=layout )
    return plotly.offline.plot( fig, validate=False, filename='ia_computing_generated_map.html' )