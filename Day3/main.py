import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


np.random.seed(42)
X = np.random.rand(50, 1) * 100
Y = 3.5 * X + np.random.randn(50, 1) * 20

model = LinearRegression()
model.fit(X,Y)
# predict_y = model.predict(np.array([50]).reshape(1,-1))
predict_y = model.predict(X)
print("Prediction: ", predict_y)
print(model.coef_)
print(model.intercept_)

plt.figure(figsize=(8,6))
plt.scatter(X,Y, color='blue', label='Data Points')
plt.plot(X, predict_y, color='red')
plt.legend()
plt.grid(True)
plt.show()