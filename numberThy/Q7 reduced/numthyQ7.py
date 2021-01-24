# coding: utf-8
from Galois import GaloisClass
import sys
from sympy import poly
from sympy.abc import x

sys.setrecursionlimit(100000)

a = input("Please enter a integer a: ")
p = input("Please enter an odd prime p: ")

fcoeff = poly(x ** 2 - a).all_coeffs()  # fcoeff is the coefficients of the function f we want
objc = GaloisClass(fcoeff, p)
objc.solution()