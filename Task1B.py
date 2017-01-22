from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Build list of stations sorted by distance
    cam_coor = (52.2053, 0.1218);
    sorted_stations = stations_by_distance(stations, cam_coor);

    # Count number of stations and print
    print("Number of stations: {}".format(len(stations)))

    # Compile list from closest 10 stations:
    closest_stations = [(item[0].name, item[0].town, item[1]) for item in sorted_stations[:10]];
    print("Closest 10 stations: {}".format(closest_stations));

    # Compile list from furthest 10 stations:
    furthest_stations = [(item[0].name, item[0].town, item[1]) for item in sorted_stations[-10:]];
    print("Furthest 10 stations: {}".format(furthest_stations));


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
