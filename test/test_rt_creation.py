import unittest
from blocks.rt import RT
from blocks.bbs import BBS


class TestBbsValidation(unittest.TestCase):
    def test_validation_bbs_is_validated(self):
        p = 7
        q = 11
        s = 9
        bbs = BBS(p, q, s)
        rt = RT(bbs)
        haystack = rt.get_errors('validation')
        needle = "BBS is not validated: "
        self.assertNotIn(needle, haystack)

    def test_validation_bbs_is_not_validated(self):
        p = 6
        q = 11
        s = 9
        bbs = BBS(p, q, s)
        rt = RT(bbs)
        haystack = rt.get_errors('validation')
        needle = "BBS is not validated: "
        self.assertIn(needle, haystack)
