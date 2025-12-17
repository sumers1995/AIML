from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error

X, y = load_diabetes(return_X_y=True, as_frame=True)
X = X[['age', 'bmi']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=23)

model = LinearRegression()
model.fit(X_train, y_train) 

mse = root_mean_squared_error(y_test, model.predict(X_test))
print("Mean Squared Error: ", mse)
