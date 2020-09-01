# colornamer
Given a color, return a hierarchy of names.

## Installation
```
pip install colornamer
```

## Usage
```
from colornamer import get_color_from_rgb
get_color_from_rgb([5, 135, 210])
```
returns (ordered for sake of explanation):

```
{
  'xkcd_color': 'cerulean',
  'xkcd_color_hex': '#0485d1',
  'xkcd_r': 4,
  'xkcd_g': 133,
  'xkcd_b': 209,
  'design_color': 'azure blue',
  'design_color_hex': '#088cda',
  'design_r': 8,
  'design_g': 140,
  'design_b': 218,
  'common_color': 'bright blue',
  'common_color_hex': '#2078c7',
  'common_r': 32,
  'common_g': 120,
  'common_b': 199,
  'color_family': 'blue',
  'color_or_neutral': 'color',
  'color_type': 'tinted color',
}
```

## Interpreting results:

- XKCD Color is the finest level of granularity, and corresponds to the [colors in the XKCD color survey](https://xkcd.com/color/rgb/). There are about 950 colors in this space. `xkcd_color` is the name of the color that is closest to the input value (using the [CIEDE2000](https://en.wikipedia.org/wiki/Color_difference#CIEDE2000) color distance metric). `xkcd_color_hex`, `xkcd_r`, `xkcd_g`, and `xkcd_b` are RGB values for the center of that color.
- Design Color is the next coarsest level. Every XKCD Color is in exactly one Design Color. There are about 250 Design Colors.
- Common Color is the next coarsest level. Every Design Color is in exactly one Common Color. There are about 120 Common Colors. This is probably the most useful level for most purposes.
- Color Family is even coarser, and has 26 families. These are all primary, secondary, or tertiary colors, or corresponding values for neutrals.
- Color Or Neutral tells whether something is a "neutral" (like white, black, or khaki) or a "color".
- Color Type is another dimension that tells, roughly, how light, dark or saturated a color is. There are 11 color types.

For more details, see the [blog post](https://multithreaded.stitchfix.com/blog/2020/09/02/what-color-is-this/).
