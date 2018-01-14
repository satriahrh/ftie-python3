import math

def is_prime(p):
    if p < 2:
        return False
    for i in range(2, math.floor(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True
