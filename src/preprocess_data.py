'''
pip install pandas, sklearn, numpy, ast
'''
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import ast

'''
Reads in the csv dataset from the kaggle national parks dataset
'''
def preprocess_data(file:str)->pd.DataFrame:

  df = pd.read_csv(file)
  
  #convert strings containing lists to lists and replace spaces with underscores
  df['features'] = [[j.strip().strip("[]'") for j in list(i.split(","))] for i in df['features']]
  df['activities'] = [[j.strip().strip("[]'") for j in list(i.split(","))] for i in df['activities']]
  df['route_type'] = [i.replace(" ","_") for i in df['route_type']]

  #convert geolocation from string to dictionary
  df['_geoloc'] = [ast.literal_eval(i) for i in df['_geoloc']]

  #use binarizer to binarize feature and activites data
  mlb = MultiLabelBinarizer()
  enc = OneHotEncoder()
  
  df_binarized_features = pd.DataFrame(mlb.fit_transform(df['features']),columns=mlb.classes_, index=df.index)
  df_binarized_activities = pd.DataFrame(mlb.fit_transform(df['activities']),columns=mlb.classes_, index=df.index)
  
  # use one-hot encoding to binarize route_type
  feature_array = enc.fit_transform(df[['route_type']]).toarray()
  feature_labels = np.concatenate(enc.categories_,axis=0)
  df_binarized_route_type = pd.DataFrame(feature_array,columns=feature_labels)

  #dropping duplicates for binarized data
  df_binarized_activities.drop(columns='rails-trails',inplace=True)
  
  #dropping original categorical columns for original dataframe
  df.drop(columns=['features','activities','route_type'],inplace=True)

  #checking to make sure that dataframes are of compatible shapes
  assert df.shape[0] == df_binarized_features.shape[0] and df.shape[0] == df_binarized_activities.shape[0] and df.shape[0] == df_binarized_route_type.shape[0]

  #converts meters to feet 
  conversion_factor = 3.281
  for i in range(df.shape[0]):
    if df.loc[i,'units'] == 'm':
      df.loc[i,'length'] *= conversion_factor 
      df.loc[i,'elevation_gain'] *= conversion_factor


  #adding binarized columns into whole dataframe
  df = df.join(df_binarized_features)
  df = df.join(df_binarized_activities)
  df = df.join(df_binarized_route_type)

  #drop NA values
  df = df.dropna()

  #adjust average rating to rate higher for trails with more ratings
  df['avg_rating'] = df['avg_rating']*(1-(1/(1+df['num_reviews']))).round(1)


  # check for duplicate and null values
  null_sum = 0
  for i in df.isnull().sum():
    null_sum += i
  assert null_sum == 0
  assert df.duplicated('trail_id').sum() == 0

  return df

#send in file name to function call -- i called it 'trails.csv' -- must be in same directory as this file
# df = preprocess_data('trails.csv')

# df
