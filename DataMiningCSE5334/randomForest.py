
from sklearn.metrics import accuracy_score

import numpy as num
from sklearn.model_selection import train_test_split
import pandas as pand
from sklearn.model_selection import cross_val_score, cross_val_predict
wineData = pand.read_csv('wine.csv')
# print(wineData)

# Column names from wineData
wineOriginalHeaders = list(wineData.columns.values)
#print(wineOriginalHeaders)

# printing the starting 2 rows
#print(wineData[0:3])

# assigning the class column
classColumn = 'quality'

# From WineData get all the features except the class column ie quality
#featureColumns = ['volatile acidity', 'residual sugar', 'chlorides', 'total sulfur dioxide', 'pH', 'sulphates','alcohol']
featureColumns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']

# splitting the Winedata in to classes and features
wineClass = wineData[classColumn]
wineFeatures = wineData[featureColumns]
trainingFeature, testingFeature, trainingClass, testingClass = train_test_split(wineFeatures,wineClass,stratify=wineClass, train_size= 0.75, test_size=0.25)

# Random Forest
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=500,max_depth=8)
clf.fit(trainingFeature,trainingClass)

classficationRF= clf.predict(testingFeature)
print(classficationRF)

print("Training Set Score with Random Forest: {:.3f}".format(clf.score(trainingFeature,trainingClass)))
print("Testing Set Score with Random Forest: {:.3f}".format(clf.score(testingFeature,testingClass)))

# Printing the Confusion Matrix
print("Confusion Matrix for Random Model(Model 1) :")
print(pand.crosstab(testingClass, classficationRF, rownames=['True'],colnames=['predicted'], margins=True))

scoresDT = cross_val_score(clf, wineFeatures, wineClass,cv=10)

print("Cross Validation Scores: {}".format(scoresDT))
print("Avg Cross Validation : {:.3f}".format(scoresDT.mean()))

# In order to improve the cross validation accuracy, we can prune the Features which does not contribute to Wine Quality.

newFeaturesColumns = ['pH','alcohol','fixed acidity','volatile acidity', 'residual sugar', 'chlorides', 'free sulfur dioxide','sulphates']
newWineFeatures = wineData[newFeaturesColumns]

scoresDTNew = cross_val_score(clf, newWineFeatures, wineClass,cv=10,scoring='accuracy')
print("New Cross Validation Scores: {}".format(scoresDTNew))
print(" New Avg Cross Validation : {:.3f}".format(scoresDTNew.mean()))
from sklearn import preprocessing

trainingscale = preprocessing.scale(newWineFeatures)
newscore=cross_val_score(clf,trainingscale,wineClass,cv=10)

print("Cross : {}".format(newscore))
print(" avg: {:.3f}".format(newscore.mean()))