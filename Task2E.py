import pytest
import floodsystem.stationdata as stationdata
import floodsystem.plot as plot
import floodsystem.datafetcher as datafetcher
import floodsystem.flood as flood
import datetime

# Build station list
stations = stationdata.build_station_list();
# Update water levels
stationdata.update_water_levels(stations);

def run():
    # Build list of stations with relative water levels
    stations_by_rel_level = flood.stations_highest_rel_level(stations, 5);

    # Fetch data over past 10 days and compile required dates and levels lists for plotting
    dt = 10
    dates = [];temp_dates = [];
    levels = [];temp_levels = [];

    for station in stations_by_rel_level:
        temp_dates, temp_levels = datafetcher.fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=dt))
        dates.append(temp_dates);
        levels.append(temp_levels);

    # Plot required graphs
    plot.plot_water_levels(stations_by_rel_level, dates, levels);

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    run()
