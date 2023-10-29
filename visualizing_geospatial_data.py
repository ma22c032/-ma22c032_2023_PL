# -*- coding: utf-8 -*-
"""Visualizing_geospatial_data

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/174Jts_nUtfxm-xlTUZQHayyRjx3B5hfl
"""

# Commented out IPython magic to ensure Python compatibility.
!pip install cartopy # for numerical operations.
import numpy as np  # for creating plots and visualizations.
import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd # or working with data in tabular form
import geopandas as gpd # for handling geospatial data.
from cartopy import crs # for cartographic projections.

#reads a GeoDataFrame from a built-in GeoPandas dataset named 'naturalearth_lowres'
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
type(world) # checks the type of the 'world' variable,

type(world.geometry)

world.geometry.name # gets the name of the column that holds the geometry information in the GeoDataFrame.

world.head() #  displays the first few rows of the GeoDataFrame 'world'.

world.plot() # plots the 'world' GeoDataFrame, showing the world map.

type(world.centroid)

# reates a new column 'centroids' in the GeoDataFrame by calculating the centroids of the existing geometries.
world['centroids'] = world.centroid
world.head() # displays the first few rows of the GeoDataFrame after adding the 'centroids' column.

world = world.set_geometry('centroids') # change the active geometrycolumn
world.plot();

crs.PlateCarree() # creates a Plate Carrée (WGS 84) coordinate reference system

world.crs # checks the CRS of the 'world' GeoDataFrame

world = world.set_geometry('geometry') # set the active geometry
world.plot(); plt.title('World in WGS 84 CRS');

world_Mercator = world.to_crs("EPSG:3395") # transforms the GeoDataFrame to a Mercator CRS (EPSG:3395)
world_Mercator.plot(); # plots the GeoDataFrame after transforming it to Mercator CRS
plt.title('World in Mercator CRS');

ae = crs.AzimuthalEquidistant() #Azimuthal Equidistant projection (AE) is defined as ae
type(ae) # checks the type of the ae variable

aeproj4 = ae.proj4_init # Convert to`proj4` string/dict usablein gpd
world_ae = world.to_crs(aeproj4) # Then call to_crs method
world_ae.plot()

# reates a new Azimuthal Equidistant projection with a custom central longitude (200) and central latitude (10)
crs.AzimuthalEquidistant(central_longitude=200, central_latitude=10)

aea = crs.AlbersEqualArea() # Albers Equal Area projection (AEA) is defined as aea.
aea

aea_geo = [aea.project_geometry(ii, src_crs=ae) # projects the geometries from the world_ae GeoDataFrame
for ii in world_ae['geometry'].values]

fig, ax = plt.subplots(subplot_kw={'projection': aea})
ax.add_geometries(aea_geo, crs=aea);

# creates a new GeoDataFrame with the projected geometries and Albers Equal Area projection as its CRS and then plots it
gpd.GeoDataFrame(world, geometry=aea_geo, crs=aea.proj4_init).plot();

!pip install gitpython
import os
from git import Repo

covidfolder = '../../data_external/covid19' #defines a local folder path where COVID-19 data will be stored
if os.path.isdir(covidfolder): # if repo exists, pull newest data
  repo = Repo(covidfolder)
  repo.remotes.origin.pull()
else: # otherwise, clone from remote
  repo = Repo.clone_from('https://github.com/CSSEGISandData/COVID-19.git',covidfolder)

#onstructs the path to the 'csse_covid_19_time_series' directory within the cloned COVID-19 data repository.
datadir = repo.working_dir + '/csse_covid_19_data/csse_covid_19_time_series'

#creates the full file path to the 'time_series_covid19_confirmed_global.csv' file within the COVID-19 data repository.
f = datadir + '/time_series_covid19_confirmed_global.csv'

#reads the COVID-19 confirmed cases data from the specified CSV file into a Pandas DataFram
c = pd.read_csv(os.path.abspath(f))

#renames the 'Country/Region' column to 'country' and removes the first column, which contains index values.
c = c.rename(columns={'Country/Region': 'country'}).iloc[:, 1:]
c.head()

#calculates the difference between the total number of countries and the number of unique countries in the dataset
len(c['country']) - len(set(c['country']))

# groups the COVID-19 data by country, sums the cases across dates,
# and calculates the mean latitude ('Lat') and longitude ('Long') for each country.
cg = c.groupby('country')[c.columns[3:]].sum()
cg['Lat'] = c.groupby('country')['Lat'].mean()
cg['Long'] = c.groupby('country')['Long'].mean()

# creates a GeoPandas GeoSeries of point geometries using the latitude and longitude coordinates from the 'Lat' and 'Long' columns.
geo = gpd.points_from_xy(cg['Long'], cg['Lat'])

#projects the point geometries from the original coordinates to the Albers Equal Area projection (AEA) defined earlier.
c_aea_geo = [aea.project_geometry(ii) for ii in geo]

# creates a new GeoDataFrame ('cg') by combining the COVID-19 data with the projected geometries in the AEA projection.
cg = gpd.GeoDataFrame(cg, geometry=c_aea_geo, crs=aea.proj4_init)

def covidworldmap(date):
  fig, ax = plt.subplots(figsize=(12, 10))
  # put the world map on an axis
  w = gpd.GeoDataFrame(world, geometry=aea_geo, crs=aea.proj4_init)
  w.plot(ax=ax, color='midnightblue', edgecolor='darkslategray')
  ax.set_facecolor('dimgray')
  mx = cg.iloc[:, :-3].max().max() # get max across data
  # set marker sizes, with a min marker size for cases > 1000
  msz = 500 * np.where(cg[date]-1000, np.maximum(cg[date]/mx, 0.001), 0)
  cg.plot(ax=ax, cmap='Wistia', markersize=msz, alpha=0.5)
  ax.set_xticks([]) # remove axis marks
  ax.set_yticks([]);

covidworldmap('5/5/20')