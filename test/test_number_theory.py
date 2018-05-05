import unittest
import suplementary.number_theory as nt
import numpy as np


class TestIsPrime(unittest.TestCase):
    def test_p_is_prime(self):
        actual = nt.is_prime(p=5)
        self.assertTrue(actual)

    def test_p_is_not_prime(self):
        actual = nt.is_prime(p=6)
        self.assertFalse(actual)

    def test_p_is_less_than_two(self):
        actual = nt.is_prime(p=1)
        self.assertFalse(actual)

    def test_p_is_root(self):
        actual = nt.is_prime(p=9)
        self.assertFalse(actual)


class TestMod(unittest.TestCase):
    def test_mod_add(self):
        expected = [0, 1, 0, 1]
        for i in range(4):
            with self.subTest(i=i):
                actual = nt.mod_add(0, i, 2)
                self.assertEqual(expected[i], actual)

    def test_mod_mul(self):
        expected = [0, 1, 2, 0, 1]
        for i in range(5):
            with self.subTest(i=i):
                actual = nt.mod_mul(1, i, 3)
                self.assertEqual(expected[i], actual)

    def test_mod_pow(self):
        expected = [1, 2, 4, ] + [0, ] * 7
        for i in range(10):
            with self.subTest(i=i):
                actual = nt.mod_pow(2, i, 8)
                self.assertEqual(expected[i], actual)

    def test_mod_matrix_mul(self):
        A = np.array([
            [1, 3],
            [3, 4]
        ])

        B = np.array([
            [5, 0],
            [1, 2]
        ])

        expected = np.array([
            [2, 0],
            [1, 2]
        ])

        actual = nt.mod_matrix_mul(A, B, 6)

        self.assertTrue(np.array_equal(expected, actual))

    def test_mod_matrix_pow(self):
        base_matrix = np.array([
            [1, 2],
            [3, 4]
        ])

        expected = np.array([
            [
                [1, 0],
                [0, 1]
            ], [
                [1, 2],
                [3, 4]
            ], [
                [2, 0],
                [0, 2]
            ],
        ])

        for i in range(3):
            with self.subTest(i=i):
                actual = nt.mod_matrix_pow(base_matrix, i, 5)
                self.assertTrue(np.array_equal(expected[i], actual))
