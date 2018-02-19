from suplementary.number_theory import fibonacy


class ACM:
    def __init__(self, _a, _b, maps_dimension):
        """
        INPUT
        a       int
        b       int
        """
        self.__errors = {}
        self.__validate(_a, _b)
        if self.validated():
            self.__a_matrix = [
                [1, _a],
                [_b, 1 + _a * _b],
            ]
            import numpy as np
            self.__a_inverse_matrix \
                = np.linalg.inv(self.__a_matrix).astype(int).tolist()
            self.__maps_dimension = maps_dimension
            self.__map = {}
            self.__period = None

            if _a == 1 and _b == 1:
                self.__type = 0
                self.__period = self.__expect_period()
            elif _a == _b:
                self.__type = 1
            else:
                self.__type = 2

    def get_errors(self, key=None):
        try:
            if key:
                return self.__errors[key]
            return self.__errors
        except KeyError:
            return ""

    def __validate(self, _a, _b):
        self.__validated = False
        if (_a < 1) or (_b < 1):
            self.__errors['validation'] = \
                "a or b is no more than 1"
            return

        self.__validated = True

    def validated(self):
        return self.__validated

    def __expect_period(self):
        N = self.__maps_dimension
        if self.__type == 0:
            if (N - 3) % 10 == 0 or (N + 3) % 10 == 0:
                return N + 1
            elif (N - 1) % 10 == 0 or (N + 1) % 10 == 0:
                return (N - 1) / 2
        return 1

    def __expect_number_of_iteration(self, number_of_iteration):
        if number_of_iteration is None:
            if self.__period is not None:
                print(self.__period)
                return self.__period - 1
            return 1
        return number_of_iteration

    def get_map(self, number_of_iteration=None):
        number_of_iteration \
            = self.__expect_number_of_iteration(number_of_iteration)

        try:
            return self.__map[number_of_iteration]
        except KeyError:
            ret = None

            if self.__type == 0:
                ret = self.__mapping_zero(number_of_iteration)

            self.__map[number_of_iteration] = ret
            return ret

    def __mapping_zero(self, number_of_iteration=None):
        number_of_iteration \
            = self.__expect_number_of_iteration(number_of_iteration)

        mapping = [
            [
                [
                    (
                        fibonacy(2 * number_of_iteration - 1) * x
                        + fibonacy(2 * number_of_iteration) * y
                    ) % self.__maps_dimension,
                    (
                        fibonacy(2 * number_of_iteration) * x
                        + fibonacy(2 * number_of_iteration + 1) * y
                    ) % self.__maps_dimension
                ]
                for y in range(self.__maps_dimension)
            ] for x in range(self.__maps_dimension)
        ]

        return mapping

    def encrypt(self, matrix, number_of_iteration=None):
        number_of_iteration \
            = self.__expect_number_of_iteration(number_of_iteration)

        maps = self.get_map(number_of_iteration)

        ret = []
        for x in range(self.__maps_dimension):
            ret.append([])
            for y in range(self.__maps_dimension):
                xy = maps[x][y]
                ret[x].append(matrix[xy[0]][xy[1]])

        return ret

    def decrypt(self, matrix, number_of_iteration=None):
        maps = self.get_map(number_of_iteration)

        ret = [
            [None for y in range(self.__maps_dimension)]
            for x in range(self.__maps_dimension)
        ]

        for x in range(self.__maps_dimension):
            for y in range(self.__maps_dimension):
                xy = maps[x][y]
                ret[xy[0]][xy[1]] = matrix[x][y]

        return ret
