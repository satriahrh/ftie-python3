import unittest
from blocks.rt import RT
from blocks.bbs import BBS
from errors import ValidationError, DiscoveryError


class TestRTConstructor(unittest.TestCase):
    @unittest.expectedFailure
    def test_validation_constructor_is_good(self):
        try:
            bbs = BBS(_p=7, _q=11, seed=8)
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


class TestRTEncryptDecrypt(unittest.TestCase):
    def test_encrypt_derypt_is_good(self):
        try:
            bbs = BBS(_p=7, _q=11, seed=8)
            rt = RT(bbs)
            rt.encrypt([1, 2, 3, 4, 5, 6, ])
            rt.decrypt([1, 2, 3, 4, 5, 6, ])
            self.assert_(True)
        except DiscoveryError as err:
            actual = err.errors
            expected = "input is not an array of integer"
            self.assertEqual(expected, actual)

    def test_encrypt_not_int(self):
        with self.assertRaises(DiscoveryError) as err:
            bbs = BBS(_p=7, _q=11, seed=8)
            rt = RT(bbs)
            rt.encrypt(['1', '2'])

        self.assertEqual(
            err.exception.errors,
            "input is not an array of integer"
        )

    def test_decrypt_not_int(self):
        try:
            bbs = BBS(_p=7, _q=11, seed=8)
            rt = RT(bbs)
            rt.decrypt(['1', '2'])
            self.fail('Validation is succeed and no errors')
        except DiscoveryError as err:
            actual = err.errors
            expected = "input is not an array of integer"
            self.assertEqual(expected, actual)

    def test_decrypt_odd(self):
        try:
            bbs = BBS(_p=7, _q=11, seed=8)
            rt = RT(bbs)
            rt.decrypt([1, ])
            self.fail('Validation is succeed and no errors')
        except ValidationError as err:
            actual = err.errors
            expected = "odd lengthed ciphertext"
            self.assertEqual(expected, actual)
