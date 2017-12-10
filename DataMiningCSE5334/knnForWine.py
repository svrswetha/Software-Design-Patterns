import pandas as pand
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing

# Referred P.ipynb for KNN Implementation

# reading the Wine data from csv
wineData = pand.read_csv('wine.csv')
# print(wineData)

# assigning the class column
classColumn = 'quality'

# From WineData get all the features except the class column ie quality
featureColumns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide','total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']

# splitting and assigning the Winedata in to classes and features
wineClass = wineData[classColumn]
wineFeatures = wineData[featureColumns]

# splitting the altered Wine data as balanced one using stratified and 75% as training and 25% as testing
trainingFeature, testingFeature, trainingClass, testingClass = train_test_split(wineFeatures,wineClass,stratify=wineClass, train_size= 0.75, test_size=0.25)

# Applying K Nearest Neighbor Classification Algorithm for Wine Data and metric is minkowski
knnForWine = KNeighborsClassifier(n_neighbors=6, metric='minkowski',p=2)

# Fitting the Winedata using KNN
fittingknn=knnForWine.fit(trainingFeature,trainingClass)

# Predicting the Class for the testing Feature using KNN
predictionClass = knnForWine.predict(testingFeature)

print("Prediction for Testing set:\n {}".format(predictionClass))
print("Accuracy for Testing set: {:.2f}".format(knnForWine.score(testingFeature,testingClass)))
print("Testing set predicion using knn:\n{}".format(predictionClass))
print("confusion matrix with knn :")
print(pand.crosstab(testingClass,predictionClass,rownames=['True'],colnames=['predicted'],margins=True))

# Applying 10 fold Stratified Cross Validation
scoreknn = cross_val_score(fittingknn,wineFeatures,wineClass, cv =10)

# Printing out the Cross Validation Scores
print("cross-validation scores: {}".format(scoreknn))

# Printing out the Average Cross Validation Score
print("Average cross-validation score:{:.3f}".format(scoreknn.mean()))

# DataFrame for Training Set referred from P.ipnyb
trainingClassdf = pand.DataFrame(trainingClass,columns=[classColumn])
traningDatadf = pand.merge(trainingClassdf, trainingFeature, left_index=True, right_index=True)
traningDatadf.to_csv('trainingData.csv', index=False)

# DataFrame for Testing Set referred from P.ipnyb
temporarydf = pand.DataFrame(testingClass,columns=[classColumn])
temporarydf['Predicted quality'] = pand.Series(predictionClass,index=temporarydf.index)
testingDatadf = pand.merge(temporarydf, testingFeature, left_index=True, right_index=True)
testingDatadf.to_csv('testingData.csv',index=False)

# In order to improve the Average Cross Validation accuracy,
# We can prune the Features which does not contribute To Wine Quality such as free sulfur dioxide, density, citric acid.

newFeaturesColumns = ['fixed acidity', 'volatile acidity', 'residual sugar', 'chlorides', 'total sulfur dioxide', 'pH', 'sulphates', 'alcohol']
newWineFeatures = wineData[newFeaturesColumns]

# Re calculating the Scores after dimension reduction using newWineFeatures and scoring parameter accuracy
scoresDTNew = cross_val_score(knnForWine, newWineFeatures, wineClass,cv=10,scoring='accuracy')
# Printing the Newly obtained cross validation scores and average cross validation score
print("New Cross Validation Scores after Dimension Reduction: {}".format(scoresDTNew))
print(" New Average Cross Validation after Dimension Reduction: {:.3f}".format(scoresDTNew.mean()))

# Using Scaling of pre processing we can achieve more average cross validation accuracy (14% increment)
trainingscale = preprocessing.scale(newWineFeatures)
newscore=cross_val_score(knnForWine,trainingscale,wineClass,cv=10)

# Printing the cross validation scores and average cross validation score after pre processing
print("Improved Cross Validation after Scaling : {}".format(newscore))
print("Improved Average Cross Validation Score after Scaling: {:.3f}".format(newscore.mean()))





