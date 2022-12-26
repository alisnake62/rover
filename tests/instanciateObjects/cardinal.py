import unittest

from src import Cardinal

from exception import BadCardinalValueException

class TestInitCardinal(unittest.TestCase):

    def test_init_cardinal(self):

        # Arrange

        # Action 
        cardinal = Cardinal(value="North")

        # Assert
        self.assertEqual(cardinal._index, 0)

    def test_init_cardinal_with_bad_value(self):

        # Arrange

        # Action 
        with self.assertRaises(BadCardinalValueException) as ar:
            Cardinal(value="Toto")

        # Assert
        self.assertEqual(str(ar.exception), "The Cardinal Value Must Be One of ('North', 'South', 'East', 'West')")