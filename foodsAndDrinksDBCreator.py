import sqlite3


conn = sqlite3.connect('restaurantDB.db')
cursor = conn.cursor()


def create_table():
    cursor.execute("CREATE TABLE foodsAndDrinks (ID INTEGER PRIMARY KEY, typeOfFood TEXT, name TEXT, rating INT, cost INT)")
    cursor.execute("CREATE TABLE reservations (ID INTEGER PRIMARY KEY, customer TEXT, foodName TEXT, row INT, column INT)")


def insert_data_foodAndDrinks(typeOfFood, name, rating, cost):
    insert_sql = "INSERT INTO foodsAndDrinks (typeOfFood, name, rating, cost) VALUES (?, ?, ?, ?)"
    cursor.execute(insert_sql, (typeOfFood, name, rating, cost))

    conn.commit()


def insert_data_reservations(customer, foodName, row, column):
    insert_sql = "INSERT INTO reservations (customer, foodName, row, column) VALUES (?, ?, ?, ?)"
    cursor.execute(insert_sql, (customer, foodName, row, column))

    conn.commit()


def main():
    create_table()
    insert_data_foodAndDrinks("fruit", "banana", 6, 2)
    insert_data_reservations("Eli", "banana", 1, 1)

if __name__ == '__main__':
    main()
