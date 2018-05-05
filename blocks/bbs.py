from errors import ValidationError
import suplementary.number_theory as nt


class BBS:
    def __init__(self, p, q, s):
        if p == q:
            raise ValidationError(
                "Try different pairs of p and q",
                "p is equal to q"
            )
        if p % 4 != 3 or q % 4 != 3:
            raise ValidationError(
                "Try different pairs of p and q",
                "p or q mod 4 are not 3"
            )
        if not nt.is_prime(p) or not nt.is_prime(q):
            raise ValidationError(
                "Try different pairs of p and q",
                "p or q are not prime"
            )
        if not (s > 0 and s < p * q):
            raise ValidationError(
                "Try different pairs of p and q",
                "s is to small or to big"
            )
        import math
        if math.gcd(p * q, s) != 1:
            raise ValidationError(
                "Try different pairs of p and q",
                "(p * q) and s are not relatively prime"
            )

        self.__m = p * q
        self.__s = s

    def next(self):
        self.__s = nt.mod_pow(self.__s, 2, self.__m)
        return self.__s
