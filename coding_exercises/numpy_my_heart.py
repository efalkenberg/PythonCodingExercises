#!/usr/bin/python
# -*- coding: utf-8 -*-

# my notes while getting a little refreshed on the basics
# https://numpy.org/doc/stable/user/absolute_beginners.html

import numpy as np

print("------------- BASIC CREATION, SHAPES, TYPES -------------")
a = np.array([1, 2, 3, 4, 5, 6])
print(f"{str(a)} is of shape {a.shape}")
print(f"`a` has {a.ndim} dimension")
print(f"The size of `a` is the overall number of elements in all dimensions which is {a.size}")
print(f"Element types in numpy arrays are homogeneous, `a` can hold values of type {a.dtype}")


print("------------- 2D ARRAYS AND ACCESS -------------")

# two-dimensional array and access
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"{str(b)} is of shape {b.shape}")
print(f"b[0] = {b[0]}")
print(f"b[0,3] = {b[0,3]}")

print("------------- SCLICING -------------")

# slicing a numpy array returns a view, not a copy of the data
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f"c[:2] = {c[:2]} (the first two elements of the top level dimension (row))")
print(f"c[:-1] = {c[:-1]} (all top level elements up to (but without) the last one")
print(f"c[c > 5] = {c[c > 5]} (all elements gt 5)")
print(f"c[c%=5==0] = {c[c%5==0]} (all elements divisible by 5)")
print(f"`c > 5` = {c > 5} (new array with same dimensions, boolean values 🤯)")
print(f"""`np.nonzero(c > 5)` = {np.nonzero(c > 5)} 
returns tuple of arrays (one per dimension with the indices matching the expr)""")

print("------------- INITIALIZE ARRAYS -------------")

# other ways to initialize arrays
print(f"""a null matrix can be created with np.zeros((3, 4)):
{np.zeros((3, 4))}""")
print(f"""a null matrix is dtype float by default but it's configurable np.zeros((3, 4), int):
{np.zeros((3, 4), np.int64)}""")
print(f"""np.ones(2, 3) is the convenient method to create arrays initialized with all ones:
{np.ones((2, 3))}
as with `zeros()` this also defaults to dtype float and can be configured""")
print(f"""if you don't care about the content, `np.empty(2, 3)` will create an array with random
values that depend on the state of the memory (faster)
{np.empty((2, 3))}
""")
print(f"""a range of elements can be created with `np.range(first number, number limit, step size)`
like `np.arange(2, 10, 2)`: (note that the limit is not included)
{np.arange(6, 24, 3)}
For multi dimensions, create a single dimensional array first and reshape afterwards
""")
print(f"""for evenly distributed values over an interval, use `np.linspace(start, end, num)`
like `np.linspace(0, 20, 5)`
{np.linspace(0, 20, 5, dtype=np.int64)}""")
print(f"""for arrays with randomized values use `np.random.rand(3, 2):
{np.random.rand(3, 2)}""")

print("------------- ARITHMETICS -------------")

a = (np.random.rand(3, 2) * 100).astype(np.int64)
b = (np.random.rand(3, 2) * 100).astype(np.int64)
print(f"""
a: {a}
b: {b}
Arithmetics are easy:
a + b = {a + b}
a - b = {a - b}
a * b = {a * b}
a . b = {a.dot(b.T)}  # b.T for the simplicity of this example so that the size matches

""")

print("------------- RESHAPING -------------")

a = (np.random.rand(3, 2) * 100).astype(np.int64)
print(f"""{a} is of shape {a.shape} but can be reshaped as long as the size (a.size) matches
`np.reshape(a, (1, 6))` (vector):
{np.reshape(a, (1, 6))}
`np.reshape(a, (6, 1))` (column vector):
{np.reshape(a, (6, 1))}
""")

# NEXT: https://numpy.org/doc/stable/user/absolute_beginners.html#how-to-create-an-array-from-existing-data
