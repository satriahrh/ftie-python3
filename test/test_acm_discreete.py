import unittest
from blocks.acm import ACM


class TestAcmDiscreete(unittest.TestCase):
    def setUp(self):
        self.create_simple_map = lambda maps_dimension: [
            [
                [x, y] for y in range(maps_dimension)
            ] for x in range(maps_dimension)
        ]
        self.create_simple_message = lambda message_dimension: [
            [
                10 * x + y for y in range(message_dimension)
            ] for x in range(message_dimension)
        ]

    def test_type_zero_period(self):
        acm = ACM(1, 1, 8)
        actual = acm.get_map(7)  # 8 is the period of this form
        expected = self.create_simple_map(7)
        self.assertEqual(expected, actual)

    def test_type_zero_not_period(self):
        acm = ACM(1, 1, 1)
        actual = acm.get_map(7)  # 1 is not the period of this form
        expected = self.create_simple_map(7)
        self.assertNotEqual(expected, actual)

    def test_encrypt_decrypt(self):
        acm = ACM(1, 1, 1)
        actual = acm.decrypt(acm.encrypt(self.create_simple_message(7)))
        expected = self.create_simple_message(7)
        self.assertEqual(actual, expected)
