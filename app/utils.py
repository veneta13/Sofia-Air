def show_by_location(df, locations):
    return df['station_name'].apply(lambda x : x in locations)
