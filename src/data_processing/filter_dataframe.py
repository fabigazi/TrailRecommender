'''
pip install geopy
'''
import pandas as pd
from geopy import distance

'''
Filters a dataframe for values within a distance threshold of a user's geographic location
Parameters:
  user_location -- dictionary for user's geographic coordinates (ex. {'lat':45.0,'lng':-116.3})
  distance_threshold -- float value representing mile radius from user location to be kept in the dataframe
  df -- pandas dataframe to be filtered based on user location and distance threshold
Returns -- a filtered pandas dataframe
'''
def filter_dataframe(user_location:dict,distance_threshold:float,df:pd.DataFrame)->pd.DataFrame:

  distances = []
  for row in df.iterrows():
    distances.append(distance.distance((user_location['lat'],user_location['lng']),(row[1]['_geoloc']['lat'],row[1]['_geoloc']['lng'])).miles)

  df['physical_distance_from_user'] = distances

  return df.loc[df['physical_distance_from_user']<= distance_threshold]

