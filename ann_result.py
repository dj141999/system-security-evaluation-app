import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from sklearn.metrics import roc_curve
from keras.models import model_from_json
import time

def pred(a):
    if a:
         return str("MALWARE")
    else:
         return str("BENIGN")
                
# Importing the dataset
def tree():
	dataset = pd.read_csv("train_file2.csv", delimiter=",")
	# split into input (X) and output (Y) variables
	X = dataset.iloc[:, 1:358].values

	#print(X)
	#print(len(X[0]))

	json_file = open('SmartAM1.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	# load weights into new model
	loaded_model.load_weights("SmartAM1_1.h5")
	print("Loaded model from disk")
	 
	# evaluate loaded model on test data
	loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

	y_pred = loaded_model.predict(X)
	y_pred = (y_pred > 0.5)

	return pred(y_pred)

