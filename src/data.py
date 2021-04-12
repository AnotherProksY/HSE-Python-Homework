# -*- coding: utf-8 -*-
"""Dishes list and fridge items."""

import json
import re


class Data:
    """Get data from specified file."""

    def __init__(self, filename):
        """Specify filename to process."""
        self.filename = filename
        self.__load()

    def __load(self):
        """Load JSON file."""
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.data = json.load(file)


class Fridge(Data):
    """Manipulate with fridge."""

    def show_items(self):
        """Open fridge and show what's inside it."""
        return self.data

    def add_item(self, item, amount):
        """Add new item to fridge."""
        with open(self.filename, 'w') as json_file:

            if item in self.data:
                self.data[item] += amount
            else:
                self.data[item] = amount

            json.dump(self.data, json_file, indent=4)

    def add_good(self):
        """Add new item to fridge."""
        # Food name
        while True:
            system('clear')  # nosec
            new_item_name = input("Add new good: ")
            if not re.search(r'\d', new_item_name):
                break
            else:
                print("I don't understand your input. Please write again")
                sleep(1)

        # Food quantity
        while True:
            system('clear')  # nosec
            try:
                new_item_quantity = int(input("Add quantity for this item: "))
                break
            except ValueError:
                print("I don't understand your input. Please write again")
                sleep(1)

        # Add to fridge
        fridge.add_item(new_item_name, new_item_quantity)

        print(f'\nItem {new_item_name} was added to your fridge in amount of {new_item_quantity}')
        sleep(2)

    def remove_item(self, item, amount):
        """Remove item from fridge."""
        with open(self.filename, 'w') as json_file:

            left = self.data[item] - amount
            if left > 0:
                self.data[item] -= amount
            else:
                del self.data[item]

            json.dump(self.data, json_file, indent=4)

    def view_all_fridge(self):
        """Show all items in fridge."""
        while True:
            system('clear')  # nosec

            all_items = fridge.show_items()

            for food in all_items:
                print(f'Food: {food}\nAmount: {all_items[food]}\n')

            try:
                exit_status = input("To go back write 'b': ")

                if exit_status == 'b':
                    system('clear')  # nosec
                    break
                else:
                    raise ValueError

            except (ValueError):
                print("I don't understand your input. Please write again")
                sleep(1)


class Recipes(Data):
    """Show all dishes."""

    def get(self):
        """Get all available dishes."""
        return self.data

    def check_food(self):
        """Show available dishes."""
        dish_index = 0
        available_dish_list = {}
        fridge_goods = fridge.show_items()

        while True:
            system('clear')  # nosec

            all_dishes = dishes.get()

            for dish in all_dishes:
                recipes = all_dishes[dish][1]

                condition = [
                    food
                    for food in fridge_goods
                    if food in recipes.keys()
                    and recipes[food] <= fridge_goods[food]
                ]

                if len(recipes) == len(condition):
                    dish_index += 1
                    available_dish_list[dish_index] = dish
                    print(f'{dish_index}. {dish}\n')

            if not available_dish_list:
                print("There's no available dishes for you")
                sleep(1)
                break

            try:
                dish_choice_index = input("To cook, write correct dish number.\nTo go back, write 'b': ")

                if dish_choice_index != 'b':
                    dish_choice_index = int(dish_choice_index)
                    choosed_dish = available_dish_list[dish_choice_index]

                    for ingredient in all_dishes[choosed_dish][1]:
                        fridge.remove_item(ingredient, all_dishes[choosed_dish][1][ingredient])

                    print('Done !')
                    sleep(1)
                else:
                    break

            except (ValueError, IndexError, KeyError):
                print("I don't understand your input. Please write again")
                sleep(1)

            dish_index = 0
            available_dish_list.clear()

    def view_recipes(self):
        """Show all recipes."""
        all_dishes = dishes.get()

        toggle_view = [False for _ in range(len(all_dishes))]

        while True:
            system('clear')  # nosec

            for idx, dish in enumerate(all_dishes):
                if toggle_view[idx] is False:
                    print(f'{idx+1}. "{dish}"\n')
                else:
                    print(f'{idx+1}. "{dish}":\n---\nDifficulty of preparation -> {all_dishes[dish][0]}\nIngredients for this dish:\n\t{all_dishes[dish][1]}\n---\n')

            print('\n')
            try:
                detail_view = input("To show or hide recipe, write correct dish number.\nTo go back write 'b': ")

                if detail_view != 'b':
                    detail_view = int(detail_view)
                    if toggle_view[detail_view - 1] is False:
                        toggle_view[detail_view - 1] = True
                    else:
                        toggle_view[detail_view - 1] = False
                else:
                    break

            except (ValueError, IndexError):
                print("I don't understand your input. Please write again")
                sleep(1)
