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
    
    # Build dict of stations by river
    stations_by_river_result = geo.stations_by_river(stations);
    
    # Compile stations in the required rivers
    result = {};
    result["River Aire"] = [];
    result["River Cam"] = [];
    result["Thames"] = [];
    for station in stations_by_river_result["River Aire"]:
        result["River Aire"].append(station.name);
    for station in stations_by_river_result["River Cam"]:
        result["River Cam"].append(station.name);
    for station in stations_by_river_result["Thames"]:
        result["Thames"].append(station.name);
    
    # Sort result and print
    result["River Aire"] = sorted(result["River Aire"]);
    result["River Cam"] = sorted(result["River Cam"]);
    result["Thames"] = sorted(result["Thames"]);
    print(result)

    
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
