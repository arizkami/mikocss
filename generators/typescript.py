def generate_ts_types():
    """Generate TypeScript type definitions"""
    lines = []
    lines.append("// MikoCSS TypeScript Definitions")
    lines.append("")
    
    # Color types
    lines.append("export interface ColorShades {")
    lines.append("  50: string;")
    lines.append("  100: string;")
    lines.append("  200: string;")
    lines.append("  300: string;")
    lines.append("  400: string;")
    lines.append("  500: string;")
    lines.append("  600: string;")
    lines.append("  700: string;")
    lines.append("  800: string;")
    lines.append("  900: string;")
    lines.append("  950: string;")
    lines.append("  [key: string]: string;")
    lines.append("}")
    lines.append("")
    
    lines.append("export interface ColorPalette {")
    lines.append("  [colorName: string]: ColorShades;")
    lines.append("}")
    lines.append("")
    
    # Typography types
    lines.append("export interface TextSize {")
    lines.append("  fontSize: string;")
    lines.append("  lineHeight: string;")
    lines.append("}")
    lines.append("")
    
    lines.append("export interface Typography {")
    lines.append("  sizes: { [key: string]: TextSize };")
    lines.append("  weights: { [key: string]: number };")
    lines.append("  families: { [key: string]: string[] };")
    lines.append("}")
    lines.append("")
    
    # Layout types
    lines.append("export interface Layout {")
    lines.append("  display: { [key: string]: string };")
    lines.append("  position: { [key: string]: string };")
    lines.append("  flex: {")
    lines.append("    direction: { [key: string]: string };")
    lines.append("    justify: { [key: string]: string };")
    lines.append("    align: { [key: string]: string };")
    lines.append("  };")
    lines.append("}")
    lines.append("")
    
    # Function types
    lines.append("export declare function getColor(name: string): string;")
    lines.append("export declare function getRgbValues(name: string): [number, number, number];")
    lines.append("export declare function getHexColor(name: string): string;")
    lines.append("")
    
    lines.append("export declare const colors: ColorPalette;")
    lines.append("export declare const typography: Typography;")
    lines.append("export declare const layout: Layout;")
    
    return "\n".join(lines)


def generate_ts_colors(all_colors):
    """Generate TypeScript color definitions with types"""
    from generators.javascript import generate_js_colors, generate_js_typography, generate_js_layout
    
    lines = []
    lines.append("/*! MikoCSS v1.0.0 | MIT License | https://github.com/arizkami/mikocss */")
    lines.append("")
    lines.append(generate_ts_types())
    lines.append("")
    
    # Import JS content but with TS syntax
    js_content = generate_js_colors(all_colors)
    js_content = js_content.replace("export const", "export const")
    lines.append(js_content)
    
    return "\n".join(lines)