import json
from statistics import mean

import folium
import pandas as pd
import streamlit as st


@st.experimental_singleton
def load_data():
    df = pd.read_csv(
        'data/Archive_Sofia_stations_processed.csv'
    )
    df['timest'] = df['timest'].apply(lambda x: x.split(' ')[0])
    grouped_df = df.groupby(
        ['timest', 'station', 'param']).agg(
        {
            'longitude': 'first',
            'latitude': 'first',
            'station_name': 'first',
            'param_name': 'first',
            'level': mean,
        })
    return grouped_df.reset_index()


@st.experimental_singleton
def load_full_data():
    df = pd.read_csv(
        'data/Archive_Sofia_stations_processed.csv'
    )
    df['timest'] = df['timest'].apply(lambda x: x.split(' ')[0])
    return df


@st.experimental_singleton
def load_content():
    with open('res/content.json', encoding="utf8") as json_file:
        return json.load(json_file)


@st.experimental_singleton
def load_levels():
    with open('res/levels.json', encoding="utf8") as json_file:
        return json.load(json_file)


def read_data():
    return load_data()


def min_max_date(df):
    return (df["timest"].min(), df["timest"].max())


def show_by_location(df, locations):
    return df[df['station_name'].apply(lambda x: x in locations)]


def show_by_metric(df, metric):
    return df[df['param_name'] == metric]


def show_by_metrics(df, metrics):
    return df[df['param_name'].isin(metrics)]


def show_by_time(df, start_date, end_date=None):
    format = '%Y-%m-%d'

    temp_df = df['timest'].copy()
    temp_df = pd.to_datetime(
        temp_df,
        format=format
    )

    start_date = pd.to_datetime(
        start_date,
        format=format
    )

    if not end_date:
        df = df[temp_df == start_date]
    else:
        end_date = pd.to_datetime(
            end_date,
            format=format
        )
        df = df[(temp_df >= start_date) & (temp_df <= end_date)]
    return df


def map(df, stations, time):
    return st.map(show_by_location(df, stations))


def get_icon(level, regulations_all, type):
    color = 'lightblue'

    if type in regulations_all:
        regulation = regulations_all[type]
        value = level / regulation

        if value < .70:
            color = 'lightblue'
        elif value < 0.99:
            color = 'orange'
        else:
            color = 'red'

    return folium.Icon(
        icon='cloud',
        color=color,
        icon_color='white'
    )
