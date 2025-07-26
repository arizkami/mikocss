def generate_css_variables(all_colors):
    """Generate CSS custom properties (variables) for all colors"""
    lines = []
    lines.append(":root {")
    
    for color_name, shades in all_colors.items():
        for shade_key, (r, g, b) in shades.items():
            # Convert to 0-255 range
            r_int = int(r * 255)
            g_int = int(g * 255)
            b_int = int(b * 255)
            
            if isinstance(shade_key, int):
                var_name = f"--color-{color_name}-{shade_key}"
            else:
                var_name = f"--color-{color_name}-{shade_key}"
                
            lines.append(f"  {var_name}: {r_int}, {g_int}, {b_int};")
            lines.append(f"  {var_name}-rgb: rgb({r_int}, {g_int}, {b_int});")
            lines.append(f"  {var_name}-rgba: rgba({r_int}, {g_int}, {b_int}, 1);")
    
    lines.append("}")
    return "\n".join(lines)


def generate_css_utilities(all_colors):
    """Generate utility classes for colors"""
    lines = []
    
    # Text color utilities
    lines.append("/* Text Colors */")
    for color_name, shades in all_colors.items():
        for shade_key in shades.keys():
            if isinstance(shade_key, int):
                class_name = f"text-{color_name}-{shade_key}"
                var_name = f"--color-{color_name}-{shade_key}-rgb"
            else:
                class_name = f"text-{color_name}-{shade_key}"
                var_name = f"--color-{color_name}-{shade_key}-rgb"
                
            lines.append(f".{class_name} {{ color: var({var_name}); }}")
    
    lines.append("")
    
    # Background color utilities
    lines.append("/* Background Colors */")
    for color_name, shades in all_colors.items():
        for shade_key in shades.keys():
            if isinstance(shade_key, int):
                class_name = f"bg-{color_name}-{shade_key}"
                var_name = f"--color-{color_name}-{shade_key}-rgb"
            else:
                class_name = f"bg-{color_name}-{shade_key}"
                var_name = f"--color-{color_name}-{shade_key}-rgb"
                
            lines.append(f".{class_name} {{ background-color: var({var_name}); }}")
    
    lines.append("")
    
    # Border color utilities
    lines.append("/* Border Colors */")
    for color_name, shades in all_colors.items():
        for shade_key in shades.keys():
            if isinstance(shade_key, int):
                class_name = f"border-{color_name}-{shade_key}"
                var_name = f"--color-{color_name}-{shade_key}-rgb"
            else:
                class_name = f"border-{color_name}-{shade_key}"
                var_name = f"--color-{color_name}-{shade_key}-rgb"
                
            lines.append(f".{class_name} {{ border-color: var({var_name}); }}")
    
    return "\n".join(lines)


def generate_css_typography():
    """Generate CSS typography utilities"""
    from typography.base import text_sizes, font_weights, font_families
    
    lines = []
    lines.append("/* Typography Utilities */")
    
    # Font sizes
    lines.append("/* Font Sizes */")
    for size_name, size_data in text_sizes.items():
        lines.append(f".text-{size_name} {{")
        lines.append(f"  font-size: {size_data['font_size']};")
        lines.append(f"  line-height: {size_data['line_height']};")
        lines.append("}")
    
    lines.append("")
    
    # Font weights
    lines.append("/* Font Weights */")
    for weight_name, weight_value in font_weights.items():
        lines.append(f".font-{weight_name} {{ font-weight: {weight_value}; }}")
    
    lines.append("")
    
    # Font families
    lines.append("/* Font Families */")
    for family_name, family_stack in font_families.items():
        family_css = ", ".join([f'"{font}"' if ' ' in font else font for font in family_stack])
        lines.append(f".font-{family_name} {{ font-family: {family_css}; }}")
    
    return "\n".join(lines)


def generate_css_layout():
    """Generate CSS layout utilities"""
    from layout.base import display, position, flex_direction, justify_content, align_items
    from spacing.base import padding, margin
    
    lines = []
    lines.append("/* Layout Utilities */")
    
    # Display utilities
    lines.append("/* Display */")
    for display_name, display_value in display.items():
        lines.append(f".{display_name} {{ display: {display_value}; }}")
    
    lines.append("")
    
    # Position utilities
    lines.append("/* Position */")
    for pos_name, pos_value in position.items():
        lines.append(f".{pos_name} {{ position: {pos_value}; }}")
    
    lines.append("")
    
    # Flexbox utilities
    lines.append("/* Flexbox */")
    for dir_name, dir_value in flex_direction.items():
        lines.append(f".flex-{dir_name} {{ flex-direction: {dir_value}; }}")
    
    for justify_name, justify_value in justify_content.items():
        lines.append(f".justify-{justify_name} {{ justify-content: {justify_value}; }}")
    
    for align_name, align_value in align_items.items():
        lines.append(f".items-{align_name} {{ align-items: {align_value}; }}")
    
    return "\n".join(lines)


def generate_complete_css(all_colors):
    """Generate complete CSS bundle"""
    lines = []
    lines.append("/*! MikoCSS v1.0.0 | MIT License | https://github.com/arizkami/mikocss */")
    lines.append("")
    lines.append(generate_css_variables(all_colors))
    lines.append("")
    lines.append(generate_css_utilities(all_colors))
    lines.append("")
    lines.append(generate_css_typography())
    lines.append("")
    lines.append(generate_css_layout())
    
    return "\n".join(lines)