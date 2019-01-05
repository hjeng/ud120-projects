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

# Loading the E + F dataset
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

# What is the total value of stock belonging to James Prentice?
tsv_james_prentice = enron_data["PRENTICE JAMES"]["total_stock_value"]
print "The total stock value of James Prentice is %d" % (tsv_james_prentice)

# How many email messages do we have from Wesley Colwell to persons of interest?
wes_colwell_to_poi = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "There were %d emails from Wesley Colwell to persons of interest" % (wes_colwell_to_poi)

# What is the value of stock options exercised by Jeffrey K Skilling?
exer_stock_jeff_skilling = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print "The value of stock options exercised by Jeffrey K Skilling is %d" % (exer_stock_jeff_skilling)

# Between Lay, Skilling, and Fastow, who took home the most money? How much was it?
total_payments_lay  = enron_data["LAY KENNETH L"]["total_payments"]
total_payments_skilling  = enron_data["SKILLING JEFFREY K"]["total_payments"]
total_payments_fastow  = enron_data["FASTOW ANDREW S"]["total_payments"]
total_payments = {"Kenneth Lay" : total_payments_lay, "Jeffrey K Skilling" : total_payments_skilling, "Andrew Fastow" : total_payments_fastow}
most_money_person = max(total_payments)
most_money_value = total_payments[most_money_person]
print "%s took home %d" % (most_money_person, most_money_value)

# How many individuals in the enron dataset have a quantified salary? Known email address?
quant_salary = 0
for j in range(len(enron_data)):
    if isinstance(enron_data.values()[j]['salary'], (int)) == True:
        quant_salary += 1
print "%d people have a quantified salary" % (quant_salary)

has_email = 0
for k in range(len(enron_data)):
    if enron_data.values()[k]['email_address'] != 'NaN':
        has_email += 1
print "%d people have a known email" % (has_email)

# How many people in the E + F dataset have "NaN" for their total payments? What percentage of people in the dataset as a whole is this?
total_pay_nan = 0
for l in range(len(enron_data)):
    if enron_data.values()[l]['total_payments'] == 'NaN':
        total_pay_nan += 1
percent = 100.0 * float(total_pay_nan)/(len(enron_data))
print "%d people have NaN for their total payments. This is %d%% of the whole." % (total_pay_nan, percent)

# How many POIs in the E + F dataset have "NaN" for their total payments? What percentage of POI's as a whole is this?
total_pay_poi_nan = 0
for m in range(len(enron_data)):
    if enron_data.values()[m]['total_payments'] == 'NaN' and enron_data.values()[m]['poi'] == True:
        total_pay_poi_nan += 1
percent_poi = 100.0 * float(total_pay_poi_nan)/(len(enron_data))
print "%d persons of interest have NaN for their total payments. This is %d%% of the whole." % (total_pay_poi_nan, percent_poi)
