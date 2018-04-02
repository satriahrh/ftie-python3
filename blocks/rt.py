from blocks.bbs import BBS
from errors import ValidationError
from suplementary import number_theory as nt

import multiprocessing as mp


class RT:
    def __init__(self, bbs_p, bbs_q, bbs_seed):
        """
        INPUT
        bbs         blocks.bbs.BBS
        """
        # TODO: REFACTOR self.__size to be key (?)
        self.__size = mp.cpu_count()  # well, the current is a disaster

        BBS(
            _p=bbs_p,
            _q=bbs_q,
            seed=bbs_seed,
        )

        self.__bbs_p = bbs_p
        self.__bbs_q = bbs_q
        self.__bbs_seed = bbs_seed

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

        def encrypt_function(bottom, top):
            bbs = BBS(
                _p=self.__bbs_p,
                _q=self.__bbs_q,
                seed=self.__bbs_seed
            )
            randomized_bytes = bytearray()
            for index in range(bottom, top):
                byte = plainbytes[index]
                random = randint(0, 256)
                key = bbs.next()
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
            return bytes(randomized_bytes)

        return run(encrypt_function, self.__size, len(plainbytes))

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

        def decrypt_function(bottom, top):
            bbs = BBS(
                _p=self.__bbs_p,
                _q=self.__bbs_q,
                seed=self.__bbs_seed
            )
            plainbytes = bytearray()
            for i in range(bottom, top, 2):
                key = bbs.next()
                # TODO investigate wether we need use modular operation on each unit
                plainbytes.append(
                    nt.mod_add(
                        nt.mod_add(
                            randomized_bytes[i],
                            nt.mod_mul(
                                -1,
                                randomized_bytes[i + 1],
                                256
                            ),
                            256
                        ),
                        key,
                        256
                    )
                )

            return bytes(plainbytes)

        def decrypt_run(size, start=0, remaining=len(randomized_bytes)):
            output = mp.Queue()

            processed = ((remaining // 2) // size) * 2

            processes = [
                mp.Process(
                    target=decrypt_function,
                    args=(
                        start + rank * processed,
                        start + rank * processed + processed,
                        output
                    )
                ) for rank in range(size)
            ]

            for process in processes:
                process.start()

            next_remaining = remaining - processed * size

            recurrance = bytes()

            if next_remaining > 0:
                recurrance = decrypt_run(
                    size=next_remaining // 2,
                    start=processed * size,
                    remaining=next_remaining
                )

            buf = output.get()
            key = [buf[0]]
            data = [buf[1]]
            for x in range(len(processes) - 1):
                buf = output.get()
                y = 0
                while y < len(key) and key[y] < buf[0]:
                    y += 1

                key.insert(y, buf[0])
                data.insert(y, buf[1])

            dt = bytes()
            for d in data:
                dt += d
            return dt + recurrance

        return run(decrypt_function, self.__size, len(randomized_bytes), 2)


def run(function, size, remaining, steps=1, start=0):
    def process_run(function, bottom, top, output):
        output.put((bottom, function(bottom, top)))

    output = mp.Queue()

    processed = ((remaining // steps) // size) * steps

    processes = [
        mp.Process(
            target=process_run,
            args=(
                function,
                start + rank * processed,
                start + rank * processed + processed,
                output
            )
        ) for rank in range(size)
    ]

    for process in processes:
        process.start()

    next_remaining = remaining - processed * size

    recurrance = bytes()

    if next_remaining > 0:
        recurrance = run(
            function=function,
            size=next_remaining // steps,
            remaining=next_remaining,
            steps=steps,
            start=processed * size
        )

    buf = output.get()
    key = [buf[0]]
    data = [buf[1]]
    for x in range(len(processes) - 1):
        buf = output.get()
        y = 0
        while y < len(key) and key[y] < buf[0]:
            y += 1

        key.insert(y, buf[0])
        data.insert(y, buf[1])

    dt = bytes()
    for d in data:
        dt += d
    return dt + recurrance
