class ACM:
    def __init__(self, a, b, n):
        """
        INPUT
        a       int
        b       int
        """
        self.__errors = {}
        self.__validate(a, b, n)
        if self.validated():
            A = [
                [1, a],
                [b, 1 + a * b],
            ]
            import numpy as np
            A_i = np.linalg.inv(A).astype(int).tolist()

            self.__A = np.linalg.matrix_power(A, n)
            self.__A_i = np.linalg.matrix_power(A_i, n)


    def get_errors(self, key=None):
        try:
            if key:
                return self.__errors[key]
            return self.__errors
        except KeyError:
            return ""

    def __validate(self, a, b, n):
        self.__validated = False
        if not (a >= 1) or not (b >= 1):
            self.__errors['validation'] = \
                "a or b is no more than 1"
            return

        self.__validated = True

    def validated(self):
        return self.__validated

    def __mapping(self, N):
        res = [
            [None for y in range(N)] for x in range(N)
        ]
