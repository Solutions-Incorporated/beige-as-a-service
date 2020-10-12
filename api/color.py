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
