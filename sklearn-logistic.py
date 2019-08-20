from sklearn.linear_model import LogisticRegression
import numpy as np

dataset = [[-2.00, 0],
           [-1.46, 0], 
           [ 0.96, 0], 
           [ 1.38, 0], 
           [ 3.06, 0], 
           [ 4.55, 0], 
           [ 5.30, 1], 
           [ 6.90, 1], 
           [ 7.65, 1], 
           [ 8.75, 1]]

X = np.array(dataset)[:,0:1]
y = np.array(dataset)[:,1]

print("X:")
print(X)
print("y values:",y)

# make predictions with L1 and L2 penalties 
print("Penalty: L1")
clf_LR = LogisticRegression(C=1.0, penalty="l1", tol=0.01)
clf_LR.fit(X,y)
print("predict: ",clf_LR.predict(X))
print("Penalty: L2")
clf_LR = LogisticRegression(C=1.0, penalty="l2", tol=0.01)
clf_LR.fit(X,y)
print("predict: ",clf_LR.predict(X))
print("-------------------------\n")
 
print("probabilities: ")
print(clf_LR.predict_proba(X))
print("-------------------------\n")

