from core.processor import ColorProcessor
from generators.css import generate_complete_css
from generators.javascript import generate_complete_js
from generators.typescript import generate_ts_colors, generate_ts_types
import json
import os


class WebProcessor(ColorProcessor):
    """Extended processor for web technologies"""
    
    def __init__(self, framework="css"):
        super().__init__(framework)
        self.web_framework = framework
    
    def generate_web_files(self, output_dir=".", format_type="css"):
        """Generate web files (CSS, JS, TS)"""
        if not self.all_colors:
            self.process_colors()
        
        files = {}
        
        if format_type in ["css", "all"]:
            # Generate CSS files
            css_content = generate_complete_css(self.all_colors)
            css_path = os.path.join(output_dir, "mikocss.css")
            with open(css_path, "w", encoding="utf-8") as f:
                f.write(css_content)
            files["css"] = css_path
        
        if format_type in ["js", "javascript", "all"]:
            # Generate JavaScript files
            js_content = generate_complete_js(self.all_colors)
            js_path = os.path.join(output_dir, "mikocss.js")
            with open(js_path, "w", encoding="utf-8") as f:
                f.write(js_content)
            files["js"] = js_path
        
        if format_type in ["ts", "typescript", "all"]:
            # Generate TypeScript files
            ts_content = generate_ts_colors(self.all_colors)
            ts_path = os.path.join(output_dir, "mikocss.ts")
            with open(ts_path, "w", encoding="utf-8") as f:
                f.write(ts_content)
            
            # Generate type definitions
            dts_content = generate_ts_types()
            dts_path = os.path.join(output_dir, "mikocss.d.ts")
            with open(dts_path, "w", encoding="utf-8") as f:
                f.write(dts_content)
            
            files["ts"] = ts_path
            files["dts"] = dts_path
        
        if format_type in ["json", "all"]:
            # Generate JSON data
            json_data = self._generate_json_data()
            json_path = os.path.join(output_dir, "mikocss.json")
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=2)
            files["json"] = json_path
        
        return files
    
    def _generate_json_data(self):
        """Generate JSON representation of all data"""
        from typography.base import text_sizes, font_weights, font_families
        from layout.base import display, position, flex_direction, justify_content, align_items
        
        # Convert colors to hex format
        colors_hex = {}
        for color_name, shades in self.all_colors.items():
            colors_hex[color_name] = {}
            for shade_key, (r, g, b) in shades.items():
                r_int = int(r * 255)
                g_int = int(g * 255)
                b_int = int(b * 255)
                hex_color = f"#{r_int:02x}{g_int:02x}{b_int:02x}"
                colors_hex[color_name][str(shade_key)] = hex_color
        
        return {
            "version": "1.0.0",
            "colors": colors_hex,
            "typography": {
                "sizes": text_sizes,
                "weights": font_weights,
                "families": font_families
            },
            "layout": {
                "display": display,
                "position": position,
                "flex": {
                    "direction": flex_direction,
                    "justify": justify_content,
                    "align": align_items
                }
            }
        }
    
    def generate_npm_package(self, output_dir=".", package_name="@mikocss/core"):
        """Generate complete npm package"""
        package_dir = os.path.join(output_dir, "package")
        os.makedirs(package_dir, exist_ok=True)
        
        # Generate all web files
        files = self.generate_web_files(package_dir, "all")
        
        # Generate package.json
        package_json = {
            "name": package_name,
            "version": "1.0.0",
            "description": "MikoCSS - Modern CSS-like utilities for web development",
            "main": "mikocss.js",
            "types": "mikocss.d.ts",
            "files": ["*.css", "*.js", "*.ts", "*.d.ts", "*.json"],
            "keywords": ["css", "utilities", "colors", "typography", "layout"],
            "author": "MikoCSS Team",
            "license": "MIT",
            "repository": {
                "type": "git",
                "url": "https://github.com/arizkami/mikocss.git"
            }
        }
        
        package_json_path = os.path.join(package_dir, "package.json")
        with open(package_json_path, "w", encoding="utf-8") as f:
            json.dump(package_json, f, indent=2)
        
        # Generate README
        readme_content = self._generate_package_readme()
        readme_path = os.path.join(package_dir, "README.md")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)
        
        files["package.json"] = package_json_path
        files["README.md"] = readme_path
        
        return files
    
    def _generate_package_readme(self):
        """Generate README for npm package"""
        return '''# MikoCSS

Modern CSS-like utilities for web development.

## Installation

```bash
npm install @mikocss/core
```

## Usage

### CSS
```css
@import '@mikocss/core/mikocss.css';

.my-element {
  color: var(--color-blue-500-rgb);
  background-color: var(--color-gray-100-rgb);
}
```

### JavaScript
```javascript
import { colors, getColor } from '@mikocss/core';

const blueColor = getColor('blue-500');
console.log(colors.blue[500]);
```

### TypeScript
```typescript
import { colors, ColorPalette } from '@mikocss/core';

const palette: ColorPalette = colors;
```
'''