#include <iostream>
#include "miko_color.hpp"
#include "miko_wrapper.hpp"
#include "miko_typography.hpp"
#include "miko_typography_wrapper.hpp"
#include "miko_layout.hpp"
#include "miko_layout_wrapper.hpp"
#include <QApplication>
#include <QWidget>
#include <QLabel>
#include <QVBoxLayout>

int main(int argc, char* argv[]) {
    QApplication app(argc, argv);
    
    // Example: Using MikoCSS colors
    auto blue = miko::get_color("blue-500");
    auto qt_color = miko::to_qt_color("blue-500");
    
    // Example: Using MikoCSS typography
    auto large_size = miko::get_text_size("lg");
    auto bold_weight = miko::get_font_weight("bold");
    
    // Example: Using MikoCSS layout
    auto flex_display = miko::get_display("flex");
    
    QWidget window;
    QVBoxLayout* layout = new QVBoxLayout(&window);
    QLabel* label = new QLabel("MikoCSS Qt5 Project initialized!");
    
    label->setStyleSheet(QString("color: rgb(%1, %2, %3); font-size: %4px; font-weight: %5;")
                        .arg(blue.r).arg(blue.g).arg(blue.b)
                        .arg(large_size.font_size_px).arg(bold_weight.weight));
    
    layout->addWidget(label);
    window.show();
    
    return app.exec();
}