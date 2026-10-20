
## 6. Effect of the applied edits

The edits in `docs/seo-proposed.diff` were applied to `scripts/content.py` and `scripts/visual.py` and the site was rebuilt. Sections 1-5 above describe the **current** state; the "before" column below is the baseline audit taken before the edits.

| Metric | Before | After |
|---|---|---|
| High-priority keywords missing (existing pages only) | 34 | 2 (listed in section 2) |
| Page titles/descriptions outside range | 38 of 60 | 2 of 60 (photo-credits, intentionally minimal) |

Owner decisions applied: URL slugs unchanged (19 product slugs and all 61 sitemap URLs identical before and after); Arabic titles and descriptions use one spelling only (the Gulf/Egyptian form: بطاطس, طماطم, فراولة, مانجو, يوسفي), with no parentheses; the alternate spelling appears once, in the product intro.

Many gains are `in_body` via the meta description only. A description does not rank a page on its own, which is why product intros also got an exporter/supplier lead sentence. Treat Search Console impressions as the real test.

## 7. New pages worth building (not in the diff; needs code in `scripts/visual.py` after approval)

Only three, each with substantive, factual content. Slugs are identical in EN and AR so hreflang pairs stay mirrored, and the build adds them to the sitemap automatically.

1. **Gulf market page** — `/en/markets/gulf-countries/` and `/ar/markets/gulf-countries/`
   - Serves: Egyptian produce for Gulf importers, export fruit from Egypt to Saudi Arabia, Egyptian vegetables to UAE, and the Arabic equivalents.
   - Outline: who we supply in the Gulf (importers, wholesalers, hotels, distributors), typical lines with links to the product pages (oranges, onions, potatoes, grapes), sea vs air, documents to plan with the importer's customs authority, how to request a quote. No named customers, volumes, prices or country-specific rules unless verified.
   - One page, not one page per country. Split into Saudi/UAE pages only once there is distinct, verified content for each; thin near-duplicate country pages would hurt.
2. **How to import fresh produce from Egypt** — `/en/insights/import-fresh-produce-from-egypt/`, `/ar/insights/import-fresh-produce-from-egypt/`
   - Serves the highest-intent informational queries ("how to import fruit from Egypt", `كيفية استيراد الفواكه والخضروات من مصر`).
   - Outline: choose product and spec, pick Incoterm, shipping mode, documents (invoice, packing list, phytosanitary, origin), what to confirm with your customs authority, then the quote form. Links to the existing quote checklist, freight and quality pages.
3. **What is IQF frozen fruit** — `/en/insights/what-is-iqf-frozen-fruit/`, `/ar/insights/what-is-iqf-frozen-fruit/`
   - Serves `what is IQF frozen fruit`, `ما هو التجميد السريع IQF للفواكه`; feeds both IQF product pages.
   - Outline: what IQF means, why manufacturers use it, typical formats and grading questions, cold-chain basics (−18 °C or below), link to the two IQF products.

Not recommended yet: an Asia market page (no verified Asian customers or routes to write about), per-country pages, any page targeting `ISO 22000 certified exporter` (blocked until SHOW_ISO is verified), and any "price" keywords (prices are quoted per enquiry).

## 8. Other observations

- **Arabic spelling variants.** One page per spelling would be thin duplication. The second spelling appears once, in parentheses, in the product intro only (never in titles or descriptions): بطاطس (بطاطا)، طماطم (بندورة)، يوسفي (ماندرين)، فراولة (فريز)، مانجو (مانجا)، كمثرى (إجاص)، خوخ (دراق)، بلح/تمور.
- **Dialect check needed.** The variant choices follow common usage (Egypt: بطاطس، يوسفي; Gulf/Levant: بطاطا، ماندرين، فريز). Validate with Keyword Planner using Saudi Arabia, UAE and Egypt as locations before leaning on any one spelling.
- **Fresh vs frozen strawberries** target different intents (fresh produce buyers vs manufacturers). The diff separates them: fresh uses "exporter / فراولة (فريز)", frozen uses "IQF / supplier / للمصانع".
- **Titles.** Product titles now follow `Egyptian <Product> Exporter | <differentiator> | EL-SHIMY`, at most 62 characters, instead of a generic second segment.
- **Arabic descriptions** were 54–106 characters; the proposal brings them to roughly 120–135, which still fits Google's pixel limit for Arabic.
- **Home H1** is unchanged ("Egyptian Products. Global Markets.") because it is your brand line. The primary keyword reaches the page through the title, description and the home strip bullet instead.
- **Volumes.** Every row is `unvalidated`. Search Console only helps after the site is verified and has been crawled for a few weeks; Keyword Planner can be used immediately.
- **GTM** (GTM-KFSWRKKQ) and everything in `build.py` are untouched.
