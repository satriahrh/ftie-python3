from suplementary.number_theory import fibonacy
from errors import ValidationError


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

        self.__a_matrix = [
            [1, _a],
            [_b, 1 + _a * _b],
        ]
        import numpy as np
        self.__a_inverse_matrix \
            = np.linalg.inv(self.__a_matrix).astype(int).tolist()
        self.__number_of_iteration = number_of_iteration
        self.__map = {}

        if _a == 1 and _b == 1:
            self.__type = 0
        elif _a == _b:
            self.__type = 1
        else:
            self.__type = 2

    def get_map(self, maps_dimension):
        try:
            return self.__map[maps_dimension]
        except KeyError:
            ret = None

            if self.__type == 0:
                ret = self.__mapping_zero(maps_dimension)

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

    def encrypt(self, matrix):
        if len(matrix) != len(matrix[0]):
            print("ACM needs square matrix")
            return
        maps_dimension = len(matrix)
        maps = self.get_map(maps_dimension)

        ret = []
        for x in range(maps_dimension):
            ret.append([])
            for y in range(maps_dimension):
                xy = maps[x][y]
                ret[x].append(matrix[xy[0]][xy[1]])

        return ret

    def decrypt(self, matrix):
        if len(matrix) != len(matrix[0]):
            print("ACM needs square matrix")
            return
        maps_dimension = len(matrix)
        maps = self.get_map(maps_dimension)

        ret = [
            [None for y in range(maps_dimension)]
            for x in range(maps_dimension)
        ]

        for x in range(maps_dimension):
            for y in range(maps_dimension):
                xy = maps[x][y]
                ret[xy[0]][xy[1]] = matrix[x][y]

        return ret
