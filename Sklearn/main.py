# load libraries 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


data = load_iris()

X = data.data
y = data.target
feature_names = data.feature_names
target_names = data.target_names
print(feature_names, target_names)
print(X, y)


# how to split datasett
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
print(X_test.shape)

# train the model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

model = KNeighborsClassifier()
model.fit(X_train, y_train)
y_predicted = model.predict(X_test)
accuracy = accuracy_score(y_predicted, y_test)
print("Here is our accuracy: {}%".format(int(accuracy*100)))
random = [[5, 5, 3, 2]]
random_pred = model.predict(random)
print(data.target_names[random_pred])


# how to save trained model and use it later
#from sklearn.externals import joblib
#joblib.dump(model, 'iris_model_classifier.joblib')
#loaded_model = joblib.load('iris_model_classifier.joblib')

#random_pred = loaded_model.predict(random)
#print(data.target_names[random_pred])


# Binarizer
from sklearn.preprocessing import Binarizer
import numpy as np
from numpy.random import randint
binarizer = Binarizer()
data = np.random.randint(0,1,10)
print(data)


