import numpy as np
m = np.arange(20).reshape(5,4)

print(m,'\n')
print(m[1:3, 1:3])
print(m[:, 1:3])
print(m[1:3,:])