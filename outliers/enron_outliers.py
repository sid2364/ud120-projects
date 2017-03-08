#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

from operator import itemgetter

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["poi", "salary", "bonus"]
data = featureFormat(data_dict, features)

data = sorted(data, key=itemgetter(2), reverse=True)
''' add this code to ../tools/feature_format.py to get name of dictionary key instead of poi
if feature == "poi":
    value = key

####

and uncomment this line:-
print "Largest data point:", data[0][0]
'''
data.pop(0)

for point in data:
    salary = point[1]
    bonus = point[2]
    name = point[0]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.show()


