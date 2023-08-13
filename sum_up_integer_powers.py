# -*- coding: utf-8 -*-
"""sum up integer powers

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KY0kUvYixXYpo9KJ92ukDijWw2MGbL3I
"""

def calculate_sum(N, i):
    total_sum = 0
    for num in range(1, N+1):
        total_sum += num ** i
    return total_sum

N = int(input("Enter the value of N: "))
i = int(input("Enter the value of i: "))

result = calculate_sum(N, i)
print(f"The summation of {N} consecutive integers raised to the power of {i} natural numbers is: {result}")