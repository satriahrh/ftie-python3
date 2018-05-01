from app import Application

import numpy as np
import unittest


class TestFunctioning(unittest.TestCase):
    def test_acm_discrete(self):
        bbs_p = 7
        bbs_q = 11
        bbs_s = 9
        acm_a = 1
        acm_b = 1
        acm_n = 5

        plainfile_begin = np.random.randint(0, 256, 58, 'B').tobytes()

        cipherimage = Application(
            bbs_p, bbs_q, bbs_s, acm_a, acm_b, acm_n
        ).encrypt(plainfile_begin)

        plainfile_end = Application(
            bbs_p, bbs_q, bbs_s, acm_a, acm_b, acm_n
        ).decrypt(cipherimage)

        self.assertEqual(plainfile_begin, plainfile_end)

    def test_acm_general_equal(self):
        bbs_p = 7
        bbs_q = 11
        bbs_s = 9
        acm_a = 2
        acm_b = 2
        acm_n = 5

        plainfile_begin = np.random.randint(0, 256, 58, 'B').tobytes()

        cipherimage = Application(
            bbs_p, bbs_q, bbs_s, acm_a, acm_b, acm_n
        ).encrypt(plainfile_begin)

        plainfile_end = Application(
            bbs_p, bbs_q, bbs_s, acm_a, acm_b, acm_n
        ).decrypt(cipherimage)

        self.assertEqual(plainfile_begin, plainfile_end)

    def test_acm_general_any(self):
        bbs_p = 7
        bbs_q = 11
        bbs_s = 9
        acm_a = 2
        acm_b = 3
        acm_n = 2

        plainfile_begin = np.random.randint(0, 256, 58, 'B').tobytes()

        cipherimage = Application(
            bbs_p, bbs_q, bbs_s, acm_a, acm_b, acm_n
        ).encrypt(plainfile_begin)

        plainfile_end = Application(
            bbs_p, bbs_q, bbs_s, acm_a, acm_b, acm_n
        ).decrypt(cipherimage)

        self.assertEqual(plainfile_begin, plainfile_end)
