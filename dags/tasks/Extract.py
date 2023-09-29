import pandas as pd 
import requests
from datetime import datetime
import datetime
from .utils.Interceptor import *
import time

pd.set_option('display.max_columns', None)

# Creating an function to be used in other pyrhon files
def return_dataframe():
    unix_time = time.time()
    current_unix_time = int(unix_time)

    # Download all songs you've listened to "after yesterday", which means in the last 24 hours
    data = sp.current_user_recently_played()
    # data = r.json()
    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Extracting only the relevant bits of data from the json object      
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    # Prepare a dictionary in order to turn it into a pandas dataframe below
    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list,
        "timestamp": timestamps
    }
    song_df = pd.DataFrame(song_dict, columns=["song_name", "artist_name", "played_at", "timestamp"])
    return song_df
    # print(song_df)
#
# return_dataframe()