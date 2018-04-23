import unittest
from blocks.acm import ACM
from errors import ValidationError
from PIL import Image


class TestAcmConstructor(unittest.TestCase):
    @unittest.expectedFailure
    def test_validation_constructor_is_good(self):
        try:
            ACM(_a=1, _b=1, number_of_iteration=400)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "a or b is no more than 1"
            self.assertEqual(expected, actual)

    def test_validation_a_and_b_problem(self):
        try:
            ACM(_a=0, _b=5, number_of_iteration=400)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "a or b is no more than 1"
            self.assertEqual(expected, actual)

    def test_validation_number_of_iteration_problem(self):
        try:
            ACM(_a=1, _b=1, number_of_iteration=0)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "number_of_iteration is too small"
            self.assertEqual(expected, actual)


class TestACMGetMap(unittest.TestCase):
    def setUp(self):
        self.acm = ACM(_a=1, _b=1, number_of_iteration=2)

    @unittest.expectedFailure
    def test_validation_get_map_is_good(self):
        try:
            self.acm.get_map(2)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "image dimension is too small"
            self.assertEqual(expected, actual)

    def test_validation_get_map_problem(self):
        try:
            self.acm.get_map(1)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "image dimension is too small"
            self.assertEqual(expected, actual)


class TestACMEncryptDecrypt(unittest.TestCase):
    def setUp(self):
        self.acm = ACM(_a=1, _b=1, number_of_iteration=2)

    @unittest.expectedFailure
    def test_validation_encrypt_matrix_is_good(self):
        try:
            image = Image.new('L', (5, 5))
            self.acm.encrypt(image)
            self.acm.decrypt(image)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "image is not a square image"
            self.assertEqual(expected, actual)

    def test_validation_encrypt_matrix_square_problem(self):
        try:
            image = Image.new('L', (5, 3))
            self.acm.encrypt(image)
            self.acm.decrypt(image)
            self.fail('Validation is succeed and no errors')
        except ValidationError as validation_error:
            actual = validation_error.errors
            expected = "image is not a square image"
            self.assertEqual(expected, actual)
