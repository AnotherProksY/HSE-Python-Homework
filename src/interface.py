# -*- coding: utf-8 -*-
"""Draw interface inside terminal."""

from os import system
from time import sleep


class Interface:
    """Draw CLI interface."""

    def __init__(self):
        """Create menu items."""
        self.main_menu = [
            "1. My kitchen",
            "2. View recipes",
            "3. Make a dish",
            "4. Exit\n\n",
        ]

        self.kitchen_menu = [
            "(a) View all",
            "(b) Add good",
            "(c) Back\n\n",
        ]

    def draw(self):
        """Draw items from menu functions and clear screen."""
        while True:

            system('clear')  # nosec


            if choice == "1":
                self.__my_kitchen()
            elif choice == "2":
                view_recipes()
            elif choice == "3":
                check_food()
            elif choice == "4":
                system('clear')  # nosec
                break
            else:
                print("I don't understand your choice. Please choose again")
                sleep(1)

    def __main_menu(self):
        """Show main menu."""
        for item in self.main_menu:
            print(item)

        print("\n\n")

        choice = input("Please make a choice: ")

    def __kitchen_menu(self):
        """Show kitchen items."""
        while True:

            system('clear')  # nosec

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
