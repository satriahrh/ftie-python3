from suplementary import number_theory as nt
from errors import ValidationError, DiscoveryError
import multiprocessing as mp


def run(function, size, remaining, start=0):
    def process_run(function, bottom, top, output):
        output.put((bottom, function(bottom, top)))

    output = mp.Queue()

    processed = remaining // size

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

    recurrance = []

    if next_remaining > 0:
        recurrance = run(
            function=function,
            size=next_remaining,
            remaining=next_remaining,
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

    dt = []
    for d in data:
        dt += d
    return dt + recurrance


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
    def get_map(self, maps_dimension):
        def discrete(bottom, top):
            return [
                [
                    [
                        (
                            nt.fibonacy(2 * self.__number_of_iteration - 1) * x
                            + nt.fibonacy(2 * self.__number_of_iteration) * y
                        ) % maps_dimension,
                        (
                            nt.fibonacy(2 * self.__number_of_iteration) * x
                            + nt.fibonacy(2 * self.__number_of_iteration + 1) * y
                        ) % maps_dimension
                    ]
                    for y in range(maps_dimension)
                ] for x in range(bottom, top)
            ]

        def general_equal(bottom, top):
            return [
                [
                    [
                        (
                            nt.fibonacy_a(
                                self.__a, 2 * self.__number_of_iteration - 1
                            ) * x
                            + nt.fibonacy_a(
                                self.__a, 2 * self.__number_of_iteration
                            ) * y
                        ) % maps_dimension,
                        (
                            nt.fibonacy_a(
                                self.__a, 2 * self.__number_of_iteration
                            ) * x
                            + nt.fibonacy_a(
                                self.__a, 2 * self.__number_of_iteration + 1
                            ) * y
                        ) % maps_dimension
                    ]
                    for y in range(maps_dimension)
                ] for x in range(bottom, top)
            ]

        def general_any(bottom, top):
            return [
                [
                    [
                        nt.mod_add(
                            nt.mod_mul(A_n[0][0], x, maps_dimension),
                            nt.mod_mul(A_n[0][1], y, maps_dimension),
                            maps_dimension
                        ), nt.mod_add(
                            nt.mod_mul(A_n[1][0], x, maps_dimension),
                            nt.mod_mul(A_n[1][1], y, maps_dimension),
                            maps_dimension
                        )
                    ]
                    for y in range(maps_dimension)
                ] for x in range(bottom, top)
            ]

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
                ret = run(discrete, mp.cpu_count(), maps_dimension)
            elif self.__type == 1:
                ret = run(general_equal, mp.cpu_count(), maps_dimension)
            elif self.__type == 2:
                A_n = nt.mod_matrix_pow(
                    self.__A,
                    self.__number_of_iteration,
                    maps_dimension
                )
                ret = run(general_any, mp.cpu_count(), maps_dimension)

            self.__map[maps_dimension] = ret
            return ret

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

        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                _map = maps[x][y]
                ret[_map[0]][_map[1]] = matrix[x][y]

        return ret
