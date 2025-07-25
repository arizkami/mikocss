import argparse
import sys
import os
from core.processor import ColorProcessor

def show_usage():
    """Display usage information and examples"""
    print("🎨 MikoCSS Generator")
    print("=" * 50)
    print("Generate C++ libraries for colors, typography, and layout\n")
    
    print("📋 Commands:")
    print("  init -p <framework>     Initialize C++ project with all styling files")
    print("  generate                Generate styling files (legacy mode)\n")
    
    print("🎯 Frameworks:")
    print("  gtk    - Generate GTK/GDK compatible code")
    print("  qt5    - Generate Qt5 compatible code")
    print("  qt6    - Generate Qt6 compatible code")
    print("  win32  - Generate Win32/COLORREF compatible code\n")
    
    print("💡 Examples:")
    print("  python main.py init -p gtk")
    print("  python main.py init -p qt5 --output ./include")
    print("  python main.py init -p qt6 --output ./include")
    print("  python main.py --cppframework qt5 --output ./build\n")
    
    print("📦 Generated files:")
    print("  • miko_color.hpp, miko_wrapper.hpp, miko_color_list.txt")
    print("  • miko_typography.hpp, miko_typography_wrapper.hpp")
    print("  • miko_layout.hpp, miko_layout_wrapper.hpp\n")
    
    print("🔧 For detailed help: python main.py --help")

