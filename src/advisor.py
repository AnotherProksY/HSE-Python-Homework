"""Entry point for advisor app."""

import functions as f


class Interface:
    """Draw CLI interface."""

    def my_kitchen(self):
        """Show kitchen items."""
        while True:

            f.system('clear')
            print("(a) View all")
            print("(b) Add good")
            print("(c) Back\n\n")

            choice = input("Please make a choice: ")

            if choice == "a":
                f.view_all_fridge()
            elif choice == "b":
                f.add_good()
            elif choice == "c":
                break
            else:
                print("I don't understand your choice. Please choose again")
                f.sleep(1)


    def show_menu(self):
        """Show start screen with menu items."""
        while True:

            f.system('clear')
            print("1. My kitchen")
            print("2. View recipes")
            print("3. Make a dish")
            print("4. Exit\n\n")

            choice = input("Please make a choice: ")

            if choice == "1":
                self.my_kitchen()
            elif choice == "2":
                f.view_recipes()
            elif choice == "3":
                f.check_food()
            elif choice == "4":
                f.system('clear')
                break
            else:
                print("I don't understand your choice. Please choose again")
                f.sleep(1)


if __name__ == "__main__":
    interface = Interface()
    interface.show_menu()
