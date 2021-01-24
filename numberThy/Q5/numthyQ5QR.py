import numpy as np
import math
import random

# this program finds all the quadratic residues mod p between 1 and 20

a = range(1, 21)
   
p = 30275233
b = bin((p - 1) / 2)[2:]

# to find the number of digits of the binary number b
n = int(b)
count = 0
while(n > 0):
    count = count + 1
    n = n // 10
numdig = count

# to compute a^((p-1)/2) by using the repeated squaring method for modular exponentiation
def a_power(basenumber, k):
    
    if(k > 0):
        p1 = a_power(basenumber, k-1)
        if(int(str(b)[k-1]) == 0 ):      # int(str(b)[k]) is the kth digit of b
            result = p1 * p1 % p
        else:
            result = p1 * p1 * basenumber % p
    else:
        result = 1
    return result

result_list = []   # qua_res is the list of values of a s.t. (a/p)=1
for i in range(20):
    result = a_power(a[i], numdig)

    legendresym = result % p
    
    if (legendresym != 1):
        legendresym = legendresym - p
    #print (a[i], int(legendresym))

    if int(legendresym) == 1:
        result_list.append(a[i])

print result_list