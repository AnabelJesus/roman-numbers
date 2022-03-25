import unittest
from roman_numbers import roman_numbers


class roman_numbers_should(unittest.TestCase):

    def test_return_I_when_1(self):

        # Arrange
        input_int = 1
        expected_output = "I"

        # Act
        output = roman_numbers().roman(input=input_int)

        # Act
        self.assertEqual(expected_output, output)
