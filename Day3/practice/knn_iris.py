from sklearn.datasets import load_iris
from sklearn.metrics import DistanceMetric
import pandas as pd 
import numpy as np 

X, y = load_iris(return_X_y=True, as_frame=True)
test_sample = [[7.7,3.0,5.1,1.3]]

def get_distance(x):
    dist = DistanceMetric.get_metric('euclidean')
    return dist.pairwise(X,x)

def get_proba(least, mode) -> float:
    count = np.count_nonzero(least==mode)
    return count/len(least)

def predict(test, k: int) -> (int, float):
    dist = get_distance(test)[:,0]
    idx = np.argpartition(dist, k)
    y_sugg = [y.iloc[idx[i]] for i in range(k)]
    # print("Y suggested: ", y_sugg)
    mode = pd.Series(y_sugg).mode()[0]
    proba = get_proba(y_sugg, mode)
    return mode, proba
    
prediction = predict(test_sample, 10)
print("Prediction: ", prediction[0])
print("Probability: ", prediction[1])