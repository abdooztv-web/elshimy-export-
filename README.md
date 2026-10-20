# EL-SHIMY website

Bilingual (English / Arabic RTL) static website for **EL-SHIMY for Trading & Agencies**: *Egyptian Products. Global Markets.*

No framework. Pages are generated from `scripts/content.py` by `scripts/build.py` into plain HTML that any static host can serve.

## Structure
```
/                      language chooser (x-default)
/en/  /ar/             home
/{lang}/products/      catalogue with category + fresh/frozen filters
/{lang}/products/<slug>/   19 product pages
/{lang}/sourcing-export/  freight-customs/  quality-food-safety/  about/  markets/  insights/  contact/
404.html  sitemap.xml  robots.txt  vercel.json  _redirects
about.html products.html faqs.html blogs.html   legacy URLs -> redirect stubs (+ 301s in vercel.json/_redirects)
```

## Workflow
```bash
pip install pillow
python scripts/build.py     # regenerate all pages, sitemap, robots, redirects
python scripts/check.py     # broken links, titles/descriptions, h1, canonical, hreflang, sitemap, alt/dimensions
python -m http.server 8000  # preview at http://localhost:8000
```
`python scripts/prepare_assets.py` re-creates the cropped logos and optimised stock photos.

## Before launch (see docs/research.md)
Set in `scripts/content.py`: `FORM_ENDPOINT` (Formspree/Netlify/etc.; otherwise the form opens an email draft), `GSC_TOKEN`, and flip `SHOW_ISO` / `SHOW_VOLUME` only after verification. Confirm `EMAIL` and `ADDRESS`. Replace stock photos with real ones. Then submit `https://elshimy.com/sitemap.xml` in Search Console (verification has **not** been done).
