import floodsystem.station as station
import floodsystem.stationdata as stationdata
def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = stationdata.build_station_list()

    print(station.inconsistent_typical_range_stations(stations))

    
if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")

    # Run Task1F
    run()