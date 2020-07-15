# csv2gpx

A simple script to convert Flightradar24 [csv files](https://www.flightradar24.com/blog/using-the-new-flightradar24-kml-and-csv-export-tools/) to a gpx track for an animated dataviz.

Just drop your csv files from the `YYYYMMDD_positions.zip` file in the same folder, set up
- `start_Flighttime`
- `end_Flighttime`
- `filename_Year`
- `filename_Month`
- `filename_Day`

in the script and run it.

You can visualize the air traffic using the Time Manager plugin in QGIS, [trackanimation](https://github.com/JoanMartin/trackanimation), [RunParticles](https://github.com/dal/RunParticles) or [GPX animator](https://github.com/zdila/gpx-animator).
