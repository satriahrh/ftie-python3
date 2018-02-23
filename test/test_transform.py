import unittest
from blocks import transform as t


class TestPadNumbersFunctioning(unittest.TestCase):
    def test_functioning(self):
        numbers = [
            1, 2, 3, 4
        ]

        expected = [
            1, 2, 3, 4, 0, 0
        ]
        actual = t.pad_numbers(numbers)
        self.assertEqual(actual, expected)


class TestPadPixelsFunctioning(unittest.TestCase):
    def test_functioning(self):
        pixels = [
            (1, 2, 3), (4, 5, 6)
        ]

        expected = [
            (1, 2, 3), (4, 5, 6),
            (0, 0, 0), (0, 0, 0)
        ]
        actual = t.pad_pixels(pixels)
        self.assertEqual(actual, expected)


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

    def test_reversing(self):
        numbers = self.numbers.copy()

        numbers_reversed = \
            t.pixels_to_numbers(
                t.matrix_to_pixels(
                    t.image_to_matrix(
                        t.matrix_to_image(
                            t.pixels_to_matrix(
                                t.numbers_to_pixels(numbers)
                            )
                        )
                    )
                )
            )
        self.assertEqual(self.numbers, numbers_reversed[:len(self.numbers)])
