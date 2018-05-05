from functools import reduce

import math as mt
import numpy as np


def is_prime(p):
    if p < 2:
        return False
    for i in range(2, mt.floor(mt.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True


def fibonacy(n, a=1, m=65536, FIBONACY={}):
    try:
        try:
            return FIBONACY[(a, m)][n]
        except KeyError:
            FIBONACY[(a, m)] = {0: 0, 1: 1}
            return FIBONACY[(a, m)][n]
    except KeyError:
        for i in range(2, n + 1):
            FIBONACY[(a, m)][i] = \
                mod_add(
                    mod_mul(a, fibonacy(i - 1, a, m, FIBONACY), m),
                    fibonacy(i - 2, a, m, FIBONACY),
                    m
                )
        return FIBONACY[(a, m)][n]


mod_add = \
    lambda a, b, m: (a + b) % m


mod_mul = \
    lambda a, b, m: (a * b) % m


mod_pow = \
    lambda b, e, m: \
    reduce(
        (lambda p, q: mod_mul(p, q, m)),
        [1] + [b] * e
    )


def mod_matrix_mul(A, B, m):
    R = np.zeros((A.shape[0], B.shape[1]), np.dtype('I'))

    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            R[i, j] = reduce(
                lambda p, q: mod_add(p, q, m),
                [mod_mul(A[i][k], B[k][j], m) for k in range(B.shape[0])]
            )
            j += 1
        i += 1

    return R


def mod_matrix_pow(B, e, m):
    if e == 0:
        return np.eye(B.shape[0])
    if e % 2 == 1:
        return mod_matrix_mul(
            B,
            mod_matrix_pow(B, e - 1, m),
            m
        )
    D = mod_matrix_pow(B, e // 2, m)
    return mod_matrix_mul(D, D, m)
