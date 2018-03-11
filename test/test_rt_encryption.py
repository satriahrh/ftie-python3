import unittest
from blocks.rt import RT
from blocks.bbs import BBS


class TestEncryptionDecryption(unittest.TestCase):
    def setUp(self):
        self.__plainbytes = b'This is the secret message'
        self.__alice = RT(BBS(_p=7, _q=11, seed=9))
        self.__bob = RT(BBS(_p=7, _q=11, seed=9))

    def test_encryption_succeed(self):
        ciphertext = self.__alice.encrypt(self.__plainbytes)
        message = "Encryption do not really encrypt the plaintext."
        self.assertNotEqual(self.__plainbytes, ciphertext, message)

    def test_decryption_succeed(self):
        ciphertext = self.__alice.encrypt(self.__plainbytes)
        decrypted = self.__bob.decrypt(ciphertext)
        message = "Decryption failed"
        self.assertEqual(self.__plainbytes, decrypted, message)


class TestAliceAndBob(unittest.TestCase):
    def setUp(self):
        self.__plainbytes = b'This is the secret message'
        self.__alice = RT(BBS(_p=7, _q=11, seed=9))
        self.__bob = RT(BBS(_p=7, _q=11, seed=9))

    def test_alice_and_bob_are_swinging(self):
        # round 1
        ciphertext = self.__alice.encrypt(self.__plainbytes)
        self.__bob.decrypt(ciphertext)

        # round 2
        ciphertext = self.__bob.encrypt(self.__plainbytes)
        decrypted = self.__alice.decrypt(ciphertext)

        message = "Alice and Bob failed in swinging"
        self.assertEqual(self.__plainbytes, decrypted, message)
