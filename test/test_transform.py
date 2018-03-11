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
