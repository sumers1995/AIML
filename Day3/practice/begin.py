from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression as LR 
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=23)

clf = LR(max_iter=10000, random_state=0)
clf.fit(X_train, y_train)

acc = f1_score(y_test, clf.predict(X_test))*100
print(f"F1 score: {acc:.2f}%")