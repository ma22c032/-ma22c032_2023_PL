# -*- coding: utf-8 -*-
"""Bisection method

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vZMlHqGnA38n_m35y6tBD5ovZIPI7DBq

"""

a=float(input("a(interval started from a)= "))
b=float(input("b(interval ended at b)= "))
eps=float(input("eps(for accuracy)= "))
f = input('type your function=')

def bisection_method(f,a,b,eps,niters):

# Implement the bisection method to find a root of the function f(x) = 0.
# f:The function for which to find the root.
# a:The left endpoint of the interval.
# b:The right endpoint of the interval.
# eps:The tolerance for the root.
#niters:The maximum number of iterations to perform.

  if f(a) * f(b) >= 0:
        print("Error: The function values at the endpoints must have different signs.")
  else:
     iteration = 0
  while (b - a) / 2 > eps and iteration < niters :
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1

  return (a + b) / 2
