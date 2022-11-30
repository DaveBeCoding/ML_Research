import numpy as np 

A=np.array([[1,0,2],[0,-1,-2],[2,-1,0]])
b=np.array([[-1,2],[2,-6],[2,-4]])
X=np.linalg.solve(A,b)
print(X)