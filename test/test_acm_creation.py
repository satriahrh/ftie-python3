import unittest
from blocks.acm import ACM
from errors import ValidationError


class TestAcmValidation(unittest.TestCase):
    @unittest.expectedFailure
    def test_validation_a_and_b_is_good(self):
        try:
            ACM(1, 1, 400)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "a or b is no more than 1"
            self.assertEqual(expected, actual)

    def test_validation_a_and_b_is_not_good(self):
        try:
            ACM(0, 5, 400)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "a or b is no more than 1"
            self.assertEqual(expected, actual)
