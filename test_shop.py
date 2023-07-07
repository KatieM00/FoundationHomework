import sys
import unittest


class Shop:
    def __init__(self):
        self.items = {
            "USB": 10,
            "Laptop": 1000,
            "Printer": 200,
            "Keyboard": 50
        }

    def shop_simulation(self, item_list, funds):
        for item in item_list:
            if item == "exit":
                sys.exit(0)
            elif item not in self.items:
                print("Invalid item selected!")
                sys.exit(1)
            elif self.items[item] > funds:
                raise InsufficientFundError("Insufficient funds!")
            else:
                print(f"Purchase successful: {item}")
                funds -= self.items[item]


class InsufficientFundError(Exception):
    pass


class MaximumAttemptsExceededError(Exception):
    pass


class ShopSimulationTestCase(unittest.TestCase):
    def setUp(self):
        self.shop = Shop()

    def test_purchase_successful(self):
        with self.assertRaises(SystemExit) as cm:
            self.shop.shop_simulation(["USB", "exit"], 100)
        self.assertEqual(cm.exception.code, 0)

    def test_insufficient_funds(self):
        with self.assertRaises(InsufficientFundError):
            self.shop.shop_simulation(["Laptop"], 10)

    def test_invalid_item_selection(self):
        with self.assertRaises(SystemExit) as cm:
            self.shop.shop_simulation(["InvalidItem", "exit"], 100)
        self.assertEqual(cm.exception.code, 1)

    def test_maximum_attempts_exceeded(self):
        with self.assertRaises(InsufficientFundError):
            self.shop.shop_simulation(["Laptop", "Printer", "Keyboard"], 100)

    def test_insufficient_funds_error_raised(self):
        with self.assertRaises(InsufficientFundError) as cm:
            self.shop.shop_simulation(["Laptop"], 100)
        self.assertEqual(str(cm.exception), "Insufficient funds!")

    def test_maximum_attempts_exceeded_error_raised(self):
        with self.assertRaises(InsufficientFundError) as cm:
            self.shop.shop_simulation(["Laptop", "Printer", "Keyboard"], 100)
        self.assertEqual(str(cm.exception), "Insufficient funds!")


if __name__ == "__main__":
    unittest.main()
