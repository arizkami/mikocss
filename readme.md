<div align="center">

# MikoCSS

<p align="center">
  <strong>A powerful C++ styling library generator that brings modern CSS-like utilities to C++ GUI frameworks</strong>
</p>

<p align="center">
  <a href="https://github.com/arizkami/mikocss/releases">
    <img src="https://img.shields.io/github/v/release/arizkami/mikocss?include_prereleases&sort=semver" alt="Latest Release">
  </a>
  <a href="https://github.com/arizkami/mikocss/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/arizkami/mikocss" alt="License">
  </a>
  <a href="https://github.com/arizkami/mikocss">
    <img src="https://img.shields.io/github/stars/arizkami/mikocss?style=social" alt="GitHub Stars">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/C%2B%2B-17%2B-blue.svg" alt="C++ 17+">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue.svg" alt="Python 3.7+">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg" alt="Platform Support">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Framework-GTK-orange.svg" alt="GTK Support">
  <img src="https://img.shields.io/badge/Framework-Qt5%2FQt6-green.svg" alt="Qt Support">
  <img src="https://img.shields.io/badge/Framework-Win32-blue.svg" alt="Win32 Support">
</p>

<p align="center">
  <em>Generate comprehensive header files with colors, typography, layout utilities, and framework-specific wrappers for GTK, Qt5, Qt6, and Win32.</em>
</p>

</div>

---

## 🚀 Features

<table>
<tr>
<td width="50%">

### 🎨 **Comprehensive Color System**
- **256+ base colors** with full shade ranges (50-950)
- **8K+ total color variations** including micro-shades and variants
- **Extended color families**: slate, gray, zinc, neutral, stone, red, orange, amber, yellow, lime, green, emerald, teal, cyan, sky, blue, indigo, violet, purple, fuchsia, pink, rose
- **Saturation and temperature variants** for fine-tuned color control
- **Framework-specific color conversions** (GDK RGBA, QColor, COLORREF)

### ✍️ **Typography System**
- **13 text sizes**: xs, sm, base, lg, xl, 2xl, 3xl, 4xl, 5xl, 6xl, 7xl, 8xl, 9xl
- **11 font weights**: thin, extralight, light, semilight, regular, medium, semibold, bold, extrabold, black, blackrr
- **Font families**: sans, serif, mono, display, body
- **Text utilities**: alignment, decoration, transform, overflow, line clamping
- **Framework-specific font creation** (Pango, QFont, HFONT)

</td>
<td width="50%">

### 📐 **Layout System**
- **Display utilities**: block, inline, flex, grid, table, hidden, etc.
- **Position utilities**: static, relative, absolute, fixed, sticky
- **Flexbox utilities**: direction, wrap, justify, align, gap
- **Grid utilities**: template columns/rows, gap, placement
- **Spacing utilities**: padding, margin, space-between with full scale
- **Sizing utilities**: width, height, min/max dimensions
- **Overflow, visibility, and z-index controls**

### 🎯 **Multi-Framework Support**
- **GTK 3+**: GDK color conversion, Pango fonts, CSS styling
- **Qt5/Qt6**: QColor conversion, QFont creation, widget styling
- **Win32**: COLORREF conversion, HFONT creation, window positioning
- **Cross-platform compatibility** with consistent APIs

</td>
</tr>
</table>

## 📦 Installation

### Prerequisites
- Python 3.7+
- C++ compiler with C++17 support
- Target framework libraries (GTK, Qt, or Win32 SDK)

### Quick Start

<details>
<summary><strong>📋 Step-by-step installation</strong></summary>

1. **Clone the repository:**
```bash
git clone https://github.com/arizkami/mikocss.git
cd mikocss
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Generate C++ project:**
```bash
python main.py init -p gtk --output my_project
```

</details>

## 🛠️ Usage

### Command Line Interface

<div align="center">

| Framework | Command | Description |
|-----------|---------|-------------|
| **GTK** | `python main.py init -p gtk --output gtk_project` | Generate GTK project |
| **Qt5** | `python main.py init -p qt5 --output qt5_project` | Generate Qt5 project |
| **Qt6** | `python main.py init -p qt6 --output qt6_project` | Generate Qt6 project |
| **Win32** | `python main.py init -p win32 --output win32_project` | Generate Win32 project |

</div>

#### Legacy Generation Mode
```bash
# Generate only header files
python main.py --cppframework gtk --output headers/
```

### Generated Files

<div align="center">

| File | Description |
|------|-------------|
| `miko_color.hpp` | Core color definitions |
| `miko_wrapper.hpp` | Framework-specific color utilities |
| `miko_typography.hpp` | Typography definitions |
| `miko_typography_wrapper.hpp` | Framework-specific typography utilities |
| `miko_layout.hpp` | Layout utilities |
| `miko_layout_wrapper.hpp` | Framework-specific layout utilities |
| `miko_color_list.txt` | Complete color reference |
| `CMakeLists.txt` | Build configuration |
| `main.cpp` | Example implementation |

</div>

## 💻 Code Examples

<details>
<summary><strong>🖥️ GTK Example</strong></summary>

```cpp
#include "miko_color.hpp"
#include "miko_wrapper.hpp"
#include "miko_typography.hpp"
#include "miko_layout.hpp"
#include <gtk/gtk.h>

