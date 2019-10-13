from .gpx_class import GPX
import pandas as pd
from datetime import datetime

from pathlib import Path

topografix_tag = '{http://www.topografix.com/GPX/1/1}'
garmin_tag = '{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}'

def extract_tracker_point_data(tracker_point, timezone_delta = '+02:00'):
    """
    :GPX tracker_point: 
    :return dict:
    """
    extracted_data = {}
    #Get latitude ang longitude from the tracker_point attributes
    extracted_data['lat'] = float(tracker_point.attrib()['lat'])
    extracted_data['lon'] = float(tracker_point.attrib()['lon'])
    #Get elevation and time from elements of the tracker_point
    extracted_data['ele'] = float(tracker_point.find('ele').text)
    str_time = tracker_point.find('time').text    # This contains the time in ISO format
    extracted_data['time'] = datetime.fromisoformat(str_time[:-1] + timezone_delta)
    # To get more data, we store the extensions of the tracker_point in another GPX object that will be queried with the garmin_tag
    tracker_extension = GPX(tree= tracker_point.find('extensions'), global_tag= garmin_tag)
    extracted_data['hr'] = float(tracker_extension.find('TrackPointExtension','hr').text) # This contains the heartrate
    extracted_data['cad'] = float(tracker_extension.find('TrackPointExtension','cad').text) # This contains the cadence

    return extracted_data

def add_dictionary(d1, d2):
    for key, value in d2.items():
        if key in d1.keys():
            d1[key].append(value)
        else:
            d1[key] = [value]

def gpx_to_dict(file_path = Path("helpers/Afternoon_Activity.gpx")):
    dict_data = {}
    gpx = GPX(file_path)
    tracker_points = gpx.findall('trk','trkseg','trkpt')
    for tracker_point in tracker_points:
        extracted_data = extract_tracker_point_data(GPX(tree=tracker_point))
        add_dictionary(dict_data,extracted_data)
    return dict_data
