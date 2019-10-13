import plotly.express as px
import pandas as pd

def show_on_map(gpx_df):

    fig = px.line_mapbox(
        gpx_df.iloc[1:],
        lat='lat',
        lon='lon',
        zoom=13,
    )
    fig.update_layout(mapbox_style='open-street-map')
    fig.show()

def plot_df_flatten(df, x, y, flat = None):
    if flat == None:
        fig = px.line(df, x=x, y=y)
        fig.show()
    else:
        y_flat = list(df[y])
        y_flat = [sum(y_flat[i:i+flat])/flat for i in range(len(y_flat) - flat)]
        new_df = pd.DataFrame({x:list(df[x])[:len(y_flat)], y: y_flat})
        fig = px.line(new_df, x=x, y=y)
        fig.show()