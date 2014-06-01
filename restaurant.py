import sqlite3
from foodsAndDrinksDBCreator import insert_data_reservations


class ReservationSystem():

    def __init__(self):

        self.conn = sqlite3.connect('restaurantDB.db')
        self.c = self.conn.cursor()

    def show(self):

        print('')
        print("Foods and Drinks: ")

        sql_to_read = "SELECT ID, typeOfFood, name, rating, cost FROM foodsAndDrinks"
        for row in self.c.execute(sql_to_read):
            print("[{}] - {} ({})".format(row[0], row[1], row[2], row[3], row[4]))

        return ""

    def show_by_rating(self):

        print('')
        print("Foods and drinks by rating: ")

        sql_to_read = "SELECT ID, typeOfFood, name, rating, cost FROM foodsAndDrinks ORDER BY rating ASC"
        for row in self.c.execute(sql_to_read):
            print("[{}] - {} ({})".format(row[0], row[1], row[2], row[3], row[4]))
            print('')

        return ""

    def make_reservation(self):

        print('')
        print("Step 1")
        customer_name = input("Choose name>")
        self.show()

        print('')
        print("Step 2")
        choose_food = input("Choose a food or drink>")

        seats = [
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

        print('')
        print("Available seats marked with 0s")
        print(' ' + ' ' + '1 2 3 4 5 6 7 8 9 10')

        index = 1
        for i in seats:
            print("{} ".format(index) + " ".join(i))
            index += 1
        print("")

        choosen_seats = []

        print('Please choose your seat:')
        choose_seat_row = int(input('Choose row>'))
        choose_seat_num = int(input('Choose seat number>'))
        choosen_seats.append((choose_seat_row, choose_seat_num))
        if (choose_seat_row) < 11 or (choose_seat_num) < 11:

            if seats[(choose_seat_row) - 1][(choose_seat_num) - 1] == "X":
                print('This seat sis already taken!')

            else:
                seats[(choose_seat_row) - 1][(choose_seat_num) - 1] = "X"
        else:
            print('Try again! ')

        print('')
        print('This is your reservation: ')
        print('Reservation under the name of {}'.format(customer_name))
        print('Seats: {}'.format(choosen_seats))

        insert_data_reservations(customer_name, choose_food, choose_seat_row, choose_seat_num)

        return "Thank you! See you soon!"
