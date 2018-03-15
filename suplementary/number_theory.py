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


# TODO Unittest for this function using mathematical induction
def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0

    ret = 1
    for i in range(exponent):
        ret = (ret * base) % modulus

    return ret


# TODO Unittest for this function using mathematical induction
matrix_mul = lambda A, B: [
        [
            sum([A[i][k] * B[k][j] for k in range(B)])
            for j in range(B[0])
        ]
        for i in range(A)
    ]


# TODO Unittest for this function using mathematical induction
__identity = lambda x, y: 1 if x == y else 0
def matrix_modular_pow(base_matrix, exponent, modulus):
    if exponent == 0:
        return [
            [__identity(x, y) for y in range(base_matrix[0])]
            for x in range(base_matrix)
        ]

    if exponent % 2 == 1:
        return (
            matrix_mul(
                base_matrix,
                matrix_modular_pow(
                    base_matrix,
                    exponent - 1,
                    modulus
                )
            )
        ) % modulus

    matrix_even = matrix_modular_pow(base_matrix, exponent / 2, modulus)
    return matrix_mul(matrix_even, matrix_even) % modulus
