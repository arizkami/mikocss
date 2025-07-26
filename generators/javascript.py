def generate_js_colors(all_colors):
    """Generate JavaScript color object"""
    lines = []
    lines.append("// MikoCSS Color System")
    lines.append("export const colors = {")
    
    for color_name, shades in all_colors.items():
        lines.append(f"  {color_name}: {{")
        
        for shade_key, (r, g, b) in shades.items():
            r_int = int(r * 255)
            g_int = int(g * 255)
            b_int = int(b * 255)
            
            if isinstance(shade_key, int):
                lines.append(f"    {shade_key}: 'rgb({r_int}, {g_int}, {b_int})',")
            else:
                lines.append(f"    '{shade_key}': 'rgb({r_int}, {g_int}, {b_int})',")
        
        lines.append("  },")
    
    lines.append("};")
    lines.append("")
    
    # Helper functions
    lines.append("// Helper functions")
    lines.append("export function getColor(name) {")
    lines.append("  const [family, shade] = name.split('-');")
    lines.append("  return colors[family]?.[shade] || colors[family]?.[parseInt(shade)] || '#000000';")
    lines.append("}")
    lines.append("")
    
    lines.append("export function getRgbValues(name) {")
    lines.append("  const color = getColor(name);")
    lines.append("  const match = color.match(/rgb\\((\\d+),\\s*(\\d+),\\s*(\\d+)\\)/);")
    lines.append("  return match ? [parseInt(match[1]), parseInt(match[2]), parseInt(match[3])] : [0, 0, 0];")
    lines.append("}")
    lines.append("")
    
    lines.append("export function getHexColor(name) {")
    lines.append("  const [r, g, b] = getRgbValues(name);")
    lines.append("  return `#${r.toString(16).padStart(2, '0')}${g.toString(16).padStart(2, '0')}${b.toString(16).padStart(2, '0')}`;")
    lines.append("}")
    
    return "\n".join(lines)


def generate_js_typography():
    """Generate JavaScript typography utilities"""
    from typography.base import text_sizes, font_weights, font_families
    
    lines = []
    lines.append("// Typography System")
    lines.append("export const typography = {")
    
    # Text sizes
    lines.append("  sizes: {")
    for size_name, size_data in text_sizes.items():
        lines.append(f"    {size_name}: {{")
        lines.append(f"      fontSize: '{size_data['font_size']}',")
        lines.append(f"      lineHeight: '{size_data['line_height']}',")
        lines.append("    },")
    lines.append("  },")
    
    # Font weights
    lines.append("  weights: {")
    for weight_name, weight_value in font_weights.items():
        lines.append(f"    {weight_name}: {weight_value},")
    lines.append("  },")
    
    # Font families
    lines.append("  families: {")
    for family_name, family_stack in font_families.items():
        family_js = str(family_stack).replace("'", '"')
        lines.append(f"    {family_name}: {family_js},")
    lines.append("  },")
    
    lines.append("};")
    
    return "\n".join(lines)


def generate_js_layout():
    """Generate JavaScript layout utilities"""
    from layout.base import display, position, flex_direction, justify_content, align_items
    
    lines = []
    lines.append("// Layout System")
    lines.append("export const layout = {")
    
    # Display
    lines.append("  display: {")
    for display_name, display_value in display.items():
        lines.append(f"    {display_name}: '{display_value}',")
    lines.append("  },")
    
    # Position
    lines.append("  position: {")
    for pos_name, pos_value in position.items():
        lines.append(f"    {pos_name}: '{pos_value}',")
    lines.append("  },")
    
    # Flexbox
    lines.append("  flex: {")
    lines.append("    direction: {")
    for dir_name, dir_value in flex_direction.items():
        lines.append(f"      {dir_name}: '{dir_value}',")
    lines.append("    },")
    
    lines.append("    justify: {")
    for justify_name, justify_value in justify_content.items():
        lines.append(f"      {justify_name}: '{justify_value}',")
    lines.append("    },")
    
    lines.append("    align: {")
    for align_name, align_value in align_items.items():
        lines.append(f"      {align_name}: '{align_value}',")
    lines.append("    },")
    
    lines.append("  },")
    lines.append("};")
    
    return "\n".join(lines)


def generate_complete_js(all_colors):
    """Generate complete JavaScript bundle"""
    lines = []
    lines.append("/*! MikoCSS v1.0.0 | MIT License | https://github.com/arizkami/mikocss */")
    lines.append("")
    lines.append(generate_js_colors(all_colors))
    lines.append("")
    lines.append(generate_js_typography())
    lines.append("")
    lines.append(generate_js_layout())
    
    return "\n".join(lines)