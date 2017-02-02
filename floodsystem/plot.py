import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import plotly
import plotly.graph_objs as go


def plot_water_levels(station, dates, levels):
	'''
		displays a plot of the water level data against time for a station, and include on the plot lines for the typical low and high levels
		arguments: station, dates: array of date objects, levels: array of water levels
	'''
	x = dates;
	data = [go.Scatter(x=x,y=levels)];
	layout = dict( title=station.name,
		xaxis = dict(title='dates'),
		yaxis = dict(title='water level')
		 );
	plotly.offline.plot(dict(data=data,layout=layout), filename='water levels plot.html');

	return True;