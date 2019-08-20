import numpy as np
import matplotlib.pyplot as plt
import seaborn

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

coef = [-0.8, 0.2]
for row in dataset:
  yhat = 1.0/(1.0+np.exp(-coef[0] - coef[1]*row[0]))
  print("yhat {0:.4f} yhat round {1} ".format(yhat, round(yhat)))

