import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))
import unittest
from unittest.mock import patch
from source.human import Human

class test_Human(unittest.TestCase):

    @patch("builtins.input", side_effect=["cls", "1", "2", "c", "1780", "q", "esc", "1", "2", "1", "2000", "Y", "3", "cls"])
    def test_title(self, mock_input):
        human = Human()
        human.title()
        human.shop()
        expected_cart = {}
        self.assertEqual(human.items_in_cart, expected_cart)
        human.title()
        expected_cart = {}
        self.assertEqual(human.items_in_cart, expected_cart)   

if __name__ == '__main__':
    unittest.main()