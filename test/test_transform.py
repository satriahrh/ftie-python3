import unittest
from blocks import transform as t


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
        self.padded = t.pad_pixels(self.pixels)

    def test_not_populated(self):
        self.assertEqual(self.pixels_not_padded, self.pixels)

    def test_functioning(self):
        self.assertEqual(self.padded, self.expected_pixels_padded)


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
    def test_functioning(self):
        pixels = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)
        ]

        expected = [
            [
                (1, 2, 3), (4, 5, 6)
            ], [
                (7, 8, 9), (10, 11, 12)
            ]
        ]
        actual = t.pixels_to_matrix(pixels)
        self.assertEqual(actual, expected)


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
        self.numbers = [
            1, 2, 3, 4, 5, 6, 7
        ]
        self.numbers_reversed = \
            t.pixels_to_numbers(
                t.matrix_to_pixels(
                    t.image_to_matrix(
                        t.matrix_to_image(
                            t.pixels_to_matrix(
                                t.numbers_to_pixels(self.numbers)
                            )
                        )
                    )
                )
            )

    def test_reversing(self):
        self.assertEqual(
            self.numbers,
            self.numbers_reversed[:len(self.numbers)]
        )

        self.subTest(self)

    def test_len(self):
        self.assertEqual(12, len(self.numbers_reversed))
