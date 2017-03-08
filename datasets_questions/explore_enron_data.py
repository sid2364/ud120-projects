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

print "Total number of data points: ", str(len(enron_data))

for key in enron_data:
	value = enron_data[key]
	print "Total number of features for each data point: ", str(len(value))
	break

count = 0
for key in enron_data:
	if enron_data[key]["poi"] == 1:
		count += 1
		continue
print "Number of POIs in the dataset: ", str(count)

for k in enron_data:
	if "PRENTICE" in k:
		print "Prentice: ", str(enron_data[k]["total_stock_value"])
	if "COLWELL" in k:
		print "Colwell: ", str(enron_data[k]["from_this_person_to_poi"])
	if "SKILLING" in k:
		print "Skilling: ", str(enron_data[k]["exercised_stock_options"])
	
print "\nTotal payments:-"
for k in enron_data:
	if "SKILLING" in k:
		print "Jeffrey Skilling: ", str(enron_data[k]["total_payments"])

	if "KENNETH" in k:
		print "Kenneth Lay: ", str(enron_data[k]["total_payments"])
	if "FASTOW" in k:
		print "Andrew Fastow: ", str(enron_data[k]["total_payments"])

print "\nKnown salaries and email addresses:-"
salaries, emails = 0, 0
for k in enron_data:
	if enron_data[k]["salary"] != "NaN":
		salaries += 1
	if enron_data[k]["email_address"] != "NaN":
		emails += 1
print "Salaries: ", salaries, " - Email addresses: ", emails
