import streamlit as st
from datetime import datetime

def show_by_location(df, locations):
    return df[df['station_name'].apply(lambda x : x in locations)]

def show_by_time(df, time):
    # print(datetime.fromisoformat(df.iloc[0]['timest']))
    pass

def map(df, stations, time):
    return st.map(show_by_location(df, stations))

