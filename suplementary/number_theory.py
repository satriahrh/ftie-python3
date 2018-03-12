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
