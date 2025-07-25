# Text size definitions (Tailwind-inspired)
text_sizes = {
    "xs": {"font_size": "0.75rem", "line_height": "1rem"},
    "sm": {"font_size": "0.875rem", "line_height": "1.25rem"},
    "base": {"font_size": "1rem", "line_height": "1.5rem"},
    "lg": {"font_size": "1.125rem", "line_height": "1.75rem"},
    "xl": {"font_size": "1.25rem", "line_height": "1.75rem"},
    "2xl": {"font_size": "1.5rem", "line_height": "2rem"},
    "3xl": {"font_size": "1.875rem", "line_height": "2.25rem"},
    "4xl": {"font_size": "2.25rem", "line_height": "2.5rem"},
    "5xl": {"font_size": "3rem", "line_height": "1"},
    "6xl": {"font_size": "3.75rem", "line_height": "1"},
    "7xl": {"font_size": "4.5rem", "line_height": "1"},
    "8xl": {"font_size": "6rem", "line_height": "1"},
    "9xl": {"font_size": "8rem", "line_height": "1"}
}

# Font weight definitions
font_weights = {
    "thin": 100,
    "extralight": 200,
    "light": 300,
    "semilight": 350,
    "regular": 400,
    "medium": 500,
    "semibold": 600,
    "bold": 700,
    "extrabold": 800,
    "black": 900,
    "blackrr": 950  # Extra black variant
}

# Additional typography utilities
# Font family utilities (expanded)
font_families = {
    "sans": ["ui-sans-serif", "system-ui", "sans-serif"],
    "serif": ["ui-serif", "Georgia", "serif"],
    "mono": ["ui-monospace", "SFMono-Regular", "monospace"],
    "display": ["ui-serif", "Georgia", "serif"],
    "body": ["ui-sans-serif", "system-ui", "sans-serif"]
}

# Font size utilities (expanded with pixel values)
font_sizes = {
    "xs": {"font_size": "0.75rem", "font_size_px": 12, "line_height": "1rem"},
    "sm": {"font_size": "0.875rem", "font_size_px": 14, "line_height": "1.25rem"},
    "base": {"font_size": "1rem", "font_size_px": 16, "line_height": "1.5rem"},
    "lg": {"font_size": "1.125rem", "font_size_px": 18, "line_height": "1.75rem"},
    "xl": {"font_size": "1.25rem", "font_size_px": 20, "line_height": "1.75rem"},
    "2xl": {"font_size": "1.5rem", "font_size_px": 24, "line_height": "2rem"},
    "3xl": {"font_size": "1.875rem", "font_size_px": 30, "line_height": "2.25rem"},
    "4xl": {"font_size": "2.25rem", "font_size_px": 36, "line_height": "2.5rem"},
    "5xl": {"font_size": "3rem", "font_size_px": 48, "line_height": "1"},
    "6xl": {"font_size": "3.75rem", "font_size_px": 60, "line_height": "1"},
    "7xl": {"font_size": "4.5rem", "font_size_px": 72, "line_height": "1"},
    "8xl": {"font_size": "6rem", "font_size_px": 96, "line_height": "1"},
    "9xl": {"font_size": "8rem", "font_size_px": 128, "line_height": "1"}
}

# Font smoothing utilities
font_smoothing = {
    "antialiased": "-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale",
    "subpixel_antialiased": "-webkit-font-smoothing: auto; -moz-osx-font-smoothing: auto"
}

# Font style utilities
font_style = {
    "italic": "italic",
    "not_italic": "normal"
}

# Font stretch utilities
font_stretch = {
    "ultra_condensed": "ultra-condensed",
    "extra_condensed": "extra-condensed",
    "condensed": "condensed",
    "semi_condensed": "semi-condensed",
    "normal": "normal",
    "semi_expanded": "semi-expanded",
    "expanded": "expanded",
    "extra_expanded": "extra-expanded",
    "ultra_expanded": "ultra-expanded"
}

# Font variant numeric utilities
font_variant_numeric = {
    "normal_nums": "normal",
    "ordinal": "ordinal",
    "slashed_zero": "slashed-zero",
    "lining_nums": "lining-nums",
    "oldstyle_nums": "oldstyle-nums",
    "proportional_nums": "proportional-nums",
    "tabular_nums": "tabular-nums",
    "diagonal_fractions": "diagonal-fractions",
    "stacked_fractions": "stacked-fractions"
}

