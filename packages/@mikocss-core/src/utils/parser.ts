import { ParsedClass } from '../types/index.js';

export class CSSParser {
  parseClassName(className: string): ParsedClass | null {
    // Handle modifiers (hover:, focus:, sm:, etc.)
    const parts = className.split(':');
    const modifiers = parts.slice(0, -1);
    const baseClass = parts[parts.length - 1];

    // Parse the base class
    const match = baseClass.match(/^([a-z-]+)-(.+)$/);
    if (!match) {
      // Check if it's a simple utility
      if (['flex', 'grid', 'block', 'inline', 'hidden', 'absolute', 'relative', 'fixed', 'sticky'].includes(baseClass)) {
        return {
          type: 'utility',
          property: baseClass,
          value: '',
          modifiers: modifiers.length > 0 ? modifiers : undefined
        };
      }
      return null;
    }

    const [, property, value] = match;

    return {
      type: 'utility',
      property,
      value,
      modifiers: modifiers.length > 0 ? modifiers : undefined
    };
  }
}