def generate_color_hpp(all_colors):
    """Generate C++ header file with color definitions"""
    lines = []
    lines.append("#pragma once")
    lines.append("#include <string>")
    lines.append("#include <unordered_map>\n")
    lines.append("namespace twcolors {\n")
    lines.append("struct Color { float r, g, b, a; };\n")

    total_colors = 0

    for name, shades in all_colors.items():
        # Generate constexpr variables
        for shade_key, (r, g, b) in shades.items():
            var_name = f"{name}_{shade_key}".replace("-", "_")
            lines.append(
                f"static constexpr Color {var_name} = {{ {r:.6f}f, {g:.6f}f, {b:.6f}f, 1.0f }};"
            )
            total_colors += 1

        lines.append("")

    lines.append("} // namespace twcolors")
    print(f"Total colors generated: {total_colors}")
    return "\n".join(lines)


def generate_wrapper_hpp(all_colors, framework="gtk"):
    """Generate C++ wrapper with framework-specific support"""
    lines = []
    lines.append("#pragma once")

    # Framework-specific includes
    if framework == "gtk":
        lines.append("#include <gdk/gdk.h>")
    elif framework in ["qt5", "qt6"]:
        lines.append("#include <QColor>")
    elif framework == "win32":
        lines.append("#include <windows.h>")

    lines.append("#include <unordered_map>")
    lines.append("#include <vector>")
    lines.append('#include "miko_color.hpp"\n')
    lines.append("namespace miko {\n")
    lines.append("using Color = twcolors::Color;\n")

    # Generate color lookup function
    lines.append("inline Color get_color(const std::string& name) {")
    lines.append(
        "    static const std::unordered_map<std::string, Color> color_map = {"
    )

    # Add all color mappings
    for color_name, shades in all_colors.items():
        for shade_key in shades:
            var_name = f"{color_name}_{shade_key}".replace("-", "_")

            # Handle different naming conventions
            if isinstance(shade_key, int):
                map_key = f"{color_name}-{shade_key}"
            else:
                map_key = f"{color_name}-{shade_key}"

            lines.append(f'        {{"{map_key}", twcolors::{var_name}}},')

    lines.append("    };")
    lines.append("")
    lines.append("    auto it = color_map.find(name);")
    lines.append("    if (it != color_map.end()) {")
    lines.append("        return it->second;")
    lines.append("}")
    lines.append("")
    lines.append("    // Return default color (white) if not found")
    lines.append("    return {1.0f, 1.0f, 1.0f, 1.0f};")
    lines.append("}\n")

    # Framework-specific conversion functions
    if framework == "gtk":
        lines.append("inline GdkRGBA to_gdk_color(const std::string& name) {")
        lines.append("    auto c = get_color(name);")
        lines.append("    return GdkRGBA{c.r, c.g, c.b, c.a};")
        lines.append("}")
    elif framework in ["qt5", "qt6"]:
        lines.append("inline QColor to_qt_color(const std::string& name) {")
        lines.append("    auto c = get_color(name);")
        lines.append("    return QColor::fromRgbF(c.r, c.g, c.b, c.a);")
        lines.append("}")
    elif framework == "win32":
        lines.append("inline COLORREF to_colorref(const std::string& name) {")
        lines.append("    auto c = get_color(name);")
        lines.append(
            "    return RGB(static_cast<int>(c.r * 255), static_cast<int>(c.g * 255), static_cast<int>(c.b * 255));"
        )
        lines.append("}")
        lines.append("")
        lines.append("inline DWORD to_argb(const std::string& name) {")
        lines.append("    auto c = get_color(name);")
        lines.append("    return (static_cast<DWORD>(c.a * 255) << 24) |")
        lines.append("           (static_cast<DWORD>(c.r * 255) << 16) |")
        lines.append("           (static_cast<DWORD>(c.g * 255) << 8) |")
        lines.append("           static_cast<DWORD>(c.b * 255);")
        lines.append("}")

    lines.append("")

    # Add helper function to list all colors
    lines.append("inline std::vector<std::string> get_all_color_names() {")
    lines.append("    static const std::vector<std::string> color_names = {")
    for color_name, shades in all_colors.items():
        for shade_key in shades:
            if isinstance(shade_key, int):
                map_key = f"{color_name}-{shade_key}"
            else:
                map_key = f"{color_name}-{shade_key}"
            lines.append(f'        "{map_key}",')
    lines.append("    };")
    lines.append("    return color_names;")
    lines.append("}")
    lines.append("")
    lines.append("} // namespace miko")

    return "\n".join(lines)


def generate_color_list(all_colors):
    """Generate a comprehensive list of all available colors"""
    lines = []
    lines.append(
        f"// Total colors available: {sum(len(shades) for shades in all_colors.values())}"
    )
    lines.append("// Available colors by family:\n")

    for color_name, shades in sorted(all_colors.items()):
        lines.append(f"// {color_name.upper()} FAMILY ({len(shades)} colors):")

        # Group by type
        standard = [
            k
            for k in shades.keys()
            if isinstance(k, int)
            and k in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
        ]
        micro = [k for k in shades.keys() if isinstance(k, int) and k not in standard]
        variants = [k for k in shades.keys() if isinstance(k, str)]

        if standard:
            shade_list = ", ".join(
                [f"{color_name}-{shade}" for shade in sorted(standard)]
            )
            lines.append(f"//   Standard: {shade_list}")

        if micro:
            shade_list = ", ".join([f"{color_name}-{shade}" for shade in sorted(micro)])
            lines.append(f"//   Micro: {shade_list}")

        if variants:
            variant_list = ", ".join(
                [f"{color_name}-{variant}" for variant in sorted(variants)]
            )
            lines.append(f"//   Variants: {variant_list}")

        lines.append("")

    return "\n".join(lines)
