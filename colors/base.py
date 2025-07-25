# color/base.py
# Extended color palette with 256+ base colors and 8k color support

# Core color families with full shade ranges (50-950)
color_shades = {
    # Slate family
    "slate": {
        "50": "#f8fafc", "100": "#f1f5f9", "200": "#e2e8f0", "300": "#cbd5e1",
        "400": "#94a3b8", "500": "#64748b", "600": "#475569", "700": "#334155",
        "800": "#1e293b", "900": "#0f172a", "950": "#020617"
    },
    # Gray family
    "gray": {
        "50": "#f9fafb", "100": "#f3f4f6", "200": "#e5e7eb", "300": "#d1d5db",
        "400": "#9ca3af", "500": "#6b7280", "600": "#4b5563", "700": "#374151",
        "800": "#1f2937", "900": "#111827", "950": "#030712"
    },
    # Zinc family
    "zinc": {
        "50": "#fafafa", "100": "#f4f4f5", "200": "#e4e4e7", "300": "#d4d4d8",
        "400": "#a1a1aa", "500": "#71717a", "600": "#52525b", "700": "#3f3f46",
        "800": "#27272a", "900": "#18181b", "950": "#09090b"
    },
    # Neutral family
    "neutral": {
        "50": "#fafafa", "100": "#f5f5f5", "200": "#e5e5e5", "300": "#d4d4d4",
        "400": "#a3a3a3", "500": "#737373", "600": "#525252", "700": "#404040",
        "800": "#262626", "900": "#171717", "950": "#0a0a0a"
    },
    # Stone family
    "stone": {
        "50": "#fafaf9", "100": "#f5f5f4", "200": "#e7e5e4", "300": "#d6d3d1",
        "400": "#a8a29e", "500": "#78716c", "600": "#57534e", "700": "#44403c",
        "800": "#292524", "900": "#1c1917", "950": "#0c0a09"
    },
    # Red family
    "red": {
        "50": "#fef2f2", "100": "#fee2e2", "200": "#fecaca", "300": "#fca5a5",
        "400": "#f87171", "500": "#ef4444", "600": "#dc2626", "700": "#b91c1c",
        "800": "#991b1b", "900": "#7f1d1d", "950": "#450a0a"
    },
    # Orange family
    "orange": {
        "50": "#fff7ed", "100": "#ffedd5", "200": "#fed7aa", "300": "#fdba74",
        "400": "#fb923c", "500": "#f97316", "600": "#ea580c", "700": "#c2410c",
        "800": "#9a3412", "900": "#7c2d12", "950": "#431407"
    },
    # Amber family
    "amber": {
        "50": "#fffbeb", "100": "#fef3c7", "200": "#fde68a", "300": "#fcd34d",
        "400": "#fbbf24", "500": "#f59e0b", "600": "#d97706", "700": "#b45309",
        "800": "#92400e", "900": "#78350f", "950": "#451a03"
    },
    # Yellow family
    "yellow": {
        "50": "#fefce8", "100": "#fef9c3", "200": "#fef08a", "300": "#fde047",
        "400": "#facc15", "500": "#eab308", "600": "#ca8a04", "700": "#a16207",
        "800": "#854d0e", "900": "#713f12", "950": "#422006"
    },
    # Lime family
    "lime": {
        "50": "#f7fee7", "100": "#ecfccb", "200": "#d9f99d", "300": "#bef264",
        "400": "#a3e635", "500": "#84cc16", "600": "#65a30d", "700": "#4d7c0f",
        "800": "#3f6212", "900": "#365314", "950": "#1a2e05"
    },
    # Green family
    "green": {
        "50": "#f0fdf4", "100": "#dcfce7", "200": "#bbf7d0", "300": "#86efac",
        "400": "#4ade80", "500": "#22c55e", "600": "#16a34a", "700": "#15803d",
        "800": "#166534", "900": "#14532d", "950": "#052e16"
    },
    # Emerald family
    "emerald": {
        "50": "#ecfdf5", "100": "#d1fae5", "200": "#a7f3d0", "300": "#6ee7b7",
        "400": "#34d399", "500": "#10b981", "600": "#059669", "700": "#047857",
        "800": "#065f46", "900": "#064e3b", "950": "#022c22"
    },
    # Teal family
    "teal": {
        "50": "#f0fdfa", "100": "#ccfbf1", "200": "#99f6e4", "300": "#5eead4",
        "400": "#2dd4bf", "500": "#14b8a6", "600": "#0d9488", "700": "#0f766e",
        "800": "#115e59", "900": "#134e4a", "950": "#042f2e"
    },
    # Cyan family
    "cyan": {
        "50": "#ecfeff", "100": "#cffafe", "200": "#a5f3fc", "300": "#67e8f9",
        "400": "#22d3ee", "500": "#06b6d4", "600": "#0891b2", "700": "#0e7490",
        "800": "#155e75", "900": "#164e63", "950": "#083344"
    },
    # Sky family
    "sky": {
        "50": "#f0f9ff", "100": "#e0f2fe", "200": "#bae6fd", "300": "#7dd3fc",
        "400": "#38bdf8", "500": "#0ea5e9", "600": "#0284c7", "700": "#0369a1",
        "800": "#075985", "900": "#0c4a6e", "950": "#082f49"
    },
    # Blue family
    "blue": {
        "50": "#eff6ff", "100": "#dbeafe", "200": "#bfdbfe", "300": "#93c5fd",
        "400": "#60a5fa", "500": "#3b82f6", "600": "#2563eb", "700": "#1d4ed8",
        "800": "#1e40af", "900": "#1e3a8a", "950": "#172554"
    },
    # Indigo family
    "indigo": {
        "50": "#eef2ff", "100": "#e0e7ff", "200": "#c7d2fe", "300": "#a5b4fc",
        "400": "#818cf8", "500": "#6366f1", "600": "#4f46e5", "700": "#4338ca",
        "800": "#3730a3", "900": "#312e81", "950": "#1e1b4b"
    },
    # Violet family
    "violet": {
        "50": "#f5f3ff", "100": "#ede9fe", "200": "#ddd6fe", "300": "#c4b5fd",
        "400": "#a78bfa", "500": "#8b5cf6", "600": "#7c3aed", "700": "#6d28d9",
        "800": "#5b21b6", "900": "#4c1d95", "950": "#2e1065"
    },
    # Purple family
    "purple": {
        "50": "#faf5ff", "100": "#f3e8ff", "200": "#e9d5ff", "300": "#d8b4fe",
        "400": "#c084fc", "500": "#a855f7", "600": "#9333ea", "700": "#7e22ce",
        "800": "#6b21a8", "900": "#581c87", "950": "#3b0764"
    },
    # Fuchsia family
    "fuchsia": {
        "50": "#fdf4ff", "100": "#fae8ff", "200": "#f5d0fe", "300": "#f0abfc",
        "400": "#e879f9", "500": "#d946ef", "600": "#c026d3", "700": "#a21caf",
        "800": "#86198f", "900": "#701a75", "950": "#4a044e"
    },
    # Pink family
    "pink": {
        "50": "#fdf2f8", "100": "#fce7f3", "200": "#fbcfe8", "300": "#f9a8d4",
        "400": "#f472b6", "500": "#ec4899", "600": "#db2777", "700": "#be185d",
        "800": "#9d174d", "900": "#831843", "950": "#500724"
    },
    # Rose family
    "rose": {
        "50": "#fff1f2", "100": "#ffe4e6", "200": "#fecdd3", "300": "#fda4af",
        "400": "#fb7185", "500": "#f43f5e", "600": "#e11d48", "700": "#be123c",
        "800": "#9f1239", "900": "#881337", "950": "#4c0519"
    }
}

