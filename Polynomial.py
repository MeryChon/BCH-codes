import numpy as np


def divide_polynomials(dividend, divisor, modulo):
    i = 0
    while divisor[i] == 0:
        i += 1
    divisor_without_zeroes = divisor[i:]
    quotient, remainder = np.polydiv(dividend, divisor_without_zeroes)
    quot = quotient.tolist()
    rem = remainder.tolist()
    return [int(q % modulo) for q in quot], [int(r % modulo) for r in rem]


def is_generator_polynomial(polynomial, word_length, mod):
    dividend = [1]
    for i in range(word_length-1):
        dividend.append(0)
    dividend.append(int(-1 % mod))
    q, r = divide_polynomials(dividend, polynomial, mod)
    return is_zero_polynomial(r), q


def is_zero_polynomial(polynomial):
    for i in polynomial:
        if i != 0:
            return False
    return True
