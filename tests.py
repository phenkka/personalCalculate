import unittest
from scripts import Scripts

class TestScripts(unittest.TestCase):
    def setUp(self):
        self.s = Scripts()
        self.s.add_expense(100.0, "Food", "Pizza")
        self.s.add_expense(50.0, "Transport", "Bus ticket")

    def test_add_expense(self):
        self.assertEqual(len(self.s.get_expenses()), 2)

    def test_get_total(self):
        self.assertEqual(self.s.get_total(), 150.0)

    def test_get_by_category(self):
        food_expenses = self.s.get_by_category("Food")
        self.assertEqual(food_expenses, [(100.0, "Pizza")])

    def test_clear_expenses(self):
        self.s.clear_expenses()
        self.assertEqual(self.s.get_expenses(), {})
        self.assertEqual(self.s.get_total(), 0)

if __name__ == "__main__":
    unittest.main()