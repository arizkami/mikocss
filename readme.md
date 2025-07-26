<div align="center">

# MikoCSS

<p align="center">
  <strong>A powerful multi-platform styling library generator that brings modern CSS-like utilities to C++ GUI frameworks and web development</strong>
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
  <img src="https://img.shields.io/badge/TypeScript-5.0%2B-blue.svg" alt="TypeScript 5.0+">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg" alt="Platform Support">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Framework-GTK-orange.svg" alt="GTK Support">
  <img src="https://img.shields.io/badge/Framework-Qt5%2FQt6-green.svg" alt="Qt Support">
  <img src="https://img.shields.io/badge/Framework-Win32-blue.svg" alt="Win32 Support">
  <img src="https://img.shields.io/badge/Web-CSS%2FJS%2FTS-purple.svg" alt="Web Support">
</p>

<p align="center">
  <em>Generate comprehensive styling libraries for C++ GUI frameworks and modern web development with JIT compilation support.</em>
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
- **Multi-format output**: C++ headers, CSS variables, JavaScript objects, TypeScript definitions

### ✍️ **Typography System**
- **13 text sizes**: xs, sm, base, lg, xl, 2xl, 3xl, 4xl, 5xl, 6xl, 7xl, 8xl, 9xl
- **11 font weights**: thin, extralight, light, semilight, regular, medium, semibold, bold, extrabold, black, blackrr
- **Font families**: sans, serif, mono, display, body
- **Text utilities**: alignment, decoration, transform, overflow, line clamping
- **Cross-platform font creation** (Pango, QFont, HFONT, CSS)

### ⚡ **JIT Compiler (NEW)**
- **Real-time CSS generation** with intelligent caching
- **Content scanning** for automatic class detection
- **Plugin system** for custom transformations
- **TypeScript-first** with full type safety
- **Performance optimized** with minification and deduplication

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

### 🌐 **Web Generation (NEW)**
- **CSS**: Custom properties, utility classes, responsive design
- **JavaScript**: Color palettes, utility functions, theme objects
- **TypeScript**: Full type definitions, IntelliSense support
- **JSON**: Structured data for API consumption
- **NPM packages**: Ready-to-publish modules

### 🎯 **Multi-Framework Support**
- **GTK 3+**: GDK color conversion, Pango fonts, CSS styling
- **Qt5/Qt6**: QColor conversion, QFont creation, widget styling
- **Win32**: COLORREF conversion, HFONT creation, window positioning
- **Web**: Modern CSS, ES6+ JavaScript, TypeScript 5.0+

</td>
</tr>
</table>

## 📦 Installation

### Prerequisites
- Python 3.7+
- C++ compiler with C++17 support (for C++ projects)
- Node.js 18+ and Bun (for TypeScript/web projects)
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

4. **Generate web project:**
```bash
python main.py web -f css --output web_project
```

5. **Generate TypeScript package:**
```bash
python main.py web -f ts --package --output @mikocss/theme
```

</details>

## 🛠️ Usage

### Command Line Interface

<div align="center">

| Target | Command | Description |
|--------|---------|-------------|
| **GTK** | `python main.py init -p gtk --output gtk_project` | Generate GTK project |
| **Qt5** | `python main.py init -p qt5 --output qt5_project` | Generate Qt5 project |
| **Qt6** | `python main.py init -p qt6 --output qt6_project` | Generate Qt6 project |
| **Win32** | `python main.py init -p win32 --output win32_project` | Generate Win32 project |
| **CSS** | `python main.py web -f css --output styles/` | Generate CSS files |
| **JavaScript** | `python main.py web -f js --output dist/` | Generate JavaScript files |
| **TypeScript** | `python main.py web -f ts --output src/` | Generate TypeScript files |
| **All Web** | `python main.py web -f all --package --output @mikocss/core` | Generate complete NPM package |

</div>

#### Web Generation Options
```bash
# Generate CSS with utility classes
python main.py web -f css --output ./styles

# Generate JavaScript with color utilities
python main.py web -f javascript --output ./src

# Generate TypeScript with full type definitions
python main.py web -f typescript --output ./types

# Generate complete NPM package
python main.py web -f all --package --output ./packages/@mikocss-theme

# Generate JSON data for APIs
python main.py web -f json --output ./data
```

### Generated Files

<div align="center">

#### C++ Projects
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

#### Web Projects
| File | Description |
|------|-------------|
| `mikocss.css` | CSS custom properties and utilities |
| `mikocss.js` | JavaScript color and utility functions |
| `mikocss.d.ts` | TypeScript type definitions |
| `colors.json` | Structured color data |
| `package.json` | NPM package configuration |
| `README.md` | Usage documentation |

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
<summary><strong>🌐 Web CSS Example</strong></summary>

```css
/* Generated CSS with custom properties */
:root {
  --color-blue-500: 59 130 246;
  --color-gray-100: 243 244 246;
  --text-lg: 1.125rem;
  --font-bold: 700;
}

/* Utility classes */
.text-blue-500 { color: rgb(var(--color-blue-500)); }
.bg-gray-100 { background-color: rgb(var(--color-gray-100)); }
.text-lg { font-size: var(--text-lg); line-height: 1.75rem; }
.font-bold { font-weight: var(--font-bold); }

/* Responsive utilities */
@media (min-width: 768px) {
  .md\:text-xl { font-size: 1.25rem; line-height: 1.75rem; }
}
```

