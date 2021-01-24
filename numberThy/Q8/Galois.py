# this code is to compute the quotient and the remainder given functions f and g 
# with coefficients in a finite field with p elements
# f = qg +r (mod p)

def quot_remain_strip(coeffs):
    if not coeffs or coeffs[0]:
        return coeffs

    count = 0

    for coeff in coeffs:
        if coeff:
            break
        else:
            count += 1

    return coeffs[count:]

def quot_remain_p(f, g, p, zz):
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

    return resultList[:resultQ + 1], quot_remain_strip(resultList[resultQ + 1:])