# Extended base colors (256+ colors)
base_colors = {
    # Primary color references (using 500 shade as default)
    "slate": "#64748b", "gray": "#6b7280", "zinc": "#71717a", "neutral": "#737373",
    "stone": "#78716c", "red": "#ef4444", "orange": "#f97316", "amber": "#f59e0b",
    "yellow": "#eab308", "lime": "#84cc16", "green": "#22c55e", "emerald": "#10b981",
    "teal": "#14b8a6", "cyan": "#06b6d4", "sky": "#0ea5e9", "blue": "#3b82f6",
    "indigo": "#6366f1", "violet": "#8b5cf6", "purple": "#a855f7", "fuchsia": "#d946ef",
    "pink": "#ec4899", "rose": "#f43f5e",
    
    # Extended color variations
    "crimson": "#dc143c", "maroon": "#800000", "cherry": "#de3163", "scarlet": "#ff2400",
    "ruby": "#e0115f", "coral": "#ff7f50", "salmon": "#fa8072", "tomato": "#ff6347",
    "orangeRed": "#ff4500", "darkOrange": "#ff8c00", "gold": "#ffd700", "goldenrod": "#daa520",
    "darkGoldenrod": "#b8860b", "khaki": "#f0e68c", "darkKhaki": "#bdb76b",
    "olive": "#808000", "oliveDrab": "#6b8e23", "yellowGreen": "#9acd32",
    "lawnGreen": "#7cfc00", "chartreuse": "#7fff00", "greenYellow": "#adff2f",
    "springGreen": "#00ff7f", "mediumSpringGreen": "#00fa9a", "lightGreen": "#90ee90",
    "paleGreen": "#98fb98", "darkSeaGreen": "#8fbc8f", "mediumSeaGreen": "#3cb371",
    "seaGreen": "#2e8b57", "forestGreen": "#228b22", "darkGreen": "#006400",
    "mediumAquamarine": "#66cdaa", "aqua": "#00ffff", "darkTurquoise": "#00ced1",
    "mediumTurquoise": "#48d1cc", "turquoise": "#40e0d0", "lightSeaGreen": "#20b2aa",
    "cadetBlue": "#5f9ea0", "darkCyan": "#008b8b", "lightSteelBlue": "#b0c4de",
    "powderBlue": "#b0e0e6", "lightBlue": "#add8e6", "skyBlue": "#87ceeb",
    "lightSkyBlue": "#87cefa", "deepSkyBlue": "#00bfff", "dodgerBlue": "#1e90ff",
    "cornflowerBlue": "#6495ed", "steelBlue": "#4682b4", "royalBlue": "#4169e1",
    "mediumBlue": "#0000cd", "darkBlue": "#00008b", "navy": "#000080",
    "midnightBlue": "#191970", "mediumSlateBlue": "#7b68ee", "slateBlue": "#6a5acd",
    "darkSlateBlue": "#483d8b", "mediumPurple": "#9370db", "darkViolet": "#9400d3",
    "darkOrchid": "#9932cc", "mediumOrchid": "#ba55d3", "thistle": "#d8bfd8",
    "plum": "#dda0dd", "orchid": "#da70d6", "magenta": "#ff00ff",
    "darkMagenta": "#8b008b", "mediumVioletRed": "#c71585", "paleVioletRed": "#db7093",
    "deepPink": "#ff1493", "hotPink": "#ff69b4", "lightPink": "#ffb6c1",
    "mistyRose": "#ffe4e1", "antiqueWhite": "#faebd7", "linen": "#faf0e6",
    "beige": "#f5f5dc", "wheat": "#f5deb3", "cornsilk": "#fff8dc",
    "lemonChiffon": "#fffacd", "lightGoldenrodYellow": "#fafad2", "lightYellow": "#ffffe0",
    "saddle Brown": "#8b4513", "sienna": "#a0522d", "chocolate": "#d2691e",
    "peru": "#cd853f", "sandyBrown": "#f4a460", "burlyWood": "#deb887",
    "tan": "#d2b48c", "rosyBrown": "#bc8f8f", "moccasin": "#ffe4b5",
    "navajoWhite": "#ffdead", "peachPuff": "#ffdab9", "papayaWhip": "#ffefd5",
    "blanchedAlmond": "#ffebcd", "bisque": "#ffe4c4", "darkSalmon": "#e9967a",
    "lightSalmon": "#ffa07a", "orange": "#ffa500", "darkorange": "#ff8c00",
    "coral": "#ff7f50", "lightCoral": "#f08080", "indianRed": "#cd5c5c",
    "firebrick": "#b22222", "brick": "#cb4154", "darkRed": "#8b0000",
    
    # Metallic colors
    "silver": "#c0c0c0", "darkGray": "#a9a9a9", "gray": "#808080",
    "dimGray": "#696969", "lightSlateGray": "#778899", "slateGray": "#708090",
    "darkSlateGray": "#2f4f4f", "black": "#000000", "white": "#ffffff",
    "snow": "#fffafa", "honeydew": "#f0fff0", "mintCream": "#f5fffa",
    "azure": "#f0ffff", "aliceBlue": "#f0f8ff", "ghostWhite": "#f8f8ff",
    "whiteSmoke": "#f5f5f5", "seashell": "#fff5ee", "oldLace": "#fdf5e6",
    "floralWhite": "#fffaf0", "ivory": "#fffff0", "gainsboro": "#dcdcdc",
    "lightGray": "#d3d3d3", "silver": "#c0c0c0", "darkGray": "#a9a9a9",
    
    # Extended metallics
    "platinum": "#e5e4e2", "copper": "#b87333", "bronze": "#cd7f32",
    "brass": "#b5a642", "pewter": "#96a8a1", "iron": "#464451",
    "steel": "#71797e", "titanium": "#878681", "chrome": "#c4c4c4",
    "nickel": "#727472", "aluminum": "#a8a8a8", "tin": "#d4d4d4",
    
    # Gemstone colors
    "diamond": "#b9f2ff", "sapphire": "#0f52ba", "emerald": "#50c878",
    "ruby": "#e0115f", "topaz": "#ffc87c", "amethyst": "#9966cc",
    "garnet": "#733635", "opal": "#a8c3bc", "pearl": "#f8f6f0",
    "jade": "#00a86b", "turquoise": "#40e0d0", "onyx": "#353839",
    
    # Nature-inspired colors
    "earth": "#8b4513", "sand": "#c2b280", "clay": "#b66a50",
    "mud": "#70543e", "bark": "#8d5524", "moss": "#8a9a5b",
    "fern": "#4f7942", "sage": "#9caf88", "pine": "#01796f",
    "forest": "#355e3b", "jungle": "#29ab87", "meadow": "#95bb72",
    "ocean": "#006994", "sea": "#2e8b57", "lake": "#4f94cd",
    "river": "#4682b4", "sky": "#87ceeb", "cloud": "#f0f8ff",
    "storm": "#4f666a", "mist": "#c4c4bc", "fog": "#d3d3d3",
    "snow": "#fffafa", "ice": "#b0e0e6", "frost": "#dce4ee",
    "sunset": "#ff8c69", "sunrise": "#ffdb58", "twilight": "#8a2be2",
    "aurora": "#4fff4f", "moonlight": "#f0f8ff", "starlight": "#fffacd"
}

