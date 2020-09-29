# Random Forest Classification
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
def pred(a):
    if a==0:
         return str("BENIGN")
    else:
         return str("MALWARE")
                
# Importing the dataset
def tree():
	dataset = pd.read_csv("MSGmalware_analysis_dataset_if.csv", delimiter=",")
	d = pd.read_csv("train_file2.csv", delimiter=",")

	# split into input (X) and output (Y) variables
	d1= d.iloc[:, :357].values 
	#d2= d.iloc[:, 358].values
	X = dataset.iloc[:, 1:358].values
	y = dataset.iloc[:, 358].values
	# Splitting the dataset into the Training set and Test set
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, 
	                                                    random_state = 0)
	# Feature Scaling
	from sklearn.preprocessing import StandardScaler
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)
	d1 = sc.transform(d1)

	# Fitting Random Forest Classification to the Training set
	from sklearn.ensemble import RandomForestClassifier
	classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
	classifier.fit(X_train, y_train)

	# Predicting the Test set results
	y_pred = classifier.predict(X_test)
	y_o = classifier.predict(d1)

	return pred(y_o)
