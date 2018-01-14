import suplementary.number_theory as nt


class BBS:
    def __init__(self, p, q, s):
        self.errors = {}
        self.__validate(p, q, s)
        if self.validated():
            self.__m = p*q
            self.__s = s

    def get_errors(self, key=None):
        try:
            if key:
                return self.errors[key]
            return self.errors
        except KeyError:
            return KeyError

    def __validate(self, p, q, s):
        self.__validated = False
        if p == q:
            self.errors['validation'] = "p is equal to q"
            return
        if p % 4 != 3 or q % 4 != 3:
            self.errors['validation'] = "p or q mod 4 are not 3"
            return
        if not nt.is_prime(p) or not nt.is_prime(q):
            self.errors['validation'] = "p or q are not prime"
            return
        if not (0 < s and s < p * q):
            self.errors['validation'] = "s is to small or to big"
            return
        import math
        if math.gcd(p * q, s) != 1:
            self.errors['validation'] = "m and s are not relatively prime"
            return
        self.__validated = True

    def validated(self):
        return self.__validated

    def next(self):
        if self.validated():
            self.__s = (self.__s ** 2) % self.__m
            return self.__s
        return None
