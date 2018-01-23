import unittest
from blocks.rt import RT
from blocks.bbs import BBS


class TestEncryptionDecryption(unittest.TestCase):
    def test_encryption_succeed(self):
        p = 7
        q = 11
        s = 9
        alice = RT(BBS(p, q, s))
        P = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        C = alice.encrypt(P)
        message = "Encryption do not really encrypt the plaintext."
        self.assertNotEqual(P, C, message)

    def test_decryption_succeed(self):
        p = 7
        q = 11
        s = 9
        alice = RT(BBS(p, q, s))
        bob = RT(BBS(p, q, s))
        P = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        C = alice.encrypt(P)
        decrypted = bob.decrypt(C)
        message = "Decryption failed"
        self.assertEqual(P, decrypted, message)


class TestAliceAndBob(unittest.TestCase):
    def test_alice_and_bob_are_swinging(self):
        p = 7
        q = 11
        s = 9
        alice = RT(BBS(p, q, s))
        bob = RT(BBS(p, q, s))
        P = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        C = alice.encrypt(P)
        bob.decrypt(C)
        C = bob.encrypt(P)
        decrypted = alice.decrypt(C)
        message = "Alice and Bob failed in swinging"
        self.assertEqual(P, decrypted, message)
