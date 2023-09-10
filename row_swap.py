# -*- coding: utf-8 -*-
"""row swap

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zj7KKtiX9qbl39S1cDi0uzZuFfo40BOU
"""

import numpy as np

def swaprow(i, j, A):
    A[i, :], A[j, :] = A[j, :], A[i, :]  # Swap rows i and j using tuple unpacking

# Example usage:
# Create a sample 2D NumPy array
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Original Array:")
print(A)

# Swap rows 0 and 2
swaprow(0, 2, A)

print("\nArray after swapping rows 0 and 2:")
print(A)