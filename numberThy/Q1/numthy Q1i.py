import numpy as np
import math
import random

# This program generates 100 random numbers between 1 and p and compute the Legendre symbol mod p for each of them

# a is a list of 100 randam numbers generated between 1 and 30275233
a = random.sample(range(1, 30275233), 100) 

p = 30275233
b = bin((p - 1) / 2)[2:]
# print(b)

# to find the number of digits of the binary number b
n = int(b)
count = 0
while(n > 0):
    count = count + 1
    n = n // 10
numdig = count
# print(numdig)   

# to compute a^((p-1)/2) by using the repeated squaring method for modular exponentiation
def a_power(basenumber, k):
    
    if(k > 0):
        p1 = a_power(basenumber, k-1)
        if(int(str(b)[k-1]) == 0 ):     # int(str(b)[k]) is the kth digit of b
            result = p1 * p1 % p
        else:
            result = p1 * p1 * basenumber % p
    else:
        result = 1
    return result

# compute legendre symbol for each of a in the list of 100 random integers
qua_res = []   # qua_res is the list of values of a s.t. (a/p)=1
for i in range(100):
    result = a_power(a[i], numdig)

    legendresym = result % p
    
    if (legendresym != 1):
        legendresym = legendresym - p
    print (a[i], int(legendresym))

    if int(legendresym) == 1:
        qua_res.append(a[i])

print qua_res
print len(qua_res)

# len(qua_res) is the number of values of a for which (a/p) = 1
