The following is the layout for the Trail Recommender Project:

    * data - contains CSVs (trail and zip codes)
    * imgs - gower_formula.png
    * setup - requirements
    * src - main project folder (application is trail_recommend)
        * data_processing - py files that clean data and execute merge sort
        * dependencies - py file gower function
    * submitted materials - the submission files for the project

Dependencies:

Run the following command in a terminal where the project is located:

pip install Django, Pillow, PyMySQL, asgiref, customtkinter, darkdetect, geographiclib, geopy, gower, image, joblib, numpy, pandas, pip, python-dateutil, pytz, scikit-learn, scipy, setuptools, six, sklearn-pandas, sqlparse, threadpoolctl, tzdata, wheel


Run Instructions:




UI overview:

    Zip Input Window:
    The user is prompted with a window to input their zip code. if the user inputs incorrect input or nothing it will
    re-prompt the user. 02215 has been extensively used. The zip window can be reached from the Trail prences tab

    Main Window:
        Trail Preferences tab
            popularity - the popularity of a trail on a ranking of 0 - 85
            length in ft - the length of the trail
            elevation in ft - the preferred elevation of a trail.
            Any Difficulty - the difficulty 1-5 that is perfered if Any Difficulty is left then difficulty is disregarded
            Search Radius - the maximum distance the user wishes to search away from given location
            No Dog Preferences - left on no does not take any inclusive or exclusive dog inputs
                dogs - dogs allowed on trail
                dogs-leash - dogs on leash allowed on trail
                dogs-no - no dogs allowed on trail
            Zip Code - returns the Zip Input Window if the user wants to change their zip
            Search - runs the search on the given inputs from all tabs

        Features tab
            15 distinct trail features that a user can add as a preference in the search.
            Search - runs the search on the given inputs

        Activities tab
            25 distinct activities associated with the trail that a user can add as a preference in the search.
            Search - runs the search on the given inputs
