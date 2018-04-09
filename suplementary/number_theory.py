import functools
import operator
import math

def is_prime(_p):
    if _p < 2:
        return False
    for i in range(2, math.floor(math.sqrt(_p)) + 1):
        if _p % i == 0:
            return False
    return True

# TODO create unittest
FIBONACY = {0: 0, 1: 1,}
def fibonacy(_n):
    try:
        return FIBONACY[_n]
    except KeyError:
        for i in range(2, _n + 1):
            FIBONACY[i] = fibonacy(i - 1) + fibonacy(i - 2)
        return FIBONACY[_n]


# TODO create unittest
FIBONACY_A = {0: 0, 1: 1, }
def fibonacy_a(_a, _n):
    try:
        return FIBONACY_A[_n]
    except KeyError:
        for i in range(2, _n + 1):
            FIBONACY_A[i] = _a * fibonacy_a(_a, i - 1) + fibonacy_a(_a, i - 2)
        return FIBONACY_A[_n]


mod_add = \
    lambda a, b, modulus: (a + b) % modulus


mod_mul = \
    lambda a, b, modulus: functools.reduce(
        (lambda p, q: mod_add(p, q, modulus)),
        [0, ] + [a for x in range(b)]
    )


mod_pow = \
    lambda base, exponent, modulus: \
    functools.reduce(
        (lambda p, q: mod_mul(p, q, modulus)),
        [1, ] + [base for x in range(exponent)]
    )


mod_matrix_mul = lambda A, B, modulus: [
    [
        functools.reduce(
            lambda p, q: mod_add(p, q, modulus),
            [mod_mul(A[i][k], B[k][j], modulus) for k in range(len(B))]
        )
        for j in range(len(B[0]))
    ]
    for i in range(len(A))
]


__identity = lambda x, y: 1 if x == y else 0
matrix_identity = lambda N: \
    [
        [__identity(x, y) for y in range(N)]
        for x in range(N)
    ]


# TODO refactor mod_matrix_pow to functional function
def mod_matrix_pow(base_matrix, exponent, modulus):
    if exponent == 0:
        return matrix_identity(
            len(base_matrix)
        )
    if exponent % 2 == 1:
        return mod_matrix_mul(
            base_matrix,
            mod_matrix_pow(
                base_matrix,
                exponent - 1,
                modulus
            ), modulus
        )
    d_matrix = mod_matrix_pow(
        base_matrix,
        exponent // 2,
        modulus
    )
    return mod_matrix_mul(
        d_matrix,
        d_matrix,
        modulus
    )


def soe(n):
    if n < 100:
        n = 100
    P = [
        True for x in range(n)
    ]

    i = 2
    while i < math.sqrt(n):
        if P[i]:
            j = i + i
            while j < n:
                P[j] = False
                j += i
        i += 1

    return [
        x for x in range(2, n) if P[x]
    ]
