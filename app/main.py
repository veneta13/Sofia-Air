# imports
import streamlit as st
import pandas as pd
import util_funcs
from content import content

# consts
lang = 'en'

# page info
st.set_page_config(
    layout="centered",
    page_title=content['page_title'][lang],
    page_icon=":cloud:"
)

# read data
df = pd.read_csv('data/sample.csv')

# get selector data
stations = df['station_name'].unique()

# add multiselect
st.multiselect(
    content['ams_selector'][lang],
    options=stations,
    default=stations[0]
)

# create map and map stations
util_funcs.map(df, stations, None)
