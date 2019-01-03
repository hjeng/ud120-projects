#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# How many data points (people) are in the dataset?
print "There are", len(enron_data.keys()), "data points (people) in the dataset."

# For each person, how many features are available?
print "There are", len(enron_data.values()[0]), "features available per person." # indexing the values in this dictionary

# How many persons of interest (POI) are there in this dataset?
# Example: enron_data.values()[0]['salary'] = 365788
x = 0
for i in range(len(enron_data.keys())):
    if enron_data.values()[i]['poi'] == True:
        x += 1
print "There are", x,"persons of interest."

# How many POI's were there in total
# Read from ../final_project/poi_names.txt file
poi = open("../final_project/poi_names.txt", 'r')
poi_length = poi.readlines()
print "There were", len(poi_length[2:]), "POIs in total."
