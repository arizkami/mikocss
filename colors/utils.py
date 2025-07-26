import colorsys


def hex_to_rgb(hex_str):
    """Convert hex color to RGB tuple (0-1 range)"""
    hex_str = hex_str.lstrip("#")
    return tuple(int(hex_str[i : i + 2], 16) / 255.0 for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    """Convert RGB tuple (0-1 range) to hex string"""
    return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))
