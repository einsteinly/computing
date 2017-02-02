import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import plotly
import plotly.graph_objs as go


def plot_water_levels(stations, dates, levels):
	'''
		displays a plot of the water level data against time for a station, and include on the plot lines for the typical low and high levels
		arguments: list of stations, dates: list of arrays of date objects, levels: list of arrays of water levels
	'''

	data = [];

	for key, station in enumerate(stations):
		data.append(go.Scatter(x=dates[key],y=levels[key], name=station.name) );
	layout = dict( title = 'Water Levels Plot',
		xaxis = dict(title='Dates'),
		yaxis = dict(title='Water level'),
		showlegend = True);
	
	return plotly.offline.plot(dict(data=data,layout=layout), filename='water levels plot.html');