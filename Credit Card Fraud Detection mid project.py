# -*- coding: utf-8 -*-
"""umar Mid Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kbn8sFM8A_DOEY6OL54ZflBU1Mas6oy_
"""

import pandas as pd
# Importing Data Set
dataset = pd.read_csv("/content/creditcard.csv")
dataset.head()

# dataset.isnull().sum()

import numpy as np

# Data Preprocessing

# labels= dataset.columns
# labels=labels.drop('Class')
# labels
# for i in labels:
  # dataset[i] = dataset[i].replace(np.nan,dataset[i].mean())

dataset.iloc[:,:-1] = dataset.iloc[:,:-1].replace(np.nan,dataset.iloc[:,:-1].mean())

dataset["Class"] = dataset['Class'].replace(np.nan,0)

# X and Y Features Extractions

x = dataset.iloc[:,:-1].values
y = dataset['Class'].values

# x=dataset.drop(['Class'])

# print(x.shape)
# print(y.shape)

# from sklearn.preprocessing import LabelEncoder
#
# dataset['New_RB'] = LabelEncoder.fit_transform(dataset['RB'])

from sklearn.model_selection import train_test_split


# Splitting Dataset into Training and Testing

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = .20, random_state = 5)

# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)


# from sklearn.ensemble import RandomForestClassifier
# RandomForestClassifier()

from sklearn.naive_bayes import GaussianNB

# Naive_Bayes Model Importing

classifier = GaussianNB()

# Naive_Bayes Model Training on Training Data
print("Training Naive Bayes Classifier")
classifier.fit(x_train,y_train)

# Testing of Naive_Bayes Model on Testing Data

y_pred_nb = classifier.predict(x_test)

from sklearn.metrics import r2_score, accuracy_score, mean_squared_error

# Calculating Accuracy of Naive_Bayes Model
print("Accuracy_Score (Naive Bayes): %.2f" % (accuracy_score(y_test,y_pred_nb)*100))

from sklearn.neighbors import KNeighborsClassifier

# Importing KNN Model
print("Training KNN Classifier")
k_model= KNeighborsClassifier(n_neighbors=5)

# Training KNN Model

k_model.fit(x_train,y_train)

# Testing KNN Model

y_pred_knn=k_model.predict(x_test)

# from sklearn.metrics import r2_score, accuracy_score

# Calculating Acuracy of KNN Model

print("Accuracy_Score (KNN): %.2f" % (accuracy_score(y_test,y_pred_knn)*100))

from sklearn import svm
# Importing & Training SVM
print("Training SVM Classifier")
C=1.0
svc=svm.SVC(kernel='linear',C=10,gamma=1).fit(x_train,y_train)

# x_min, x_max = x_train[:,0].min() - 1, x_train[:,0].max() + 1
# y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1
# h = (x_max / x_min)/100
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Testing SVM

y_pred_svm=svc.predict(x_test)

# from sklearn.metrics import r2_score, accuracy_score, mean_squared_error

# Calculating Accuracy of SVM

print("Accuracy_Score (SVM): %.2f" % (accuracy_score(y_test,y_pred_svm)*100))

from sklearn.tree import DecisionTreeClassifier

# Importing Decision Tree
print("Training Decision Tree")
dt_classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)

# Training Decision Tree

dt_classifier.fit(x_train, y_train)

# Testing Decision Tree

y_pred_decision_tree = dt_classifier.predict(x_test)

# Testing Accuracy of Decision Tree

print("Accuracy_Score (Decision Tree): %.2f" %  (accuracy_score(y_test,y_pred_decision_tree)*100))

# import matplotlib.pyplot as plt
# # import seaborn as sns
# dataset.hist(figsize = (15, 15))
# plt.show()

# from sklearn.metrics import confusion_matrix

# cm_decision = confusion_matrix(y_test, y_pred_decision_tree)
# print("confusion Marix : \n", cm_decision)
# Accuracy_Decison = ((cm_decision[0][0] + cm_decision[1][1]) / cm_decision.sum()) *100
# print("Accuracy_Decison    : ", Accuracy_Decison)

# Error_rate_Decison = ((cm_decision[0][1] + cm_decision[1][0]) / cm_decision.sum()) *100
# print("Error_rate_Decison  : ", Error_rate_Decison)

# # True Fake Recognition Rate
# Specificity_Decison = (cm_decision[1][1] / (cm_decision[1][1] + cm_decision[0][1])) *100
# print("Specificity_Decison : ", Specificity_Decison)

# # True Genuine Recognition Rate
# Sensitivity_Decison = (cm_decision[0][0] / (cm_decision[0][0] + cm_decision[1][0])) *100
# print("Sensitivity_Decison : ", Sensitivity_Decison)