# Spacing scale (Tailwind-inspired)
spacing_scale = {
    "0": "0px",
    "px": "1px",
    "0_5": "0.125rem",
    "1": "0.25rem",
    "1_5": "0.375rem",
    "2": "0.5rem",
    "2_5": "0.625rem",
    "3": "0.75rem",
    "3_5": "0.875rem",
    "4": "1rem",
    "5": "1.25rem",
    "6": "1.5rem",
    "7": "1.75rem",
    "8": "2rem",
    "9": "2.25rem",
    "10": "2.5rem",
    "11": "2.75rem",
    "12": "3rem",
    "14": "3.5rem",
    "16": "4rem",
    "20": "5rem",
    "24": "6rem",
    "28": "7rem",
    "32": "8rem",
    "36": "9rem",
    "40": "10rem",
    "44": "11rem",
    "48": "12rem",
    "52": "13rem",
    "56": "14rem",
    "60": "15rem",
    "64": "16rem",
    "72": "18rem",
    "80": "20rem",
    "96": "24rem",
    "auto": "auto"
}

# Padding utilities
padding = {
    # All sides
    **{f"p_{k}": v for k, v in spacing_scale.items()},
    # Horizontal (left + right)
    **{f"px_{k}": v for k, v in spacing_scale.items()},
    # Vertical (top + bottom)
    **{f"py_{k}": v for k, v in spacing_scale.items()},
    # Individual sides
    **{f"pt_{k}": v for k, v in spacing_scale.items()},  # top
    **{f"pr_{k}": v for k, v in spacing_scale.items()},  # right
    **{f"pb_{k}": v for k, v in spacing_scale.items()},  # bottom
    **{f"pl_{k}": v for k, v in spacing_scale.items()},  # left
    # Start/End (logical properties)
    **{f"ps_{k}": v for k, v in spacing_scale.items()},  # start
    **{f"pe_{k}": v for k, v in spacing_scale.items()},  # end
}

# Margin utilities
margin = {
    # All sides
    **{f"m_{k}": v for k, v in spacing_scale.items()},
    # Horizontal (left + right)
    **{f"mx_{k}": v for k, v in spacing_scale.items()},
    # Vertical (top + bottom)
    **{f"my_{k}": v for k, v in spacing_scale.items()},
    # Individual sides
    **{f"mt_{k}": v for k, v in spacing_scale.items()},  # top
    **{f"mr_{k}": v for k, v in spacing_scale.items()},  # right
    **{f"mb_{k}": v for k, v in spacing_scale.items()},  # bottom
    **{f"ml_{k}": v for k, v in spacing_scale.items()},  # left
    # Start/End (logical properties)
    **{f"ms_{k}": v for k, v in spacing_scale.items()},  # start
    **{f"me_{k}": v for k, v in spacing_scale.items()},  # end
    # Negative margins
    **{f"-m_{k}": f"-{v}" for k, v in spacing_scale.items() if k != "auto"},
    **{f"-mx_{k}": f"-{v}" for k, v in spacing_scale.items() if k != "auto"},
    **{f"-my_{k}": f"-{v}" for k, v in spacing_scale.items() if k != "auto"},
    **{f"-mt_{k}": f"-{v}" for k, v in spacing_scale.items() if k != "auto"},
    **{f"-mr_{k}": f"-{v}" for k, v in spacing_scale.items() if k != "auto"},
    **{f"-mb_{k}": f"-{v}" for k, v in spacing_scale.items() if k != "auto"},
    **{f"-ml_{k}": f"-{v}" for k, v in spacing_scale.items() if k != "auto"},
    **{f"-ms_{k}": f"-{v}" for k, v in spacing_scale.items() if k != "auto"},
    **{f"-me_{k}": f"-{v}" for k, v in spacing_scale.items() if k != "auto"},
}

# Space between utilities (for flex/grid children)
space_between = {
    **{f"space_x_{k}": v for k, v in spacing_scale.items()},
    **{f"space_y_{k}": v for k, v in spacing_scale.items()},
    **{f"-space_x_{k}": f"-{v}" for k, v in spacing_scale.items() if k != "auto"},
    **{f"-space_y_{k}": f"-{v}" for k, v in spacing_scale.items() if k != "auto"},
}