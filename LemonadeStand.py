'''
Author: Mike Crozier
github: crozierman
date: 01/15/2024
Program to create and store inventory, track sales by item and amount sold, and find profit made from each item per day
'''

class InvalidSalesItemError(Exception):
    pass


class MenuItem:

    def __init__(self, item_name, cost, price):
        self._item_name = item_name
        self._cost = cost
        self._price = price

    def get_name(self):
        return self._item_name

    def get_wholesale_cost(self):
        return self._cost

    def get_selling_price(self):
        return self._price


class SalesForDay:

    def __init__(self, number_of_days, sales_dictionary):
        self.number_of_days = number_of_days
        self.sales_dictionary = sales_dictionary

    def get_number_of_days(self):
        return self.number_of_days

    def get_sales_dictionary(self):
        return self.sales_dictionary


class LemonadeStand:

    def __init__(self, name):
        self.name = name
        self.current_day = 0
        self._menu = {}
        self.sales_record = []

    def get_name(self):
        return self.name

    def add_menu_item(self, new_item):
        self._menu[new_item.get_name()] = new_item

    def enter_sales_for_today(self, sales_dictionary):
        try:
            self.current_day += 1
            sales_for_day = SalesForDay(self.current_day, sales_dictionary)
            self.sales_record.append(sales_for_day)
        except InvalidSalesItemError:
            raise InvalidSalesItemError


    def sales_of_menu_item_for_day(self, current_day, item_name):
        for sales_for_day in self.sales_record:
            if sales_for_day.get_day() == current_day:
                sales_dictionary = sales_for_day.get_sales_dictionary()
                return sales_dictionary.get(item_name, 0)
        # return 0

    def total_sales_for_menu_item(self, item_name):
        total_sales = 0
        for sales_for_day in self.sales_record:
            sales_dictionary = sales_for_day.get_sales_dictionary()
            total_sales += sales_dictionary.get(item_name, 0)
        return total_sales

    def total_profit_for_menu_item(self, item_name):
        total_profit = 0
        for sales_for_day in self.sales_record:
            sales_dictionary = sales_for_day.get_sales_dictionary()
            quantity_sold = sales_dictionary.get(item_name, 0)
            menu_item = self._menu.get(item_name)
            if menu_item:
                total_profit += quantity_sold * (menu_item.get_selling_price() - menu_item.get_wholesale_cost())
            return total_profit

    def total_profit_for_stand(self):
        total_profit = 0
        for item_name in self._menu:
            total_profit += self.total_profit_for_menu_item(item_name)
        return total_profit


