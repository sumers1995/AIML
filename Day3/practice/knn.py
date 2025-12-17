from sklearn.datasets import load_iris
from sklearn.metrics import DistanceMetric
import pandas as pd 
import numpy as np 

X, y = load_iris(return_X_y=True, as_frame=True)
test_sample = [[7.7,3.0,5.1,1.3]]

def get_distance(x):
    dist = DistanceMetric.get_metric('euclidean')
    return dist.pairwise(X,x)

def predict(test, k) -> int:
    dist = get_distance(test)[:,0]
    idx = np.argpartition(dist, k)
    y_sugg = [y.iloc[idx[i]] for i in range(k)]
    print("Y suggested: ", y_sugg)
    return pd.Series(y_sugg).mode()[0]
    
print("Prediction: ", predict(test_sample, 10))