# -*- coding: utf-8 -*-
"""Entry point for advisor app."""

from src.advisor import Advisor


if __name__ == "__main__":

    init_data = (
        "recipes.json",
        "fridge.json",
    )

    app = Advisor(init_data)
    app.run()
