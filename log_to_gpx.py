#!/usr/bin/env python

# Generate JSON from a LOCUS log file
# (c) 2013 Don Coleman

import locus
import json
import datetime
from shutil import copyfile

coords = locus.parseFile('sample2.log')

# filter out bad data
coords = [c for c in coords if c.fix > 0 and c.fix < 5]

class Encoder(json.JSONEncoder):
    def default(self, obj):
    	if isinstance(obj, locus.Coordinates):
    		return obj.__dict__

        if isinstance(obj, datetime.datetime):
    	    return obj.strftime("%Y-%m-%dT%H:%M:%S%z")

        return json.JSONEncoder.default(self, obj)

def spaces(n):
    return n * ' '
coords_json = json.loads(json.dumps(coords, cls = Encoder, sort_keys=True, indent=4))

start_time = coords_json[0]['datetime']

file_name = start_time + '.gpx'
copyfile('gpx_header.txt', file_name)

with open(file_name, 'a') as new_file:
    num_spaces = 1
    new_file.write(spaces(num_spaces) + '<metadata>\n')
    num_spaces += 1
    new_file.write(spaces(num_spaces) + '<time>' + start_time + '</time>\n')
    num_spaces -= 1
    new_file.write(spaces(num_spaces) + '</metadata>\n')
    new_file.write(spaces(num_spaces) + '<trk>\n')
    num_spaces += 1
    new_file.write(spaces(num_spaces) + '<name>' + start_time + ' Run' + '</name>\n')
    new_file.write(spaces(num_spaces) + '<type>9</type>\n')
    new_file.write(spaces(num_spaces) + '<trkseg>\n')
    num_spaces += 1
    for coord in coords_json:
        new_file.write(spaces(num_spaces) + '<trkpt lat="' + str(coord['latitude']) + '"' + ' lon="' + str(coord['longitude']) + '">\n')
        num_spaces += 1
        new_file.write(spaces(num_spaces) + '<ele>' + str(coord['height']) + '</ele>\n')
        new_file.write(spaces(num_spaces) + '<time>' + coord['datetime'] + 'Z</time>\n')
        num_spaces -= 1
        new_file.write(spaces(num_spaces) + '</trkpt>\n')
    num_spaces -= 1
    new_file.write(spaces(num_spaces) + '</trkseg>\n')
    num_spaces -= 1
    new_file.write(spaces(num_spaces) + '</trk>\n')
    num_spaces - 1
    new_file.write(spaces(num_spaces) + '</gpx>')

