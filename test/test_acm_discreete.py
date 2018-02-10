import unittest
from blocks.acm import ACM


class TestAcmDiscreete(unittest.TestCase):
    def setUp(self):
        self.__acm = ACM(1,1,11)
        self.__original_map = [
            [
                [x,y] for y in range(11)
            ] for x in range(11)
        ]

    def test_type_zero_period(self):
        actual = self.__acm.encryption_map(5)  # 5 is the period of this form
        expected = self.__original_map
        self.assertEqual(expected, actual)

    def test_type_zero_not_period(self):
        actual = self.__acm.encryption_map(4)  # 4 is not the period of this form
        expected = self.__original_map
        self.assertNotEqual(expected, actual)
