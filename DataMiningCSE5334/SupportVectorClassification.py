from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pand

wineData = pand.read_csv('wine.csv')
# print(wineData)

# Column names from wineData
wineOriginalHeaders = list(wineData.columns.values)
print(wineOriginalHeaders)

# printing the starting 2 rows
print(wineData[0:3])

# assigning the class column
classColumn = 'quality'

# From WineData get all the features except the class column ie quality
featureColumns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']

# splitting the Winedata in to classes and features
wineClass = wineData[classColumn]
wineFeatures = wineData[featureColumns]
trainingFeature, testingFeature, trainingClass, testingClass = train_test_split(wineFeatures,wineClass,stratify=wineClass, train_size= 0.75, test_size=0.25)

#  Support Vector Classification
classificationSVC = SVC()
classificationSVC.fit(trainingFeature,trainingClass)
SVC(C=10, cache_size=150, class_weight=None, coef0=0.0, decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',max_iter=-1,probability=False, random_state= None,
    shrinking=True, tol=0.001, verbose=False)

print(classificationSVC.predict(testingFeature))
print("Training Set Score with SVC: {:.3f}".format(classificationSVC.score(trainingFeature,trainingClass)))
print("Testing Set Score with SVC: {:.3f}".format(classificationSVC.score(testingFeature,testingClass)))

predictionClassSVC = classificationSVC.predict(testingFeature)
# Printing the Confusion Matrix
print("Confusion Matrix for SVC(Model 1) :")
print(pand.crosstab(testingClass,predictionClassSVC,rownames=['True'],colnames=['predicted'],margins=True))

