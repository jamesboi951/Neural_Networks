from sklearn.datasets import fetch_mldata
mnist = fetch_mldata("MNIST original")

print("mnist:", mnist)
print("length mnist:", len(mnist['data']))
 
X, y = mnist['data'], mnist['target']
print("X:", X)
print("y:", y)
 
print("X[69999]:", X[69999])
print("y[69999]:", y[69999])

print("X.shape:",X.shape)
print("y.shape:",y.shape)

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

_ = X[1000]
_image = _.reshape(28,28)
plt.imshow(_image)
plt.show()

