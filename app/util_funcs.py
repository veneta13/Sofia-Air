import pandas as pd
import streamlit as st


@st.experimental_singleton
def load_data():
    return pd.read_csv(
        'data/Archive_Sofia_stations_processed.csv',
        nrows=10000
    )


def read_data():
    return load_data()


def show_by_location(df, locations):
    return df[df['station_name'].apply(lambda x: x in locations)]


def show_by_time(df, time):
    # print(datetime.fromisoformat(df.iloc[0]['timest']))
    pass


def map(df, stations, time):
    return st.map(show_by_location(df, stations))
