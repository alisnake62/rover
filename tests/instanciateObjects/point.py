import unittest

from main import Point

from exception import BadPointValueException

class TestInitPoint(unittest.TestCase):

    def test_init_point(self):

        # Arrange

        # Action 
        point = Point(value=1)

        # Assert
        self.assertEqual(point._value, 1)

    def test_init_point_with_negative_value(self):

        # Arrange

        # Action 
        with self.assertRaises(BadPointValueException) as ar:
            Point(value=-1)

        # Assert
        self.assertEqual(str(ar.exception), "The Point Value Must Positive or 0")

    def test_init_point_with_float_value(self):

        # Arrange

        # Action 
        with self.assertRaises(BadPointValueException) as ar:
            Point(value=1.5)

        # Assert
        self.assertEqual(str(ar.exception), "The Point Value Must Be Integer")