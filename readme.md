# Trail Recommender

This is our final project for CS5800 - Algorithms at Northeastern University. To view a video of our presentation, [click here](https://youtu.be/qj9sqizcPlI). View our submitted materials in the `submitted materials` folder.


### The following is the layout for the Trail Recommender Project:
* `data` - contains CSVs (trail and zip codes)
* `setup` - dependency requirements list
* `src` - main project folder 
* `src/data_processing` - py files that clean data and execute merge sort
* `submitted materials` - the submission files for the project
* `trail_recommend.py` - Python file that runs the GUI

## Running the program:
These commands work on Mac OS only -- see [this link](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) for guidance on Windows setup.

1) Create a virtual environment
```
make venv
```
2) Initialize the Python virtual environment
```
source .gitignore/venv/bin/activate
```
3) Install the necessary packages
```
make requirements
```
4) Run the program
```
Make trails
```
5) Deactivate the Python virtual environment
```
deactivate
```
6) Delete the virtual environment from your machine
```
Make teardown
```

## Data we used
Our demo works on the [Kaggle National Parks AllTrails dataset](https://www.kaggle.com/datasets/planejane/national-park-trails).
### **Numerical features:**
* _geoloc
* popularity
* elevation_gain
* difficulty_rating
* avg_rating

### **Categorical features:**
* route_type
* features
    * [dogs-no, dogs-leash, ada, beach, cave, strollers, paved, partially-paved, forest, river, waterfall, wild-flowers, lake, historic-site, wildlife, kids, views]
* activities
    * [birding, camping, hiking, nature-trips, trail-running, walking, backpacking, sea-kayaking, canoeing, mountain-biking, horseback-riding, scenic-driving]
    
## How the algorithm works:
### 1) Filters by distance:
The list of trails is first filtered by physical distance. We achieved this by calculating the [geodesic distance](https://geopy.readthedocs.io/en/stable/#module-geopy.distance) between the trail heads and the user's location (employ's the World Geodetic System WGS84 standard for coordinates). The user provides their location and acceptable search radius in miles.

### 2) Calculates the degree of similarity to the user's trail preference:
Program uses the Gower distance function to calculate trail similarity based on user input -- [this video](https://www.youtube.com/watch?v=PHu8VoPv-o4) is a simple explanation of the Gower distance function for mixed data. [View this paper](https://www.researchgate.net/publication/327832223_Distance-based_clustering_of_mixed_data) for a more in-depth explanation of computing similarity for mixed data.

<img src="imgs/gower_formula.png">

A user may, for example, seek a trail that's around 2 miles long, is good for trail running, and is dog-friendly.

### 3) Sorts the trails by degree of similarity to the user's preference
Once the trail list has been filtered, we use merge sort to sort the list of trails, with the those most relevant to the user appearing first and those least relevant to the user appearing last.

## UI overview:

#### Zip Input Window:
* The user is prompted with a window to input their zip code. if the user inputs incorrect input or nothing it will
* re-prompt the user. 02215 has been extensively used. The zip window can be reached from the Trail prences tab

#### Main Window:
##### Trail Preferences tab
* popularity - the popularity of a trail on a ranking of 0 - 85
* length in ft - the length of the trail
* elevation in ft - the preferred elevation of a trail.
* Any Difficulty - the difficulty 1-5 that is perfered if Any Difficulty is left then difficulty is disregarded

* Search Radius - the maximum distance the user wishes to search away from given location

* No Dog Preferences - left on no does not take any inclusive or exclusive dog inputs
  * dogs - dogs allowed on trail
  * dogs-leash - dogs on leash allowed on trail
  * dogs-no - no dogs allowed on trail

* Zip Code - returns the Zip Input Window if the user wants to change their zip
            Search - runs the search on the given inputs from all tabs

##### Features tab
* 15 distinct trail features that a user can add as a preference in the search.
            Search - runs the search on the given inputs

##### Activities tab
* 25 distinct activities associated with the trail that a user can add as a preference in the search.

##### Search
* Runs the search on the given inputs