import numpy as np

tmp = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
rounded = np.round(tmp)

# default 'cutoff' value of 0.5:
# under 0.5: => 0
# over  0.5: => 1
print("rounded:",rounded)

# specify 'cutoff' value of 0.7:
print("tmp > 0.7:", np.array(tmp)>0.7)

