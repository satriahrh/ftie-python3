from blocks.bbs import BBS
from errors import ValidationError
from suplementary import number_theory as nt


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

    def encrypt(self, plainbytes):
        """
        INPUT
        plainbytes    bytes which length is N
        OUTPUT
        randomized_bytes   bytes [which length is 2N
        """
        if type(plainbytes) is not bytes:
            raise ValidationError(
                "Try another plainbytes",
                "plainbytes is not bytes type"
            )
        from random import randint
        randomized_bytes = bytearray()
        for byte in plainbytes:
            random = randint(0, 256)
            key = self.__bbs.next()
            randomized_bytes.append(
                nt.mod_add(
                    nt.mod_add(
                        key,
                        nt.mod_mul(
                            2,
                            byte,
                            256
                        ),
                        256
                    ),
                    random,
                    256
                )
            )
            randomized_bytes.append(
                nt.mod_add(
                    nt.mod_add(
                        nt.mod_mul(
                            2,
                            key,
                            256
                        ),
                        byte,
                        256
                    ),
                    random,
                    256
                )
            )
        randomized_bytes = bytes(randomized_bytes)

        return randomized_bytes

    def decrypt(self, randomized_bytes):
        """
        INPUT
        randomized_bytes   bytes [which length is 2N
        OUTPUT
        plainbytes    bytes which length is N
        """
        if type(randomized_bytes) is not bytes:
            raise ValidationError(
                "Try another randomized_bytes",
                "randomized_bytes is not bytes type"
            )
        len_rb = len(randomized_bytes)
        if len_rb % 2 != 0:
            raise ValidationError(
                "Try another ciphertext: an even lengthed",
                "odd lengthed ciphertext"
            )
        plainbytes = bytearray()
        for i in range(int(len(randomized_bytes) / 2)):
            key = self.__bbs.next()
            plainbytes.append(
                nt.mod_add(
                    nt.mod_add(
                        randomized_bytes[2 * i],
                        nt.mod_mul(
                            -1,
                            randomized_bytes[2 * i + 1],
                            256
                        ),
                        256
                    ),
                    key,
                    256
                )
            )

        plainbytes = bytes(plainbytes)

        return plainbytes
