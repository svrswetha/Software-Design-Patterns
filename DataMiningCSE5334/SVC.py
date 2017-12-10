import pandas as pand
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn.svm import SVC

wineData = pand.read_csv('wine.csv')
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

#  Support Vector Classification
classificationSVC = SVC()
classificationSVC.fit(trainingFeature,trainingClass)
SVC(C=0.5, cache_size=150, class_weight=None, coef0=0.0, decision_function_shape='ovr', degree=3, gamma='auto', kernel='callable',max_iter=-1,probability=False, random_state= None,
    shrinking=True, tol=0.001, verbose=False)

print(classificationSVC.predict(testingFeature))
print("Training Set Score with SVC: {:.3f}".format(classificationSVC.score(trainingFeature,trainingClass)))
print("Testing Set Score with SVC: {:.3f}".format(classificationSVC.score(testingFeature,testingClass)))

predictionClassSVC = classificationSVC.predict(testingFeature)
# Printing the Confusion Matrix
print("confusion matrix with Decision Tree :")
print(pand.crosstab(testingClass,predictionClassSVC,rownames=['True'],colnames=['predicted'],margins=True))


# SVC  Classifier for Calculating cross validation

scaler = preprocessing.StandardScaler().fit(trainingFeature)
trainingFeature_transformed = scaler.transform(trainingFeature)
clf = SVC(C=1).fit(trainingFeature_transformed,trainingClass)
testingFeature_transformed = scaler.transform(testingFeature)
scores=clf.score(testingFeature_transformed,testingClass)
print("cross validation scores with SVC: {:.3f}".format(scores))
print("Avg Cross_scores with SVC: {:.3f}".format(scores.mean()))

