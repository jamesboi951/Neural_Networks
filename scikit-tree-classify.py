from sklearn import tree

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# predict the class of samples:
predict1 = clf.predict([[2., 2.]])
print("predict [2,2]:",predict1)

# predict the probability of each class: 
probability1 = clf.predict_proba([[2., 2.]])
print("probability [2,2]:",probability1)

probability2 = clf.predict_proba([[-1., -1.]])
print("probability [-1,-1]:",probability2)

