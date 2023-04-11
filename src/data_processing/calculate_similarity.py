'''
pip install gower
'''
import pandas as pd
import numpy as np
from dependencies.gower_dist import gower_matrix

'''
Appends a column of similarty scores onto a pandas dataframe using the Gower distance function, with inputs based on dictionary parameters passed in for user's trail preference
Parameters:
  considered_features -- dictionary for user's trail preference; format is {"feature":(value,weight)} -- (ex. {"trail-running":(1,.33),"length":(5000,.33),"loop":(1,.33)})
  df -- pandas DataFrame to add similarity value column, labeled "gower_distance_from_user_preference"
Returns -- pandas dataframe containing new column called "gower_distance_from_user_preference"
'''
def calculate_similarity(considered_features:dict,df:pd.DataFrame)->pd.DataFrame:

  #eliminate outlier distances so that gower min-max normalization not thrown off
  if 'length' in considered_features.keys():
    max_dist = considered_features['length'][0]*5
    df = df.loc[df['length']<=max_dist]

  # pare down df to consider only columns of interest to user
  df_target_columns = df[list(considered_features.keys())]

  # put user preference observation at the end of pared df
  considered_features_values = {}
  for k,v in considered_features.items():
    considered_features_values[k]=v[0]
  
  df_target_columns = pd.concat([df_target_columns,pd.DataFrame(considered_features_values, index=[0])])
  
  #extract gower distance feature weights determined by user
  user_weights = np.array([v[1] for v in considered_features.values()])

  # calculate gower distance and extract list of distances in comparison to user preference (last row)
  distances = gower_matrix(df_target_columns,weight=user_weights)[-1]

  # add distance column to dataframe passed in  
  df.insert(df.shape[1],"gower_distance_from_user_preference",distances[:-1])
  return df