# Line clamp utilities
line_clamp = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "none": "none"
}

# List style image utilities
list_style_image = {
    "none": "none"
}

# List style position utilities
list_style_position = {
    "inside": "inside",
    "outside": "outside"
}

# List style type utilities
list_style_type = {
    "none": "none",
    "disc": "disc",
    "decimal": "decimal",
    "square": "square",
    "circle": "circle",
    "upper_roman": "upper-roman",
    "lower_roman": "lower-roman",
    "upper_alpha": "upper-alpha",
    "lower_alpha": "lower-alpha"
}

# Text align utilities
text_align = {
    "left": "left",
    "center": "center",
    "right": "right",
    "justify": "justify",
    "start": "start",
    "end": "end"
}

# Text color utilities (references to color system)
text_colors = {
    # This will reference the main color system
    "inherit": "inherit",
    "current": "currentColor",
    "transparent": "transparent"
}

# Text decoration line utilities
text_decoration_line = {
    "underline": "underline",
    "overline": "overline",
    "line_through": "line-through",
    "no_underline": "none"
}

# Text decoration color utilities
text_decoration_color = {
    "inherit": "inherit",
    "current": "currentColor",
    "transparent": "transparent"
}

# Text decoration style utilities
text_decoration_style = {
    "solid": "solid",
    "double": "double",
    "dotted": "dotted",
    "dashed": "dashed",
    "wavy": "wavy"
}

# Text decoration thickness utilities
text_decoration_thickness = {
    "auto": "auto",
    "from_font": "from-font",
    "0": "0px",
    "1": "1px",
    "2": "2px",
    "4": "4px",
    "8": "8px"
}

# Text underline offset utilities
text_underline_offset = {
    "auto": "auto",
    "0": "0px",
    "1": "1px",
    "2": "2px",
    "4": "4px",
    "8": "8px"
}

# Text transform utilities
text_transform = {
    "uppercase": "uppercase",
    "lowercase": "lowercase",
    "capitalize": "capitalize",
    "normal_case": "none"
}

# Text overflow utilities
text_overflow = {
    "truncate": "ellipsis",
    "text_ellipsis": "ellipsis",
    "text_clip": "clip"
}

# Text wrap utilities
text_wrap = {
    "wrap": "wrap",
    "nowrap": "nowrap",
    "balance": "balance",
    "pretty": "pretty"
}

# Text indent utilities
text_indent = {
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
    "96": "24rem"
}

# Vertical align utilities
vertical_align = {
    "baseline": "baseline",
    "top": "top",
    "middle": "middle",
    "bottom": "bottom",
    "text_top": "text-top",
    "text_bottom": "text-bottom",
    "sub": "sub",
    "super": "super"
}

# White space utilities
white_space = {
    "normal": "normal",
    "nowrap": "nowrap",
    "pre": "pre",
    "pre_line": "pre-line",
    "pre_wrap": "pre-wrap",
    "break_spaces": "break-spaces"
}

# Word break utilities
word_break = {
    "normal": "normal",
    "words": "break-word",
    "all": "break-all",
    "keep": "keep-all"
}

# Overflow wrap utilities
overflow_wrap = {
    "normal": "normal",
    "words": "break-word",
    "anywhere": "anywhere"
}

# Hyphens utilities
hyphens = {
    "none": "none",
    "manual": "manual",
    "auto": "auto"
}

# Content utilities
content = {
    "none": "none",
    "empty": "\"\""
}

# Letter spacing utilities
letter_spacing = {
    "tighter": "-0.05em",
    "tight": "-0.025em",
    "normal": "0em",
    "wide": "0.025em",
    "wider": "0.05em",
    "widest": "0.1em"
}

# Line height utilities
line_heights = {
    "3": ".75rem",
    "4": "1rem",
    "5": "1.25rem",
    "6": "1.5rem",
    "7": "1.75rem",
    "8": "2rem",
    "9": "2.25rem",
    "10": "2.5rem",
    "none": "1",
    "tight": "1.25",
    "snug": "1.375",
    "normal": "1.5",
    "relaxed": "1.625",
    "loose": "2"
}