#!/usr/bin/env python3
"""Build script for MikoCSS using PyInstaller"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        print(f"✅ PyInstaller {PyInstaller.__version__} found")
        return True
    except ImportError:
        print("❌ PyInstaller not found. Installing...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✅ PyInstaller installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install PyInstaller")
            return False

def clean_build():
    """Clean previous build artifacts"""
    print("🧹 Cleaning previous build artifacts...")
    
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   Removed {dir_name}/")
    
    # Clean __pycache__ in subdirectories
    for root, dirs, files in os.walk('.'):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            shutil.rmtree(pycache_path)
            print(f"   Removed {pycache_path}")

def build_executable():
    """Build the executable using PyInstaller"""
    print("🔨 Building MikoCSS executable with PyInstaller...")
    
    try:
        # Run PyInstaller with the spec file
        cmd = [sys.executable, "-m", "PyInstaller", "main.spec", "--clean"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Build completed successfully!")
            return True
        else:
            print("❌ Build failed:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Build error: {e}")
        return False

def create_distribution():
    """Create distribution package"""
    print("📦 Creating distribution package...")
    
    dist_dir = Path("dist")
    if not dist_dir.exists():
        print("❌ No dist directory found")
        return False
    
    # Create README for distribution
    readme_content = """# MikoCSS Generator

🎨 Generate C++ libraries for colors, typography, and layout

## Usage

### Initialize a new C++ project:
```bash
mikocss.exe init -p <framework>
```

### Supported frameworks:
- `gtk`   - GTK/GDK compatible code
- `qt5`   - Qt5 compatible code  
- `qt6`   - Qt6 compatible code
- `win32` - Win32/COLORREF compatible code

### Examples:
```bash
mikocss.exe init -p gtk
mikocss.exe init -p qt5 --output ./include
mikocss.exe init -p qt6 --output ./include
```

### Legacy mode:
```bash
mikocss.exe --cppframework qt5 --output ./build
```

## Generated Files
- `miko_color.hpp` - Color definitions and utilities
- `miko_wrapper.hpp` - Framework-specific color conversions
- `miko_typography.hpp` - Typography definitions
- `miko_typography_wrapper.hpp` - Typography utilities
- `miko_layout.hpp` - Layout definitions
- `miko_layout_wrapper.hpp` - Layout utilities
- `CMakeLists.txt` - Build configuration
- `main.cpp` - Example usage

## Features
- 🎨 256+ colors with 8k color support
- ✍️ Comprehensive typography system
- 📐 Complete layout utilities
- 🎯 Multi-framework support (GTK, Qt5/6, Win32)
- 📦 Ready-to-use C++ headers
"""
    
    readme_path = dist_dir / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    # Create batch file for Windows
    batch_content = """@echo off
echo MikoCSS Generator
echo ================
echo.
echo Usage: mikocss.exe init -p ^<framework^>
echo.
echo Frameworks: gtk, qt5, qt6, win32
echo.
echo Examples:
echo   mikocss.exe init -p gtk
echo   mikocss.exe init -p qt5 --output ./include
echo.
pause
"""
    
    batch_path = dist_dir / "run_example.bat"
    with open(batch_path, 'w') as f:
        f.write(batch_content)
    
    print(f"📄 Created README.md: {readme_path}")
    print(f"📄 Created run_example.bat: {batch_path}")
    
    # Show final executable info
    exe_path = dist_dir / "mikocss.exe"
    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"\n🎉 Executable created: {exe_path}")
        print(f"📏 Size: {size_mb:.1f} MB")
        return True
    else:
        print("❌ Executable not found")
        return False

def main():
    """Main build process"""
    print("🚀 MikoCSS PyInstaller Build Script")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("main.py"):
        print("❌ main.py not found. Please run this script from the MikoCSS root directory.")
        sys.exit(1)
    
    # Check PyInstaller
    if not check_pyinstaller():
        sys.exit(1)
    
    # Clean previous builds
    clean_build()
    
    # Build executable
    if not build_executable():
        sys.exit(1)
    
    # Create distribution
    if not create_distribution():
        sys.exit(1)
    
    print("\n🎉 Build completed successfully!")
    print("\n📦 Distribution ready in ./dist/")
    print("\n💡 Test the executable:")
    print("   cd dist")
    print("   mikocss.exe init -p gtk")

if __name__ == "__main__":
    main()