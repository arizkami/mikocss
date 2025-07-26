import { TypographyScale, CSSRule } from '../types/index.js';
import { defaultTypography } from './scale.js';

export class TypographyGenerator {
  private scale: TypographyScale;

  constructor(customTypography?: Partial<TypographyScale>) {
    this.scale = { ...defaultTypography, ...customTypography };
  }

  generateUtility(property: string, value: string): CSSRule | null {
    if (property.startsWith('text-')) {
      const size = this.scale[value];
      if (size) {
        return {
          'font-size': size.fontSize,
          'line-height': size.lineHeight,
          ...(size.letterSpacing && { 'letter-spacing': size.letterSpacing })
        };
      }
    }

    if (property.startsWith('font-')) {
      const weightMap: Record<string, number> = {
        thin: 100,
        light: 300,
        normal: 400,
        medium: 500,
        semibold: 600,
        bold: 700,
        extrabold: 800,
        black: 900
      };
      
      const weight = weightMap[value];
      if (weight) {
        return { 'font-weight': weight.toString() };
      }
    }

    return null;
  }

  registerUtilities(utilities: Map<string, string>): void {
    // Register typography utilities
    Object.entries(this.scale).forEach(([size, config]) => {
      utilities.set(`text-${size}`, `font-size: ${config.fontSize}; line-height: ${config.lineHeight};`);
    });
  }
}