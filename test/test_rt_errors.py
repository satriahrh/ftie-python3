# TODO: CREATE NEW UNIT TEST
import unittest
from blocks.rt import RT
from blocks.bbs import BBS
from errors import ValidationError

import numpy as np


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

    # def test_validation_bbs_problem(self):
    #     try:
    #         RT(None)
    #         self.fail('Validation is succeed and no errors')
    #     except ValidationError as err:
    #         actual = err.errors
    #         expected = "bbs is not BBS type"
    #         self.assertEqual(expected, actual)


class TestRTEncryptDecrypt(unittest.TestCase):
    def test_encrypt_is_good(self):
        bbs = BBS(_p=7, _q=11, seed=8)
        rt = RT(bbs)
        rt.encrypt(np.zeros(10))
        self.assert_(True)

    def test_decrypt_is_good(self):
        bbs = BBS(_p=7, _q=11, seed=8)
        rt = RT(bbs)
        rt.decrypt(np.zeros(10))
        self.assert_(True)
#
#     def test_encrypt_not_int(self):
#         with self.assertRaises(ValidationError) as err:
#             bbs = BBS(_p=7, _q=11, seed=8)
#             rt = RT(bbs)
#             rt.encrypt(['1', '2'])
#
#         self.assertEqual(
#             err.exception.errors,
#             "plainbytes is not bytes type"
#         )
#
#     def test_decrypt_not_int(self):
#         try:
#             bbs = BBS(_p=7, _q=11, seed=8)
#             rt = RT(bbs)
#             rt.decrypt(['1', '2'])
#             self.fail('Validation is succeed and no errors')
#         except ValidationError as err:
#             actual = err.errors
#             expected = "randomized_bytes is not bytes type"
#             self.assertEqual(expected, actual)
#
#     def test_decrypt_odd(self):
#         try:
#             bbs = BBS(_p=7, _q=11, seed=8)
#             rt = RT(bbs)
#             rt.decrypt(bytes(1))
#             self.fail('Validation is succeed and no errors')
#         except ValidationError as err:
#             actual = err.errors
#             expected = "odd lengthed ciphertext"
#             self.assertEqual(expected, actual)
