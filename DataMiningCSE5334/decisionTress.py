import pandas as PAN
import numpy as NUM
from sklearn.model_selection import train_test_split
from sklearn.model_selection import  cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

wineData = PAN.read_csv('wine.csv')
# Printing the Wine Data
print(wineData)

# To see the Features given in the Wine Data
wineOriginalHeaders = list(wineData.columns.values)
#print(wineOriginalHeaders)

# Assigning the Class Label
classLabel = 'quality'

# Extract Features except the free sulfur dioxide (Omit it since we have total sulfur dioxide) and class label: quality
featureColumns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']

# Printing whether all features and class label assigned properly
print(classLabel)
print(featureColumns)

# Splitting Wine Data in Classes and Features
wineClass = wineData[classLabel]
wineFeatures = wineData[featureColumns]

# Splitting the altered Wine data as balanced one using stratified and 75% as training anf 25% as testing
trainingFeature, testingFeature, trainingClass, testingClass = train_test_split(wineFeatures,wineClass,stratify=wineClass, train_size= 0.75, test_size=0.25)

# Decision Tree
# Since we have 10 Features we can have max_depth as 7
decisionTree = DecisionTreeClassifier(max_depth=8, random_state=0)
decisionTree.fit(trainingFeature,trainingClass)

# Now then we fitted the data we can print the accuracy for both training set and testing set
print("Training Set Score with Decision Tree: {:.3f}".format(decisionTree.score(trainingFeature,trainingClass)))
print("Testing Set Score with Decision Tree: {:.3f}".format(decisionTree.score(testingFeature,testingClass)))

predictionClass = decisionTree.predict(testingFeature)
# Printing the Confusion Matrix
print("confusion matrix with Decision Tree :")
print(PAN.crosstab(testingClass,predictionClass,rownames=['True'],colnames=['predicted'],margins=True))

scoresDT = cross_val_score(decisionTree, wineFeatures, wineClass,cv=10)


print("cross validation scores: {}".format(scoresDT))
print("Avg Cross: {:.3f}".format(scoresDT.mean()))

#newFeaturesColumns = ['pH','alcohol','fixed acidity','volatile acidity', 'residual sugar', 'chlorides', 'free sulfur dioxide','sulphates']
newFeaturesColumns = ['fixed acidity', 'volatile acidity', 'residual sugar', 'chlorides', 'total sulfur dioxide', 'pH', 'sulphates', 'alcohol']

newWineFeatures = wineData[newFeaturesColumns]

scoresDTNew = cross_val_score(decisionTree, newWineFeatures, wineClass,cv=10,scoring='accuracy')
print("New Cross Validation Scores: {}".format(scoresDTNew))
print(" New Avg Cross Validation : {:.3f}".format(scoresDTNew.mean()))
from sklearn import preprocessing

trainingscale = preprocessing.scale(newWineFeatures)
newscore=cross_val_score(decisionTree,trainingscale,wineClass,cv=10)

print("Cross : {}".format(newscore))
print(" avg: {:.3f}".format(newscore.mean()))