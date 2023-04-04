import math

from preprocess_data import *
from filter_dataframe import *
from calculate_similarity import *
from sort_df import *
import customtkinter
import tkinter as tk
from tkinter import ttk
import pandas as pd

import os

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

latitude = 45.316094085851695
longitude = -69.3804148103108

df_sorted = df = pd.DataFrame({'name': pd.Series(dtype='str'),
                               'area_name': pd.Series(dtype='str'),
                               'city_name': pd.Series(dtype='str'),
                               'state_name': pd.Series(dtype='str')})

df_sorted = df_sorted[['name', 'area_name', 'city_name', 'state_name']]
df_sorted = df_sorted.rename(
    columns={'name': 'Trail Name', 'area_name': 'Area', 'city_name': 'City', 'state_name': 'State'})
features = []

user_preferences = {}


class TrailRec(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.is_on = {}

        # configure window
        self.title("Trail Recommender")
        self.geometry(f"{1140}x{660}")

        # when defining the row and col of the over arching grid

        # create tabview
        self.tab_view_filters = customtkinter.CTkTabview(self, width=1100, height=100)
        self.tab_view_filters.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tab_view_filters.add("Trail Preferences")
        self.tab_view_filters.add("Features")
        self.tab_view_filters.tab("Trail Preferences").grid_columnconfigure(3, weight=1)  # configure grid of
        # individual tabs
        self.tab_view_filters.tab("Features").grid_columnconfigure(0, weight=1)

        # self.tabview.tab("tabX") assigns the obect to the given tabX tab
        self.popularity_entry = customtkinter.CTkEntry(self.tab_view_filters.tab("Trail Preferences"),
                                                       placeholder_text="Popularity")
        self.popularity_entry.grid(row=0, column=0, padx=20, pady=(10, 10))

        self.length_entry = customtkinter.CTkEntry(self.tab_view_filters.tab("Trail Preferences"),
                                                   placeholder_text="length in mi")
        self.length_entry.grid(row=0, column=1, padx=20, pady=(10, 10))

        self.elevation_entry = customtkinter.CTkEntry(self.tab_view_filters.tab("Trail Preferences"),
                                                      placeholder_text="elevation in ft")
        self.elevation_entry.grid(row=0, column=2, padx=20, pady=(10, 10))

        # self.slider_1 = customtkinter.CTkSlider(self.tab_view_filters.tab("Trail Preferences"), from_=0, to=1,
        #                                       number_of_steps=4)
        # self.slider_1.grid(row=0, column=3, padx=(20, 10), pady=(10, 10), sticky="ew")

        self.difficulty = customtkinter.CTkOptionMenu(self.tab_view_filters.tab("Trail Preferences"),
                                                      dynamic_resizing=True,
                                                      values=["Any Difficulty", "1", "2", "3", "4", "5"])

        self.difficulty.grid(row=0, column=3, padx=20, pady=(10, 10))

        activity = ["Any Activity", "backpacking", "bike-touring", "birding", "camping", "canoeing",
                    "cross-country-skiing", "fishing", "fly-fishing", "hiking", "horseback-riding", "ice-climbing",
                    "mountain-biking", "nature-trips", "off-road-driving", "paddle-sports", "road-biking",
                    "rock-climbing", "scenic-driving", "sea-kayaking", "skiing", "snowboarding", "surfing",
                    "trail-running", "walking", "whitewater-kayaking"]

        self.activity = customtkinter.CTkOptionMenu(self.tab_view_filters.tab("Trail Preferences"),
                                                    dynamic_resizing=False, values=activity)

        self.activity.grid(row=0, column=4, padx=20, pady=(10, 10))

        self.switch_dog_friendly = customtkinter.CTkSwitch(self.tab_view_filters.tab("Trail Preferences"),
                                                           text=f"Dog Friendly")
        self.switch_dog_friendly.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.lat_long = customtkinter.CTkButton(self.tab_view_filters.tab("Trail Preferences"), text="Lat & Long",
                                                command=self.input_latitude_and_longitude)
        self.lat_long.grid(row=0, column=5, padx=20, pady=(10, 10))

        self.search_button = customtkinter.CTkButton(self.tab_view_filters.tab("Trail Preferences"), text="Search",
                                                     command=self.run_search)
        self.search_button.grid(row=2, column=5, padx=20, pady=(10, 10))

        # added to the features tab
        self.feature_switches = []

        global features
        features = ["beach", "cave", "city-walk", "forest", "historic-site", "hot-springs", "lake", "partially-paved",
                    "paved", "rails-trails", "river", "views", "waterfall", "wild-flowers", "wildlife"]
        for i in range(len(features)):
            switch = customtkinter.CTkSwitch(self.tab_view_filters.tab("Features"),
                                             text=features.__getitem__(i))
            switch.grid(row=math.floor(i / 8), column=i - math.floor(i / 8) * 8, padx=10, pady=(10, 10))
            self.is_on[features[i]] = False
            self.feature_switches.append(switch)

        # tree view frame
        self.treeview_frame = ttk.Treeview(self, height=20, padding=1, show="headings")
        self.treeview_frame.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.treeview_frame['columns'] = list(df_sorted.columns)

        # Create heading columns
        for column in df_sorted.columns:
            self.treeview_frame.heading(column, text=column)

    def run_search(self):
        # Add df rows to treeview
        global user_preferences
        user_preferences = {"trail-running": (1, .05), "length": (5000, .05), "loop": (1, .0)}

        for i in range(len(features)):
            if self.feature_switches[i].__getattribute__("_check_state"):
                user_preferences[features[i]] = (1, .05)

        if not (self.popularity_entry.get() == ""):
            user_preferences["popularity"] = (int(self.popularity_entry.get()), .05)

        if not (self.length_entry.get() == ""):
            user_preferences["length"] = (int(self.length_entry.get()), .05)

        if not (self.elevation_entry.get() == ""):
            user_preferences["elevation_gain"] = (int(self.elevation_entry.get()), .05)

        if not (self.elevation_entry.get() == ""):
            user_preferences["elevation_gain"] = (int(self.elevation_entry.get()), .05)

        if not (self.difficulty.get() == "Any Difficulty"):
            user_preferences["difficulty_rating"] = (int(self.difficulty.get()), .05)

        if not (self.activity.get() == "Any Activity"):
            user_preferences[self.activity.get()] = (1, .05)

        user_location = {'lat': latitude, 'lng': longitude}
        distance_threshold = 1000

        # get trails data path
        current_directory = os.getcwd()
        trail_data_path = os.path.abspath(os.path.join(current_directory, os.pardir)) + "/data/trails.csv"

        # flow of function calls to return dataframe ranked by user preference
        df1 = preprocess_data(trail_data_path)
        df_filtered = filter_dataframe(user_location, distance_threshold, df1)
        df_filtered = calculate_similarity(user_preferences, df_filtered)
        global df_sorted
        df_sorted = sort_df(df_filtered)
        # print(df_sorted)

        reduced_df = df_sorted[["name", "area_name", "city_name", "state_name"]]

        for index, row in reduced_df.iterrows():
            self.treeview_frame.insert("", tk.END, values=list(row))

    def input_latitude_and_longitude(self):
        dialog = customtkinter.CTkInputDialog(text="Latitude, Longitude in degrees separated by a comma",
                                              title="Latitude")
        try:
            split = dialog.get_input().split(",")
            global latitude
            global longitude
            latitude = float(split[0])
            longitude = float(split[1])
        except ValueError:
            self.input_latitude_and_longitude()


if __name__ == "__main__":
    app = TrailRec()
    app.input_latitude_and_longitude()
    app.mainloop()
