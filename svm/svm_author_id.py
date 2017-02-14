#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

from sklearn import svm

classifier = svm.SVC(kernel="rbf", C=10000)
t1 = time()
classifier.fit(features_train, labels_train)
print "Training time: ", str(round(time()-t1, 3)), "s"

t2 = time()
prediction = classifier.predict(features_test)
print "Prediction time: ", str(round(time()-t2, 3)), "s"

#print "10th: ", prediction[10]
#print "26th: ", prediction[26]
#print "50th: ", prediction[50]

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(prediction, labels_test)

print "Accuracy: ", str(accuracy)
print "Accuracy %: ", str(round(accuracy*100, 2))

import numpy as np
print "There were", str(np.count_nonzero(prediction == 1)), " out of a total of", str(prediction.size), "emails predicted for Chris (class 1)."
