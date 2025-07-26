export class CSSOptimizer {
  minify(css: string): string {
    return css
      .replace(/\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\//g, '') // Remove comments
      .replace(/\s+/g, ' ') // Collapse whitespace
      .replace(/;\s*}/g, '}') // Remove last semicolon in blocks
      .replace(/\s*{\s*/g, '{') // Clean up braces
      .replace(/}\s*/g, '}') // Clean up closing braces
      .trim();
  }

  deduplicate(css: string): string {
    const rules = new Map<string, string>();
    const ruleRegex = /([^{]+)\{([^}]+)\}/g;
    
    let match;
    while ((match = ruleRegex.exec(css)) !== null) {
      const [, selector, declarations] = match;
      const cleanSelector = selector.trim();
      const cleanDeclarations = declarations.trim();
      
      if (rules.has(cleanSelector)) {
        // Merge declarations
        const existing = rules.get(cleanSelector)!;
        rules.set(cleanSelector, `${existing}; ${cleanDeclarations}`);
      } else {
        rules.set(cleanSelector, cleanDeclarations);
      }
    }
    
    return Array.from(rules.entries())
      .map(([selector, declarations]) => `${selector} { ${declarations} }`)
      .join('\n');
  }
}