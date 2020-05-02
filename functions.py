from data import fridge, dishes
from os import system
from time import sleep
import re


def check_food():
    dish_index = 0
    available_dish_list = {}

    exit_condition = False
    while not exit_condition:
        system('clear')
        for dish in dishes:
            recipes = dishes[dish][1]

            condition = [food for food in fridge if food in recipes.keys() and recipes[food] <= fridge[food]]

            if len(recipes) == len(condition):
                dish_index += 1
                available_dish_list[dish_index] = dish
                print(f'{dish_index}. {dish}\n')

        if not available_dish_list:
            print("There's no available dishes for you")
            sleep(1)
            break

        try:
            dish_choice_index = input(
                """To cook, write correct dish number. To go back write 'b': """
            )

            if dish_choice_index != 'b':
                dish_choice_index = int(dish_choice_index)
                choosed_dish = available_dish_list[dish_choice_index]

                for ingredient in dishes[choosed_dish][1]:
                    fridge[ingredient] -= dishes[choosed_dish][1][ingredient]

                print(f'Done !')
                sleep(1)
            else:
                exit_condition = True

        except (ValueError, IndexError, KeyError):
            print("I don't understand your input. Please write again")
            sleep(1)

        dish_index = 0
        available_dish_list.clear()


def view_all_fridge():
    exit_condition = False
    while not exit_condition:
        system('clear')
        for food in fridge:
            print(f'Food: {food}\nAmount: {fridge[food]}\n')

        try:
            exit_status = input("To go back write 'b': ")

            if exit_status == 'b':
                system('clear')
                break
            else:
                raise ValueError

        except (ValueError):
            print("I don't understand your input. Please write again")
            sleep(1)


def add_good():
    # Food name
    new_item_name_check = False
    while not new_item_name_check:
        system('clear')
        new_item_name = input("Add new good: ")
        if not re.search(r'\d', new_item_name):
            new_item_name_check = True
        else:
            print("I don't understand your input. Please write again")
            sleep(1)

    # Food quantity
    new_item_quantity_check = False
    while not new_item_quantity_check:
        system('clear')
        try:
            new_item_quantity = int(input("Add quantity for this item: "))
            new_item_quantity_check = True
        except ValueError:
            print("I don't understand your input. Please write again")
            sleep(1)

    # Add to fridge
    if new_item_name in fridge.keys():
        fridge[new_item_name] += new_item_quantity
    else:
        fridge[new_item_name] = new_item_quantity

    print(f'\nItem {new_item_name} was added to your fridge in amount of {new_item_quantity}')
    sleep(2)


def view_recipes():
    toggle_view = [False, False, False]

    exit_condition = False
    while not exit_condition:
        system('clear')

        for idx, dish in enumerate(dishes):
            if toggle_view[idx] is False:
                print(f'{idx+1}. Dish name: "{dish}"\n')
            else:
                print(f'{idx+1}. Dish name: "{dish}"\nDifficulty of preparation -> {dishes[dish][0]}\nIngredients for this dish:\n  {dishes[dish][1]}\n')

        print('\n')
        try:
            detail_view = input("To show or hide recipe, write correct dish number. To go back write 'b': ")

            if detail_view != 'b':
                detail_view = int(detail_view)
                if toggle_view[detail_view - 1] is False:
                    toggle_view[detail_view - 1] = True
                else:
                    toggle_view[detail_view - 1] = False
            else:
                exit_condition = True

        except (ValueError, IndexError):
            print("I don't understand your input. Please write again")
            sleep(1)
