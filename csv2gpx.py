#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import os
import sys
import datetime, time

#####################
start_Flighttime = 8 # convert all flights from this hour...
end_Flighttime = 9 # ...to this.
filename_Year = 2019 # year in your csv files
filename_Month = 6 # month in your csv files
filename_Day = 7 # day in your csv files
#####################

cwd = os.getcwd()
in_files = [f for f in listdir(cwd) if isfile(join(cwd, f))]
# First argument is the name of the gpx file
out_file = open(sys.argv[0]+".gpx","w") 
out_file.write("<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\"?>\n<gpx version=\"1.1\" creator=\"csv2gpx\" xmlns=\"http://www.topografix.com/GPX/1/1\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd\">\n")

# Timezone from the local computer
start_time = int(time.mktime(datetime.datetime(filename_Year, filename_Month, filename_Day, start_Flighttime, 0, 0).timetuple()))
end_time = int(time.mktime(datetime.datetime(filename_Year, filename_Month, filename_Day, end_Flighttime, 0, 0).timetuple()))

file_count = 0
for in_file in in_files:
	if in_file.endswith(".csv"):
		file_count += 1
		print(in_file + " {0}".format(file_count))
		with open(in_file) as f:
			lis = [line.split() for line in f]        # create a list of lists
			lines = []
			for i, x in enumerate(lis):              #print the list items 
				if i != 0:
					line = x[0].split(",")
					if start_time <= int(line[0]) < end_time:
						lines.append(line)
		if len(lines) != 0:
			out_file.write("<trk>\n  <name>"+in_file[:-4]+"</name>\n  <trkseg>\n")
			for line in lines:
				time = datetime.datetime.fromtimestamp(int(line[0])).strftime('%Y-%m-%dT%H:%M:%SZ')
				out_file.write("    <trkpt lat=\""+line[3]+"\" lon=\""+line[4]+"\">\n"+"      <time>"+time+"</time>\n"+"    </trkpt>\n")
			out_file.write("  </trkseg>\n</trk>\n")

out_file.write("</gpx>")
out_file.close()
