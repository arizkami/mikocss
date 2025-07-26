#pragma once
#include <unordered_map>
#include <string>
#include "miko_layout.hpp"

namespace miko {

using LayoutProperty = twlayout::LayoutProperty;

inline LayoutProperty get_aspect_ratio(const std::string& name) {
    static const std::unordered_map<std::string, LayoutProperty> aspect_ratio_map = {
        {"auto", twlayout::aspect_auto},
        {"square", twlayout::aspect_square},
        {"video", twlayout::aspect_video},
        {"photo", twlayout::aspect_photo},
        {"portrait", twlayout::aspect_portrait},
        {"wide", twlayout::aspect_wide},
        {"ultrawide", twlayout::aspect_ultrawide},
        {"golden", twlayout::aspect_golden},
    };
    auto it = aspect_ratio_map.find(name);
    return (it != aspect_ratio_map.end()) ? it->second : twlayout::aspect_auto;
}

inline LayoutProperty get_columns(const std::string& name) {
    static const std::unordered_map<std::string, LayoutProperty> columns_map = {
        {"1", twlayout::columns_1},
        {"2", twlayout::columns_2},
        {"3", twlayout::columns_3},
        {"4", twlayout::columns_4},
        {"5", twlayout::columns_5},
        {"6", twlayout::columns_6},
        {"7", twlayout::columns_7},
        {"8", twlayout::columns_8},
        {"9", twlayout::columns_9},
        {"10", twlayout::columns_10},
        {"11", twlayout::columns_11},
        {"12", twlayout::columns_12},
        {"auto", twlayout::columns_auto},
        {"3xs", twlayout::columns_3xs},
        {"2xs", twlayout::columns_2xs},
        {"xs", twlayout::columns_xs},
        {"sm", twlayout::columns_sm},
        {"md", twlayout::columns_md},
        {"lg", twlayout::columns_lg},
        {"xl", twlayout::columns_xl},
        {"2xl", twlayout::columns_2xl},
        {"3xl", twlayout::columns_3xl},
        {"4xl", twlayout::columns_4xl},
        {"5xl", twlayout::columns_5xl},
        {"6xl", twlayout::columns_6xl},
        {"7xl", twlayout::columns_7xl},
    };
    auto it = columns_map.find(name);
    return (it != columns_map.end()) ? it->second : twlayout::columns_1;
}

inline LayoutProperty get_display(const std::string& name) {
    static const std::unordered_map<std::string, LayoutProperty> display_map = {
        {"block", twlayout::display_block},
        {"inline_block", twlayout::display_inline_block},
        {"inline", twlayout::display_inline},
        {"flex", twlayout::display_flex},
        {"inline_flex", twlayout::display_inline_flex},
        {"table", twlayout::display_table},
        {"inline_table", twlayout::display_inline_table},
        {"table_caption", twlayout::display_table_caption},
        {"table_cell", twlayout::display_table_cell},
        {"table_column", twlayout::display_table_column},
        {"table_column_group", twlayout::display_table_column_group},
        {"table_footer_group", twlayout::display_table_footer_group},
        {"table_header_group", twlayout::display_table_header_group},
        {"table_row_group", twlayout::display_table_row_group},
        {"table_row", twlayout::display_table_row},
        {"flow_root", twlayout::display_flow_root},
        {"grid", twlayout::display_grid},
        {"inline_grid", twlayout::display_inline_grid},
        {"contents", twlayout::display_contents},
        {"list_item", twlayout::display_list_item},
        {"hidden", twlayout::display_hidden},
    };
    auto it = display_map.find(name);
    return (it != display_map.end()) ? it->second : twlayout::display_block;
}

inline LayoutProperty get_position(const std::string& name) {
    static const std::unordered_map<std::string, LayoutProperty> position_map = {
        {"static", twlayout::position_static},
        {"fixed", twlayout::position_fixed},
        {"absolute", twlayout::position_absolute},
        {"relative", twlayout::position_relative},
        {"sticky", twlayout::position_sticky},
    };
    auto it = position_map.find(name);
    return (it != position_map.end()) ? it->second : twlayout::position_static;
}

inline LayoutProperty get_overflow(const std::string& name) {
    static const std::unordered_map<std::string, LayoutProperty> overflow_map = {
        {"auto", twlayout::overflow_auto},
        {"hidden", twlayout::overflow_hidden},
        {"clip", twlayout::overflow_clip},
        {"visible", twlayout::overflow_visible},
        {"scroll", twlayout::overflow_scroll},
    };
    auto it = overflow_map.find(name);
    return (it != overflow_map.end()) ? it->second : twlayout::overflow_auto;
}

inline LayoutProperty get_z_index(const std::string& name) {
    static const std::unordered_map<std::string, LayoutProperty> z_index_map = {
        {"0", twlayout::z_0},
        {"10", twlayout::z_10},
        {"20", twlayout::z_20},
        {"30", twlayout::z_30},
        {"40", twlayout::z_40},
        {"50", twlayout::z_50},
        {"auto", twlayout::z_auto},
    };
    auto it = z_index_map.find(name);
    return (it != z_index_map.end()) ? it->second : twlayout::z_0;
}

inline LayoutProperty get_inset(const std::string& name) {
    static const std::unordered_map<std::string, LayoutProperty> inset_map = {
        {"0", twlayout::inset_0},
        {"px", twlayout::inset_px},
        {"0_5", twlayout::inset_0_5},
        {"1", twlayout::inset_1},
        {"1_5", twlayout::inset_1_5},
        {"2", twlayout::inset_2},
        {"2_5", twlayout::inset_2_5},
        {"3", twlayout::inset_3},
        {"3_5", twlayout::inset_3_5},
        {"4", twlayout::inset_4},
        {"5", twlayout::inset_5},
        {"6", twlayout::inset_6},
        {"7", twlayout::inset_7},
        {"8", twlayout::inset_8},
        {"9", twlayout::inset_9},
        {"10", twlayout::inset_10},
        {"11", twlayout::inset_11},
        {"12", twlayout::inset_12},
        {"14", twlayout::inset_14},
        {"16", twlayout::inset_16},
        {"20", twlayout::inset_20},
        {"24", twlayout::inset_24},
        {"28", twlayout::inset_28},
        {"32", twlayout::inset_32},
        {"36", twlayout::inset_36},
        {"40", twlayout::inset_40},
        {"44", twlayout::inset_44},
        {"48", twlayout::inset_48},
        {"52", twlayout::inset_52},
        {"56", twlayout::inset_56},
        {"60", twlayout::inset_60},
        {"64", twlayout::inset_64},
        {"72", twlayout::inset_72},
        {"80", twlayout::inset_80},
        {"96", twlayout::inset_96},
        {"auto", twlayout::inset_auto},
        {"1_2", twlayout::inset_1_2},
        {"1_3", twlayout::inset_1_3},
        {"2_3", twlayout::inset_2_3},
        {"1_4", twlayout::inset_1_4},
        {"2_4", twlayout::inset_2_4},
        {"3_4", twlayout::inset_3_4},
        {"full", twlayout::inset_full},
    };
    auto it = inset_map.find(name);
    return (it != inset_map.end()) ? it->second : twlayout::inset_0;
}


inline std::vector<std::string> get_all_display_types() {
    return {
        "block",
        "inline_block",
        "inline",
        "flex",
        "inline_flex",
        "table",
        "inline_table",
        "table_caption",
        "table_cell",
        "table_column",
        "table_column_group",
        "table_footer_group",
        "table_header_group",
        "table_row_group",
        "table_row",
        "flow_root",
        "grid",
        "inline_grid",
        "contents",
        "list_item",
        "hidden",
    };
}

inline std::vector<std::string> get_all_position_types() {
    return {
        "static",
        "fixed",
        "absolute",
        "relative",
        "sticky",
    };
}

} // namespace miko