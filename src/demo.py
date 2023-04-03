'''
#all the external packages necessary:
pip install pandas, sklearn, numpy, ast, geopy, gower
'''
from preprocess_data import *
from filter_dataframe import *
from calculate_similarity import *
from sort_df import *
import os
from pathlib import Path

'''
Demo of trail recommender algorithm
'''


def demo():
    # setting user preferences
    user_preferences = {"trail-running": (1, .05), "length": (5000, .05), "loop": (1, .9)}
    user_location = {'lat': 45.316094085851695, 'lng': -69.3804148103108}
    distance_threshold = 90

    # get trails data path
    current_directory = os.getcwd()
    trail_data_path = os.path.abspath(os.path.join(current_directory, os.pardir)) + "/data/trails.csv"

    # if you have issues with the file path (like me) you can just hardcode it
    # trail_data_path = '/Users/btwitchell/OneDrive - Northeastern University/Classes/5800/final project/TrailRecommender/data/trails.csv'

    # flow of function calls to return dataframe ranked by user preference
    df = preprocess_data(trail_data_path)
    df_filtered = filter_dataframe(user_location, distance_threshold, df)
    df_filtered = calculate_similarity(user_preferences, df_filtered)
    df_sorted = sort_df(df_filtered)

    # displaying the dataframe in the terminal with trail name
    print(df_sorted[["name", "area_name"] + [key for key in user_preferences.keys()]].head(10))


if __name__ == "__main__":
    demo()
