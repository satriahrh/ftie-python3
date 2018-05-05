from suplementary import number_theory as nt
from errors import ValidationError

import numpy as np


class ACM:
    def __init__(self, _a, _b, number_of_iteration):
        """
        INPUT
        a       int
        b       int
        """
        if (_a < 1) or (_b < 1):
            raise ValidationError(
                "Try different pairs of a and b",
                "a or b is no more than 1"
            )
        if number_of_iteration < 1:
            raise ValidationError(
                "Try different number_of_iteration",
                "number_of_iteration is too small"
            )

        self.__a = _a
        self.__b = _b
        self.__number_of_iteration = number_of_iteration
        self.__map = {}

        if _a == 1 and _b == 1:
            self.__type = 0
        elif _a == _b:
            self.__type = 1
        else:
            self.__type = 2
            self.__A = [
                [1, _a],
                [_b, 1 + _a * _b]
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
        mapping = np.zeros(
            2 * (maps_dimension ** 2),
            np.dtype('I')
        ).reshape(
            maps_dimension,
            maps_dimension,
            2
        )

        x = 0
        while x < maps_dimension:
            y = 0
            while y < maps_dimension:
                mapping[x, y] = (
                    (
                        nt.fibonacy(
                            2 * self.__number_of_iteration - 1,
                            m=maps_dimension
                        ) * x
                        + nt.fibonacy(
                            2 * self.__number_of_iteration,
                            m=maps_dimension
                        ) * y
                    ) % maps_dimension,
                    (
                        nt.fibonacy(
                            2 * self.__number_of_iteration,
                            m=maps_dimension
                        ) * x
                        + nt.fibonacy(
                            2 * self.__number_of_iteration + 1,
                            m=maps_dimension
                        ) * y
                    ) % maps_dimension
                )
                y += 1
            x += 1

        return mapping

    def __mapping_one(self, maps_dimension):
        mapping = np.zeros(
            2 * (maps_dimension ** 2),
            np.dtype('I')
        ).reshape(
            maps_dimension,
            maps_dimension,
            2
        )

        x = 0
        while x < maps_dimension:
            y = 0
            while y < maps_dimension:
                mapping[x, y] = (
                    (
                        nt.fibonacy(
                            2 * self.__number_of_iteration - 1,
                            a=self.__a,
                            m=maps_dimension
                        ) * x
                        + nt.fibonacy(
                            2 * self.__number_of_iteration,
                            a=self.__a,
                            m=maps_dimension
                        ) * y
                    ) % maps_dimension,
                    (
                        nt.fibonacy(
                            2 * self.__number_of_iteration,
                            a=self.__a,
                            m=maps_dimension
                        ) * x
                        + nt.fibonacy(
                            2 * self.__number_of_iteration + 1,
                            a=self.__a,
                            m=maps_dimension
                        ) * y
                    ) % maps_dimension
                )
                y += 1
            x += 1

        return mapping

    def __mapping_two(self, maps_dimension):
        A_n = nt.mod_matrix_pow(
            self.__A,
            self.__number_of_iteration,
            maps_dimension
        )

        mapping = np.zeros(
            2 * (maps_dimension ** 2),
            np.dtype('I')
        ).reshape(
            maps_dimension,
            maps_dimension,
            2
        )

        x = 0
        while x < maps_dimension:
            y = 0
            while y < maps_dimension:
                mapping[x, y] = (
                    nt.mod_add(
                        nt.mod_mul(A_n[0][0], x, maps_dimension),
                        nt.mod_mul(A_n[0][1], y, maps_dimension),
                        maps_dimension
                    ), nt.mod_add(
                        nt.mod_mul(A_n[1][0], x, maps_dimension),
                        nt.mod_mul(A_n[1][1], y, maps_dimension),
                        maps_dimension
                    )
                )
                y += 1
            x += 1

        return mapping

    def __check_input_matrix(self, matrix):
        print(matrix.shape)
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
