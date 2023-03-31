import pandas as pd

'''
Performs merge sort on pandas dataframe dictionary based on key string passed in
Parameters:
  arr -- the array to be sorted (our pandas dataframe)
  key -- column used to sort (will be 'gower_distance_from_user_preference' column)
  reverse -- boolean determining whether sort will be in ascending or descending order (false is ascending)
Returns -- a sorted pandas dataframe formatted as a dictionary
'''
def merge_sort(arr: list, key: str, reverse: bool = False):

    # splits the collection in half if it's not at its base case
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        #recursive call on split halves
        merge_sort(left_half, key, reverse)
        merge_sort(right_half, key, reverse)

        #merging of two halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if (not reverse and left_half[i][key] <= right_half[j][key]) or (
                    reverse and left_half[i][key] >= right_half[j][key]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        #adds items in left or right half to end, if there are any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

'''
Transforms a pandas dataframe into a dictionary to be sorted with the merge_sort function, and then transforms it back into a pandas dataframe
Parameters:
  df -- pandas dataframe to be sorted
Returns -- a pandas dataframe sorted by its "gower_distance_from_user_preference" column
'''
def sort_df(df:pd.DataFrame):
  df = df.to_dict('records')
  df_sorted = merge_sort(df,"gower_distance_from_user_preference")
  return pd.DataFrame(df_sorted)
