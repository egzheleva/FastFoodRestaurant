import sqlite3


conn = sqlite3.connect('restaurantDB.db')
cursor = conn.cursor()


def create_table():
    create_first_query = '''CREATE TABLE if not exists
        foodsAndDrinks (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        typeOfFood TEXT,
                        name TEXT,
                        ingredient TEXT,
                        rating INT,
                        cost INT,
                        quantity INT)'''

    cursor.execute(create_first_query)


def print_data():
    select_query = '''SELECT id, typeOfFood, name, ingredient, rating, cost
                      FROM foodsAndDrinks'''
    print("[id] - typeOfFood | name | ingredient | rating | cost")
    for row in cursor.execute(select_query):
        print("[{}] - {} | {} | {} | {} | {}".format(row[0],
                                                     row[1],
                                                     row[2],
                                                     row[3],
                                                     row[4],
                                                     row[5]))
    return True


def print_data_by_raiting():
    select_query = '''SELECT id, typeOfFood, name, ingredient, rating, cost
                      FROM foodsAndDrinks
                      ORDER BY rating ASC'''
    print("[id] - typeOfFood | name | ingredient | rating | cost")
    for row in cursor.execute(select_query):
        print("[{}] - {} | {} | {} | {} | {}".format(row[0],
                                                     row[1],
                                                     row[2],
                                                     row[3],
                                                     row[4],
                                                     row[5]))


def print_data_by_id(id):
    select_query = """SELECT * FROM foodsAndDrinks WHERE id = ? """
    result = cursor.execute(select_query, (id, )).fetchone()
    if result:
        print(result)
        return True
    else:
        return False


def increase_raiting(rating, name, typeOfFood):
    update_query = '''UPDATE foodsAndDrinks
                      SET rating = ?
                      WHERE name = ?
                      AND typeOfFood = ?'''
    cursor.execute(update_query,
                  (get_rating(name, typeOfFood) + 0.1,
                   name,
                   typeOfFood)
                   )
    return get_rating(name, typeOfFood)
    conn.commit()


def decrease_raiting(rating, name, typeOfFood):
    update_query = '''UPDATE foodsAndDrinks
                      SET rating = ?
                      WHERE name = ?
                      AND typeOfFood = ?'''
    cursor.execute(update_query,
                  (get_rating(name, typeOfFood) - 0.1,
                   name,
                   typeOfFood)
                   )
    return get_rating(name, typeOfFood)
    conn.commit()


def insert_data_foodAndDrinks(typeOfFood,
                              name,
                              ingredient,
                              rating,
                              cost,
                              quantity
                              ):
    insert_query = '''INSERT into foodsAndDrinks
                   (typeOfFood, name, ingredient, rating, cost, quantity)
                   values (?, ?, ?, ?, ?, ?)'''

    cursor.execute(
        insert_query,
        (typeOfFood, name, ingredient, rating, cost, quantity)
    )
    conn.commit()


def sell_food(name, typeOfFood):
    update_query = '''UPDATE foodsAndDrinks
                      SET quantity = ?
                      WHERE name = ?
                      AND typeOfFood = ?'''
    cursor.execute(update_query,
                  (get_quantity(name, typeOfFood) - 1,
                   name,
                   typeOfFood)
                   )
    conn.commit()


def delete_food(name, typeOfFood):
    delete_query = '''DELETE FROM foodsAndDrinks
                      WHERE name = ?
                      AND typeOfFood = ? '''
    cursor.execute(delete_query, (name, typeOfFood))
    conn.commit()


def get_quantity(name, typeOfFood):
    select_query = '''SELECT quantity FROM foodsAndDrinks
                      WHERE name = ? AND typeOfFood = ?'''
    cursor.execute(select_query, (name, typeOfFood))
    quantity = cursor.fetchone()
    return quantity[0]


def get_rating(name, typeOfFood):
    select_query = '''SELECT rating FROM foodsAndDrinks
                      WHERE name = ? AND typeOfFood = ?'''
    cursor.execute(select_query, (name, typeOfFood))
    rating = cursor.fetchone()
    return rating[0]


