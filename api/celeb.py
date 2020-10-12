import random
import re

BORING_COLOURS = [
    "red",
    "blue",
    "green",
    "yellow",
    "pink",
    "orange",
    "purple",
    "white",
]

def load_names():
    with open("famous_names.txt") as f:
        names = []
        for line in f:
            _, name, *_ = line.split(",")
            names.append(name)
        return names

def remove_boring_part(color_name):
    name = random.choice(NAMES).rstrip()
    for color in BORING_COLOURS:
        new_color = color_name.replace(color, name)

        if new_color != color_name:
           return new_color

    return color_name

NAMES = load_names()
