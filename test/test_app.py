from app import Application

import numpy as np
import unittest


class TestFunctioning(unittest.TestCase):
    def test_acm_discrete(self):
        p = 7
        q = 11
        s = 9
        a = 1
        b = 1
        n = 5

        plainfile_begin = np.random.randint(0, 256, 58, 'B').tobytes()

        cipherimage = Application(
            p, q, s, a, b, n
        ).encrypt(plainfile_begin)

        plainfile_end = Application(
            p, q, s, a, b, n
        ).decrypt(cipherimage)

        self.assertEqual(plainfile_begin, plainfile_end)

    def test_acm_general_equal(self):
        p = 7
        q = 11
        s = 9
        a = 2
        b = 2
        n = 5

        plainfile_begin = np.random.randint(0, 256, 58, 'B').tobytes()

        cipherimage = Application(
            p, q, s, a, b, n
        ).encrypt(plainfile_begin)

        plainfile_end = Application(
            p, q, s, a, b, n
        ).decrypt(cipherimage)

        self.assertEqual(plainfile_begin, plainfile_end)

    def test_acm_general_any(self):
        p = 7
        q = 11
        s = 9
        a = 2
        b = 3
        n = 2

        plainfile_begin = np.random.randint(0, 256, 58, 'B').tobytes()

        cipherimage = Application(
            p, q, s, a, b, n
        ).encrypt(plainfile_begin)

        plainfile_end = Application(
            p, q, s, a, b, n
        ).decrypt(cipherimage)

        self.assertEqual(plainfile_begin, plainfile_end)
