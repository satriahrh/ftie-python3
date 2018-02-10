import math

def is_prime(p):
    if p < 2:
        return False
    for i in range(2, math.floor(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

FIBONACY = {0: 0, 1: 1,}
def fibonacy(n):
    try:
        return FIBONACY[n]
    except KeyError:
        for i in range(2, n+1):
            FIBONACY[i] = fibonacy(i - 1) + fibonacy(i - 2)
        return FIBONACY[n]
