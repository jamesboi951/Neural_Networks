# Applying to Iris Dataset
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
iris.data[0:5]
iris.feature_names

X = iris.data[:, 2:]
y = iris.target
y
clf = tree.DecisionTreeClassifier(random_state=42)
clf = clf.fit(X, y)

from sklearn.tree import export_graphviz
export_graphviz(clf,
                out_file="tree.dot",
                feature_names=iris.feature_names[2:],
                class_names=iris.target_names,
                rounded=True,
                filled=True)

