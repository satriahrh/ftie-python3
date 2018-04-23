from blocks.bbs import BBS
from errors import ValidationError

import numpy as np


class RT:
    def __init__(self, bbs: BBS):
        if type(bbs) != BBS:
            raise ValidationError(
                "Create a right bbs",
                "bbs is not BBS type"
            )
        self.__bbs = bbs

    def encrypt(self, plainbytes: np.ndarray):
        cipherbytes = np.zeros(2 * plainbytes.size, np.dtype('B'))
        random = np.random.randint(
            low=0, high=255, size=plainbytes.size, dtype='B'
        )
        for i in range(plainbytes.size):
            key = self.__bbs.next()
            cipherbytes[2 * i] = \
                key + 2 * plainbytes[i] + random[i]
            cipherbytes[2 * i + 1] = \
                2 * key + plainbytes[i] + random[i]

        return cipherbytes

    def decrypt(self, cipherbytes: np.ndarray):
        if cipherbytes.size % 2 != 0:
            raise ValidationError(
                "Try another ciphertext: an even lengthed",
                "odd lengthed ciphertext"
            )
        plainbytes = np.zeros(cipherbytes.size // 2, np.dtype('B'))
        for i in range(plainbytes.size):
            key = self.__bbs.next()
            plainbytes[i] = \
                cipherbytes[2 * i] - cipherbytes[2 * i + 1] + key

        return plainbytes
