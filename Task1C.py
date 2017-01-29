import floodsystem.geo as geo
import floodsystem.stationdata as stationdata

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = stationdata.build_station_list()

    # Build list of stations within 10km from cambridge
    cam_coor = (52.2053, 0.1218);
    radius = 10; 
    stations_within_10_km = geo.stations_within_radius(stations, cam_coor, radius);

    # Compile list that contains only the names of the stations
    station_names = [station.name for station in stations_within_10_km];

    # Sort
    station_names = sorted(station_names);

    # print result
    print(station_names);
    


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