</details>

<details>
<summary><strong>📜 JavaScript Example</strong></summary>

```javascript
// Generated JavaScript utilities
import { getColor, colors, createTheme } from './mikocss.js';

// Get specific colors
const blue500 = getColor('blue-500'); // { r: 59, g: 130, b: 246 }
const grayPalette = colors.gray;

// Create custom theme
const theme = createTheme({
  primary: 'blue-600',
  secondary: 'gray-500',
  accent: 'purple-500'
});

// Apply colors dynamically
document.documentElement.style.setProperty(
  '--primary-color', 
  `rgb(${blue500.r}, ${blue500.g}, ${blue500.b})`
);
```

</details>

<details>
<summary><strong>📘 TypeScript JIT Example</strong></summary>

```typescript
// TypeScript JIT Compiler usage
import { createJIT, MikoCSSJIT } from '@mikocss/core';

// Quick setup with content scanning
const jit = createJIT({
  content: ['./src/**/*.{ts,tsx,html}'],
  theme: {
    colors: {
      brand: {
        '500': { r: 59, g: 130, b: 246 }
      }
    }
  },
  minify: true
});

// Generate CSS for specific classes
const css = jit.generateCSS([
  'text-blue-500', 
  'bg-gray-100', 
  'hover:text-brand-500',
  'md:text-xl'
]);

// Scan content and build complete CSS
const fullCSS = jit.build();
console.log(fullCSS);

// Advanced usage with plugins
const advancedJIT = new MikoCSSJIT({
  content: ['./app/**/*.tsx'],
  plugins: [
    {
      name: 'custom-plugin',
      transform: (css, context) => {
        return css.replace(/\.custom-/g, '.my-');
      }
    }
  ],
  purge: true
});
```

</details>

## 🏗️ Building Your Project

### C++ Projects
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

### TypeScript/Web Projects
```bash
# Navigate to generated package
cd @mikocss-core

# Install dependencies
bun install

# Build the package
bun run build

# Run development server
bun run dev

# Run tests
bun test
```

## 📚 Available Utilities

<div align="center">

<table>
<tr>
<th>🎨 Colors</th>
<th>✍️ Typography</th>
<th>📐 Layout</th>
<th>⚡ JIT Features</th>
</tr>
<tr>
<td>

- **Base families**: 20+ color families
- **Shades**: 50-950 range
- **Micro-shades**: 425, 475, 525, 575
- **Variants**: saturated, desaturated, warm, cool
- **Formats**: RGB, HSL, HEX, CSS custom properties

</td>
<td>

- **Sizes**: xs (12px) to 9xl (128px)
- **Weights**: 100 (thin) to 950 (blackrr)
- **Families**: sans, serif, mono, display, body
- **Utilities**: italic, decoration, transform
- **Responsive**: breakpoint-specific sizing

</td>
<td>

- **Display**: block, inline, flex, grid, table
- **Position**: static, relative, absolute, fixed
- **Flexbox**: direction, wrap, justify, align
- **Grid**: template-columns, template-rows, gap
- **Responsive**: mobile-first breakpoints

</td>
<td>

- **Real-time**: On-demand CSS generation
- **Caching**: Intelligent performance optimization
- **Scanning**: Automatic class detection
- **Plugins**: Extensible transformation system
- **Types**: Full TypeScript support

</td>
</tr>
</table>

</div>

## 🔧 Project Structure

```
mikocss/
├── packages/
│   ├── @mikocss-core/       # TypeScript JIT compiler
│   │   ├── src/
│   │   │   ├── jit/         # JIT compiler core
│   │   │   ├── colors/      # Color generation
│   │   │   ├── typography/  # Typography utilities
│   │   │   ├── layout/      # Layout utilities
│   │   │   └── utils/       # Parser and optimizer
│   │   ├── index.ts         # Main entry point
│   │   └── package.json     # NPM configuration
│   └── @mikocss-vite/       # Vite plugin (coming soon)
├── generators/              # Code generators
│   ├── cpp.py              # C++ header generation
│   ├── css.py              # CSS generation
│   ├── javascript.py       # JavaScript generation
│   └── typescript.py       # TypeScript generation
├── core/
│   ├── processor.py         # Core C++ processor
│   └── web_processor.py     # Web generation processor
├── colors/                  # Core color system
├── typography/              # Typography system
├── layout/                  # Layout utilities
├── .github/workflows/       # CI/CD pipeline
├── main.py                 # CLI entry point
└── README.md               # This file
```

## 🚀 CI/CD & Releases

MikoCSS includes automated CI/CD with:
- **Automated testing** on multiple platforms
- **Code quality checks** (Black, flake8, isort)
- **Multi-platform builds** (Windows, macOS, Linux)
- **Automatic releases** with date-based versioning (YYYY.MM.DD)
- **Pre-built executables** for easy distribution
- **NPM package publishing** for TypeScript modules

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
- Built for modern C++ GUI development and web applications
- Supports major C++ GUI frameworks and modern web technologies
- TypeScript-first approach for excellent developer experience

---

**MikoCSS** - Bringing modern CSS-like styling to C++ GUI development and web applications with JIT compilation! 🎨✨⚡
