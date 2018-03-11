import unittest
from blocks import transform as t


class TestPadStripBytesFunctioning(unittest.TestCase):
    def setUp(self):
        self.bts = b'1234'
        self.bts_padded_expected = b'1234\x00\x00'
        self.bts_padded_actual = t.pad_bytes(self.bts)
        self.bts_padded_stripped = t.strip_bytes(self.bts_padded_actual)

    def test_pad_bytes_functioning(self):
        self.assertEqual(
            self.bts_padded_expected, self.bts_padded_actual
        )

    def test_strip_bytes_functioning(self):
        self.assertEqual(
            self.bts, self.bts_padded_stripped
        )


class TestCompileBytesToPixelsFunctioning(unittest.TestCase):
    def test_functioning(self):
        bts = b'0123456789AB'
        expected = [
            (48, 49, 50), (51, 52, 53), (54, 55, 56), (57, 65, 66)
        ]

        actual = t.compile_bytes_to_pixels(bts)
        self.assertEqual(actual, expected)


class TestCompilePixelsToMatrixFunctioning(unittest.TestCase):
    def test_functioning(self):
        pixels = [
            (48, 49, 50), (51, 52, 53), (54, 55, 56), (57, 65, 66)
        ]
        expected = [
            [
                (48, 49, 50), (51, 52, 53)
            ], [
                (54, 55, 56), (57, 65, 66)
            ]
        ]

        actual = t.compile_pixels_to_matrix(pixels)
        self.assertEqual(actual, expected)


class TestDecompileMatrixToPixelsFunctioning(unittest.TestCase):
    def test_functioning(self):
        matrix = [
            [
                (48, 49, 50), (51, 52, 53)
            ], [
                (54, 55, 56), (57, 65, 66)
            ]
        ]

        expected = [
            (48, 49, 50), (51, 52, 53), (54, 55, 56), (57, 65, 66)
        ]
        actual = t.decompile_matrix_to_pixels(matrix)
        self.assertEqual(actual, expected)


class TestDecompilePixelsToBytesFunctioning(unittest.TestCase):
    def test_functioning(self):
        pixels = [
            (48, 49, 50), (51, 52, 53), (54, 55, 56), (57, 65, 66)
        ]

        expected = b'0123456789AB'
        actual = t.decompile_pixels_to_bytes(pixels)
        self.assertEqual(actual, expected)


class TestPadNumbersFunctioning(unittest.TestCase):
    def setUp(self):
        self.numbers = [
            1, 2, 3, 4
        ]
        self.numbers_not_padded = [
            1, 2, 3, 4
        ]
        self.expected_numbers_padded = [
            1, 2, 3, 4, 0, 0
        ]
        self.padded = t.pad_numbers(self.numbers)

    def test_not_populated(self):
        self.assertEqual(self.numbers_not_padded, self.numbers)

    def test_functioning(self):
        self.assertEqual(self.padded, self.expected_numbers_padded)


class TestPadPixelsFunctioning(unittest.TestCase):
    def setUp(self):
        self.pixels = [
            (1, 2, 3), (4, 5, 6)
        ]
        self.pixels_not_padded = [
            (1, 2, 3), (4, 5, 6)
        ]
        self.expected_pixels_padded = [
            (1, 2, 3), (4, 5, 6),
            (0, 0, 0), (0, 0, 0)
        ]
        self.expected_pixels_padded_len = [
            (1, 2, 3), (4, 5, 6),
            (0, 0, 0)
        ]
        self.padded = t.pad_pixels(self.pixels)
        self.padded_with_len = t.pad_pixels(self.pixels, 3)

    def test_not_populated(self):
        self.assertEqual(self.pixels_not_padded, self.pixels)

    def test_functioning_len_none(self):
        self.assertEqual(self.padded, self.expected_pixels_padded)

    def test_functioning_len(self):
        self.assertEqual(self.padded_with_len, self.expected_pixels_padded_len)


class TestNumbersToPixelsFunctioning(unittest.TestCase):
    def test_functioning(self):
        numbers = [
            1, 2, 3, 4, 5, 6
        ]

        expected = [
            (1, 2, 3), (4, 5, 6)
        ]
        actual = t.numbers_to_pixels(numbers)
        self.assertEqual(actual, expected)


class TestPixelsToMatrixFunctioning(unittest.TestCase):
    def setUp(self):
        self.pixels = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)
        ]
        self.expected_n_none = [
            [
                (1, 2, 3), (4, 5, 6)
            ], [
                (7, 8, 9), (10, 11, 12)
            ]
        ]
        self.expected_n = [
            [
                (1, 2, 3), (4, 5, 6), (7, 8, 9)
            ], [
                (10, 11, 12), (0, 0, 0), (0, 0, 0)
            ], [
                (0, 0, 0), (0, 0, 0), (0, 0, 0)
            ]
        ]

    def test_functioning_n_none(self):
        actual = t.pixels_to_matrix(self.pixels)
        self.assertEqual(actual, self.expected_n_none)

    def test_functioning_len(self):
        n_matrix = 3

        actual = t.pixels_to_matrix(self.pixels, n_matrix)
        self.assertEqual(actual, self.expected_n)


class TestMatrixToPixelsFunctioning(unittest.TestCase):
    def test_functioning(self):
        matrix = [
            [
                (1, 2, 3), (4, 5, 6)
            ], [
                (7, 8, 9), (10, 11, 12)
            ]
        ]

        expected = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)
        ]
        actual = t.matrix_to_pixels(matrix)
        self.assertEqual(actual, expected)


class TestPixelsToNumbersFunctioning(unittest.TestCase):
    def test_functioning(self):
        pixels = [
            (1, 2, 3), (4, 5, 6)
        ]

        expected = [
            1, 2, 3, 4, 5, 6
        ]
        actual = t.pixels_to_numbers(pixels)
        self.assertEqual(actual, expected)


class TestReversing(unittest.TestCase):
    def setUp(self):
        from math import ceil

        self.bts = b'1234'

        temp = t.decompile_pixels_to_bytes(
            t.decompile_matrix_to_pixels(
                t.image_to_matrix(
                    t.matrix_to_image(
                        t.compile_pixels_to_matrix(
                            t.compile_bytes_to_pixels(
                                t.pad_bytes(self.bts) * 2
                            )
                        )
                    )
                )
            )
        )
        self.bts_reversed = \
            t.strip_bytes(
                temp[:ceil(len(temp)/2)]
            )

    def test_reversing(self):
        self.assertEqual(
            self.bts,
            self.bts_reversed
        )
