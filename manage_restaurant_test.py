import unittest
import manage_restaurant
import sqlite3
from subprocess import call


class TestManageCompany(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect("test_employees.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE employees (id int,
                                                       name text,
                                                       monthly_salary int,
                                                       yearly_bonus int,
                                                       position text)''')
        self.employee = {
            'id': 0,
            'name': "elka",
            'monthly_salary': -100,
            'yearly_bonus': 0,
            'position': "tester"}

    def test_add_employee(self):
        manage_restaurant.add_employee(self.cursor, self.employee)
        result = self.cursor.execute("SELECT * FROM employees").fetchall()
        self.assertEqual([(0, "elka", -100, 0, "tester")], result)

    def test_list_employees_while_empty(self):
        result = manage_restaurant.list_employees(self.cursor)
        self.assertEqual("", result)

    def test_list_employees_while_not_empty(self):
        manage_restaurant.add_employee(self.cursor, self.employee)
        result = manage_restaurant.list_employees(self.cursor)
        self.assertEqual("0 - elka - tester", result)

    def test_delete_employee(self):
        manage_restaurant.add_employee(self.cursor, self.employee)
        first_count = self.cursor.execute("SELECT COUNT(*) FROM employees")
        self.assertEqual(1, first_count.fetchone()[0])
        manage_restaurant.delete_employee(self.cursor, 0)
        second_count = self.cursor.execute("SELECT COUNT(*) FROM employees")
        self.assertEqual(0, second_count.fetchone()[0])

    def test_monthly_spending(self):
        manage_restaurant.add_employee(self.cursor, self.employee)
        result = manage_restaurant.monthly_spending(self.cursor)
        self.assertEqual(-100, result)

    def test_yearly_spending(self):
        manage_restaurant.add_employee(self.cursor, self.employee)
        manage_restaurant.add_employee(self.cursor, {'id': 1, 'name': "bar",
                                                     'monthly_salary': 100,
                                                     'yearly_bonus': 1000,
                                                     'position': "foo"})

        result = manage_restaurant.yearly_spending(self.cursor)
        self.assertEqual(1000, result)

    def tearDown(self):
        self.conn.close()
        call("rm -r test_employees.db", shell=True)


if __name__ == '__main__':
    unittest.main()
