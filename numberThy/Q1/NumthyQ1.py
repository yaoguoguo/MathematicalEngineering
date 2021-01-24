import numpy as np
import math
import sys
 
# This program are been used to compute the Legendre symbol (a/p)

sys.setrecursionlimit(100000)

a = input("Please enter a integer a: ")
p = input("Please enter an odd prime p: ")
b = bin((p - 1) / 2)[2:]   # b is the binary expression of (p - 1) / 2

# to find the number of digits of the binary number b
n = int(b)
count = 0
while(n > 0):
    count = count + 1
    n = n // 10
numdig = count  

# to compute a^((p-1)/2) by using the repeated squaring method for modular exponentiation
def a_power(k):
    if(k > 0):
        po = a_power(k-1)
        if(int(str(b)[k-1]) == 0 ):    # int(str(b)[k]) is the kth digit of b
            result = po * po
        else:
            result = po * po * a
    else:
        result = 1
    return result

finalpower = a_power(numdig)

# to convert the Legendre symbol to the correct forms i.e. +1,-1,0
legendresym = finalpower % p

if ((legendresym != 1) and (legendresym != 0)):
    legendresym = legendresym - p

print(legendresym)
        
