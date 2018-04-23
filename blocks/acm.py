from suplementary import number_theory as nt
from errors import ValidationError, DiscoveryError
from PIL import Image


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
                    "image dimension is too small"
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
                (
                    (
                        nt.fibonacy(2 * self.__number_of_iteration - 1) * x
                        + nt.fibonacy(2 * self.__number_of_iteration) * y
                    ) % maps_dimension,
                    (
                        nt.fibonacy(2 * self.__number_of_iteration) * x
                        + nt.fibonacy(2 * self.__number_of_iteration + 1) * y
                    ) % maps_dimension
                )
                for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ]

        return mapping

    def __mapping_one(self, maps_dimension):
        mapping = [
            [
                (
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
                )
                for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ]

        return mapping

    def __mapping_two(self, maps_dimension):
        A_n = nt.mod_matrix_pow(
            self.__A,
            self.__number_of_iteration,
            maps_dimension
        )

        mapping = [
            [
                (
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
                for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ]

        return mapping

    def __check_input_matrix(self, image):
        if image.size[0] != image.size[1]:
            raise ValidationError(
                "Try different matrix",
                "image is not a square image"
            )

        if image.size[0] < 2:
            raise ValidationError(
                "Try different maps_dimension",
                "image dimension is too small"
            )

    def encrypt(self, plainimage: Image):
        self.__check_input_matrix(plainimage)

        maps_dimension = plainimage.size[0]
        maps = self.get_map(maps_dimension)

        cipherimage = Image.new(plainimage.mode, plainimage.size)
        for x in range(maps_dimension):
            for y in range(maps_dimension):
                _map = maps[x][y]
                new_px = plainimage.getpixel(_map)
                cipherimage.putpixel((x, y), new_px)

        return cipherimage

    def decrypt(self, cipherimage: Image):
        self.__check_input_matrix(cipherimage)

        maps_dimension = cipherimage.size[0]
        maps = self.get_map(maps_dimension)

        plainimage = Image.new(cipherimage.mode, cipherimage.size)
        for x in range(maps_dimension):
            for y in range(maps_dimension):
                    _map = maps[x][y]
                    new_px = cipherimage.getpixel((x, y))
                    plainimage.putpixel(_map, new_px)

        return plainimage
