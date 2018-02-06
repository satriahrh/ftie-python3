import unittest
import suplementary.matrix as mt

class TestMulGf(unittest.TestCase):
    def test_simple(self):
        A = [
            [1,2],
            [3,4]
        ]
        B = [
            [5],
            [6]
        ]
        n = 7
        actual = mt.mul_gf(A,B,n)
        expected = [
            [3],
            [4]
        ]
        self.assertEqual(expected, actual)

    def test_error(self):
        A = [
            [1,2],
            [3,4]
        ]
        B = [
            [5],
            [6]
        ]
        n = 7
        self.assertRaises(ValueError, mt.mul_gf, B, A, n)
