#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()

################################################################################

print "Choose an algorithm to test:-\n \
	1. kNN\n \
	2. AdaBoost\n \
	3. Random Forest"
choice = int(raw_input("Enter your choice here: "))

from sklearn.metrics import accuracy_score

if choice == 1:
	from sklearn import neighbors
	clf = neighbors.KNeighborsClassifier(algorithm="auto", weights="distance", n_neighbors=15)
elif choice == 2:
	from sklearn import ensemble
	clf = ensemble.AdaBoostClassifier(n_estimators=25, learning_rate=0.5)
elif choice == 3:
	from sklearn import ensemble
	clf = ensemble.RandomForestClassifier(n_estimators=50, max_features="log2")

clf.fit(features_train, labels_train)
prediction = clf.predict(features_test)
accuracy = accuracy_score(prediction, labels_test)
print "Accuracy: ", str(round(accuracy*100, 3))

try:
	print "Drawing prettyPicture..."
	prettyPicture(clf, features_test, labels_test, choice)
except NameError:
	pass
