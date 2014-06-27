import unittest
import sql_manager


class FoodsAndDrinksTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_table()
        sql_manager.create_reservations_table()
        sql_manager.create_staff_table()
        sql_manager.insert_data_foodAndDrinks("Sandwich",
                                              "Bacon",
                                              "Bacon",
                                              5.0,
                                              2.30,
                                              20)
        sql_manager.insert_data_foodAndDrinks("Sandwich",
                                              "Cheese",
                                              "Cheese",
                                              7.1,
                                              3.10,
                                              23)
        sql_manager.make_reservation("tester", 2)

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE foodsAndDrinks')
        sql_manager.cursor.execute('DROP TABLE staff')
        sql_manager.cursor.execute('DROP TABLE reservations')

    def test_print_data(self):
        self.assertTrue(sql_manager.print_data())

    def test_insert_data(self):
        select_query = '''SELECT Count(*)
                          FROM FoodsAndDrinks
                          WHERE typeOfFood = ?'''
        sql_manager.cursor.execute(select_query, ("Sandwich",))
        items = sql_manager.cursor.fetchone()

        self.assertEqual(items[0], 2)

    def test_get_quantity_of_bacon(self):
        quantity = sql_manager.get_quantity("Bacon", "Sandwich")
        self.assertEqual(20, quantity)

    def test_get_quantity_of_cheese(self):
        quantity = sql_manager.get_quantity("Cheese", "Sandwich")
        self.assertEqual(23, quantity)

    def test_sell_bacon(self):
        sql_manager.sell_food("Bacon", "Sandwich")
        quantity = sql_manager.get_quantity("Bacon", "Sandwich")
        self.assertEqual(19, quantity)

    def test_sell_another_bacon(self):
        sql_manager.sell_food("Bacon", "Sandwich")
        sql_manager.sell_food("Bacon", "Sandwich")
        quantity = sql_manager.get_quantity("Bacon", "Sandwich")
        self.assertEqual(18, quantity)

    def test_delete_food(self):
        sql_manager.delete_food("Cheese", "Sandwich")
        sql_manager.cursor.execute("SELECT Count(*) FROM FoodsAndDrinks")
        result = sql_manager.cursor.fetchone()
        self.assertEqual(result[0], 1)

    def test_add_quantity(self):
        sql_manager.add_quantity(2)
        quantity = sql_manager.get_quantity("Bacon", "Sandwich")
        self.assertEqual(20, quantity)

    def test_decrease_rating(self):
        sql_manager.decrease_raiting(2, "Bacon", "Sandwich")
        rating = sql_manager.get_rating("Bacon", "Sandwich")
        self.assertEqual(4.9, rating)

    def test_increase_rating(self):
        sql_manager.increase_raiting(8, "Bacon", "Sandwich")
        rating = sql_manager.get_rating("Bacon", "Sandwich")
        self.assertEqual(5.1, rating)

    def test_make_reservation(self):
        select_query = '''SELECT Count(*)
                          FROM reservations
                          WHERE name = ?'''
        sql_manager.cursor.execute(select_query, ("tester",))
        number = sql_manager.cursor.fetchone()

        self.assertEqual(number[0], 1)

    def test_cancel_reservation(self):
        sql_manager.cancel_reservation("tester")
        select_query = '''SELECT Count(*)
                          FROM reservations
                          WHERE name = ?'''
        sql_manager.cursor.execute(select_query, ("tester",))
        number = sql_manager.cursor.fetchone()
        self.assertEqual(number[0], 0)

    def test_add_staff(self):
        sql_manager.add_staff("lqlq", "elka", "parola")
        sql_manager.cursor.execute("SELECT Count(*) FROM staff")
        staff_count = sql_manager.cursor.fetchone()

        self.assertEqual(1, staff_count[0])

    def test_get_staff_information(self):
        sql_manager.add_staff("lqlq", "elka", "parola")
        result = ("elka", "parola")
        self.assertEqual(
            result,
            sql_manager.get_staff_information("lqlq")
        )


if __name__ == '__main__':
    unittest.main()
