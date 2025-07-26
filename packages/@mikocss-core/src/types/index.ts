// Color system types
export interface ColorValue {
  r: number;
  g: number;
  b: number;
  a?: number;
}

export interface ColorPalette {
  [family: string]: {
    [shade: string]: ColorValue;
  };
}

// Typography types
export interface TypographyScale {
  [size: string]: {
    fontSize: string;
    lineHeight: string;
    letterSpacing?: string;
  };
}

export interface FontWeights {
  [weight: string]: number;
}

// Layout types
export interface LayoutProperties {
  display?: string;
  position?: string;
  overflow?: string;
  aspectRatio?: string;
  zIndex?: number;
}

// JIT Compiler types
export interface JITConfig {
  content: string[];
  theme?: {
    colors?: Partial<ColorPalette>;
    typography?: Partial<TypographyScale>;
    extend?: Record<string, any>;
  };
  plugins?: JITPlugin[];
  purge?: boolean;
  minify?: boolean;
}

export interface JITPlugin {
  name: string;
  transform: (css: string, context: JITContext) => string;
}

export interface JITContext {
  config: JITConfig;
  utilities: Map<string, string>;
  components: Map<string, string>;
}

// Utility types
export type CSSProperty = string;
export type CSSValue = string | number;
export type CSSRule = Record<string, CSSValue>;

export interface ParsedClass {
  type: 'utility' | 'component' | 'modifier';
  property: string;
  value: string;
  modifiers?: string[];
}