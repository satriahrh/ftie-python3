import unittest
from blocks.rt import RT
from errors import ValidationError, DiscoveryError


class TestRTEncryptDecrypt(unittest.TestCase):
    def test_encrypt_derypt_is_good(self):
        try:
            rt = RT(bbs_p=7, bbs_q=11, bbs_seed=8)
            rt.encrypt(bytes(6))
            rt.decrypt(bytes(6))
            self.assert_(True)
        except DiscoveryError as err:
            actual = err.errors
            expected = "input is not an array of integer"
            self.assertEqual(expected, actual)

    def test_encrypt_not_int(self):
        with self.assertRaises(ValidationError) as err:
            rt = RT(bbs_p=7, bbs_q=11, bbs_seed=8)
            rt.encrypt(['1', '2'])

        self.assertEqual(
            err.exception.errors,
            "plainbytes is not bytes type"
        )

    def test_decrypt_not_int(self):
        try:
            rt = RT(bbs_p=7, bbs_q=11, bbs_seed=8)
            rt.decrypt(['1', '2'])
            self.fail('Validation is succeed and no errors')
        except ValidationError as err:
            actual = err.errors
            expected = "randomized_bytes is not bytes type"
            self.assertEqual(expected, actual)

    def test_decrypt_odd(self):
        try:
            rt = RT(bbs_p=7, bbs_q=11, bbs_seed=8)
            rt.decrypt(bytes(1))
            self.fail('Validation is succeed and no errors')
        except ValidationError as err:
            actual = err.errors
            expected = "odd lengthed ciphertext"
            self.assertEqual(expected, actual)