def init_project(framework, output_dir):
    """Initialize a C++ project with all MikoCSS styling files"""
    print("🚀 Initializing MikoCSS C++ Project")
    print("=" * 50)
    print(f"🎯 Target Framework: {framework.upper()}")
    print(f"📁 Output Directory: {os.path.abspath(output_dir)}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize processor with framework
    processor = ColorProcessor(framework=framework)
    
    # Process all colors
    print("\n🎨 Processing colors...")
    all_colors = processor.process_colors()
    
    # Generate C++ files
    print("📝 Generating C++ files...")
    files = processor.generate_cpp_files(output_dir)
    
    # Display statistics
    stats = processor.get_color_stats()
    
    print(f"\n✅ Project initialized successfully!")
    print(f"\n📄 Generated files:")
    for file_type, path in files.items():
        print(f"   • {file_type}: {path}")
    
    print(f"\n🎯 Project statistics:")
    print(f"   • {stats['total_families']} base color families")
    print(f"   • ~38 variations per family (standard + micro + variants)")
    print(f"   • Total: {stats['total_colors']} unique colors")
    
    # Generate a simple CMakeLists.txt template
    cmake_content = f"""# MikoCSS C++ Project
cmake_minimum_required(VERSION 3.10)
project(MikoCSSProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include MikoCSS headers
include_directories(${{CMAKE_CURRENT_SOURCE_DIR}})

# Find required packages based on framework
"""
    
    if framework == "gtk":
        cmake_content += """find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK3 REQUIRED gtk+-3.0)

include_directories(${GTK3_INCLUDE_DIRS})
link_directories(${GTK3_LIBRARY_DIRS})
add_definitions(${GTK3_CFLAGS_OTHER})
"""
    elif framework == "qt5":
        cmake_content += """find_package(Qt5 REQUIRED COMPONENTS Core Widgets Gui)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
"""
    elif framework == "qt6":
        cmake_content += """find_package(Qt6 REQUIRED COMPONENTS Core Widgets Gui)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
"""
    elif framework == "win32":
        cmake_content += """# Win32 libraries are automatically linked
"""
    
    cmake_content += f"""
# Example executable
add_executable(example main.cpp)
"""
    
    if framework == "gtk":
        cmake_content += "target_link_libraries(example ${GTK3_LIBRARIES})\n"
    elif framework == "qt5":
        cmake_content += "target_link_libraries(example Qt5::Core Qt5::Widgets Qt5::Gui)\n"
    elif framework == "qt6":
        cmake_content += "target_link_libraries(example Qt6::Core Qt6::Widgets Qt6::Gui)\n"
    
    cmake_path = os.path.join(output_dir, "CMakeLists.txt")
    with open(cmake_path, 'w') as f:
        f.write(cmake_content)
    
    # Generate example main.cpp
    example_content = f"""#include <iostream>
#include "miko_color.hpp"
#include "miko_wrapper.hpp"
#include "miko_typography.hpp"
#include "miko_typography_wrapper.hpp"
#include "miko_layout.hpp"
#include "miko_layout_wrapper.hpp"
"""
    
    if framework == "gtk":
        example_content += """#include <gtk/gtk.h>

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
}"""
    elif framework in ["qt5", "qt6"]:
        qt_version = "5" if framework == "qt5" else "6"
        example_content += f"""#include <QApplication>
#include <QWidget>
#include <QLabel>
#include <QVBoxLayout>

int main(int argc, char* argv[]) {{
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
    QLabel* label = new QLabel("MikoCSS Qt{qt_version} Project initialized!");
    
    label->setStyleSheet(QString("color: rgb(%1, %2, %3); font-size: %4px; font-weight: %5;")
                        .arg(blue.r).arg(blue.g).arg(blue.b)
                        .arg(large_size.font_size_px).arg(bold_weight.weight));
    
    layout->addWidget(label);
    window.show();
    
    return app.exec();
}}"""
    elif framework == "win32":
        example_content += """#include <windows.h>
#include <iostream>

int main() {
    // Example: Using MikoCSS colors
    auto blue = miko::get_color("blue-500");
    auto colorref = miko::to_colorref("blue-500");
    
    // Example: Using MikoCSS typography
    auto large_size = miko::get_text_size("lg");
    auto bold_weight = miko::get_font_weight("bold");
    
    // Example: Using MikoCSS layout
    auto flex_display = miko::get_display("flex");
    
    std::cout << "MikoCSS Win32 Project initialized!" << std::endl;
    std::cout << "Blue-500: R=" << (int)blue.r << ", G=" << (int)blue.g << ", B=" << (int)blue.b << std::endl;
    std::cout << "COLORREF: 0x" << std::hex << colorref << std::endl;
    
    return 0;
}"""
    
    example_path = os.path.join(output_dir, "main.cpp")
    with open(example_path, 'w') as f:
        f.write(example_content)
    
    print(f"\n📄 Additional files created:")
    print(f"   • CMakeLists.txt: {cmake_path}")
    print(f"   • main.cpp: {example_path}")
    
    print(f"\n🔨 Build instructions:")
    print(f"   mkdir build && cd build")
    print(f"   cmake ..")
    print(f"   make  # or cmake --build .")
    
    print(f"\n💡 Next steps:")
    print(f"   1. Include the generated headers in your C++ project")
    print(f"   2. Use the miko:: namespace for styling utilities")
    print(f"   3. Build and run the example with the provided CMakeLists.txt")

def main():
    """Main entry point for MikoCSS generator"""
    # Check if no arguments provided
    if len(sys.argv) == 1:
        show_usage()
        return
    
    # Create main parser
    parser = argparse.ArgumentParser(
        description="MikoCSS Generator - Generate C++ libraries for colors, typography, and layout",
        prog="main.py"
    )
    
    # Create subparsers for commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Init command
    init_parser = subparsers.add_parser('init', help='Initialize C++ project with styling files')
    init_parser.add_argument(
        '-p', '--project',
        choices=["gtk", "qt5", "qt6", "win32"],
        required=True,
        help="Target C++ framework for the project"
    )
    init_parser.add_argument(
        '--output',
        default=".",
        help="Output directory for project files (default: current directory)"
    )
    
    # Legacy generate mode (backward compatibility)
    parser.add_argument(
        "--cppframework",
        choices=["gtk", "qt5", "qt6", "win32"],
        help="Target C++ framework for generation (legacy mode)"
    )
    parser.add_argument(
        "--output",
        default=".",
        help="Output directory for generated files (default: current directory)"
    )
    
    args = parser.parse_args()
    
    # Handle init command
    if args.command == 'init':
        init_project(args.project, args.output)
        return
    
    # Handle legacy mode
    if args.cppframework:
        print("🎨 MikoCSS Complete Generator")
        print("=" * 50)
        print(f"🎯 Target Framework: {args.cppframework.upper()}")
        
        # Initialize processor with framework
        processor = ColorProcessor(framework=args.cppframework)
        
        # Process all colors
        all_colors = processor.process_colors()
        
        # Generate C++ files
        files = processor.generate_cpp_files(args.output)
        
        # Display statistics
        stats = processor.get_color_stats()
        
        print(f"\n✅ Generated files:")
        for file_type, path in files.items():
            print(f"   📄 {file_type}: {path}")
        
        print(f"\n🎯 Color breakdown:")
        print(f"   - {stats['total_families']} base color families")
        print(f"   - ~38 variations per family (standard + micro + variants)")
        print(f"   - Total: {stats['total_colors']} unique colors")
        
        print(f"\n💡 Example usage ({args.cppframework}):")
        print(f"\n🎨 Colors:")
        if args.cppframework == "gtk":
            print(f'   miko::get_color("blue-500")      // Standard shade')
            print(f'   miko::to_gdk_color("blue-425")   // GDK RGBA conversion')
        elif args.cppframework in ["qt5", "qt6"]:
            print(f'   miko::get_color("blue-500")      // Standard shade')
            print(f'   miko::to_qt_color("blue-425")    // QColor conversion')
        elif args.cppframework == "win32":
            print(f'   miko::get_color("blue-500")      // Standard shade')
            print(f'   miko::to_colorref("blue-425")    // COLORREF conversion')
        
        print(f"\n✍️ Typography:")
        print(f'   miko::get_text_size("lg")         // Large text size')
        print(f'   miko::get_font_weight("bold")     // Bold font weight')
        if args.cppframework == "gtk":
            print(f'   miko::create_font("xl", "semibold", "sans") // Pango font')
        elif args.cppframework in ["qt5", "qt6"]:
            print(f'   miko::create_font("xl", "semibold", "sans") // QFont')
        elif args.cppframework == "win32":
            print(f'   miko::create_font("xl", "semibold", "sans") // HFONT')
        
        print(f"\n📐 Layout:")
        print(f'   miko::get_display("flex")         // Flex display')
        print(f'   miko::get_position("absolute")    // Absolute positioning')
        print(f'   miko::get_overflow("hidden")      // Hidden overflow')
        print(f'   miko::get_aspect_ratio("video")   // 16:9 aspect ratio')
        if args.cppframework == "gtk":
            print(f'   miko::apply_layout_style(widget, "flex-container") // GTK CSS')
        elif args.cppframework in ["qt5", "qt6"]:
            print(f'   miko::set_widget_display(widget, "flex") // Qt styling')
        elif args.cppframework == "win32":
            print(f'   miko::set_window_position(hwnd, "fixed", 100, 100, 800, 600) // Win32')
        
        print(f"\n📏 Available utilities:")
        print(f"   • Text sizes: xs, sm, base, lg, xl, 2xl, 3xl, 4xl, 5xl, 6xl, 7xl, 8xl, 9xl")
        print(f"   • Font weights: thin, extralight, light, semilight, regular, medium, semibold, bold, extrabold, black, blackrr")
        print(f"   • Display: block, inline, flex, grid, table, hidden, etc.")
        print(f"   • Position: static, relative, absolute, fixed, sticky")
        print(f"   • Aspect ratios: square, video, photo, portrait, wide, ultrawide, golden")
        print(f"   • Overflow: auto, hidden, clip, visible, scroll")
        print(f"   • Z-index: 0, 10, 20, 30, 40, 50, auto")
        return
    
    # If no valid command or framework specified, show usage
    show_usage()

if __name__ == "__main__":
    main()