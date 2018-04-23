import unittest
from blocks import transform as t

import numpy as np


class TestPadStripBytesFunctioning(unittest.TestCase):
    def setUp(self):
        self.bts = np.ones(4, np.dtype('B'))
        self.bts_padded_expected = np.array([1, 1, 1, 1, 0, 0], np.dtype('B'))
        self.bts_padded_actual = t.pad_bytes(self.bts)
        self.bts_padded_stripped = t.strip_bytes(self.bts_padded_actual)

    def test_pad_bytes_functioning(self):
        self.assertEqual(
            self.bts_padded_expected.all(), self.bts_padded_actual.all()
        )

    def test_strip_bytes_functioning(self):
        self.assertEqual(
            self.bts.all(), self.bts_padded_stripped.all()
        )


class TestBytesToMatrixFunctioning(unittest.TestCase):
    def test_functioning(self):
        bts = np.array(
            [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
            ], np.dtype('B')
        )
        expected = np.array(
                [
                    [[1, 2, 3], [4, 5, 6]],
                    [[7, 8, 9], [10, 11, 12]],
                ], np.dtype('B')
        )

        actual = t.bytes_to_matrix(bts)
        self.assertEqual(actual.all(), expected.all())


class TestMatrixToBytesFunctioning(unittest.TestCase):
    def test_functioning(self):
        matrix = np.array(
                [
                    [[1, 2, 3], [4, 5, 6]],
                    [[7, 8, 9], [10, 11, 12]],
                ], np.dtype('B')
        )

        expected = np.array(
            [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
            ], np.dtype('B')
        )
        actual = t.matrix_to_bytes(matrix)
        self.assertEqual(actual.all(), expected.all())
