#pragma once
#include <string>
#include <unordered_map>
#include <vector>

#include <QFont>
#include <QFontMetrics>

namespace twtypo {

struct TextSize {
    float font_size_px;
    float line_height_px;
    const char* font_size_rem;
    const char* line_height_rem;
};

struct FontWeight {
    int weight;
    const char* name;
};

// Text Sizes
static constexpr TextSize text_xs = {
    12.0f, 16.0f,
    "0.75rem", "1rem"
};
static constexpr TextSize text_sm = {
    14.0f, 20.0f,
    "0.875rem", "1.25rem"
};
static constexpr TextSize text_base = {
    16.0f, 24.0f,
    "1rem", "1.5rem"
};
static constexpr TextSize text_lg = {
    18.0f, 28.0f,
    "1.125rem", "1.75rem"
};
static constexpr TextSize text_xl = {
    20.0f, 28.0f,
    "1.25rem", "1.75rem"
};
static constexpr TextSize text_2xl = {
    24.0f, 32.0f,
    "1.5rem", "2rem"
};
static constexpr TextSize text_3xl = {
    30.0f, 36.0f,
    "1.875rem", "2.25rem"
};
static constexpr TextSize text_4xl = {
    36.0f, 40.0f,
    "2.25rem", "2.5rem"
};
static constexpr TextSize text_5xl = {
    48.0f, 48.0f,
    "3rem", "1"
};
static constexpr TextSize text_6xl = {
    60.0f, 60.0f,
    "3.75rem", "1"
};
static constexpr TextSize text_7xl = {
    72.0f, 72.0f,
    "4.5rem", "1"
};
static constexpr TextSize text_8xl = {
    96.0f, 96.0f,
    "6rem", "1"
};
static constexpr TextSize text_9xl = {
    128.0f, 128.0f,
    "8rem", "1"
};

// Font Weights
static constexpr FontWeight font_thin = {100, "thin"};
static constexpr FontWeight font_extralight = {200, "extralight"};
static constexpr FontWeight font_light = {300, "light"};
static constexpr FontWeight font_semilight = {350, "semilight"};
static constexpr FontWeight font_regular = {400, "regular"};
static constexpr FontWeight font_medium = {500, "medium"};
static constexpr FontWeight font_semibold = {600, "semibold"};
static constexpr FontWeight font_bold = {700, "bold"};
static constexpr FontWeight font_extrabold = {800, "extrabold"};
static constexpr FontWeight font_black = {900, "black"};
static constexpr FontWeight font_blackrr = {950, "blackrr"};

} // namespace twtypo