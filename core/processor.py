from colors.base import base_colors
from colors.generators import (generate_extended_shades,
                               generate_saturation_variants, generate_shades,
                               generate_temperature_variants)
from generators.cpp import (generate_color_hpp, generate_color_list,
                            generate_wrapper_hpp)
from generators.layout import generate_layout_hpp, generate_layout_wrapper_hpp
from generators.typography import (generate_typography_hpp,
                                   generate_typography_wrapper_hpp)


class ColorProcessor:
    """Main processor that orchestrates color generation using reflector pattern"""

    def __init__(self, framework="gtk"):
        self.base_colors = base_colors
        self.all_colors = {}
        self.framework = framework
        self.generators = [
            self._generate_standard_shades,
            self._generate_extended_shades,
            self._generate_saturation_variants,
            self._generate_temperature_variants,
        ]

    def _generate_standard_shades(self, name, base_hex):
        """Generate standard shades for a color"""
        return generate_shades(base_hex, 10)

    def _generate_extended_shades(self, name, base_hex):
        """Generate extended micro shades"""
        return generate_extended_shades(base_hex, name)

    def _generate_saturation_variants(self, name, base_hex):
        """Generate saturation variants"""
        variants = generate_saturation_variants(base_hex, name)
        return {variant_name: rgb for variant_name, rgb in variants.items()}

    def _generate_temperature_variants(self, name, base_hex):
        """Generate temperature variants"""
        variants = generate_temperature_variants(base_hex, name)
        return {variant_name: rgb for variant_name, rgb in variants.items()}

    def process_colors(self):
        """Process all colors using registered generators"""
        total_colors = 0

        for name, base_hex in self.base_colors.items():
            self.all_colors[name] = {}

            # Apply all generators using reflection
            for generator in self.generators:
                generated = generator(name, base_hex)
                self.all_colors[name].update(generated)
                total_colors += len(generated)

        print(f"🎨 Processed {len(self.base_colors)} color families")
        print(f"📊 Generated {total_colors} total color variations")
        return self.all_colors

    def generate_cpp_files(self, output_dir="."):
        """Generate C++ header files including typography and layout"""
        if not self.all_colors:
            self.process_colors()

        # Generate miko_color.hpp
        color_hpp_content = generate_color_hpp(self.all_colors)
        with open(f"{output_dir}/miko_color.hpp", "w", encoding="utf-8") as f:
            f.write(color_hpp_content)

        # Generate miko_wrapper.hpp with framework support
        wrapper_hpp_content = generate_wrapper_hpp(self.all_colors, self.framework)
        with open(f"{output_dir}/miko_wrapper.hpp", "w", encoding="utf-8") as f:
            f.write(wrapper_hpp_content)

        # Generate miko_typography.hpp
        typography_hpp_content = generate_typography_hpp(self.framework)
        with open(f"{output_dir}/miko_typography.hpp", "w", encoding="utf-8") as f:
            f.write(typography_hpp_content)

        # Generate miko_typography_wrapper.hpp
        typography_wrapper_content = generate_typography_wrapper_hpp(self.framework)
        with open(
            f"{output_dir}/miko_typography_wrapper.hpp", "w", encoding="utf-8"
        ) as f:
            f.write(typography_wrapper_content)

        # Generate miko_layout.hpp
        layout_hpp_content = generate_layout_hpp(self.framework)
        with open(f"{output_dir}/miko_layout.hpp", "w", encoding="utf-8") as f:
            f.write(layout_hpp_content)

        # Generate miko_layout_wrapper.hpp
        layout_wrapper_content = generate_layout_wrapper_hpp(self.framework)
        with open(f"{output_dir}/miko_layout_wrapper.hpp", "w", encoding="utf-8") as f:
            f.write(layout_wrapper_content)

        # Generate miko_color_list.txt for reference
        color_list = generate_color_list(self.all_colors)
        with open(f"{output_dir}/miko_color_list.txt", "w", encoding="utf-8") as f:
            f.write(color_list)

        return {
            "miko_color_hpp": f"{output_dir}/miko_color.hpp",
            "miko_wrapper_hpp": f"{output_dir}/miko_wrapper.hpp",
            "miko_typography_hpp": f"{output_dir}/miko_typography.hpp",
            "miko_typography_wrapper_hpp": f"{output_dir}/miko_typography_wrapper.hpp",
            "miko_layout_hpp": f"{output_dir}/miko_layout.hpp",
            "miko_layout_wrapper_hpp": f"{output_dir}/miko_layout_wrapper.hpp",
            "miko_color_list": f"{output_dir}/miko_color_list.txt",
        }

    def add_generator(self, generator_func):
        """Add a new color generator function (extensibility)"""
        self.generators.append(generator_func)

    def get_color_stats(self):
        """Get statistics about generated colors"""
        if not self.all_colors:
            return {}

        stats = {
            "total_families": len(self.all_colors),
            "total_colors": sum(len(shades) for shades in self.all_colors.values()),
            "families": {},
        }

        for name, shades in self.all_colors.items():
            standard = len(
                [
                    k
                    for k in shades.keys()
                    if isinstance(k, int)
                    and k in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
                ]
            )
            micro = len(
                [
                    k
                    for k in shades.keys()
                    if isinstance(k, int)
                    and k not in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
                ]
            )
            variants = len([k for k in shades.keys() if isinstance(k, str)])

            stats["families"][name] = {
                "total": len(shades),
                "standard": standard,
                "micro": micro,
                "variants": variants,
            }

        return stats
