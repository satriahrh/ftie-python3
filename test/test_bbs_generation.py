import unittest
from blocks.bbs import BBS


class TestGenerationInduction(unittest.TestCase):
    # profing by mathematical induction for i >= 1

    def test_x_one_generation(self):
        # s(1) is True? i = k + 1, using seed s(0) = 9

        bbs = BBS(_p=7, _q=11, seed=9)

        actual = bbs.next()
        expected = 4  # calculated by hand
        self.assertEqual(expected, actual)

    def test_x_plus_one_generation(self):
        # s(i+1) is True by assumption. x = k + 1
        # using s(1) = 4
        # is s(i+1) = 16?

        bbs = BBS(_p=7, _q=11, seed=9)
        bbs.next()

        actual = bbs.next()
        expected = 16  # calculated by hand
        self.assertEqual(expected, actual)
