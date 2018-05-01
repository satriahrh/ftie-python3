from functools import reduce
import math

def is_prime(_p):
    if _p < 2:
        return False
    for i in range(2, math.floor(math.sqrt(_p)) + 1):
        if _p % i == 0:
            return False
    return True

# TODO create unittest
FIBONACY = {}
def fibonacy(n, a=1, m=65536):
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
                    mod_mul(a, fibonacy(i - 1, a, m), m),
                    fibonacy(i - 2, a, m),
                    m
                )
        return FIBONACY[(a, m)][n]


mod_add = \
    lambda a, b, modulus: (a + b) % modulus


mod_mul = \
    lambda a, b, modulus: (a * b) % modulus


mod_pow = \
    lambda base, exponent, modulus: \
    reduce(
        (lambda p, q: mod_mul(p, q, modulus)),
        [1] + [base] * exponent
    )


mod_matrix_mul = lambda A, B, modulus: [
    [
        reduce(
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
