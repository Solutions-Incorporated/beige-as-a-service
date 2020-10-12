from colorharmonies import Color, triadicColor

def build_map():
    with open("rgb.txt") as f:
        color_to_name_map = {}
        for line in f:
            name, rgb, *_ = line.split("\t")
            color_to_name_map[rgb.upper()] = name
        return color_to_name_map

COLOR_TO_NAME_MAP = build_map()

def rgb_to_name(rgb):
    return COLOR_TO_NAME_MAP.get(rgb.upper(), 'beige')

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


# Color is expected to be an array of RGB e.g [255,255,255]
def scheme_from_rgb(color):
    baseColor = Color(color, "", "")
    scheme = triadicColor(baseColor)
    scheme.append(color)
    scheme.reverse()

    return list(map(rgb_to_hex, scheme))
