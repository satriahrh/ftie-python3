import unittest
from blocks.acm import ACM


class TestAcmValidation(unittest.TestCase):
    def test_validation_a_and_b_is_good(self):
        _a = 1
        _b = 1
        _n = 4000
        acm = ACM(_a, _b, _n)
        haystack = acm.get_errors('validation')
        needle = "a or b is no more than 1"
        self.assertNotIn(needle, haystack)

    def test_validation_a_and_b_is_not_good(self):
        _a = 0
        _b = 5
        _n = 4000
        acm = ACM(_a, _b, _n)
        haystack = acm.get_errors('validation')
        needle = "a or b is no more than 1"
        self.assertIn(needle, haystack)
