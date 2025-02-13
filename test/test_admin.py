import unittest
from source.admin import Admin
from unittest.mock import patch
class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.admin = Admin()

    def test_initial_prices(self):
        self.assertEqual(self.admin.items["1"]["price"], 1000)
        self.assertEqual(self.admin.items["2"]["price"], 780)
        self.assertEqual(self.admin.items["3"]["price"], 880)
        self.assertEqual(self.admin.items["4"]["price"], 150)
    @patch('builtins.input', side_effect=['1', '1200', 'Y'])
    def test_command2_price_change(self, mock_input):
        self.admin.command2(skip_menu=True)
        self.assertEqual(int(self.admin.items["1"]["price"]), 1200)
    def test_command1(self):
        self.admin.command1(skip_menu=True)
        self.assertEqual(int(self.admin.items["1"]["pieces"]), 0)
        self.assertEqual(int(self.admin.items["1"]["sum"]), 0)
        self.assertEqual(int(self.admin.items["2"]["pieces"]), 0)
        self.assertEqual(int(self.admin.items["2"]["sum"]), 0)
        self.assertEqual(int(self.admin.items["3"]["pieces"]), 0)
        self.assertEqual(int(self.admin.items["3"]["sum"]), 0)
        self.assertEqual(int(self.admin.items["4"]["pieces"]), 0)
        self.assertEqual(int(self.admin.items["4"]["sum"]), 0)
    
if __name__ == '__main__':
    unittest.main()