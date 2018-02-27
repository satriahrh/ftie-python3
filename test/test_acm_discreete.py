import unittest
from blocks.acm import ACM


class TestAcmDiscreete(unittest.TestCase):
    def setUp(self):
        maps_dimension = 7
        self.__acm = ACM(1, 1, maps_dimension)
        self.__original_map = [
            [
                [x, y] for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ]
        self.__plaintext = [
            [
                10 * x + y for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ]
        self.__ciphertext = [
            [
                10 * x + y for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ]

    def test_type_zero_period(self):
        actual = self.__acm.get_map(8)  # 8 is the period of this form
        expected = self.__original_map
        self.assertEqual(expected, actual)

    def test_type_zero_not_period(self):
        actual = self.__acm.get_map()  # 7 is not the period of this form
        expected = self.__original_map
        self.assertNotEqual(expected, actual)

    def test_encrypt_decrypt(self):
        actual = self.__acm.decrypt(self.__acm.encrypt(self.__plaintext))
        expected = self.__plaintext
        self.assertEqual(actual, expected)