def get_cost(name):
    select_query = '''SELECT cost
                      FROM foodsAndDrinks
                      WHERE name = ?'''
    cursor.execute(select_query, (name, ))
    price = cursor.fetchone()
    return price[0]


def add_quantity(quantity):
    update_query = "UPDATE foodsAndDrinks SET quantity = ? WHERE quantity = 0"
    cursor.execute(update_query, (quantity, ))
    conn.commit()


def create_reservations_table():
    create_query = ''' CREATE TABLE if not exists
        reservations(name TEXT,
                     number_of_seats INT)'''
    cursor.execute(create_query)


def make_reservation(name, seats):
    insert_query = '''INSERT into reservations
                   (name, number_of_seats)
                   values (?, ?)'''

    cursor.execute(
        insert_query,
        (name, seats)
    )
    conn.commit()


def cancel_reservation(name):
    delete_query = '''DELETE FROM reservations
                      WHERE name = ?'''
    cursor.execute(delete_query, (name,))
    conn.commit()


def create_staff_table():
    create_query = '''CREATE TABLE if not exists
        staff(name TEXT,
              username TEXT,
              password TEXT)'''

    cursor.execute(create_query)


def get_staff_information(name):
    select_query = 'SELECT username, password FROM staff WHERE name = ?'
    result = cursor.execute(select_query, (name, )).fetchone()
    return result


def add_staff(name, username, password):
    insert_query = '''INSERT into staff (name, username, password)
                      values (?, ?, ?)'''
    cursor.execute(insert_query, (name, username, password))
    conn.commit()


def main():
    create_table()
    create_staff_table()
    create_reservations_table()
    add_staff("test", "test", "parola")
    foods = [("Vegetable salad",
              "Acar",
              "Yardlong beans,carrots and cabbage",
              7.0,
              2.50,
              10
              ),
             ("Pasta salad",
              "Agrigento Salad",
              "tomatoes, peppers, artichokes, mushrooms, and Kalamata Olives",
              6,
              3.00,
              13
              ),
             ("Fruit salad",
              "Ambrosia",
              "marshmallows,pineapple, mandarin oranges and coconut",
              5.7,
              3.40,
              12
              ),
             ("Vegetable salad",
              "Arab salads",
              "Combines many different vegetables and spices",
              8.75,
              3.40,
              13
              ),
             ("Meat salad",
              "Antipasto",
              "Italian salami,Italian cheese, olives, Italian dressing",
              6.5,
              4.30,
              8
              ),
             ("Sandwich", "Bacon", "Bacon!", 7, 2.35, 21),
             ("Sandwich",
              "Bacon, egg and cheese",
              "Bacon, eggs and cheese",
              6,
              4.20,
              15
              ),
             ("Sandwich",
              "Butterbrot",
              "Single, open-faced, containing butter, sweet or savory topping",
              6,
              3.80,
              7
              ),
             ("Sandwich",
              "Cheese",
              "Butter and cheese",
              8,
              2.50,
              22
              ),
             ("Cake",
              "Apple cake",
              "Apple and nuts",
              5.5,
              3.10,
              16
              ),
             ("Cake", "Angel cake", "Sponge cake, cream", 8.1, 4.10, 12),
             ("Cake", "Banana", "Nuts and chocolate", 5.5, 3.10, 23),
             ("Cake",
              "Banoffee pie",
              "Bananas, toffee, biscuits",
              5.7,
              3.10,
              4
              ),
             ("Cake", "Battenberg cake", "Marzipan, apricot jam", 6, 3.10, 12),
             ("Cake",
              "Bara brith",
              "Raisins,currants and candied peel",
              5.5,
              3.10,
              14
              ),
             ("Juice", "Orange juice", "Oranges", 5.5, 3.10, 43)
             ]

    for food in foods:
        insert_data_foodAndDrinks(*food)

    conn.close()

if __name__ == '__main__':
    main()
