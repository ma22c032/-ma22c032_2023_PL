# -*- coding: utf-8 -*-
"""null space

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11NIloVIexJJC5j2o36lqX-tN60bVE6Gv
"""

import numpy as np
from scipy.linalg import svd

# Given matrix A
A = np.array([[1, -2, 9, 5, 4], [1, -1, 6, 5, -3], [-2, 0, -6, 1, -2], [4, 1, 9, 1, -9]])

# Perform SVD on A
u, s, vh = svd(A)

# Find the null space from SVD
null_space_svd = vh.T[:, np.where(s < 1e-10)].squeeze()
print("Null space using SVD:")
print(null_space_svd)

from scipy.linalg import qr

# Given matrix A
A = np.array([[1, -2, 9, 5, 4], [1, -1, 6, 5, -3], [-2, 0, -6, 1, -2], [4, 1, 9, 1, -9]])

# Perform QR factorization on the transpose of A
Q, R = qr(A.T)

# Extract the orthogonal complement from QR factorization
null_space_qr = Q[:, np.where(np.abs(np.diag(R)) < 1e-10)].squeeze()
print("Null space using QR factorization (orthogonal complement of range of transpose A):")
print(null_space_qr)

# Check if both null spaces span the same space
span_same_space = np.allclose(null_space_svd, null_space_qr)
if span_same_space:
    print("Both null spaces span the same space.")
else:
    print("Both null spaces do not span the same space.")