int main(int argc, char* argv[]) {
    gtk_init(&argc, &argv);
    
    // Colors
    auto blue = miko::get_color("blue-500");
    auto gdk_color = miko::to_gdk_color("blue-500");
    
    // Typography
    auto large_size = miko::get_text_size("lg");
    auto bold_weight = miko::get_font_weight("bold");
    auto font = miko::create_font("xl", "semibold", "sans");
    
    // Layout
    auto flex_display = miko::get_display("flex");
    miko::apply_layout_style(widget, "flex-container");
    
    return 0;
}
```

</details>

<details>
<summary><strong>🔷 Qt Example</strong></summary>

```cpp
#include "miko_color.hpp"
#include "miko_wrapper.hpp"
#include "miko_typography.hpp"
#include <QApplication>
#include <QWidget>
#include <QLabel>

int main(int argc, char* argv[]) {
    QApplication app(argc, argv);
    
    // Colors
    auto blue = miko::get_color("blue-500");
    auto qt_color = miko::to_qt_color("blue-500");
    
    // Typography
    auto font = miko::create_font("lg", "bold", "sans");
    
    // Layout
    miko::set_widget_display(widget, "flex");
    
    return app.exec();
}
```

</details>

<details>
<summary><strong>🪟 Win32 Example</strong></summary>

```cpp
#include "miko_color.hpp"
#include "miko_wrapper.hpp"
#include "miko_typography.hpp"
#include <windows.h>

int main() {
    // Colors
    auto blue = miko::get_color("blue-500");
    auto colorref = miko::to_colorref("blue-500");
    
    // Typography
    auto font = miko::create_font("lg", "bold", "sans");
    
    // Layout
    miko::set_window_position(hwnd, "fixed", 100, 100, 800, 600);
    
    return 0;
}
```

</details>

## 🏗️ Building Your Project

```bash
# Navigate to your generated project
cd my_project

# Create build directory
mkdir build && cd build

# Configure with CMake
cmake ..

# Build
make  # or cmake --build .

# Run example
./example
```

## 📚 Available Utilities

<div align="center">

<table>
<tr>
<th>🎨 Colors</th>
<th>✍️ Typography</th>
<th>📐 Layout</th>
</tr>
<tr>
<td>

- **Base families**: 20+ color families
- **Shades**: 50-950 range
- **Micro-shades**: 425, 475, 525, 575
- **Variants**: saturated, desaturated, warm, cool

</td>
<td>

- **Sizes**: xs (12px) to 9xl (128px)
- **Weights**: 100 (thin) to 950 (blackrr)
- **Families**: sans, serif, mono, display, body
- **Utilities**: italic, decoration, transform

</td>
<td>

- **Display**: block, inline, flex, grid, table
- **Position**: static, relative, absolute, fixed
- **Flexbox**: direction, wrap, justify, align
- **Grid**: template-columns, template-rows, gap

</td>
</tr>
</table>

</div>

## 🔧 Project Structure

```
mikocss/
├── backgrounds/          # Background utilities
├── borders/             # Border and ring utilities
├── colors/              # Core color system
├── core/                # Main processor
├── effects/             # Visual effects utilities
├── generators/          # C++ code generators
├── layout/              # Layout utilities
├── sizing/              # Sizing utilities
├── spacing/             # Spacing utilities
├── typography/          # Typography system
├── .github/workflows/   # CI/CD pipeline
├── main.py             # CLI entry point
└── main.spec           # PyInstaller configuration
```

## 🚀 CI/CD & Releases

MikoCSS includes automated CI/CD with:
- **Automated testing** on multiple platforms
- **Code quality checks** (Black, flake8, isort)
- **Multi-platform builds** (Windows, macOS, Linux)
- **Automatic releases** with date-based versioning (YYYY.MM.DD)
- **Pre-built executables** for easy distribution

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and ensure tests pass
4. Run code formatting: `black . && isort . && flake8 .`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by Tailwind CSS color system and utilities
- Built for modern C++ GUI development
- Supports major C++ GUI frameworks

---

**MikoCSS** - Bringing modern CSS-like styling to C++ GUI development! 🎨✨
        