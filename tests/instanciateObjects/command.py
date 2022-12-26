import unittest

from src import Command

from exception import BadCommandValueException

class TestInitCommand(unittest.TestCase):

    def test_init_command(self):

        # Arrange

        # Action 
        cardinal = Command(value="Up")

        # Assert
        self.assertEqual(cardinal._value, "Up")

    def test_init_cardinal_with_bad_value(self):

        # Arrange

        # Action 
        with self.assertRaises(BadCommandValueException) as ar:
            Command(value="Toto")

        # Assert
        self.assertEqual(str(ar.exception), "The Command Value Must Be One of ('Up', 'Down', 'Left', 'Right')")