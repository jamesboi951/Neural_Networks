from sklearn import tree

X = [[0, 0], [1, 2]]
y = [0, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
clf.predict([[2., 2.]])
clf.predict_proba([[2. , 2.]])
clf.predict([[0.4, 1.2]])
clf.predict_proba([[0.4, 1.2]])
clf.predict_proba([[0, 0.2]])

