import sys
import unittest

sys.path.append("..")

import foodsAndDrinksDBCreator


class DBCreatorTests(unittest.TestCase):

    def setUp(self):
        foodsAndDrinksDBCreator.create_table()
        foodsAndDrinksDBCreator.insert_data_foodAndDrinks("Tester", "test", 2, 1)
        foodsAndDrinksDBCreator.insert_data_reservations("Tester", "test", 3, 2)

    def tearDown(self):
        foodsAndDrinksDBCreator.cursor.execute('DROP TABLE foodsAndDrinks')
        foodsAndDrinksDBCreator.cursor.execute('DROP TABLE reservations')

    def testCreateTableFood(self):
        foodsAndDrinksDBCreator.insert_data_foodAndDrinks('lqlq', 'lq', 3, 2)

        foodsAndDrinksDBCreator.cursor.execute('SELECT Count(*) FROM foodsAndDrinks WHERE typeOfFood = (?) AND name = (?)', ('lqlq', 'lq'))
        users_count = foodsAndDrinksDBCreator.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def testCreateTableReservations(self):
        foodsAndDrinksDBCreator.insert_data_reservations('lqlq', 'lq', 3, 2)

        foodsAndDrinksDBCreator.cursor.execute('SELECT Count(*) FROM reservations WHERE customer = (?) AND foodName = (?)', ('lqlq', 'lq'))
        users_count = foodsAndDrinksDBCreator.cursor.fetchone()

        self.assertEqual(users_count[0], 1)


if __name__ == '__main__':
    unittest.main()
