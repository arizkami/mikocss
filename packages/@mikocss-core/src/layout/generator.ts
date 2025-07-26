import { CSSRule } from '../types/index.js';

export class LayoutGenerator {
  generateUtility(property: string, value: string): CSSRule | null {
    const layoutMap: Record<string, CSSRule> = {
      'flex': { display: 'flex' },
      'grid': { display: 'grid' },
      'block': { display: 'block' },
      'inline': { display: 'inline' },
      'hidden': { display: 'none' },
      'absolute': { position: 'absolute' },
      'relative': { position: 'relative' },
      'fixed': { position: 'fixed' },
      'sticky': { position: 'sticky' }
    };

    return layoutMap[property] || null;
  }

  registerUtilities(utilities: Map<string, string>): void {
    const layoutUtilities = {
      'flex': 'display: flex',
      'grid': 'display: grid',
      'block': 'display: block',
      'inline': 'display: inline',
      'hidden': 'display: none',
      'absolute': 'position: absolute',
      'relative': 'position: relative',
      'fixed': 'position: fixed',
      'sticky': 'position: sticky'
    };

    Object.entries(layoutUtilities).forEach(([key, value]) => {
      utilities.set(key, value);
    });
  }
}