#include <iostream>
#include "miko_color.hpp"
#include "miko_wrapper.hpp"
#include "miko_typography.hpp"
#include "miko_typography_wrapper.hpp"
#include "miko_layout.hpp"
#include "miko_layout_wrapper.hpp"
#include <gtk/gtk.h>

int main(int argc, char* argv[]) {
    gtk_init(&argc, &argv);
    
    // Example: Using MikoCSS colors
    auto blue = miko::get_color("blue-500");
    auto gdk_color = miko::to_gdk_color("blue-500");
    
    // Example: Using MikoCSS typography
    auto large_size = miko::get_text_size("lg");
    auto bold_weight = miko::get_font_weight("bold");
    
    // Example: Using MikoCSS layout
    auto flex_display = miko::get_display("flex");
    
    std::cout << "MikoCSS GTK Project initialized!" << std::endl;
    std::cout << "Blue-500: R=" << (int)blue.r << ", G=" << (int)blue.g << ", B=" << (int)blue.b << std::endl;
    
    return 0;
}