import floodsystem.geo as geo
import floodsystem.stationdata as stationdata
import floodsystem.flood as flood

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = stationdata.build_station_list()

    # Update water levels
    stationdata.update_water_levels(stations);

    result = flood.stations_level_over_threshold(stations, .8);

    # print required data
    for item in result:
        print(item[0].name + '     ', item[1]);


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    # Run Task1A
    run()
