from suplementary.number_theory import fibonacy


class ACM:
    def __init__(self, a, b, N):
        """
        INPUT
        a       int
        b       int
        """
        self.__errors = {}
        self.__validate(a, b, N)
        if self.validated():
            A = [
                [1, a],
                [b, 1 + a * b],
            ]
            import numpy as np
            A_i = np.linalg.inv(A).astype(int).tolist()

            self.__A = A
            self.__A_i = A_i
            self.__N = N

            if a == 1 and b == 1:
                self.__type = 0
            elif a == b:
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

    def __validate(self, a, b, N):
        self.__validated = False
        if not (a >= 1) or not (b >= 1):
            self.__errors['validation'] = \
                "a or b is no more than 1"
            return

        self.__validated = True

    def validated(self):
        return self.__validated

    def encryption_map(self, n):
        if self.__type == 0:
            return self.__mapping_zero(n)


    def __mapping_zero(self, n):
        M = [
            [
                [
                    (fibonacy(2 * n - 1) * x + fibonacy(2 * n) * y) % self.__N,
                    (fibonacy(2 * n) * x + fibonacy(2 * n + 1) * y) % self.__N
                ]
                for y in range(self.__N)
            ] for x in range(self.__N)
        ]

        return M
