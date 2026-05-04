# DB Branding Kit

This folder contains the processed logo and assets derived from `db-logo.png`.

## Contents

### Logos (`/logos`)
- `logo-main.png`: The original logo with the background removed and trimmed.
- `logo-light.png`: A white version of the logo for use on dark backgrounds.
- `logo-dark.png`: A black version of the logo for use on light backgrounds.
- `logo-main.svg`: SVG version of the main logo (embedded bitmap).
- `logo-light.svg`: SVG version of the light logo.
- `logo-dark.svg`: SVG version of the dark logo.
- `logo-icon.png`: Extracted main icon from the logo.
- `logo-icon-light.png` / `logo-icon-dark.png`: Monochrome versions of the icon.

### Favicons (`/favicons`)
- `favicon.ico`: Standard favicon containing 16x16, 32x32, and 48x48 versions.
- `favicon-16.png` to `favicon-256.png`: Individual PNG favicon sizes.

### Banners (`/banners`)
- `banner-og-light.png` / `banner-og-dark.png`: 1200x630 banners for OpenGraph.
- `banner-twitter-light.png` / `banner-twitter-dark.png`: 1500x500 banners for Twitter/X.

## Technical Details
- Background removed using color detection at (0,0) with a 10% fuzz factor.
- SVG versions are currently embedded bitmaps as vectorization tools were not available in this environment.
- Light/Dark variants are monochrome colorized versions of the original logo shape.
