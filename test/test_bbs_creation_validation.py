import unittest
from blocks.bbs import BBS


class TestPAndQEquality(unittest.TestCase):
    def test_validation_p_is_equal_to_q(self):
        bbs = BBS(_p=5, _q=5, seed=3)
        actual = bbs.get_errors('validation')
        expected = "p is equal to q"
        self.assertEqual(expected, actual)

    def test_validation_p_is_not_equal_to_q(self):
        bbs = BBS(_p=1, _q=2, seed=3)
        actual = bbs.get_errors('validation')
        expected = "p is equal to q"
        self.assertNotEqual(expected, actual)


class TestPAndQCongruency(unittest.TestCase):
    def test_validation_p_mod_4_are_not_3(self):
        bbs = BBS(_p=1, _q=3, seed=3)
        actual = bbs.get_errors('validation')
        expected = "p or q mod 4 are not 3"
        self.assertEqual(expected, actual)

    def test_validation_q_mod_4_are_not_3(self):
        bbs = BBS(_p=3, _q=2, seed=3)
        actual = bbs.get_errors('validation')
        expected = "p or q mod 4 are not 3"
        self.assertEqual(expected, actual)

    def test_validation_p_q_both_mod_4_are_not_3(self):
        bbs = BBS(_p=1, _q=2, seed=3)
        actual = bbs.get_errors('validation')
        expected = "p or q mod 4 are not 3"
        self.assertEqual(expected, actual)

    def test_validation_p_q_both_mod_4_are_3(self):
        bbs = BBS(_p=7, _q=11, seed=-1)
        actual = bbs.get_errors('validation')
        expected = "p or q mod 4 are not 3"
        self.assertNotEqual(expected, actual)


class TestPAndQPrimality(unittest.TestCase):
    def test_validation_p_is_not_prime_q_is_prime(self):
        bbs = BBS(_p=15, _q=3, seed=3)
        actual = bbs.get_errors('validation')
        expected = "p or q are not prime"
        self.assertEqual(expected, actual)

    def test_validation_p_is_prime_q_is_not_prime(self):
        bbs = BBS(_p=3, _q=15, seed=3)
        actual = bbs.get_errors('validation')
        expected = "p or q are not prime"
        self.assertEqual(expected, actual)

    def test_validation_p_and_q_are_not_prime(self):
        bbs = BBS(_p=27, _q=15, seed=3)
        actual = bbs.get_errors('validation')
        expected = "p or q are not prime"
        self.assertEqual(expected, actual)

    def test_validation_p_and_q_are_prime(self):
        bbs = BBS(_p=3, _q=7, seed=3)
        actual = bbs.get_errors('validation')
        expected = "p or q are not prime"
        self.assertNotEqual(expected, actual)


class TestSInRange(unittest.TestCase):
    def test_validation_s_is_too_small(self):
        bbs = BBS(_p=7, _q=11, seed=-3)
        actual = bbs.get_errors('validation')
        expected = "s is to small or to big"
        self.assertEqual(expected, actual)

    def test_validation_s_is_too_big(self):
        bbs = BBS(_p=7, _q=11, seed=78)
        actual = bbs.get_errors('validation')
        expected = "s is to small or to big"
        self.assertEqual(expected, actual)

    def test_validation_s_is_in_range(self):
        bbs = BBS(_p=7, _q=11, seed=8)
        actual = bbs.get_errors('validation')
        expected = "s is to little or to big"
        self.assertNotEqual(expected, actual)


class TestPAndSPrimeRelativity(unittest.TestCase):
    def test_validation_s_and_m_are_not_relatively_prime(self):
        bbs = BBS(_p=7, _q=11, seed=7)
        actual = bbs.get_errors('validation')
        expected = "m and s are not relatively prime"
        self.assertEqual(expected, actual)

    def test_validation_s_and_m_are_relatively_prime(self):
        bbs = BBS(_p=7, _q=11, seed=8)
        actual = bbs.get_errors('validation')
        expected = "m and s are not relatively prime"
        self.assertNotEqual(expected, actual)
