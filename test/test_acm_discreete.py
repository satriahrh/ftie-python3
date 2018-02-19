import unittest
from blocks.acm import ACM


class TestAcmDiscreete(unittest.TestCase):
    def setUp(self):
        number_of_iteration = 7
        self.__acm = ACM(1, 1, number_of_iteration)
        self.__original_map = [
            [
                [x, y] for y in range(number_of_iteration)
            ] for x in range(number_of_iteration)
        ]
        self.__plaintext = [
            [
                10 * x + y for y in range(number_of_iteration)
            ] for x in range(number_of_iteration)
        ]
        self.__ciphertext = [
            [
                10 * x + y for y in range(number_of_iteration)
            ] for x in range(number_of_iteration)
        ]
        self.__number_of_iteration = number_of_iteration

    def test_type_zero_period(self):
        actual = self.__acm.get_map(8)  # 5 is the period of this form
        expected = self.__original_map
        self.assertEqual(expected, actual)

    def test_type_zero_not_period(self):
        actual = self.__acm.get_map()  # 4 is not the period of this form
        expected = self.__original_map
        self.assertNotEqual(expected, actual)

    def test_encrypt_decrypt(self):
        actual = self.__acm.decrypt(self.__acm.encrypt(self.__plaintext))
        expected = self.__plaintext
        self.assertEqual(actual, expected)
