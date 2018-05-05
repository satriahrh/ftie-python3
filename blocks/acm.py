from suplementary import number_theory as nt
from errors import ValidationError

import numpy as np


class ACM:
    def __init__(self, a, b, n):
        """
        INPUT
        a       int
        b       int
        """
        if (a < 1) or (b < 1):
            raise ValidationError(
                "Try different pairs of a and b",
                "a or b is no more than 1"
            )
        if n < 1:
            raise ValidationError(
                "Try different number_of_iteration",
                "number_of_iteration is too small"
            )

        self.__a = a
        self.__b = b
        self.__n = n
        self.__map = {}

        if a == 1 and b == 1:
            self.__type = 0
        elif a == b:
            self.__type = 1
        else:
            self.__type = 2
            self.__A = [
                [1, a],
                [b, 1 + a * b]
            ]

    # TODO to private function
    # TODO: do optimization using numpy
    def get_map(self, maps_dimension):
        try:
            return self.__map[maps_dimension]
        except KeyError:
            if maps_dimension < 2:
                raise ValidationError(
                    "Try different maps_dimension",
                    "matrix dimension is too small"
                )

            ret = None

            if self.__type == 0:
                ret = self.__mapping_zero(maps_dimension)
            elif self.__type == 1:
                ret = self.__mapping_one(maps_dimension)
            elif self.__type == 2:
                ret = self.__mapping_two(maps_dimension)

            self.__map[maps_dimension] = ret
            return ret

    def __mapping_zero(self, maps_dimension):
        N = maps_dimension

        mapping = np.zeros(
            2 * (N ** 2), np.dtype('I')
        ).reshape(N, N, 2)

        x = 0
        while x < N:
            y = 0
            while y < N:
                mapping[x, y] = (
                    nt.mod_add(
                        nt.mod_mul(
                            nt.fibonacy(2 * self.__n - 1, m=N),
                            x,
                            N
                        ), nt.mod_mul(
                            nt.fibonacy(2 * self.__n, m=N),
                            y,
                            N
                        ), N
                    ),
                    nt.mod_add(
                        nt.mod_mul(
                            nt.fibonacy(2 * self.__n, m=N),
                            x,
                            N
                        ), nt.mod_mul(
                            nt.fibonacy(2 * self.__n + 1, m=N),
                            y,
                            N
                        ), N
                    )
                )
                y += 1
            x += 1

        return mapping

    def __mapping_one(self, maps_dimension):
        N = maps_dimension

        mapping = np.zeros(
            2 * (N ** 2), np.dtype('I')
        ).reshape(N, N, 2)

        x = 0
        while x < N:
            y = 0
            while y < N:
                mapping[x, y] = (
                    nt.mod_add(
                        nt.mod_mul(
                            nt.fibonacy(2 * self.__n - 1, a=self.__a, m=N),
                            x,
                            N
                        ), nt.mod_mul(
                            nt.fibonacy(2 * self.__n, a=self.__a, m=N),
                            y,
                            N
                        ), N
                    ),
                    nt.mod_add(
                        nt.mod_mul(
                            nt.fibonacy(2 * self.__n, a=self.__a, m=N),
                            x,
                            N
                        ), nt.mod_mul(
                            nt.fibonacy(2 * self.__n + 1, a=self.__a, m=N),
                            y,
                            N
                        ), N
                    )
                )
                y += 1
            x += 1

        return mapping

    def __mapping_two(self, maps_dimension):
        N = maps_dimension

        A_n = nt.mod_matrix_pow(
            self.__A,
            self.__n,
            N
        )

        mapping = np.zeros(
            2 * (N ** 2), np.dtype('I')
        ).reshape(N, N, 2)

        x = 0
        while x < N:
            y = 0
            while y < N:
                mapping[x, y] = (
                    nt.mod_add(
                        nt.mod_mul(A_n[0][0], x, N),
                        nt.mod_mul(A_n[0][1], y, N),
                        N
                    ), nt.mod_add(
                        nt.mod_mul(A_n[1][0], x, N),
                        nt.mod_mul(A_n[1][1], y, N),
                        N
                    )
                )
                y += 1
            x += 1

        return mapping

    def __check_input_matrix(self, matrix):
        if matrix.shape[0] != matrix.shape[1]:
            raise ValidationError(
                "Try different matrix",
                "matrix is not a square matrix"
            )

        if matrix.shape[0] < 2:
            raise ValidationError(
                "Try different maps_dimension",
                "matrix dimension is too small"
            )

    def encrypt(self, plainmatrix: np.ndarray):
        self.__check_input_matrix(plainmatrix)

        maps_dimension = plainmatrix.shape[0]
        maps = self.get_map(maps_dimension)

        ciphermatrix = plainmatrix.copy()
        for x in range(maps_dimension):
            for y in range(maps_dimension):
                _map = maps[x][y]
                new_val = plainmatrix[_map[0], _map[1]]
                # print(new_val)
                ciphermatrix[x, y] = new_val

        return ciphermatrix

    def decrypt(self, ciphermatrix: np.ndarray):
        self.__check_input_matrix(ciphermatrix)

        maps_dimension = ciphermatrix.shape[0]
        maps = self.get_map(maps_dimension)

        plainmatrix = ciphermatrix.copy()
        for x in range(maps_dimension):
            for y in range(maps_dimension):
                    _map = maps[x][y]
                    new_val = ciphermatrix[x, y]
                    plainmatrix[_map[0], _map[1]] = new_val

        return plainmatrix
