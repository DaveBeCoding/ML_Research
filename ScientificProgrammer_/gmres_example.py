import numpy as np, warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

'''
Used psuedo code form .png files, 

implement algorithm into Assignment1.py

have this checked over for context if possible
'''

def GMRes(A, b, x0, nmax_iter):
    r = b - np.asarray(np.dot(A, x0)).reshape(-1)

    x = []
    q = [0] * (nmax_iter)

    x.append(r)

    q[0] = r / np.linalg.norm(r)

    h = np.zeros((nmax_iter + 1, nmax_iter))

    for k in range(min(nmax_iter, A.shape[0])):
        y = np.asarray(np.dot(A, q[k])).reshape(-1)

        for j in range(k + 1):
            h[j, k] = np.dot(q[j], y)
            y = y - h[j, k] * q[j]
        h[k + 1, k] = np.linalg.norm(y)
        if (h[k + 1, k] != 0 and k != nmax_iter - 1):
            q[k + 1] = y / h[k + 1, k]

        b = np.zeros(nmax_iter + 1)
        b[0] = np.linalg.norm(r)

        result = np.linalg.lstsq(h, b, rcond=None)[0]

        x.append(np.dot(np.asarray(q).transpose(), result) + x0)

    return x


A = np.matrix('1 1; 3 -4')
b = np.array([3, 2])
x0 = np.array([1, 2])

e = 0
nmax_iter = 5

x = GMRes(A, b, x0, nmax_iter)

print(x)

# [array([0, 7]), array([1.        , 0.35294118]), array([2., 1.])]
''''
This problem was checked with -> [array([0, 7]), array([1.        , 0.35294118]), array([2., 1.])]

>>> import numpy as np
>>> from scipy.sparse import csc_matrix
>>> from scipy.sparse.linalg import gmres
>>> A = csc_matrix([[1, 1], [3, -4]], dtype=float)
>>> b = np.array([1, 2], dtype=float)
>>> x, exitCode = gmres(A, b) # exitCode == return 0 -> True/Successful (convergence)
>>> print(exitCode) #successful -> 0        
0
>>> np.allclose(A.dot(x), b) # Orthonormality??
True
>>> print(x)
[2. 1.]
'''