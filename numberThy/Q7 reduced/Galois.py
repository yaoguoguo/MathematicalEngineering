# coding: utf-8
import numpy as np
import random
from sympy.polys.domains import ZZ

class GaloisClass:
    fcoeff = []
    p = 0
    gx = []  # g(x) is the greatest common divisor of the original function f(x) x^p - x

    def __init__(self, coeffs, p):
        self.fcoeff = coeffs
        self.p = p
        self.gx = self.GCD([1, 0], p, [-1, 0], coeffs)

    # this function computes the gcd
    def GCD(self, start, p, y, fcoeff):
        binary_p = bin(p)[2:]
        yoly1d = np.poly1d(y)
        digits = [int(d) for d in str(binary_p)]
        relist = list(reversed(digits))
        position = [i for i, e in enumerate(relist) if
                    e == 1]  # ths gives the values of k we should multipled together to get x^p mod f(x)
        mod_xpminusx = np.polyadd((self.mod_xp(position, fcoeff, start)), yoly1d)
        list1 = mod_xpminusx.coeffs
        ress = self.modp(list1, fcoeff)  # ress is the x^p -x mod f(x)

        # this recursion is to do the Euclid Algorithm by repeating the process until get the gcd
        i = 0
        while 1:
            re = self.recursion(i, fcoeff, ress)
            if re == []:
                break
            i += 1
        gcd = self.recursion(i - 1, fcoeff, ress)
        return gcd

    def x_powermod(self, k, fcoeff, a1):  # this function genrates x^(2^k) mod function f(x)
        if (k > 0):
            p1 = np.poly1d((np.poly1d(self.x_powermod((k - 1), fcoeff, a1)) ** 2).coeffs % self.p)
            result = self.quot_remain_p(ZZ.map(p1.coeffs), ZZ.map(fcoeff), self.p, ZZ)[1]
        else:
            result = a1
        return [item % self.p for item in result]

    def mod_xp(self, position, fcoeff, a1):  # mod_xp(p) is x^p mod f(x)
        # multiply elements one by one
        result = np.poly1d(1)
        for x in position:
            result = np.poly1d((result * np.poly1d(self.x_powermod(x, fcoeff, a1))).coeffs % self.p)
            result = self.quot_remain_p(ZZ.map(np.poly1d(result).coeffs), ZZ.map(fcoeff), self.p, ZZ)[1]
        return result

    def modp(self, list1, fcoeff):
        return list1 % self.p

    # this part is to do the Euclid's Algorithm
    def recursion(self, k, fcoeff, re):
        gcd = [1]
        if k > 1:
            gcd = self.quot_remain_p(ZZ.map(self.recursion((k - 2), fcoeff, re)), ZZ.map(self.recursion((k - 1), fcoeff, re)), self.p, ZZ)[1]
        elif any(re) == False:
            gcd = fcoeff
        else:
            if k == 0:
                gcd = re
            else:
                gcd = self.quot_remain_p(ZZ.map(fcoeff), ZZ.map(re), self.p, ZZ)[1]
        return [item % self.p for item in gcd]

    def rand_startP(self):  # this function generates random value v
        v = random.randint(0, 100)
        newP = [1, v]
        return newP

    def modInverse(self, a, m):  # this function is to find the inverse of a mod m
        a = a % m
        for x in range(1, m):
            if ((a * x) % m == 1):
                return x
        return 1

    def monic(self, GCD):  # this function is to compute the monic gcd
        modIn = self.modInverse(GCD[0], self.p)
        return [1, modIn * GCD[1] % self.p]

    # this function is to compute the final solutions, if one v doesn't work then change another one
    def roots_f(self, startP, g_x, resss):
        if np.poly1d(g_x).order == 1:
            resss.append(self.monic(g_x))
            return resss
        else:
            P = (self.p - 1) / 2
            Y = [-1]
            r = self.GCD(startP, P, Y, g_x)
            if np.poly1d(r).order < np.poly1d(g_x).order and np.poly1d(r).order != 0:
                resss.append(self.monic(r))
                g_x = self.quot_remain_p(ZZ.map(g_x), ZZ.map(np.poly1d(self.monic(r))), self.p, ZZ)[0]
                return self.roots_f(startP, g_x, resss)
            else:
                startP = self.rand_startP()
                return self.roots_f(startP, g_x, resss)

    def solution(self):
        solutions = self.roots_f(self.rand_startP(), self.gx, [])
        print solutions

        roots = []
        for term in solutions:
            sol = term[1] % self.p
            roots.append(sol)

        print "---------------roots---------------"
        print roots

        return roots


    # the following part of the code computes the quotient and the remainder given functions f and g
    # with coefficients in a finite field with p elements
    # f = qg +r (mod p)

    def quot_remain_strip(self, coeffs):
        if not coeffs or coeffs[0]:
            return coeffs

        count = 0

        for coeff in coeffs:
            if coeff:
                break
            else:
                count += 1

        return coeffs[count:]
    
    # this function computes the quotient and the remainder 
    def quot_remain_p(self, f, g, p, zz):
        lenF = len(f) - 1
        lenG = len(g) - 1

        if lenF < lenG:
            return [], f

        resultList, resultQ, resultR = list(f), lenF - lenG, lenG - 1

        invert = zz.invert(g[0], p)

        for index in range(0, lenF + 1):
            coe = resultList[index]

            start = max(0, lenG - index)
            end = min(lenF - index, resultR) + 1

            for i in range(start, end):
                coe = coe - resultList[index + i - lenG] * g[lenG - i]

            if index <= resultQ:
                coe = coe * invert

            resultList[index] = coe % p

        return resultList[:resultQ + 1], self.quot_remain_strip(resultList[resultQ + 1:])