import unittest
from blocks.bbs import BBS
from errors import ValidationError


class TestPAndQEquality(unittest.TestCase):
    def test_validation_p_is_equal_to_q(self):
        try:
            BBS(p=5, q=5, s=3)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "p is equal to q"
            self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_validation_p_is_not_equal_to_q(self):
        try:
            BBS(p=1, q=2, s=3)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "p is equal to q"
            self.assertEqual(expected, actual)


class TestPAndQCongruency(unittest.TestCase):
    def test_validation_p_mod_4_are_not_3(self):
        try:
            BBS(p=1, q=3, s=3)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "p or q mod 4 are not 3"
            self.assertEqual(expected, actual)

    def test_validation_q_mod_4_are_not_3(self):
        try:
            BBS(p=3, q=2, s=3)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "p or q mod 4 are not 3"
            self.assertEqual(expected, actual)

    def test_validation_p_q_both_mod_4_are_not_3(self):
        try:
            BBS(p=1, q=2, s=3)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "p or q mod 4 are not 3"
            self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_validation_p_q_both_mod_4_are_3(self):
        try:
            BBS(p=7, q=11, s=3)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "p or q mod 4 are not 3"
            self.assertEqual(expected, actual)


class TestPAndQPrimality(unittest.TestCase):
    def test_validation_p_is_not_prime_q_is_prime(self):
        try:
            BBS(p=15, q=3, s=3)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "p or q are not prime"
            self.assertEqual(expected, actual)

    def test_validation_p_is_prime_q_is_not_prime(self):
        try:
            BBS(p=3, q=15, s=3)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "p or q are not prime"
            self.assertEqual(expected, actual)

    def test_validation_p_and_q_are_not_prime(self):
        try:
            BBS(p=27, q=15, s=3)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "p or q are not prime"
            self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_validation_p_and_q_are_prime(self):
        try:
            BBS(p=3, q=7, s=3)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "p or q are not prime"
            self.assertEqual(expected, actual)


class TestSInRange(unittest.TestCase):
    def test_validation_s_is_too_small(self):
        try:
            BBS(p=7, q=11, s=-3)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "s is to small or to big"
            self.assertEqual(expected, actual)

    def test_validation_s_is_too_big(self):
        try:
            BBS(p=7, q=11, s=78)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "s is to small or to big"
            self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_validation_s_is_in_range(self):
        try:
            BBS(p=7, q=11, s=8)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "s is to small or to big"
            self.assertEqual(expected, actual)


class TestPAndSPrimeRelativity(unittest.TestCase):
    def test_validation_s_and_m_are_not_relatively_prime(self):
        try:
            BBS(p=7, q=11, s=7)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "(p * q) and s are not relatively prime"
            self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_validation_s_and_m_are_relatively_prime(self):
        try:
            BBS(p=7, q=11, s=8)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "(p * q) and s are not relatively prime"
            self.assertEqual(expected, actual)
