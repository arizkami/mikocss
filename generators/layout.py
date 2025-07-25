from layout.base import (
    aspect_ratios, columns, break_values, box_decoration_break, box_sizing,
    display, float_values, clear_values, isolation, object_fit, object_position,
    overflow, overscroll_behavior, position, inset_values, visibility, z_index
)

def generate_layout_hpp(framework="gtk"):
    """Generate C++ header file with layout definitions"""
    lines = []
    lines.append("#pragma once")
    lines.append("#include <string>")
    lines.append("#include <unordered_map>")
    lines.append("#include <vector>\n")
    
    if framework == "gtk":
        lines.append("#include <gtk/gtk.h>")
    elif framework == "qt":
        lines.append("#include <QWidget>")
        lines.append("#include <QLayout>")
    elif framework == "win32":
        lines.append("#include <windows.h>")
    
    lines.append("\nnamespace twlayout {\n")
    
    # Layout property structure
    lines.append("struct LayoutProperty {")
    lines.append("    const char* name;")
    lines.append("    const char* value;")
    lines.append("    const char* css_property;")
    lines.append("};\n")
    
    # Position structure
    lines.append("struct Position {")
    lines.append("    const char* top;")
    lines.append("    const char* right;")
    lines.append("    const char* bottom;")
    lines.append("    const char* left;")
    lines.append("};\n")
    
    # Generate aspect ratio constants
    lines.append("// Aspect Ratios")
    for name, value in aspect_ratios.items():
        var_name = f"aspect_{name}"
        lines.append(f'static constexpr LayoutProperty {var_name} = {{"{name}", "{value}", "aspect-ratio"}};')
    lines.append("")
    
    # Generate column constants
    lines.append("// Columns")
    for name, value in columns.items():
        var_name = f"columns_{name}"
        lines.append(f'static constexpr LayoutProperty {var_name} = {{"{name}", "{value}", "columns"}};')
    lines.append("")
    
    # Generate display constants
    lines.append("// Display")
    for name, value in display.items():
        var_name = f"display_{name}"
        lines.append(f'static constexpr LayoutProperty {var_name} = {{"{name}", "{value}", "display"}};')
    lines.append("")
    
    # Generate position constants
    lines.append("// Position")
    for name, value in position.items():
        var_name = f"position_{name}"
        lines.append(f'static constexpr LayoutProperty {var_name} = {{"{name}", "{value}", "position"}};')
    lines.append("")
    
    # Generate overflow constants
    lines.append("// Overflow")
    for name, value in overflow.items():
        var_name = f"overflow_{name}"
        lines.append(f'static constexpr LayoutProperty {var_name} = {{"{name}", "{value}", "overflow"}};')
    lines.append("")
    
    # Generate z-index constants
    lines.append("// Z-Index")
    for name, value in z_index.items():
        var_name = f"z_{name}"
        lines.append(f'static constexpr LayoutProperty {var_name} = {{"{name}", "{value}", "z-index"}};')
    lines.append("")
    
    # Generate inset constants
    lines.append("// Inset Values")
    for name, value in inset_values.items():
        var_name = f"inset_{name}"
        lines.append(f'static constexpr LayoutProperty {var_name} = {{"{name}", "{value}", "inset"}};')
    lines.append("")
    
    lines.append("} // namespace twlayout")
    
    return "\n".join(lines)

