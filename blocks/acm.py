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

            if _a == 1 and _b == 1:
                self.__type = 0
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

    def encryption_map(self, number_of_iteration):
        if self.__type == 0:
            return self.__mapping_zero(number_of_iteration)
        return None

    def __mapping_zero(self, number_of_iteration):
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
