# imports
import streamlit as st
import pandas as pd

# read data
df = pd.read_csv('data/Archive_Sofia_stations_processed.csv')

# get stations
stations = df['station_name'].unique()

# create map and map stations
st.map(df)
