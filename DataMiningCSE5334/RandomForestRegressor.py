# Importing Libraries and Modules

import numpy as num
import pandas as pan

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


# Wind Data reading from wine.csv
wineData = pan.read_csv('wine.csv')
#print(wineData)

Testing = wineData.quality
Training = wineData.drop('quality',axis =1)

Train, Test, train, test = train_test_split(Training,Testing,test_size=0.75,random_state=0,stratify=Testing)
print(Train)

#clf = RandomForestClassifier(max_depth=3)
clf = RandomForestRegressor(max_depth=5)
clf.fit(Train,train)
print(clf.feature_importances_)
classficationRF= clf.predict(Test)
print(classficationRF)

print("Training Set Score with Random Forest: {:.3f}".format(clf.score(Train,train)))
print("Testing Set Score with Random Forest: {:.3f}".format(clf.score(Test,test)))

# Printing the Confusion Matrix
print("Confusion Matrix for Random Model(Model 1) :")
print(pan.crosstab(test, classficationRF, rownames=['True'],colnames=['predicted'], margins=True))

# Preprocessing Steps in the Data
pipeline = make_pipeline(preprocessing.StandardScaler(),RandomForestRegressor(n_estimators=100))

# For Tuning our model we need to have hyper parameters
hyperParameters= {'randomforestregressor__max_features':['auto','sqrt','log2'],'randomforestregressor__max_depth':[None,5,3, 1]}
#clf = RandomForestClassifier(max_depth=3)
#clf.fit(Train,Test)
# Using Cross validation pipeline
classification = GridSearchCV(pipeline,hyperParameters,cv =10)
classification.fit(Train,train)

# Evaluating the test data
prediction = classification.predict(Test)
print(r2_score(test, prediction))


