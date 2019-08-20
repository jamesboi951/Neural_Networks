import numpy as np
import matplotlib.pyplot as plt
import seaborn

x = np.linspace(-5,5,num=1000)
plt.figure(figsize=(10,8))
plt.plot(x, 1/(1+np.exp(-x)))
plt.title("Sigmoid Function")
plt.show()

