from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.inspection import DecisionBoundaryDisplay
import matplotlib.pyplot as plt

X, y = load_breast_cancer(return_X_y=True)
X = X[:,:2]

plt.scatter(X[:,0], X[:,1], c= y, )
plt.show()

model = SVC(kernel='linear', C=1)
model.fit(X, y)

