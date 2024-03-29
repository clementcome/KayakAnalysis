# Kayak Analysis
This project aims at retrieving data from gpx files and analysing and visualize this data.

## Acquired skills
- Retrieving data from xml files
- Creating a custom class to ease gpx file reading
- Handling the creation of custom packages
- Use of `*args` in the definition of function to handle various parameters
- Use of pandas DataFrames
- Visualizing with plotly and its extension plotly express

## Organization of the project

There are 3 custom packages : `gpx_collect, data_process, data_visualization`, a helpers directory containing examples of gpx. And finally, there is the `main.py` which is the only file that should be executed because the project involves package dependencies. From this file, function defined in the 3 packages can be called.

### `gpx_collect` package
This package allows us to retrieve the data from gpx files in a python dictionary really easy to use and to convert into a pandas DataFrame.

### `data_process` package
This package allows us to generate the relevant data from the dictionary extracted by the previous package into a pandas DataFrame, such as distance, speed, total time, etc...

### `data_visualization` package
This package allows us to visualize the data generated by the previous package using an interactive plotting library : `plotly`.