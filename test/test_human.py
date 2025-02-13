import unittest
from unittest.mock import patch
from source.human import Human
from source.admin import Admin

class test_Human(unittest.TestCase):

    @patch("builtins.input", side_effect=["1", "2", "c", "1780"])
    def test_shop_cart_content(self, mock_input):
        human = Human()
        human.shop()
        expected_cart = {"1": 1, "2": 1}
        self.assertEqual(human.items_in_cart, expected_cart)

if __name__ == '__main__':
    unittest.main()