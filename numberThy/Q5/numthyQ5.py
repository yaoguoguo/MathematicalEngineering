import numpy as py
import math

p = 23
pminus = p - 1


# this part of the program is to write p in the form 2^k+1
def judgment(pminus):
    i = 0
    while (pminus % 2) == 0:
        i += 1
        pminus /= 2
    return i


power_2 = judgment(pminus)  # this is the power of 2 in p-1

print power_2

s = pminus / 2 ** power_2  # s is odd here
print s

b = (10 ** s) % p
print b

# this part of the program is to find the square roots mod p for each quadratic residues between 1 and 20 given a
a = 4  # need to ensure that this a is indeed a quadratic residue mod p


def result(k):  # result is the list of r0,...rk, which is the binary digits of r
    listr = []
    if a ** ((p - 1) / 4) % p == 1:
        listr.append(0)
    else:
        listr.append(1)
    i = 1
    while (i < k):
        Gi = b
        j = i - 1
        while (j >= 0):
            Gi *= ((b ** (2 ** (power_2 - (i + 1 - j)) * listr[j] * s) % p) % p)
            Gi = Gi % p
            print Gi
            j -= 1
        ai = a ** ((p - 1) / 2 ** (i + 2)) % p  # this is to compute a^[(p-1)/(2^(k+2))] mod p
        # if ai == Gi, then ri = 0,otherwise 1
        if ai == Gi:
            listr.append(0)
        else:
            listr.append(1)

        i += 1
    return listr


listr = result(power_2 - 1)
print listr

result = []
for index, i in enumerate(listr):
    if i == 1:
        result.append(index)

r = 0
for i in result:
    r += (2 ** i) * s

print r 
y = b ** r % p
print y 


# solve for y^2=a (mod p) by using y^2=a^s (mod p)
b = bin(p)[2:]   # b is the binary expression of p

# to find the number of digits of the binary number b
n = int(b)
count = 0
while(n > 0):
    count = count + 1
    n = n // 10
numdig = count  

# to compute a^p by using the repeated squaring method for modular exponentiation
def a_power(k):
    if(k > 0):
        po = a_power(k-1)
        if(int(str(b)[k-1]) == 0 ):    # int(str(b)[k]) is the kth digit of b
            result = po * po
        else:
            result = po * po * y
    else:
        result = 1
    return result

finalpower = a_power(numdig)

y = finalpower % p




print (y, p - y)
print(y ** 2 % p)  # this is to check that it works