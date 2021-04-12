# -*- coding: utf-8 -*-
"""Main logic of advisor app."""

from interface import Interface
from data import Fridge, Recipes


class Advisor:
    """Main app for managing data and user interaction."""

    def __init__(self, files) -> None:
        """Unpack data from tuple and create objects."""
        # Assume that you pass a tuple of filenames
        self.recipes_file = files[0]
        self.fridge_file = files[1]

        self.recipes = Recipes(self.recipes_file)
        self.fridge = Fridge(self.fridge_file)

    def run(self):
        """."""
        pass


# interface = Interface()
# interface.draw()
