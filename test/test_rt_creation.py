import unittest
from blocks.rt import RT
from blocks.bbs import BBS


class TestBbsValidation(unittest.TestCase):
    def test_validation_bbs_is_validated(self):
        bbs = BBS(_p=7, _q=11, seed=9)
        _rt = RT(bbs)
        haystack = _rt.get_errors('validation')
        needle = "BBS is not validated: "
        self.assertNotIn(needle, haystack)

    def test_validation_bbs_is_not_validated(self):
        bbs = BBS(_p=6, _q=11, seed=9)
        _rt = RT(bbs)
        haystack = _rt.get_errors('validation')
        needle = "BBS is not validated: "
        self.assertIn(needle, haystack)
