#pragma once
#include <string>
#include <unordered_map>
#include <vector>


namespace twlayout {

struct LayoutProperty {
    const char* name;
    const char* value;
    const char* css_property;
};

struct Position {
    const char* top;
    const char* right;
    const char* bottom;
    const char* left;
};

// Aspect Ratios
static constexpr LayoutProperty aspect_auto = {"auto", "auto", "aspect-ratio"};
static constexpr LayoutProperty aspect_square = {"square", "1 / 1", "aspect-ratio"};
static constexpr LayoutProperty aspect_video = {"video", "16 / 9", "aspect-ratio"};
static constexpr LayoutProperty aspect_photo = {"photo", "4 / 3", "aspect-ratio"};
static constexpr LayoutProperty aspect_portrait = {"portrait", "3 / 4", "aspect-ratio"};
static constexpr LayoutProperty aspect_wide = {"wide", "21 / 9", "aspect-ratio"};
static constexpr LayoutProperty aspect_ultrawide = {"ultrawide", "32 / 9", "aspect-ratio"};
static constexpr LayoutProperty aspect_golden = {"golden", "1.618 / 1", "aspect-ratio"};

// Columns
static constexpr LayoutProperty columns_1 = {"1", "1", "columns"};
static constexpr LayoutProperty columns_2 = {"2", "2", "columns"};
static constexpr LayoutProperty columns_3 = {"3", "3", "columns"};
static constexpr LayoutProperty columns_4 = {"4", "4", "columns"};
static constexpr LayoutProperty columns_5 = {"5", "5", "columns"};
static constexpr LayoutProperty columns_6 = {"6", "6", "columns"};
static constexpr LayoutProperty columns_7 = {"7", "7", "columns"};
static constexpr LayoutProperty columns_8 = {"8", "8", "columns"};
static constexpr LayoutProperty columns_9 = {"9", "9", "columns"};
static constexpr LayoutProperty columns_10 = {"10", "10", "columns"};
static constexpr LayoutProperty columns_11 = {"11", "11", "columns"};
static constexpr LayoutProperty columns_12 = {"12", "12", "columns"};
static constexpr LayoutProperty columns_auto = {"auto", "auto", "columns"};
static constexpr LayoutProperty columns_3xs = {"3xs", "16rem", "columns"};
static constexpr LayoutProperty columns_2xs = {"2xs", "18rem", "columns"};
static constexpr LayoutProperty columns_xs = {"xs", "20rem", "columns"};
static constexpr LayoutProperty columns_sm = {"sm", "24rem", "columns"};
static constexpr LayoutProperty columns_md = {"md", "28rem", "columns"};
static constexpr LayoutProperty columns_lg = {"lg", "32rem", "columns"};
static constexpr LayoutProperty columns_xl = {"xl", "36rem", "columns"};
static constexpr LayoutProperty columns_2xl = {"2xl", "42rem", "columns"};
static constexpr LayoutProperty columns_3xl = {"3xl", "48rem", "columns"};
static constexpr LayoutProperty columns_4xl = {"4xl", "56rem", "columns"};
static constexpr LayoutProperty columns_5xl = {"5xl", "64rem", "columns"};
static constexpr LayoutProperty columns_6xl = {"6xl", "72rem", "columns"};
static constexpr LayoutProperty columns_7xl = {"7xl", "80rem", "columns"};

// Display
static constexpr LayoutProperty display_block = {"block", "block", "display"};
static constexpr LayoutProperty display_inline_block = {"inline_block", "inline-block", "display"};
static constexpr LayoutProperty display_inline = {"inline", "inline", "display"};
static constexpr LayoutProperty display_flex = {"flex", "flex", "display"};
static constexpr LayoutProperty display_inline_flex = {"inline_flex", "inline-flex", "display"};
static constexpr LayoutProperty display_table = {"table", "table", "display"};
static constexpr LayoutProperty display_inline_table = {"inline_table", "inline-table", "display"};
static constexpr LayoutProperty display_table_caption = {"table_caption", "table-caption", "display"};
static constexpr LayoutProperty display_table_cell = {"table_cell", "table-cell", "display"};
static constexpr LayoutProperty display_table_column = {"table_column", "table-column", "display"};
static constexpr LayoutProperty display_table_column_group = {"table_column_group", "table-column-group", "display"};
static constexpr LayoutProperty display_table_footer_group = {"table_footer_group", "table-footer-group", "display"};
static constexpr LayoutProperty display_table_header_group = {"table_header_group", "table-header-group", "display"};
static constexpr LayoutProperty display_table_row_group = {"table_row_group", "table-row-group", "display"};
static constexpr LayoutProperty display_table_row = {"table_row", "table-row", "display"};
static constexpr LayoutProperty display_flow_root = {"flow_root", "flow-root", "display"};
static constexpr LayoutProperty display_grid = {"grid", "grid", "display"};
static constexpr LayoutProperty display_inline_grid = {"inline_grid", "inline-grid", "display"};
static constexpr LayoutProperty display_contents = {"contents", "contents", "display"};
static constexpr LayoutProperty display_list_item = {"list_item", "list-item", "display"};
static constexpr LayoutProperty display_hidden = {"hidden", "none", "display"};

// Position
static constexpr LayoutProperty position_static = {"static", "static", "position"};
static constexpr LayoutProperty position_fixed = {"fixed", "fixed", "position"};
static constexpr LayoutProperty position_absolute = {"absolute", "absolute", "position"};
static constexpr LayoutProperty position_relative = {"relative", "relative", "position"};
static constexpr LayoutProperty position_sticky = {"sticky", "sticky", "position"};

// Overflow
static constexpr LayoutProperty overflow_auto = {"auto", "auto", "overflow"};
static constexpr LayoutProperty overflow_hidden = {"hidden", "hidden", "overflow"};
static constexpr LayoutProperty overflow_clip = {"clip", "clip", "overflow"};
static constexpr LayoutProperty overflow_visible = {"visible", "visible", "overflow"};
static constexpr LayoutProperty overflow_scroll = {"scroll", "scroll", "overflow"};

// Z-Index
static constexpr LayoutProperty z_0 = {"0", "0", "z-index"};
static constexpr LayoutProperty z_10 = {"10", "10", "z-index"};
static constexpr LayoutProperty z_20 = {"20", "20", "z-index"};
static constexpr LayoutProperty z_30 = {"30", "30", "z-index"};
static constexpr LayoutProperty z_40 = {"40", "40", "z-index"};
static constexpr LayoutProperty z_50 = {"50", "50", "z-index"};
static constexpr LayoutProperty z_auto = {"auto", "auto", "z-index"};

// Inset Values
static constexpr LayoutProperty inset_0 = {"0", "0px", "inset"};
static constexpr LayoutProperty inset_px = {"px", "1px", "inset"};
static constexpr LayoutProperty inset_0_5 = {"0_5", "0.125rem", "inset"};
static constexpr LayoutProperty inset_1 = {"1", "0.25rem", "inset"};
static constexpr LayoutProperty inset_1_5 = {"1_5", "0.375rem", "inset"};
static constexpr LayoutProperty inset_2 = {"2", "0.5rem", "inset"};
static constexpr LayoutProperty inset_2_5 = {"2_5", "0.625rem", "inset"};
static constexpr LayoutProperty inset_3 = {"3", "0.75rem", "inset"};
static constexpr LayoutProperty inset_3_5 = {"3_5", "0.875rem", "inset"};
static constexpr LayoutProperty inset_4 = {"4", "1rem", "inset"};
static constexpr LayoutProperty inset_5 = {"5", "1.25rem", "inset"};
static constexpr LayoutProperty inset_6 = {"6", "1.5rem", "inset"};
static constexpr LayoutProperty inset_7 = {"7", "1.75rem", "inset"};
static constexpr LayoutProperty inset_8 = {"8", "2rem", "inset"};
static constexpr LayoutProperty inset_9 = {"9", "2.25rem", "inset"};
static constexpr LayoutProperty inset_10 = {"10", "2.5rem", "inset"};
static constexpr LayoutProperty inset_11 = {"11", "2.75rem", "inset"};
static constexpr LayoutProperty inset_12 = {"12", "3rem", "inset"};
static constexpr LayoutProperty inset_14 = {"14", "3.5rem", "inset"};
static constexpr LayoutProperty inset_16 = {"16", "4rem", "inset"};
static constexpr LayoutProperty inset_20 = {"20", "5rem", "inset"};
static constexpr LayoutProperty inset_24 = {"24", "6rem", "inset"};
static constexpr LayoutProperty inset_28 = {"28", "7rem", "inset"};
static constexpr LayoutProperty inset_32 = {"32", "8rem", "inset"};
static constexpr LayoutProperty inset_36 = {"36", "9rem", "inset"};
static constexpr LayoutProperty inset_40 = {"40", "10rem", "inset"};
static constexpr LayoutProperty inset_44 = {"44", "11rem", "inset"};
static constexpr LayoutProperty inset_48 = {"48", "12rem", "inset"};
static constexpr LayoutProperty inset_52 = {"52", "13rem", "inset"};
static constexpr LayoutProperty inset_56 = {"56", "14rem", "inset"};
static constexpr LayoutProperty inset_60 = {"60", "15rem", "inset"};
static constexpr LayoutProperty inset_64 = {"64", "16rem", "inset"};
static constexpr LayoutProperty inset_72 = {"72", "18rem", "inset"};
static constexpr LayoutProperty inset_80 = {"80", "20rem", "inset"};
static constexpr LayoutProperty inset_96 = {"96", "24rem", "inset"};
static constexpr LayoutProperty inset_auto = {"auto", "auto", "inset"};
static constexpr LayoutProperty inset_1_2 = {"1_2", "50%", "inset"};
static constexpr LayoutProperty inset_1_3 = {"1_3", "33.333333%", "inset"};
static constexpr LayoutProperty inset_2_3 = {"2_3", "66.666667%", "inset"};
static constexpr LayoutProperty inset_1_4 = {"1_4", "25%", "inset"};
static constexpr LayoutProperty inset_2_4 = {"2_4", "50%", "inset"};
static constexpr LayoutProperty inset_3_4 = {"3_4", "75%", "inset"};
static constexpr LayoutProperty inset_full = {"full", "100%", "inset"};

} // namespace twlayout