from functions import *


def draw_cli():

    def my_kitchen():
        while True:

            system('clear')
            print("(a) View all")
            print("(b) Add good")
            print("(c) Back\n\n")

            choice = input("Please make a choice: ")

            if choice == "a":
                view_all_fridge()
            elif choice == "b":
                add_good()
            elif choice == "c":
                break
            else:
                print("I don't understand your choice. Please choose again")
                sleep(1)

    def first_layer():
        while True:

            system('clear')
            print("1. My kitchen")
            print("2. View recipes")
            print("3. Make a dish")
            print("4. Exit\n\n")

            choice = input("Please make a choice: ")

            if choice == "1":
                my_kitchen()
            elif choice == "2":
                view_recipes()
            elif choice == "3":
                check_food()
            elif choice == "4":
                system('clear')
                break
            else:
                print("I don't understand your choice. Please choose again")
                sleep(1)

    first_layer()
