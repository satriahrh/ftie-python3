from errors import ValidationError
import suplementary.number_theory as nt


class BBS:
    def __init__(self, _p, _q, seed):
        self.__validate(_p, _q, seed)
        self.__modulo = _p * _q
        self.__seed = seed

    def __validate(self, _p, _q, seed):
        if _p == _q:
            raise ValidationError(
                "Try different pairs of p and q",
                "p is equal to q"
            )
        if _p % 4 != 3 or _q % 4 != 3:
            raise ValidationError(
                "Try different pairs of p and q",
                "p or q mod 4 are not 3"
            )
        if not nt.is_prime(_p) or not nt.is_prime(_q):
            raise ValidationError(
                "Try different pairs of p and q",
                "p or q are not prime"
            )
        if not (seed > 0 and seed < _p * _p):
            raise ValidationError(
                "Try different pairs of p and q",
                "s is to small or to big"
            )
        import math
        if math.gcd(_p * _p, seed) != 1:
            raise ValidationError(
                "Try different pairs of p and q",
                "(p * q) and s are not relatively prime"
            )

    def next(self):
        self.__seed = (self.__seed ** 2) % self.__modulo
        return self.__seed
