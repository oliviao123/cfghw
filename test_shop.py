import unittest
from shop import select_item, purchase_item, add_money, NotEnoughMoneyError, MaximumAttemptsExceededError


class TestShop(unittest.TestCase):

    def test_select_item(self):
        self.assertEqual(select_item("item1"), 50)
        self.assertEqual(select_item("item2"), 100)
        self.assertEqual(select_item("item3"), 150)
        with self.assertRaises(KeyError):
            select_item("item4")

    def test_purchase_item(self):
        self.assertEqual(purchase_item(100, 50), 50)
        with self.assertRaises(NotEnoughMoneyError):
            purchase_item(50, 100)

    def test_add_money(self):
        self.assertEqual(add_money(100), 150)

    def test_not_enough_money_error(self):
        with self.assertRaises(NotEnoughMoneyError):
            raise NotEnoughMoneyError("Not enough money")

    def test_maximum_attempts_exceeded_error(self):
        with self.assertRaises(MaximumAttemptsExceededError):
            raise MaximumAttemptsExceededError("Maximum attempts exceeded")


if __name__ == '__main__':
    unittest.main()