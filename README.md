# csv2gpx

A simple script to convert [data from flightradar24.com](https://www.flightradar24.com/blog/using-the-new-flightradar24-kml-and-csv-export-tools/) to a gpx track.

Just drop your csv files in the same folder, set a `start_Flighttime` and `end_Flighttime` in the script and run it. File names must contain a timestamp (YYYYMMDD_uniqueflightid.csv).

You can animate the air traffic using the Time Manager plugin in QGIS, [trackanimation](https://github.com/JoanMartin/trackanimation), [RunParticles](https://github.com/dal/RunParticles) or [GPX animator](https://github.com/zdila/gpx-animator).