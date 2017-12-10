import numpy as num
import pandas as pan
import matplotlib.pyplot as plot
from sklearn import neighbors
from sklearn.model_selection import train_test_split

# Reading the Data File

dataset = pan.read_csv("wine.csv", header=None)
classLabelArray = num.asarray(dataset.ix[0, :])
dataValues = num.asarray(dataset.ix[1:, :])

print(classLabelArray.shape)
print(dataValues.shape)
transposedataValues = dataValues.T
training_accuracy = []
testing_accuracy = []

# Splitting the dataset as 75% Training and 25% Testing

trainX, testX, trainY, testY = train_test_split(transposedataValues, classLabelArray, test_size=0.25)

# Array Creation for K = 3
predictedArray = []

# Fitting the Data
neighbors = neighbors.KNeighborsClassifier(n_neighbors=3, weights='uniform')
neighbors.fit(trainX, trainY)
neighbors_setting = range(0, 12)
# Predicting the Data

for nneighbors in neighbors_setting:
  testdatafetching = num.asarray(testX[i, :])
  testdatafetching = num.reshape(testdatafetching, (1, -1))
  print("KNN for K = 3")
  pred = neighbors.predict(testdatafetching)
  predictedArray.insert(i, pred[0])
  print(pred)
  print("Test Accuracy: {:.2f}".format(neighbors.score(testX, testY)))

