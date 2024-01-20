import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand, InvalidSalesItemError


class TestStoreName(unittest.TestCase):

    def test_menu_1(self):
        stand = "The Best Lemonade Stand"
        result = LemonadeStand(stand)
        self.assertEqual(LemonadeStand.get_name(result), "The Best Lemonade Stand")

    def test_menu_2(self):
        """ test made to fail Menu Item test to ensure true and false were accounted for"""
        print("This test was made to fail")
        stand = "Lemmony Aiddicts"
        result = LemonadeStand(stand)
        self.assertEqual(LemonadeStand.get_name(result), "Not the store name you are looking for")

    def test_menu_3(self):
        stand = "Lemons for Aide"
        result = LemonadeStand(stand)
        self.assertEqual(LemonadeStand.get_name(result), "Lemons for Aide")


class TestMenuItem(unittest.TestCase):

    def test_item_1(self):
        item = MenuItem("deconstructed lemons", 5, 10)
        self.assertEqual(MenuItem.get_name(item), "deconstructed lemons")
        self.assertEqual(MenuItem.get_wholesale_cost(item), 5)
        self.assertEqual(MenuItem.get_selling_price(item), 10)

    def test_item_2(self):
        """ test made to fail Menu Item test to ensure true and false were accounted for"""
        print("This test was made to fail")
        item = MenuItem("God's gift: Lemons", 50, 1)
        self.assertEqual(MenuItem.get_name(item), "Lemonade")
        self.assertEqual(MenuItem.get_wholesale_cost(item), 50)
        self.assertEqual(MenuItem.get_selling_price(item), 1)


    def test_item_3(self):
        item = MenuItem("Lemonade", .50, 2)
        self.assertEqual(MenuItem.get_name(item), "Lemonade")
        self.assertEqual(MenuItem.get_wholesale_cost(item), .50)
        self.assertEqual(MenuItem.get_selling_price(item), 2)


class TestSalesForDay(unittest.TestCase):

    def test_sales_1(self):
        day_1_sales = {
            "Le mon aide": 4,
            "Lee maj aide": 10,
            "Les more aide": 2
        }
        result = SalesForDay(1, day_1_sales)
        self.assertDictEqual(day_1_sales, SalesForDay.get_sales_dictionary(result))

    def test_sales_2(self):
        """ test made to fail Menu Item test to ensure true and false were accounted for"""
        print("This test was made to fail")
        day_45_sales = {
            "Lemons": 6,
            "Cookies": 11,
            "Pretzels": 8
        }
        day_16_sales = {
            "cupcakes": 9,
            "cranberry juice": 4,
            "Graham Crackers": 6
        }
        result = SalesForDay(1, day_45_sales)
        self.assertDictEqual(day_16_sales, SalesForDay.get_sales_dictionary(result))


def main():

        stand = LemonadeStand('Dragons Rest')
        item1 = MenuItem('Fire Lemonade', 1.50, 10)
        stand.add_menu_item(item1)
        item2 = MenuItem('Ice Berries', 2.00, 15)
        stand.add_menu_item(item2)
        item3 = MenuItem('Elixir of Sour', 5, 25)
        stand.add_menu_item(item3)

        day_0_sales = {
            'Fire Lemonade': 3,
            'Ice Berries': 5,
            'Elxir of Sour': 1
        }
        stand.enter_sales_for_today(day_0_sales)

        print(f"our profit for Fire Lemonade is = {stand.total_profit_for_menu_item('Fire Lemonade')}")
        print(LemonadeStand.get_name(stand))


if __name__ == "__main__":
    LemonadeStand.main()
