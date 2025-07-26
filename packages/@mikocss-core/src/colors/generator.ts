import { ColorValue, ColorPalette, CSSRule } from '../types/index.js';
import { defaultColors } from './palette.js';

export class ColorGenerator {
  private palette: ColorPalette;

  constructor(customColors?: Partial<ColorPalette>) {
    this.palette = { ...defaultColors, ...customColors };
  }

  generateUtility(property: string, value: string): CSSRule | null {
    const color = this.getColor(value);
    if (!color) return null;

    const cssProperty = this.mapPropertyToCSS(property);
    if (!cssProperty) return null;

    return {
      [cssProperty]: this.formatColor(color)
    };
  }

  private getColor(colorName: string): ColorValue | null {
    const [family, shade] = colorName.split('-');
    return this.palette[family]?.[shade] || null;
  }

  private mapPropertyToCSS(property: string): string | null {
    if (property.startsWith('text-')) return 'color';
    if (property.startsWith('bg-')) return 'background-color';
    if (property.startsWith('border-')) return 'border-color';
    return null;
  }

  private formatColor(color: ColorValue): string {
    const { r, g, b, a = 1 } = color;
    return a === 1 ? `rgb(${r}, ${g}, ${b})` : `rgba(${r}, ${g}, ${b}, ${a})`;
  }

  registerUtilities(utilities: Map<string, string>): void {
    // Register color utilities
    Object.keys(this.palette).forEach(family => {
      Object.keys(this.palette[family]).forEach(shade => {
        const colorKey = `${family}-${shade}`;
        utilities.set(`text-${colorKey}`, `color: ${this.formatColor(this.palette[family][shade])}`);
        utilities.set(`bg-${colorKey}`, `background-color: ${this.formatColor(this.palette[family][shade])}`);
        utilities.set(`border-${colorKey}`, `border-color: ${this.formatColor(this.palette[family][shade])}`);
      });
    });
  }

  getColorPalette(): ColorPalette {
    return { ...this.palette };
  }
}