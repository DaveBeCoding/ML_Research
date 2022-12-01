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
        self.Creating_msg()

    def gmres(self):
        print('Initializing Matrix')

    def menu(self):
        print('1. GMRES')
        print('2. Build Matrix')
        print('3. Vector B')
        print('4. Main Menu')
        print('5. Exit')
        choice = int(input('Enter your choice: '))

        match choice:
            case 1:
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


