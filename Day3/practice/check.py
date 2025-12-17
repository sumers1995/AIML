from sklearn.metrics import DistanceMetric

dist = DistanceMetric.get_metric('euclidean')

X = [[1,2,3,4],
     [2,3,4,5]]
y = [[1,2,3,4]]

print(dist.pairwise(X,y))