import numpy as np 
import pandas as pd 

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True, as_frame=True)
X = X[50:]
y = y[50:] - 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accu = accuracy_score(y_pred, y_test) * 100
print("Accuracy: ", accu)
# print("Prob: ", model.predict_proba(X_test))
