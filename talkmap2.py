#!/usr/bin/env python3

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks.
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob
import getorg
#from geopy import Nominatim

class Coordinate:
    def __init__(self,lati,long):
        self.latitude = lati
        self.longitude = long

g = glob.glob("_talks/*.md")

#geocoder = Nominatim(user_agent="my-talkmapgenerator/1.0")
location_dict = {}
location = ""
permalink = ""
title = ""

for file in g:
    with open(file, 'r') as f:
        print(file)
        lines = f.read()
        if lines.find('location: "') > 1:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]
        if lines.find('longitude: "') > 1:
            loc_start = lines.find('longitude: "') + 12
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            longitude = lines_trim[:loc_end]
        if lines.find('latitude: "') > 1:
            loc_start = lines.find('latitude: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            latitude = lines_trim[:loc_end]

        location_dict[location] = Coordinate(latitude,longitude)
        print(location, "\n", location_dict[location].latitude,location_dict[location].longitude)

#for user, loca in location_dict.items():
    #print(user,loca)

m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="./talkmap", hashed_usernames=False)
