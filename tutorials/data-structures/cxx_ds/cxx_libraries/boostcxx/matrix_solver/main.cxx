#include <iostream>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/numeric/ublas/lu.hpp>
#include <boost/numeric/ublas/vector.hpp>

using namespace boost::numeric::ublas;

int main () {
    matrix<double> A (3, 3);
    A(0,0) = 3; A(0,1) = 0; A(0,2) = 1;
    A(1,0) = 2; A(1,1) = 0; A(1,2) = -1;
    A(2,0) = 1; A(2,1) = 1; A(2,2) = -1;

    vector<double> b(3);
    b(0) = 4; b(1) = 1; b(2) = -2;

    //LU decomposition of A
    permutation_matrix<std::size_t> pm(A.size1());
    lu_factorize(A,pm);

    //Ax = b,LU decomposition
    lu_substitute(A, pm, b);

    std::cout << "The solution x is: " << b << std::endl;

    return 0;
}

