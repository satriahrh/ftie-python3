import unittest
from blocks.rt import RT
from blocks.bbs import BBS
from errors import ValidationError


class TestRTConstructor(unittest.TestCase):
    @unittest.expectedFailure
    def test_validation_constructor_is_good(self):
        try:
            bbs = BBS(_p=5, _q=5, seed=3)
            RT(bbs)
            self.fail('Validation is succeed and no errors')
        except ValidationError as err:
            actual = err.errors
            expected = "bbs is not BBS type"
            self.assertEqual(expected, actual)

    def test_validation_bbs_problem(self):
        try:
            bbs = None
            RT(bbs)
            self.fail('Validation is succeed and no errors')
        except ValidationError as err:
            actual = err.errors
            expected = "bbs is not BBS type"
            self.assertEqual(expected, actual)
