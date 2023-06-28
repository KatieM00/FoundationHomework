import unittest
from shop.py import shop_simulation, InsufficientFundError, MaximumAttemptsExceededError


class ShopSimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.items = {
            "Headphones": 30,
            "Kindle": 80,
            "USB": 15,
            "LaptopCase": 28,
            "Mouse": 18,
            "Keyboard": 35,
            "Printer": 82,
            "Laptop": 250,
            "SmartWatch": 100
        }

    def test_purchase_successful(self):
        # Test a successful purchase of an item
        expected_output = "here's your USB!\nPurchase successful!\nYour remaining balance is £85"
        with self.assertRaises(SystemExit) as cm:
            shop_simulation(["USB", "exit"], self.items, 100)
        self.assertEqual(cm.exception.code, 0)
        self.assertEqual(self.output.getvalue().strip(), expected_output)

    def test_insufficient_funds(self):
        # Test when customer has insufficient funds for an item
        expected_output = "you don't have enough money for this item.\n" \
                          "Would you like to add more money to your account? Enter the amount (or 0 to exit):"
        with self.assertRaises(SystemExit) as cm:
            shop_simulation(["Laptop", "0"], self.items, 200)
        self.assertEqual(cm.exception.code, 0)
        self.assertIn(expected_output, self.output.getvalue())

    def test_invalid_item_selection(self):
        # Test when customer selects an invalid item
        expected_output = "Invalid item selected\nPlease try again."
        with self.assertRaises(SystemExit) as cm:
            shop_simulation(["InvalidItem", "exit"], self.items, 100)
        self.assertEqual(cm.exception.code, 0)
        self.assertEqual(self.output.getvalue().strip(), expected_output)

    def test_maximum_attempts_exceeded(self):
        # Test when the customer exceeds the maximum number of purchase attempts
        expected_output = "You have exceeded the maximum number of purchase attempts!\nExiting the shop."
        with self.assertRaises(SystemExit) as cm:
            shop_simulation(["Laptop", "Printer", "Keyboard"], self.items, 100)
        self.assertEqual(cm.exception.code, 0)
        self.assertEqual(self.output.getvalue().strip(), expected_output)

    def test_insufficient_funds_error_raised(self):
        # Test if InsufficientFundError is raised
        with self.assertRaises(InsufficientFundError):
            shop_simulation(["Laptop"], self.items, 0)

    def test_maximum_attempts_exceeded_error_raised(self):
        # Test if MaximumAttemptsExceededError is raised
        with self.assertRaises(MaximumAttemptsExceededError):
            shop_simulation(["Laptop", "Printer", "Keyboard"], self.items, 100)


if __name__ == "__main__":
    unittest.main()
