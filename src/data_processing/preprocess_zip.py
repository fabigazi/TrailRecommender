import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import ast

'''
Reads in the csv dataset from the us zip https://simplemaps.com/data/us-zips
'''

def preprocess_zip(file: str) -> pd.DataFrame:
    df = pd.read_csv(file)