def generate_layout_wrapper_hpp(framework="gtk"):
    """Generate layout wrapper with framework-specific support"""
    lines = []
    lines.append("#pragma once")
    
    if framework == "gtk":
        lines.append("#include <gtk/gtk.h>")
    elif framework == "qt":
        lines.append("#include <QWidget>")
        lines.append("#include <QStyleSheet>")
    elif framework == "win32":
        lines.append("#include <windows.h>")
    
    lines.append("#include <unordered_map>")
    lines.append("#include <string>")
    lines.append("#include \"layout.hpp\"\n")
    lines.append("namespace miko {\n")
    lines.append("using LayoutProperty = twlayout::LayoutProperty;\n")
    
    # Generate lookup functions for each category
    categories = [
        ("aspect_ratio", aspect_ratios, "aspect"),
        ("columns", columns, "columns"),
        ("display", display, "display"),
        ("position", position, "position"),
        ("overflow", overflow, "overflow"),
        ("z_index", z_index, "z"),
        ("inset", inset_values, "inset")
    ]
    
    for func_name, values_dict, prefix in categories:
        lines.append(f"inline LayoutProperty get_{func_name}(const std::string& name) {{")
        lines.append(f"    static const std::unordered_map<std::string, LayoutProperty> {func_name}_map = {{")
        
        for name in values_dict.keys():
            var_name = f"{prefix}_{name}"
            lines.append(f'        {{"{name}", twlayout::{var_name}}},')
        
        lines.append("    };")
        lines.append(f"    auto it = {func_name}_map.find(name);")
        default_var = f"twlayout::{prefix}_{list(values_dict.keys())[0]}"
        lines.append(f"    return (it != {func_name}_map.end()) ? it->second : {default_var};")
        lines.append("}\n")
    
    # Framework-specific style application functions
    if framework == "gtk":
        lines.append("inline void apply_layout_style(GtkWidget* widget, const std::string& css_class) {")
        lines.append("    GtkStyleContext* context = gtk_widget_get_style_context(widget);")
        lines.append("    gtk_style_context_add_class(context, css_class.c_str());")
        lines.append("}")
        lines.append("")
        lines.append("inline void set_widget_position(GtkWidget* widget, const std::string& pos_type) {")
        lines.append("    auto pos = get_position(pos_type);")
        lines.append("    // GTK positioning through CSS classes or manual positioning")
        lines.append("    if (pos_type == \"fixed\" || pos_type == \"absolute\") {")
        lines.append("        gtk_widget_set_halign(widget, GTK_ALIGN_START);")
        lines.append("        gtk_widget_set_valign(widget, GTK_ALIGN_START);")
        lines.append("    }")
        lines.append("}")
        
    elif framework == "qt":
        lines.append("inline void apply_layout_style(QWidget* widget, const std::string& property, const std::string& value) {")
        lines.append("    QString styleSheet = widget->styleSheet();")
        lines.append("    styleSheet += QString::fromStdString(property + \": \" + value + \";\");")
        lines.append("    widget->setStyleSheet(styleSheet);")
        lines.append("}")
        lines.append("")
        lines.append("inline void set_widget_display(QWidget* widget, const std::string& display_type) {")
        lines.append("    auto disp = get_display(display_type);")
        lines.append("    if (display_type == \"hidden\") {")
        lines.append("        widget->hide();")
        lines.append("    } else {")
        lines.append("        widget->show();")
        lines.append("        apply_layout_style(widget, \"display\", disp.value);")
        lines.append("    }")
        lines.append("}")
        
    elif framework == "win32":
        lines.append("inline void set_window_position(HWND hwnd, const std::string& pos_type, int x, int y, int width, int height) {")
        lines.append("    auto pos = get_position(pos_type);")
        lines.append("    UINT flags = SWP_NOZORDER;")
        lines.append("    ")
        lines.append("    if (pos_type == \"fixed\" || pos_type == \"absolute\") {")
        lines.append("        SetWindowPos(hwnd, NULL, x, y, width, height, flags);")
        lines.append("    } else if (pos_type == \"relative\") {")
        lines.append("        RECT rect;")
        lines.append("        GetWindowRect(hwnd, &rect);")
        lines.append("        SetWindowPos(hwnd, NULL, rect.left + x, rect.top + y, width, height, flags);")
        lines.append("    }")
        lines.append("}")
        lines.append("")
        lines.append("inline void set_window_visibility(HWND hwnd, const std::string& visibility_type) {")
        lines.append("    if (visibility_type == \"visible\") {")
        lines.append("        ShowWindow(hwnd, SW_SHOW);")
        lines.append("    } else if (visibility_type == \"invisible\") {")
        lines.append("        ShowWindow(hwnd, SW_HIDE);")
        lines.append("    }")
        lines.append("}")
    
    lines.append("")
    
    # Utility functions
    lines.append("inline std::vector<std::string> get_all_display_types() {")
    lines.append("    return {")
    for name in display.keys():
        lines.append(f'        "{name}",')
    lines.append("    };")
    lines.append("}")
    lines.append("")
    
    lines.append("inline std::vector<std::string> get_all_position_types() {")
    lines.append("    return {")
    for name in position.keys():
        lines.append(f'        "{name}",')
    lines.append("    };")
    lines.append("}")
    lines.append("")
    
    lines.append("} // namespace miko")
    
    return "\n".join(lines)