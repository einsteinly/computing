import floodsystem.geo as geo
import floodsystem.flood as flood
import floodsystem.stationdata as stationdata


# Build station list
stations = stationdata.build_station_list();
# Update water levels
stationdata.update_water_levels(stations);

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    result = flood.stations_highest_rel_level(stations, 10);

    # print result
    for item in result:
        print(item.name + '     ', item.relative_water_level());
    


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
