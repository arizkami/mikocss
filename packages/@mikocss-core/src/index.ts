export { MikoCSSJIT } from './jit/compiler.js';
export { ColorGenerator } from './colors/generator.js';
export { TypographyGenerator } from './typography/generator.js';
export { LayoutGenerator } from './layout/generator.js';
export { CSSParser } from './utils/parser.js';
export { CSSOptimizer } from './utils/optimizer.js';
export { defaultColors } from './colors/palette.js';
export { defaultTypography } from './typography/scale.js';
export * from './types/index.js';

// Convenience function for quick setup
export function createJIT(config: Partial<JITConfig> = {}): MikoCSSJIT {
  const defaultConfig: JITConfig = {
    content: ['./src/**/*.{js,ts,jsx,tsx,html}'],
    purge: true,
    minify: true,
    plugins: []
  };
  
  return new MikoCSSJIT({ ...defaultConfig, ...config });
}