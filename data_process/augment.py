from haversine import haversine

def speed_km_h(distance,timedelta):
    return distance/timedelta.total_seconds()*3600

def augment_df(gpx_df):
    """
    :pd.DatatFrame gpx_df: Should contain at least columns 'lat, 'lon', 'time'
    """
    gpx_df['diff_time'] = gpx_df['time'].diff()
    gpx_df['elapsed_time'] = gpx_df['diff_time'][1:].cumsum()
    gpx_df['last_lat'] = gpx_df['lat'].shift()
    gpx_df['last_lon'] = gpx_df['lon'].shift()
    gpx_df['diff_dist'] = gpx_df.apply(lambda row: haversine((row['lat'], row['lon']), (row['last_lat'], row['last_lon'])), axis=1)
    gpx_df['elapsed_dist'] = gpx_df['diff_dist'].cumsum()
    gpx_df['instant_speed(km/h)'] = gpx_df.apply(lambda row: speed_km_h(row['diff_dist'],row['diff_time']), axis=1)