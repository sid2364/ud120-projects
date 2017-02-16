#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print "Number of features: ", str(len(features_train[0]))

from sklearn import tree

classifier = tree.DecisionTreeClassifier(min_samples_split=40)

t0 = time()
classifier.fit(features_train, labels_train)
print "Training time: ", str(round(time()-t0, 3))

t1 = time()
prediction = classifier.predict(features_test)
print "Prediction time: ", str(round(time()-t1, 3))

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(prediction, labels_test)
print "Accuracy: ", str(accuracy)

