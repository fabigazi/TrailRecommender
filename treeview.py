import tkinter as tk
from tkinter import ttk
import pandas as pd

df_sorted=pd.read_csv(r'C:\Users\fgazi\AllTrails.csv')

df_sorted = df_sorted[['name','area_name','city_name','state_name']]
df_sorted = df_sorted.rename(columns={'name': 'Trail Name', 'area_name': 'Area', 'city_name': 'City', 'state_name': 'State'})

root= tk.Tk()

root.title('5 Best Hikes For You')

# Create tree widget
tree = ttk.Treeview(root, height=5, padding=1)
tree.pack()

# Define treeview columns
tree['columns'] = list(df_sorted.columns)

# Create heading columns
for column in df_sorted.columns:
    tree.heading(column, text=column)

# Add df rows to treeview
for index, row in df_sorted.iterrows():
    tree.insert("", tk.END, values=list(row))

root.mainloop()