import pandas as pd
import matplotlib.pyplot as plt

from gpx_collect import gpx_to_dict
from data_visualization import show_on_map, plot_df_flatten
from data_process import augment_df

gpx_dict = gpx_to_dict()
gpx_df = pd.DataFrame(gpx_dict)
augment_df(gpx_df)
show_on_map(gpx_df)
# plot_df_flatten(gpx_df, x='elapsed_dist', y='instant_speed(km/h)', flat=20)