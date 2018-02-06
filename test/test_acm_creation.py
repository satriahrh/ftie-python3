import unittest
from blocks.acm import ACM


class TestAcmValidation(unittest.TestCase):
    def test_validation_a_and_b_is_good(self):
        a = 3
        b = 5
        n = 4000
        acm = ACM(a, b, n)
        haystack = acm.get_errors('validation')
        needle = "a or b is no more than 1"
        self.assertNotIn(needle, haystack)

    def test_validation_a_and_b_is_not_good(self):
        a = 0
        b = 5
        n = 4000
        acm = ACM(a, b, n)
        haystack = acm.get_errors('validation')
        needle = "a or b is no more than 1"
        self.assertIn(needle, haystack)
