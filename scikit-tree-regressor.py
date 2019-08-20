from sklearn import tree

X = [[0, 0], [2, 2]]
y = [0.5, 2.5]

clf = tree.DecisionTreeRegressor()
clf = clf.fit(X, y)

predict1 = clf.predict([[1, 1]])
print("predict [1, 1]:",predict1)

predict2 = clf.predict([[1, 5]])
print("predict [1, 5]:",predict2)

