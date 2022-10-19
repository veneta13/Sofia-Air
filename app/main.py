# imports
import streamlit as st
import pandas as pd
import utils

# read data
df = pd.read_csv('data/sample.csv')

# get stations
stations = df['station_name'].unique()

# create map and map stations
st.map(df)
