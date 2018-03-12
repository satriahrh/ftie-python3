from suplementary.number_theory import fibonacy, fibonacy_a
from errors import ValidationError, DiscoveryError


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
            import numpy as np
            self.__A_n = np.array([
                [1, _a],
                [_b, 1 + _a * _b]
            ]) ** number_of_iteration

    # TODO to private function
    def get_map(self, maps_dimension):
        try:
            return self.__map[maps_dimension]
        except KeyError:
            if maps_dimension < 2:
                raise ValidationError(
                    "Try different maps_dimension",
                    "maps_dimension is too small"
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
        mapping = [
            [
                [
                    (
                        fibonacy(2 * self.__number_of_iteration - 1) * x
                        + fibonacy(2 * self.__number_of_iteration) * y
                    ) % maps_dimension,
                    (
                        fibonacy(2 * self.__number_of_iteration) * x
                        + fibonacy(2 * self.__number_of_iteration + 1) * y
                    ) % maps_dimension
                ]
                for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ]

        return mapping

    def __mapping_one(self, maps_dimension):
        mapping = [
            [
                [
                    (
                        fibonacy_a(
                            self.__a, 2 * self.__number_of_iteration - 1
                        ) * x
                        + fibonacy_a(
                            self.__a, 2 * self.__number_of_iteration
                        ) * y
                    ) % maps_dimension,
                    (
                        fibonacy_a(
                            self.__a, 2 * self.__number_of_iteration
                        ) * x
                        + fibonacy_a(
                            self.__a, 2 * self.__number_of_iteration + 1
                        ) * y
                    ) % maps_dimension
                ]
                for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ]

        return mapping

    def __mapping_two(self, maps_dimension):
        A_n = [
            [
                self.__A_n[0][0] % maps_dimension,
                self.__A_n[0][1] % maps_dimension
            ], [
                self.__A_n[1][0] % maps_dimension,
                self.__A_n[1][1] % maps_dimension
            ]
        ]
        mapping = [
            [
                [
                    (
                        A_n[0][0] * x + A_n[0][1] * y
                    ) % maps_dimension,
                    (
                        A_n[1][0] * x + A_n[1][1] * y
                    ) % maps_dimension
                ]
                for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ]

        return mapping

    def __check_input_matrix(self, matrix):
        row_count = len(matrix[0])
        column_count = len(matrix)

        if row_count != column_count:
            raise ValidationError(
                "Try different matrix",
                "matrix is not a square matrix"
            )

        if row_count < 2:
            raise ValidationError(
                "Try different maps_dimension",
                "maps_dimension is too small"
            )

    def encrypt(self, matrix):
        self.__check_input_matrix(matrix)

        maps_dimension = len(matrix)
        maps = self.get_map(maps_dimension)

        ret = []
        for x, row in enumerate(matrix):
            len_row = len(row)
            if len_row != maps_dimension:
                raise DiscoveryError(
                    "Try another matrix",
                    "this is not a consistent matrix"
                )
            ret.append([])
            for y in range(len_row):
                try:
                    _map = maps[x][y]
                    ret[x].append(matrix[_map[0]][_map[1]])
                except IndexError:
                    raise DiscoveryError(
                        "Try another matrix",
                        "this is not a consistent matrix"
                    )

        return ret

    def decrypt(self, matrix):
        self.__check_input_matrix(matrix)

        maps_dimension = len(matrix)
        maps = self.get_map(maps_dimension)

        ret = [
            [None for y in range(maps_dimension)]
            for x in range(maps_dimension)
        ]

        for x, row in enumerate(matrix):
            len_row = len(row)
            if len_row != maps_dimension:
                raise DiscoveryError(
                    "Try another matrix",
                    "this is not a consistent matrix"
                )
            for y in range(len_row):
                try:
                    _map = maps[x][y]
                    ret[_map[0]][_map[1]] = matrix[x][y]
                except IndexError:
                    raise DiscoveryError(
                        "Try another matrix",
                        "this is not a consistent matrix"
                    )

        return ret
