import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np 

from sklearn.linear_model import LinearRegression

# one feature
rng = np.random.RandomState(1)
X = 10 * rng.rand(100,3)
y = 0.3 + np.dot(X, [1.5,-2.,1.]) * rng.rand(X.shape)

model = LinearRegression()
model.fit(X, y)

xfit = np.linspace(0,10,1000)
yfit = model.predict(X)

print("Slope: ", model.coef_)
print("Intercept: ", model.intercept_)

# plt.scatter(X,y)
# plt.plot(xfit,yfit,color='red')
# plt.legend()
# plt.grid(True)
# plt.show()