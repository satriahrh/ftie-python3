import unittest
import suplementary.number_theory as nt

class TestIsPrime(unittest.TestCase):
    def test_p_is_prime(self):
        actual = nt.is_prime(_p=5)
        self.assertTrue(actual)

    def test_p_is_not_prime(self):
        actual = nt.is_prime(_p=6)
        self.assertFalse(actual)

    def test_p_is_less_than_two(self):
        actual = nt.is_prime(_p=1)
        self.assertFalse(actual)

    def test_p_is_root(self):
        actual = nt.is_prime(_p=9)
        self.assertFalse(actual)
