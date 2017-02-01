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