from typography.base import text_sizes, font_weights, font_families, letter_spacing, line_heights

def generate_typography_hpp(framework="gtk"):
    """Generate C++ header file with typography definitions"""
    lines = []
    lines.append("#pragma once")
    lines.append("#include <string>")
    lines.append("#include <unordered_map>")
    lines.append("#include <vector>\n")
    
    if framework == "gtk":
        lines.append("#include <pango/pango.h>")
    elif framework in ["qt5", "qt6"]:
        lines.append("#include <QFont>")
        lines.append("#include <QFontMetrics>")
    elif framework == "win32":
        lines.append("#include <windows.h>")
    
    lines.append("\nnamespace twtypo {\n")
    
    # Text size structure
    lines.append("struct TextSize {")
    lines.append("    float font_size_px;")
    lines.append("    float line_height_px;")
    lines.append("    const char* font_size_rem;")
    lines.append("    const char* line_height_rem;")
    lines.append("};\n")
    
    # Font weight structure
    lines.append("struct FontWeight {")
    lines.append("    int weight;")
    lines.append("    const char* name;")
    lines.append("};\n")
    
    # Generate text size constants
    lines.append("// Text Sizes")
    for size_name, size_data in text_sizes.items():
        font_size_px = float(size_data["font_size"].replace("rem", "")) * 16  # Convert rem to px (assuming 16px base)
        line_height_px = float(size_data["line_height"].replace("rem", "")) * 16 if "rem" in size_data["line_height"] else float(size_data["line_height"]) * font_size_px
        
        var_name = f"text_{size_name}".replace("-", "_")
        lines.append(f'static constexpr TextSize {var_name} = {{')
        lines.append(f'    {font_size_px:.1f}f, {line_height_px:.1f}f,')
        lines.append(f'    "{size_data["font_size"]}", "{size_data["line_height"]}"')
        lines.append(f'}};')
    
    lines.append("")
    
    # Generate font weight constants
    lines.append("// Font Weights")
    for weight_name, weight_value in font_weights.items():
        var_name = f"font_{weight_name}"
        lines.append(f'static constexpr FontWeight {var_name} = {{{weight_value}, "{weight_name}"}};')
    
    lines.append("")
    lines.append("} // namespace twtypo")
    
    return "\n".join(lines)

def generate_typography_wrapper_hpp(framework="gtk"):
    """Generate typography wrapper with framework-specific support"""
    lines = []
    lines.append("#pragma once")
    
    if framework == "gtk":
        lines.append("#include <pango/pango.h>")
        lines.append("#include <gtk/gtk.h>")
    elif framework in ["qt5", "qt6"]:
        lines.append("#include <QFont>")
        lines.append("#include <QApplication>")
    elif framework == "win32":
        lines.append("#include <windows.h>")
    
    lines.append("#include <unordered_map>")
    lines.append("#include <string>")
    lines.append("#include \"typography.hpp\"\n")
    lines.append("namespace miko {\n")
    lines.append("using TextSize = twtypo::TextSize;")
    lines.append("using FontWeight = twtypo::FontWeight;\n")
    
    # Generate text size lookup function
    lines.append("inline TextSize get_text_size(const std::string& name) {")
    lines.append("    static const std::unordered_map<std::string, TextSize> size_map = {")
    
    for size_name in text_sizes.keys():
        var_name = f"text_{size_name}".replace("-", "_")
        lines.append(f'        {{"{size_name}", twtypo::{var_name}}},')
    
    lines.append("    };")
    lines.append("    auto it = size_map.find(name);")
    lines.append("    return (it != size_map.end()) ? it->second : twtypo::text_base;")
    lines.append("}\n")
    
    # Generate font weight lookup function
    lines.append("inline FontWeight get_font_weight(const std::string& name) {")
    lines.append("    static const std::unordered_map<std::string, FontWeight> weight_map = {")
    
    for weight_name in font_weights.keys():
        var_name = f"font_{weight_name}"
        lines.append(f'        {{"{weight_name}", twtypo::{var_name}}},')
    
    lines.append("    };")
    lines.append("    auto it = weight_map.find(name);")
    lines.append("    return (it != weight_map.end()) ? it->second : twtypo::font_regular;")
    lines.append("}\n")
    
    # Framework-specific font creation functions
    if framework == "gtk":
        lines.append("inline PangoFontDescription* create_font(const std::string& size, const std::string& weight, const std::string& family = \"sans\") {")
        lines.append("    auto text_size = get_text_size(size);")
        lines.append("    auto font_weight = get_font_weight(weight);")
        lines.append("    ")
        lines.append("    PangoFontDescription* desc = pango_font_description_new();")
        lines.append("    pango_font_description_set_size(desc, text_size.font_size_px * PANGO_SCALE);")
        lines.append("    pango_font_description_set_weight(desc, static_cast<PangoWeight>(font_weight.weight));")
        lines.append("    ")
        lines.append("    if (family == \"sans\") pango_font_description_set_family(desc, \"Sans\");")
        lines.append("    else if (family == \"serif\") pango_font_description_set_family(desc, \"Serif\");")
        lines.append("    else if (family == \"mono\") pango_font_description_set_family(desc, \"Monospace\");")
        lines.append("    ")
        lines.append("    return desc;")
        lines.append("}")
    elif framework in ["qt5", "qt6"]:
        lines.append("inline QFont create_font(const std::string& size, const std::string& weight, const std::string& family = \"sans\") {")
        lines.append("    auto text_size = get_text_size(size);")
        lines.append("    auto font_weight = get_font_weight(weight);")
        lines.append("    ")
        lines.append("    QFont font;")
        lines.append("    font.setPointSizeF(text_size.font_size_px * 0.75f); // Convert px to pt")
        
        # Qt5/Qt6 weight handling difference
        if framework == "qt5":
            lines.append("    font.setWeight(static_cast<QFont::Weight>(font_weight.weight));")
        else:  # qt6
            lines.append("    font.setWeight(QFont::Weight(font_weight.weight));")
        
        lines.append("    ")
        lines.append("    if (family == \"sans\") font.setFamily(\"Arial\");")
        lines.append("    else if (family == \"serif\") font.setFamily(\"Times New Roman\");")
        lines.append("    else if (family == \"mono\") font.setFamily(\"Courier New\");")
        lines.append("    ")
        lines.append("    return font;")
        lines.append("}")
    elif framework == "win32":
        lines.append("inline HFONT create_font(const std::string& size, const std::string& weight, const std::string& family = \"sans\") {")
        lines.append("    auto text_size = get_text_size(size);")
        lines.append("    auto font_weight = get_font_weight(weight);")
        lines.append("    ")
        lines.append("    const char* font_name = \"Arial\";")
        lines.append("    if (family == \"serif\") font_name = \"Times New Roman\";")
        lines.append("    else if (family == \"mono\") font_name = \"Courier New\";")
        lines.append("    ")
        lines.append("    return CreateFontA(")
        lines.append("        static_cast<int>(-text_size.font_size_px), 0, 0, 0,")
        lines.append("        font_weight.weight, FALSE, FALSE, FALSE,")
        lines.append("        DEFAULT_CHARSET, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS,")
        lines.append("        DEFAULT_QUALITY, DEFAULT_PITCH | FF_DONTCARE,")
        lines.append("        font_name")
        lines.append("    );")
        lines.append("}")
    
    lines.append("")
    lines.append("} // namespace miko")
    
    return "\n".join(lines)