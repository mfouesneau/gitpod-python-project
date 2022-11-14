# cython: language_level=3, boundscheck=False
from __future__ import print_function
import cython

def fib(n: cython.int):
    """Print the Fibonacci series up to n."""
    a: cython.int = 0
    b: cython.int = 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

def hello_world():
    print("hello_world")
