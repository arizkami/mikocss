import { JITConfig, JITContext, ParsedClass, CSSRule } from '../types/index.js';
import { ColorGenerator } from '../colors/generator.js';
import { TypographyGenerator } from '../typography/generator.js';
import { LayoutGenerator } from '../layout/generator.js';
import { CSSParser } from '../utils/parser.js';
import { CSSOptimizer } from '../utils/optimizer.js';

export class MikoCSSJIT {
  private config: JITConfig;
  private context: JITContext;
  private colorGenerator: ColorGenerator;
  private typographyGenerator: TypographyGenerator;
  private layoutGenerator: LayoutGenerator;
  private parser: CSSParser;
  private optimizer: CSSOptimizer;
  private cache: Map<string, string> = new Map();

  constructor(config: JITConfig) {
    this.config = config;
    this.context = {
      config,
      utilities: new Map(),
      components: new Map()
    };
    
    this.colorGenerator = new ColorGenerator(config.theme?.colors);
    this.typographyGenerator = new TypographyGenerator(config.theme?.typography);
    this.layoutGenerator = new LayoutGenerator();
    this.parser = new CSSParser();
    this.optimizer = new CSSOptimizer();
    
    this.initializeUtilities();
  }

  /**
   * Generate CSS for specific classes
   */
  generateCSS(classes: string[]): string {
    const cacheKey = classes.sort().join(' ');
    
    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey)!;
    }

    const cssRules: string[] = [];
    const processedClasses = new Set<string>();

    for (const className of classes) {
      if (processedClasses.has(className)) continue;
      
      const css = this.generateClassCSS(className);
      if (css) {
        cssRules.push(css);
        processedClasses.add(className);
      }
    }

    let result = cssRules.join('\n');
    
    // Apply plugins
    for (const plugin of this.config.plugins || []) {
      result = plugin.transform(result, this.context);
    }
    
    // Optimize if enabled
    if (this.config.minify) {
      result = this.optimizer.minify(result);
    }
    
    this.cache.set(cacheKey, result);
    return result;
  }

  /**
   * Generate CSS for a single class
   */
  private generateClassCSS(className: string): string | null {
    const parsed = this.parser.parseClassName(className);
    if (!parsed) return null;

    switch (parsed.type) {
      case 'utility':
        return this.generateUtilityCSS(className, parsed);
      case 'component':
        return this.generateComponentCSS(className, parsed);
      default:
        return null;
    }
  }

  /**
   * Generate utility CSS
   */
  private generateUtilityCSS(className: string, parsed: ParsedClass): string {
    const { property, value, modifiers } = parsed;
    
    let cssRule: CSSRule | null = null;
    
    // Color utilities
    if (property.startsWith('text-') || property.startsWith('bg-') || property.startsWith('border-')) {
      cssRule = this.colorGenerator.generateUtility(property, value);
    }
    // Typography utilities
    else if (property.startsWith('text-') || property.startsWith('font-') || property.startsWith('leading-')) {
      cssRule = this.typographyGenerator.generateUtility(property, value);
    }
    // Layout utilities
    else if (['flex', 'grid', 'block', 'inline', 'absolute', 'relative'].some(p => property.includes(p))) {
      cssRule = this.layoutGenerator.generateUtility(property, value);
    }
    
    if (!cssRule) return '';
    
    // Apply modifiers (hover, focus, etc.)
    const selector = this.buildSelector(className, modifiers);
    return this.formatCSSRule(selector, cssRule);
  }

  /**
   * Generate component CSS
   */
  private generateComponentCSS(className: string, parsed: ParsedClass): string {
    const componentCSS = this.context.components.get(parsed.property);
    if (!componentCSS) return '';
    
    return componentCSS.replace(/\.component/g, `.${className}`);
  }

  /**
   * Build CSS selector with modifiers
   */
  private buildSelector(className: string, modifiers?: string[]): string {
    let selector = `.${className}`;
    
    if (modifiers) {
      for (const modifier of modifiers) {
        switch (modifier) {
          case 'hover':
            selector += ':hover';
            break;
          case 'focus':
            selector += ':focus';
            break;
          case 'active':
            selector += ':active';
            break;
          case 'dark':
            selector = `@media (prefers-color-scheme: dark) { ${selector}`;
            break;
          default:
            if (modifier.startsWith('sm:') || modifier.startsWith('md:') || modifier.startsWith('lg:')) {
              const breakpoint = modifier.split(':')[0];
              selector = `@media (min-width: ${this.getBreakpoint(breakpoint)}) { ${selector}`;
            }
        }
      }
    }
    
    return selector;
  }

  /**
   * Format CSS rule
   */
  private formatCSSRule(selector: string, rule: CSSRule): string {
    const properties = Object.entries(rule)
      .map(([prop, value]) => `  ${prop}: ${value};`)
      .join('\n');
    
    return `${selector} {\n${properties}\n}`;
  }

  /**
   * Get breakpoint value
   */
  private getBreakpoint(breakpoint: string): string {
    const breakpoints: Record<string, string> = {
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1280px',
      '2xl': '1536px'
    };
    return breakpoints[breakpoint] || '0px';
  }

  /**
   * Initialize built-in utilities
   */
  private initializeUtilities(): void {
    // This will be populated by generators
    this.colorGenerator.registerUtilities(this.context.utilities);
    this.typographyGenerator.registerUtilities(this.context.utilities);
    this.layoutGenerator.registerUtilities(this.context.utilities);
  }

  /**
   * Scan content for classes
   */
  scanContent(): string[] {
    const classes = new Set<string>();
    const classRegex = /class(?:Name)?=["']([^"']*)["']/g;
    
    for (const contentPath of this.config.content) {
      try {
        const content = Bun.file(contentPath).text();
        let match;
        while ((match = classRegex.exec(content)) !== null) {
          const classList = match[1].split(/\s+/).filter(Boolean);
          classList.forEach(cls => classes.add(cls));
        }
      } catch (error) {
        console.warn(`Failed to read content file: ${contentPath}`);
      }
    }
    
    return Array.from(classes);
  }

  /**
   * Generate complete CSS from content scan
   */
  build(): string {
    const classes = this.scanContent();
    return this.generateCSS(classes);
  }

  /**
   * Clear cache
   */
  clearCache(): void {
    this.cache.clear();
  }

  /**
   * Add custom component
   */
  addComponent(name: string, css: string): void {
    this.context.components.set(name, css);
  }

  /**
   * Get configuration
   */
  getConfig(): JITConfig {
    return { ...this.config };
  }
}