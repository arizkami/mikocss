#pragma once
#include <QFont>
#include <QApplication>
#include <unordered_map>
#include <string>
#include "miko_typography.hpp"

namespace miko {

using TextSize = twtypo::TextSize;
using FontWeight = twtypo::FontWeight;

inline TextSize get_text_size(const std::string& name) {
    static const std::unordered_map<std::string, TextSize> size_map = {
        {"xs", twtypo::text_xs},
        {"sm", twtypo::text_sm},
        {"base", twtypo::text_base},
        {"lg", twtypo::text_lg},
        {"xl", twtypo::text_xl},
        {"2xl", twtypo::text_2xl},
        {"3xl", twtypo::text_3xl},
        {"4xl", twtypo::text_4xl},
        {"5xl", twtypo::text_5xl},
        {"6xl", twtypo::text_6xl},
        {"7xl", twtypo::text_7xl},
        {"8xl", twtypo::text_8xl},
        {"9xl", twtypo::text_9xl},
    };
    auto it = size_map.find(name);
    return (it != size_map.end()) ? it->second : twtypo::text_base;
}

inline FontWeight get_font_weight(const std::string& name) {
    static const std::unordered_map<std::string, FontWeight> weight_map = {
        {"thin", twtypo::font_thin},
        {"extralight", twtypo::font_extralight},
        {"light", twtypo::font_light},
        {"semilight", twtypo::font_semilight},
        {"regular", twtypo::font_regular},
        {"medium", twtypo::font_medium},
        {"semibold", twtypo::font_semibold},
        {"bold", twtypo::font_bold},
        {"extrabold", twtypo::font_extrabold},
        {"black", twtypo::font_black},
        {"blackrr", twtypo::font_blackrr},
    };
    auto it = weight_map.find(name);
    return (it != weight_map.end()) ? it->second : twtypo::font_regular;
}

inline QFont create_font(const std::string& size, const std::string& weight, const std::string& family = "sans") {
    auto text_size = get_text_size(size);
    auto font_weight = get_font_weight(weight);
    
    QFont font;
    font.setPointSizeF(text_size.font_size_px * 0.75f); // Convert px to pt
    font.setWeight(QFont::Weight(font_weight.weight));
    
    if (family == "sans") font.setFamily("Arial");
    else if (family == "serif") font.setFamily("Times New Roman");
    else if (family == "mono") font.setFamily("Courier New");
    
    return font;
}

} // namespace miko