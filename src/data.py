"""Dishes list and fridge items."""

import json


class LoadJson:
    """Get data from JSON."""

    def __init__(self, filename):
        """Specify filename to process."""
        self.filename = filename
        self.__load()

    def __load(self):
        """Load JSON file."""
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def show_json(self):
        """Print out JSON data."""
        print(json.dumps(self.data, indent=4))


class Fridge(LoadJson):
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

    def remove_item(self, item, amount):
        """Remove item from fridge."""
        with open(self.filename, 'w') as json_file:

            left = self.data[item] - amount
            if left > 0:
                self.data[item] -= amount
            else:
                del self.data[item]

            json.dump(self.data, json_file, indent=4)


class Dishes(LoadJson):
    """Show all dishes."""

    def get(self):
        """Get all available dishes."""
        return self.data


dishes = Dishes("../data/recipes.json")
fridge = Fridge("../data/fridge.json")
