from colorharmonies import Color, triadicColor
from PIL import ImageColor
import math

def build_map():
    with open("rgb.txt") as f:
        color_to_name_map = {}
        for line in f:
            name, color_hex, *_ = line.split("\t")
            color_to_name_map[ImageColor.getrgb(color_hex)] = name
        return color_to_name_map

def color_hex_to_name(color_hex):
    target_rgb = ImageColor.getrgb(color_hex)
    closest_color = find_closest_color(target_rgb, COLOR_TO_NAME_MAP.keys())
    return COLOR_TO_NAME_MAP[closest_color]

def find_closest_color(target_rgb, available_rgb_list):
    return min(available_rgb_list, key=lambda x: color_distance(x, target_rgb))

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

# Color is expected to be an array of RGB e.g [255,255,255]
def scheme_from_rgb(color):
    baseColor = Color(color, "", "")
    scheme = triadicColor(baseColor)
    scheme.append(color)
    scheme.reverse()

    return list(map(rgb_to_hex, scheme))

def color_distance(rgb1, rgb2):
    r1, b1, g1 = rgb1
    r2, b2, g2 = rgb2
    return math.hypot(r2 - r1, g2 - g1, b2 - b1)

COLOR_TO_NAME_MAP = build_map()
