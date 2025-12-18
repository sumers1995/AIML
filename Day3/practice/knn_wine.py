from sklearn.datasets import load_iris
from sklearn.metrics import DistanceMetric
import pandas as pd 
import numpy as np

wine_data = pd.read_csv("winequality-red.csv", sep=";")
X = wine_data.loc[:,:"alcohol"]
y = wine_data.iloc[:,-1]

test_sample = [[11.45, 0.615, 0.78, 1.6, 0.089, 56, 32, 0.9943, 3.58, 0.52, 9.9]]

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
    print("Y suggested: ", y_sugg)
    mode = pd.Series(y_sugg).mode()[0]
    proba = get_proba(y_sugg, mode)
    return mode, proba
    
prediction = predict(test_sample, 20)
print("Prediction: ", prediction[0])
print("Probability: ", prediction[1])

