import floodsystem.geo as geo
import floodsystem.stationdata as stationdata

def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = stationdata.build_station_list()

    
    print(geo.rivers_by_station_number(stations, 9));

    
    


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")

    # Run Task1E
    run()