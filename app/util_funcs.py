import json

import pandas as pd
import streamlit as st


@st.experimental_singleton
def load_data():
    return pd.read_csv(
        'data/Archive_Sofia_stations_processed.csv',
        nrows=10000
    )


@st.experimental_singleton
def load_content():
    with open('res/content.json', encoding="utf8") as json_file:
        return json.load(json_file)


def read_data():
    return load_data()


def min_max_date(df):
    return (df["timest"].min(), df["timest"].max())


def show_by_location(df, locations):
    return df[df['station_name'].apply(lambda x: x in locations)]


def show_by_time(df, start_date, end_date):
    format = '%Y-%m-%d %H:%M:%S'

    print(f'start {start_date}')

    df['timest'] = pd.to_datetime(
        df['timest'],
        format=format
    )

    start_date = pd.to_datetime(
        start_date,
        format=format
    )

    end_date = pd.to_datetime(
        end_date,
        format=format
    )

    return df[
        (df['timest'] >= start_date) & \
        (df['timest'] <= end_date)
    ]


def map(df, stations, time):
    return st.map(show_by_location(df, stations))
