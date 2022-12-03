from time import sleep as pause
import scipy.sparse as sparse
from os import system, name, _exit
import scipy.stats as stats
import numpy as np
 
STOP = 0b11
"""
Create infrastructure for studying this algorithm
    Create a reasonable CLI (command-line interface) that allows the user to tweak settings like n, m and density (what % of elements are non-zero)
    Be able to generate random A matrices that will converge on a correct solution
        I did this by randomly adding values between 0-1 for non-zero elements, except for along the diagonal which were all non-zero and set to cube root 
        of n . With this approach, I was getting matrices that worked up to 1000x1000 which is as high as you'll need in the python phase of this course. 
        Only the largest of my test matrices required restarts.
    Be able to generate random dense f (100% non-zero, values 0-1).
    You should also have infrastructure for hardcoded test fixtures for testing etc
Create classes and methods for mathematical concepts
    A dense matrix class with
        scalar add/multiply
        matrix/matrix add/multiply
        element indexing
        normalize (assumes it's a vector (the second dimension is 1)). Whether you make Vector a special class or just use matrices with second dim=1 is 
        up to you.
        get euclidean norm (vector-only)
        dot product (vector-only)
        QR factorization
        inverse
        submatrix
Jennifer Loe lecture on why we care about GMRES. Optional?

algorithm details: https://en.wikipedia.org/wiki/Generalized_minimal_residual_method
"""

class GMRES:
    def __init__(self) -> None:
        self.clear()
        self.main_msg()
    
    def clear(self): # system agnostic 
        if(name == 'nt'):
            _ = system('cls')
        else:
            _ = system('clear')

    def greating(self) -> None:
        print("The Size of the Matrix is " + '"' + str(self.n) + "x" 
                    + str(self.m) + '"' + " with Density of " + str(self.dens)+"%")
        n_X_m = self.build_matrix()
        print(n_X_m)
        pause(STOP)
    
    def build_matrix(self) -> int:
        np.random.seed(42)
        A = sparse.random(self.n, self.m, density=self.dens)
        return A.toarray()
    
    def Creating_msg(self):
        '''Create Matrix-A for Ax=b'''
        print('Creating Matrix A')
        n = int(input("Enter Size of N rows "))
        m = int(input("Enter Size of M columns "))
        dens = int(input('Enter Density % of Matrix -> Example "25" for 25% '))
        self.n = n
        self.m = m
        self.dens = (dens / 100)
    
    def vector_b(self):
        '''Create Vector-b for Ax=b'''
        print('Creating Vector b')
        v = int(input("Enter Size of Vector column "))
        self.v = v
    
    def main_msg(self):
        print('Welcome to the GMRES Assignment-1 Calulator, ' 
        + ' Select from the following Options')
        self.menu()
        # Add further options, use Create_msg as a setup example
        # Start here once test methods are flowing correctly
        self.Creating_msg()

    def gmres(self, A, b, x0, nmax_iter):
        print('Initializing Matrix')

        r = b - np.asarray(np.dot(A, x0)).reshape(-1)
        x = []
        q = [0] * (nmax_iter)

        x.append(r)

        q[0] = r / np.linalg.norm(r)

        h = np.zeros((nmax_iter + 1, nmax_iter))

        # for k in range(nmax_iter):
        #     y = np.asarray(np.dot(A, q[k])).reshape(-1)
        for k in range(min(nmax_iter, A.shape[0])):
            y = np.asarray(np.dot(A, q[k])).reshape(-1)

            # for j in range(k):
            for j in range(k + 1):
                h[j, k] = np.dot(q[j], y)
                y = y - h[j, k] * q[j]
            h[k + 1, k] = np.linalg.norm(y)
            if (h[k + 1, k] != 0 and k != nmax_iter - 1):
                q[k + 1] = y / h[k + 1, k]

            b = np.zeros(nmax_iter + 1)
            b[0] = np.linalg.norm(r)

            result = np.linalg.lstsq(h, b)[0]

            x.append(np.dot(np.asarray(q).transpose(), result) + x0)

        return x


    def menu(self):
        print('1. GMRES')
        print('2. Build Matrix')
        print('3. Vector B')
        print('4. Main Menu')
        print('5. Exit')
        choice = int(input('Enter your choice: '))

        match choice:
            case 1:
                A = np.matrix('1 1; 3 -4') #replace with dynamic matrix input 
                b = np.array([3, 2])
                x0 = np.array([1, 2])

                e = 0
                nmax_iter = 5

                x = self.gmres(A, b, x0, nmax_iter)

                print(x)
                self.gmres()
            case 2:
                self.build_matrix()
            case 3:
                self.vector_b()
            case 4:
                self.menu()
            case 5:
                self.clear()
                print('Exiting...')
                pause(STOP)
                _exit(0)
                
    def main(self) -> None:
        self.greating()

try:
    if __name__ == "__main__":
        gmres = GMRES()
        pause(STOP)
        gmres.main()
except:
    print("ERROR, Please check your configuration")