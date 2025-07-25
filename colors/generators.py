import colorsys
from .utils import hex_to_rgb

def generate_shades(base_hex, steps=10):
    """Generate standard Tailwind-style shades"""
    r, g, b = hex_to_rgb(base_hex)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    shades = {}
    
    # Standard Tailwind shades
    shade_values = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    
    for i, shade in enumerate(shade_values):
        # More sophisticated lightness distribution
        if shade <= 100:
            # Very light shades
            new_l = 0.95 - (i * 0.05)
        elif shade <= 400:
            # Light to medium shades  
            new_l = 0.85 - ((i-2) * 0.15)
        elif shade == 500:
            # Base color (keep original lightness)
            new_l = l
        else:
            # Dark shades
            new_l = l * (1.0 - ((shade - 500) / 1000))
        
        new_l = max(0.05, min(0.95, new_l))
        nr, ng, nb = colorsys.hls_to_rgb(h, new_l, s)
        shades[shade] = (nr, ng, nb)
    
    return shades

def generate_extended_shades(base_hex, color_name):
    """Generate extended shade variations for more colors"""
    r, g, b = hex_to_rgb(base_hex)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    extended = {}
    
    # Add micro shades (25, 75, 125, etc.)
    micro_shades = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]
    
    for shade in micro_shades:
        # Calculate lightness based on shade value
        if shade < 500:
            # Lighter than base
            new_l = 0.98 - (shade / 500) * (0.98 - l)
        else:
            # Darker than base  
            new_l = l - ((shade - 500) / 500) * (l - 0.02)
        
        new_l = max(0.02, min(0.98, new_l))
        nr, ng, nb = colorsys.hls_to_rgb(h, new_l, s)
        extended[shade] = (nr, ng, nb)
    
    return extended

def generate_saturation_variants(base_hex, color_name):
    """Generate saturation variants (muted, vivid, etc.)"""
    r, g, b = hex_to_rgb(base_hex)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    variants = {}
    
    # Saturation variants
    sat_variants = {
        'muted': s * 0.3,
        'soft': s * 0.6, 
        'vivid': min(1.0, s * 1.4),
        'intense': min(1.0, s * 1.8)
    }
    
    for variant_name, new_s in sat_variants.items():
        nr, ng, nb = colorsys.hls_to_rgb(h, l, new_s)
        variants[f"{variant_name}"] = (nr, ng, nb)
    
    return variants

def generate_temperature_variants(base_hex, color_name):
    """Generate warm/cool temperature variants"""
    r, g, b = hex_to_rgb(base_hex)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    variants = {}
    
    # Temperature shifts (hue adjustments)
    temp_variants = {
        'warm': (h + 0.05) % 1.0,   # Shift towards red
        'cool': (h - 0.05) % 1.0,   # Shift towards blue
        'hot': (h + 0.1) % 1.0,     # More red shift
        'cold': (h - 0.1) % 1.0,    # More blue shift
    }
    
    for variant_name, new_h in temp_variants.items():
        nr, ng, nb = colorsys.hls_to_rgb(new_h, l, s)
        variants[f"{variant_name}"] = (nr, ng, nb)
    
    return variants