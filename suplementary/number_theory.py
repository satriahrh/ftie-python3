import math

def is_prime(_p):
    if _p < 2:
        return False
    for i in range(2, math.floor(math.sqrt(_p)) + 1):
        if _p % i == 0:
            return False
    return True

FIBONACY = {0: 0, 1: 1,}
def fibonacy(_n):
    try:
        return FIBONACY[_n]
    except KeyError:
        for i in range(2, _n + 1):
            FIBONACY[i] = fibonacy(i - 1) + fibonacy(i - 2)
        return FIBONACY[_n]
