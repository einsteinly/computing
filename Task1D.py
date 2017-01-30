import floodsystem.geo as geo
import floodsystem.stationdata as stationdata

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = stationdata.build_station_list()

    # Build list of rivers with stations
    rivers = sorted( geo.rivers_with_station(stations) );
    rivers_restricted = set();
    i = 1;
    for river in rivers:
        rivers_restricted.add(river);
        i += 1;
        if i > 10:
            break;
    print(sorted(rivers_restricted));
    


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
