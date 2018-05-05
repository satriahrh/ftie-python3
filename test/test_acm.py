import unittest
from blocks.acm import ACM

import numpy as np


class TestAcmDiscreete(unittest.TestCase):
    def setUp(self):
        self.create_simple_map = lambda maps_dimension: np.array([
            [
                (x, y) for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ])
        self.plainmatrix = \
            np.random.randint(0, 256, 27, 'B').reshape(3, 3, 3)

    def test_type_zero_period(self):
        acm = ACM(_a=1, _b=1, number_of_iteration=8)
        actual = acm.get_map(7)  # 8 is the period of this form
        expected = self.create_simple_map(7)
        self.assertTrue(np.array_equal(expected, actual))

    def test_type_zero_not_period(self):
        acm = ACM(_a=1, _b=1, number_of_iteration=1)
        actual = acm.get_map(7)  # 1 is not the period of this form
        expected = self.create_simple_map(7)
        print(expected.any)
        self.assertFalse(np.array_equal(expected, actual))

    def test_encrypt_decrypt(self):
        acm = ACM(_a=1, _b=1, number_of_iteration=1)
        ciphermatrix = acm.encrypt(self.plainmatrix)
        actual = acm.decrypt(ciphermatrix)
        expected = self.plainmatrix
        self.assertTrue(np.array_equal(expected, actual))


class TestAcmGeneralEqual(unittest.TestCase):
    def setUp(self):
        self.create_simple_map = lambda maps_dimension: np.array([
            [
                (x, y) for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ])
        self.plainmatrix = \
            np.random.randint(0, 256, 27, 'B').reshape(3, 3, 3)

    def test_type_one_period(self):
        acm = ACM(_a=3, _b=3, number_of_iteration=3)
        actual = acm.get_map(9)  # 3 is the period of this form
        expected = self.create_simple_map(9)
        self.assertTrue(np.array_equal(expected, actual))

    def test_type_one_not_period(self):
        acm = ACM(_a=3, _b=3, number_of_iteration=2)
        actual = acm.get_map(9)  # 2 is not the period of this form
        expected = self.create_simple_map(9)
        self.assertFalse(np.array_equal(expected, actual))

    def test_encrypt_decrypt(self):
        acm = ACM(_a=3, _b=3, number_of_iteration=1)
        ciphermatrix = acm.encrypt(self.plainmatrix)
        actual = acm.decrypt(ciphermatrix)
        expected = self.plainmatrix
        self.assertTrue(np.array_equal(expected, actual))


# TODO unittest for its period
class TestAcmGeneralDifferent(unittest.TestCase):
    def setUp(self):
        self.create_simple_map = lambda maps_dimension: np.array([
            [
                (x, y) for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ])
        self.plainmatrix = \
            np.random.randint(0, 256, 27, 'B').reshape(3, 3, 3)

    def test_type_one_period(self):
        acm = ACM(_a=2, _b=3, number_of_iteration=4)
        actual = acm.get_map(8)  # 4 is the period of this form
        expected = self.create_simple_map(8)
        self.assertTrue(np.array_equal(expected, actual))

    def test_type_one_not_period(self):
        acm = ACM(_a=2, _b=3, number_of_iteration=3)
        actual = acm.get_map(8)  # 3 is not the period of this form
        expected = self.create_simple_map(8)
        self.assertFalse(np.array_equal(expected, actual))

    def test_encrypt_decrypt(self):
        acm = ACM(_a=1, _b=2, number_of_iteration=1)
        ciphermatrix = acm.encrypt(self.plainmatrix)
        actual = acm.decrypt(ciphermatrix)
        expected = self.plainmatrix
        self.assertTrue(np.array_equal(expected, actual))
