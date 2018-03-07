from blocks.bbs import BBS
from errors import ValidationError, DiscoveryError


class RT:
    def __init__(self, bbs):
        """
        INPUT
        bbs         blocks.bbs.BBS
        """
        if type(bbs) != BBS:
            raise ValidationError(
                "Create a right bbs",
                "bbs is not BBS type"
            )
        self.__bbs = bbs

    def encrypt(self, plaintext):
        """
        INPUT
        plaintext   [int 0...N-1]
        OUTPUT
        ciphertext   [int 0...2N-2]
        """
        from random import randint
        ciphertext = []
        for _p in plaintext:
            try:
                random = randint(0, 256)
                key = self.__bbs.next()
                ciphertext.append(
                    (key + 2 * _p + random) % 256
                )
                ciphertext.append(
                    (2 * key + _p + random) % 256
                )
            except TypeError:
                raise DiscoveryError(
                    "Try another plaintext that is an array like of integer",
                    "input is not an array of integer"
                )

        return ciphertext

    def decrypt(self, ciphertext):
        """
        INPUT
        ciphertext   [int 0...2N-2]
        OUTPUT
        plaintext   [int 0...N-1]
        """
        len_ciphertext = len(ciphertext)
        if len_ciphertext % 2 != 0:
            raise ValidationError(
                "Try another ciphertext: an even lengthed",
                "odd lengthed ciphertext"
            )
        plaintext = []
        for i in range(int(len(ciphertext) / 2)):
            try:
                key = self.__bbs.next()
                plaintext.append(
                    (ciphertext[2 * i] - ciphertext[2 * i + 1] + key) % 256
                )
            except TypeError:
                raise DiscoveryError(
                    "Try another plaintext that is an array like of integer",
                    "input is not an array of integer"
                )

        return plaintext
