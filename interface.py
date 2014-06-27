import sql_manager


class Interface():

    def is_part_of_the_staff(self):
        name_of_the_staff = input("name: ")
        username = input("username: ")
        password = input("password: ")
        staff = sql_manager.get_staff_information(name_of_the_staff)
        return username == staff[0] and password == staff[1]

    def staff_menu(self):
        print('''* for deleting type of food - enter delete
* For adding quantity - enter add
* For adding new type of food - enter new_type
* For quiting the program - enter quit ''')

        staff_choice = input(">")

        if staff_choice == "delete":
            name = input("name of the food: ")
            type_of_food = input("the type of the food: ")
            sql_manager.delete_food(name, type_of_food)

        elif staff_choice == "add":
            quantity = input("> quantity: ")
            sql_manager.add_quantity(quantity)

        elif staff_choice == "new_type":
            name = input("name of the food: ")
            type_of_food = input("the type of the food: ")
            ingredient = input("ingredient: ")
            raiting = input("raiting: ")
            cost = input("cost: ")
            quantity = input("quantity: ")

            sql_manager.insert_data_foodAndDrinks(
                type_of_food,
                name,
                ingredient,
                raiting,
                cost,
                quantity
            )

        elif staff_choice == "quit":
            exit(0)

        else:
            print("Invalid command")

        return True

    def buyer_menu(self):
        print('''* For listing the menu - enter menu
* For listing the information for a food by id - enter by_id
* For listing food, sorted by rating - enter by_rating
* For buying food - enter buy
* For rating food - enter rate
* For paying food - enter pay
* For making a reservation - enter make_reservation
* For cancelling a reservation - enter cancel_reservation
* For exiting - enter exit
            ''')

        buyer_choice = input(">")

        if buyer_choice == "menu":
            sql_manager.print_data()

        elif buyer_choice == "by_id":
            id = input("id: ")
            sql_manager.print_data_by_id(id)

        elif buyer_choice == "by_rating":
            sql_manager.print_data_by_raiting()

        elif buyer_choice == "buy":
            name = input("Name of the food: ")
            type_of_food = input("The type of the food: ")
            sql_manager.sell_food(name, type_of_food)
            print("You just bought {} ".format(name))
            cost = sql_manager.get_cost(name)
            print("The {} {} costs {}".format(name, type_of_food, cost))

        elif buyer_choice == "rate":
            name = input("Name of the food: ")
            type_of_food = input("The type of the food: ")
            rating = float(input("Rate: "))
            if rating > 7:
                sql_manager.increase_raiting(rating, name, type_of_food)
            elif rating < 5:
                sql_manager.decrease_raiting(rating, name, type_of_food)
            print("You just rate for {}! Thank you!".format(name))

        elif buyer_choice == "pay":
            name = input("Enter the name of your food: ")
            money = float(input("Enter the money you give: "))
            price = float(sql_manager.get_cost(name))
            exchange = money - price
            print("Your exchange is {}! Have a nice day!".format(exchange))

        elif buyer_choice == "make_reservation":
            name = input("Your name is: ")
            seats = input("Number of seats: ")
            sql_manager.make_reservation(name, seats)
            print("You have a reservation for {}, for {} people".format(name,
                                                                        seats))

        elif buyer_choice == "cancel_reservation":
            name = input("Your name is: ")
            sql_manager.cancel_reservation(name)
            print("You have just cancelled your reservation!")

        elif buyer_choice == "exit":
            print("You just left! Take care! ")
            exit(0)

        else:
            print("invalid command")

        return True

    def enter(self):
        print('''Hi there! Welcome to our restaurant!,
* You are part of the staff? Type staff,
* You want to have a meal? Type guest,
* You want to leave? :( Type exit''')

        choice = input(">")

        if choice == "staff":
            if self.is_part_of_the_staff():
                while True:
                    execute = self.staff_menu()
                    if not execute:
                        break
            else:
                print("Wrong password or username!")

        elif choice == "guest":
            while True:
                execute = self.buyer_menu()
                if not execute:
                    break

        elif choice == "exit":
            print("You just left our restaurant! Take care! ")
            exit(0)
