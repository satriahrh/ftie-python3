import suplementary.number_theory as nt


class BBS:
    def __init__(self, _p, _q, seed):
        self.__errors = {}
        self.__validate(_p, _q, seed)
        if self.validated():
            self.__modulo = _p * _q
            self.__seed = seed

    def get_errors(self, key=None):
        try:
            if key:
                return self.__errors[key]
            return self.__errors
        except KeyError:
            return ""

    def __validate(self, _p, _q, seed):
        self.__validated = False
        if _p == _q:
            self.__errors['validation'] = "p is equal to q"
            return
        if _p % 4 != 3 or _q % 4 != 3:
            self.__errors['validation'] = "p or q mod 4 are not 3"
            return
        if not nt.is_prime(_p) or not nt.is_prime(_q):
            self.__errors['validation'] = "p or q are not prime"
            return
        if not (seed > 0 and seed < _p * _p):
            self.__errors['validation'] = "s is to small or to big"
            return
        import math
        if math.gcd(_p * _p, seed) != 1:
            self.__errors['validation'] = "m and s are not relatively prime"
            return
        self.__validated = True

    def validated(self):
        return self.__validated

    def next(self):
        if self.validated():
            self.__seed = (self.__seed ** 2) % self.__modulo
            return self.__seed
        return None
