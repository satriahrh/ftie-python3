import unittest
import suplementary.number_theory as nt

class TestIsPrime(unittest.TestCase):
    def test_p_is_prime(self):
        p = 5
        actual = nt.is_prime(p)
        self.assertTrue(actual)

    def test_p_is_not_prime(self):
        p = 6
        actual = nt.is_prime(p)
        self.assertFalse(actual)

    def test_p_is_less_than_two(self):
        p = 1
        actual = nt.is_prime(p)
        self.assertFalse(actual)

    def test_p_is_root(self):
        p = 9
        actual = nt.is_prime(p)
        self.assertFalse(actual)