# 8K Color Support - High precision color definitions
# These provide ultra-fine color gradations for professional applications
eight_k_colors = {
    # Ultra-fine grayscale (256 levels)
    **{f"gray_{i}": f"#{i:02x}{i:02x}{i:02x}" for i in range(0, 256)},
    
    # High-precision RGB combinations (selected subset for performance)
    # Red variations
    **{f"red_{r}_{g}_{b}": f"#{r:02x}{g:02x}{b:02x}" 
       for r in range(128, 256, 8) for g in range(0, 128, 16) for b in range(0, 128, 16)},
    
    # Green variations
    **{f"green_{r}_{g}_{b}": f"#{r:02x}{g:02x}{b:02x}" 
       for r in range(0, 128, 16) for g in range(128, 256, 8) for b in range(0, 128, 16)},
    
    # Blue variations
    **{f"blue_{r}_{g}_{b}": f"#{r:02x}{g:02x}{b:02x}" 
       for r in range(0, 128, 16) for g in range(0, 128, 16) for b in range(128, 256, 8)},
    
    # Cyan variations
    **{f"cyan_{r}_{g}_{b}": f"#{r:02x}{g:02x}{b:02x}" 
       for r in range(0, 128, 16) for g in range(128, 256, 8) for b in range(128, 256, 8)},
    
    # Magenta variations
    **{f"magenta_{r}_{g}_{b}": f"#{r:02x}{g:02x}{b:02x}" 
       for r in range(128, 256, 8) for g in range(0, 128, 16) for b in range(128, 256, 8)},
    
    # Yellow variations
    **{f"yellow_{r}_{g}_{b}": f"#{r:02x}{g:02x}{b:02x}" 
       for r in range(128, 256, 8) for g in range(128, 256, 8) for b in range(0, 128, 16)}
}

# Combine all color systems
all_colors = {**base_colors, **eight_k_colors}

# Color utility functions
def get_color_shade(color_family, shade):
    """Get a specific shade of a color family"""
    if color_family in color_shades and str(shade) in color_shades[color_family]:
        return color_shades[color_family][str(shade)]
    return None

def get_all_shades(color_family):
    """Get all shades of a color family"""
    return color_shades.get(color_family, {})

def generate_color_variants(base_hex, steps=10):
    """Generate lighter and darker variants of a base color"""
    # This would contain logic to generate color variants
    # Implementation would involve HSL manipulation
    pass

# Export the main color dictionary for backward compatibility
colors = base_colors
