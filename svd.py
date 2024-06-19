import numpy as np

# A = UDV^T
#   A is the mxm input matrix
#   U is the mxm orthogonal matrix of left-singular vectors (eigenvectors of A*A^T)
#   D is the mxn diagonal matrix of singular values of A (sqrt of eigenvalues of A*A^T and A^T*A)
#   V is the nxn orthogonal matrix of right-singular vectors (eigenvectors of A^T*A)

A = [[4, 3, 2],
     [5, 6, 7],
     [9, 8, 1]] # input matrix

# TODO: svd implementation

# TODO: visualization of signular value importance for compression

# TODO: implemetation of data compression using SVD for basic ML problem (gradient descent?)