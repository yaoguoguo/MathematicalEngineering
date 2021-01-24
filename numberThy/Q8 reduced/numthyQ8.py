# coding: utf-8
import sys
from Galois import GaloisClass

sys.setrecursionlimit(100000)

fcoeff = input("Please enter the list of coefficients of the function f: ")
p = input("Please enter an odd prime p: ")  # this is the prime p we are takig modulo with
objc = GaloisClass(fcoeff, p)
objc.solution()