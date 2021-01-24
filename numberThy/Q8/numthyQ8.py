import numpy as np
import math
import random
import sys
from Galois import quot_remain_p
from sympy import poly
from sympy.abc import x
from sympy.polys.domains import ZZ

sys.setrecursionlimit(100000)

fcoeff = input("Please enter the list of coefficients of the function f: ")
p = input("Please enter an odd prime p: ")  # this is the prime p we are takig modulo with


# this function computes the gcd
def GCD(start, p, y, fcoeff):
    binary_p = bin(p)[2:]
    yoly1d = np.poly1d(y)
    digits = [int(d) for d in str(binary_p)]
    relist = list(reversed(digits))
    position = [i for i, e in enumerate(relist) if
                e == 1]  # ths gives the values of k we should multipled together to get x^p mod f(x)
    mod_xpminusx = np.polyadd((mod_xp(position, fcoeff, start)), yoly1d)
    list1 = mod_xpminusx.coeffs
    ress = modp(list1, fcoeff)  # ress is the x^p -x mod f(x)

    # this recursion is to do the Euclid Algorithm by repeating the process until get the gcd
    i = 0
    while 1:
        re = recursion(i, fcoeff, ress)
        if re == []:
            break
        i += 1
    gcd = recursion(i - 1, fcoeff, ress)
    return gcd


def x_powermod(k, fcoeff, a1):  # this function genrates x^(2^k) mod function f(x)
    if (k > 0):
        p1 = np.poly1d(x_powermod((k - 1), fcoeff, a1)) ** 2
        result = quot_remain_p(ZZ.map(p1.coeffs), ZZ.map(fcoeff), p, ZZ)[1]
    else:
        result = a1
    return [item % p for item in result]


def mod_xp(position, fcoeff, a1):  # mod_xp(p) is x^p mod f(x)
    # multiply elements one by one
    result = np.poly1d(1)
    for x in position:
        result = np.poly1d((result * np.poly1d(x_powermod(x, fcoeff, a1)) ).coeffs % p)
        result = quot_remain_p(ZZ.map(np.poly1d(result).coeffs), ZZ.map(fcoeff), p, ZZ)[1]
    return result


def modp(list1, fcoeff):
    return list1 % p


# this part is to do the Euclid's Algorithm
def recursion(k, fcoeff, re):
    gcd = [1]
    if k > 1:
        gcd = quot_remain_p(ZZ.map(recursion((k - 2), fcoeff, re)), ZZ.map(recursion((k - 1), fcoeff, re)), p, ZZ)[1]
    elif any(re) == False:
        gcd = fcoeff
    else:
        if k == 0:
            gcd = re
        else:
            gcd = quot_remain_p(ZZ.map(fcoeff), ZZ.map(re), p, ZZ)[1]
    return [item % p for item in gcd]


gx = GCD([1, 0], p, [-1, 0], fcoeff)  # g(x) is the greatest common divisor of the original function f(x) x^p - x

P = (p - 1) / 2
Y = [-1]


def rand_startP():  # this function generates random value v
    v = random.randint(0, 20)
    newP = [1, v]
    return newP


def modInverse(a, m):  # this function is to find the inverse of a mod m
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1


def monic(GCD):  # this function is to compute the monic gcd
    modIn = modInverse(GCD[0], p)
    return [1, modIn * GCD[1] % p]


# this function is to compute the final solutions, if one v doesn't work then change another one
def roots_f(startP, g_x, resss):
    if np.poly1d(g_x).order == 1:
        resss.append(monic(g_x))
        return resss
    else:
        r = GCD(startP, P, Y, g_x)
        if np.poly1d(r).order < np.poly1d(g_x).order and np.poly1d(r).order != 0:
            resss.append(monic(r))
            g_x = quot_remain_p(ZZ.map(g_x), ZZ.map(np.poly1d(monic(r))), p, ZZ)[0]
            return roots_f(startP, g_x, resss)
        else:
            startP = rand_startP()
            return roots_f(startP, g_x, resss)


solutions = roots_f(rand_startP(), gx, [])
print solutions

roots = []
for term in solutions:
    sol = term[1] % p
    roots.append(sol)

print "---------------roots---------------"
print roots