import floodsystem.geo as geo
import floodsystem.stationdata as stationdata
import floodsystem.map as map

def run():
    """Run script for extensions"""

    # Build list of stations
    stations = stationdata.build_station_list()

    map.plot_map_with_MornitoringStations(stations);

if __name__ == "__main__":
    print("*** Einsteinly: Extensions ***")

    # Run Task1A
    run()
