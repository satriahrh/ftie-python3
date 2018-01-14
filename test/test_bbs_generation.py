import unittest
from blocks.bbs import BBS


class TestFailureCreation(unittest.TestCase):
    def test_creation_failed(self):
        bbs = BBS(p=7, q=11, s=7)
        actual = bbs.next()
        self.assertIsNone(actual)

    def test_creation_succeed(self):
        bbs = BBS(p=7, q=11, s=9)
        actual = bbs.next()
        self.assertIsNotNone(actual)


class TestGenerationInduction(unittest.TestCase):
    # profing by mathematical induction for i >= 1

    def test_x_one_generation(self):
        # s(1) is True? i = k + 1, using seed s(0) = 9

        bbs = BBS(p=7, q=11, s=9)

        actual = bbs.next()
        expected = 4  # calculated by hand
        self.assertEqual(expected, actual)

    def test_x_plus_one_generation(self):
        # s(i+1) is True by assumption. x = k + 1
        # using s(1) = 4
        # is s(i+1) = 16?

        bbs = BBS(p=7, q=11, s=9)
        bbs.next()

        actual = bbs.next()
        expected = 16  # calculated by hand
        self.assertEqual(expected, actual)
