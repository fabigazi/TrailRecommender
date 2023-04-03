import math

from preprocess_data import *
from filter_dataframe import *
from calculate_similarity import *
from sort_df import *
import customtkinter
from PIL import Image
import tkinter as tk
from tkinter import ttk
import pandas as pd

import os

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


def states():
    return ["None", "MA", "NH", "MI", "VT", "CT", "RI"]


df_sorted = pd.read_csv(r'C:\Users\fgazi\AllTrails.csv')

df_sorted = df_sorted[['name', 'area_name', 'city_name', 'state_name']]
df_sorted = df_sorted.rename(
    columns={'name': 'Trail Name', 'area_name': 'Area', 'city_name': 'City', 'state_name': 'State'})


class TrailRec(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Trail Recommender")
        self.geometry(f"{1100}x{660}")

        # when defining the row and col of the over arching grid

        # create tabview
        self.tab_view_filters = customtkinter.CTkTabview(self, width=250, height=100)
        self.tab_view_filters.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tab_view_filters.add("Trail Preferences")
        self.tab_view_filters.add("Features")
        self.tab_view_filters.tab("Trail Preferences").grid_columnconfigure(3, weight=1)  # configure grid of
        # individual tabs
        self.tab_view_filters.tab("Features").grid_columnconfigure(0, weight=1)

        # self.tabview.tab("tabX") assigns the obect to the given tabX tab
        self.states_menu = customtkinter.CTkOptionMenu(self.tab_view_filters.tab("Trail Preferences"),
                                                       dynamic_resizing=True,
                                                       values=states())

        self.states_menu.grid(row=0, column=0, padx=20, pady=(10, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tab_view_filters.tab("Trail Preferences"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=0, column=1, padx=20, pady=(10, 10))

        self.switch_dog_friendly = customtkinter.CTkSwitch(self.tab_view_filters.tab("Trail Preferences"),
                                                           text=f"Dog Friendly")
        self.switch_dog_friendly.grid(row=0, column=2, padx=20, pady=(10, 10))

        self.search_button = customtkinter.CTkButton(self.tab_view_filters.tab("Trail Preferences"), text="Search",
                                                     command=self.open_input_dialog_event)
        self.search_button.grid(row=2, column=5, padx=20, pady=(10, 10))

        # added to the features tab
        self.feature_switches = []

        features = ["beach", "cave", "city-walk", "forest", "historic-site", "hot-springs", "lake", "partially-paved",
                    "paved", "rails-trails", "river", "views", "waterfall", "wild-flowers", "wildlife"]
        for i in range(len(features)):
            switch = customtkinter.CTkSwitch(self.tab_view_filters.tab("Features"),
                                             text=features.__getitem__(i))
            switch.grid(row=math.floor(i / 5), column=i - math.floor(i / 5) * 5, padx=10, pady=(10, 10))
            self.feature_switches.append(switch)

        # tree view frame
        self.treeview_frame = ttk.Treeview(self, height=10, padding=1, show="headings")
        self.treeview_frame.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.treeview_frame['columns'] = list(df_sorted.columns)

        # Create heading columns
        for column in df_sorted.columns:
            self.treeview_frame.heading(column, text=column)

    def open_input_dialog_event(self):
        # Add df rows to treeview
        user_preferences = {"trail-running": (1, .05), "length": (5000, .05), "loop": (1, .0)}
        #user_preferences = {"trail-running": (1, .05), "length": (5000, .05)}
        user_location = {'lat': 45.316094085851695, 'lng': -69.3804148103108}
        distance_threshold = 90

        # get trails data path
        current_directory = os.getcwd()
        trail_data_path = os.path.abspath(os.path.join(current_directory, os.pardir)) + "/data/trails.csv"

        # if you have issues with the file path (like me) you can just hardcode it trail_data_path =
        # '/Users/btwitchell/OneDrive - Northeastern University/Classes/5800/final
        # project/TrailRecommender/data/trails.csv'

        # flow of function calls to return dataframe ranked by user preference
        df = preprocess_data(trail_data_path)
        df_filtered = filter_dataframe(user_location, distance_threshold, df)
        df_filtered = calculate_similarity(user_preferences, df_filtered)
        df_sorted = sort_df(df_filtered)

        for index, row in df_sorted.iterrows():
            self.treeview_frame.insert("", tk.END, values=list(row))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = TrailRec()
    app.mainloop()
