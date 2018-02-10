import unittest
import suplementary.matrix as mt

class TestMulGf(unittest.TestCase):
    def test_simple(self):
        matrix_a = [
            [1, 2],
            [3, 4]
        ]
        matrix_b = [
            [5],
            [6]
        ]
        _n = 7
        actual = mt.mul_gf(matrix_a, matrix_b, _n)
        expected = [
            [3],
            [4]
        ]
        self.assertEqual(expected, actual)

    def test_error(self):
        matrix_a = [
            [1, 2],
            [3, 4]
        ]
        matrix_b = [
            [5],
            [6]
        ]
        _n = 7
        self.assertRaises(ValueError, mt.mul_gf, matrix_b, matrix_a, _n)
