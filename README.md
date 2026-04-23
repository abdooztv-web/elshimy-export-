# El-Shimy for Trading & Agencies

**Egypt's premier agricultural exporter** — premium fresh fruits and vegetables delivered to 85+ countries worldwide since 2016.

---

## About the Website

A fully responsive, 5-page static website showcasing El-Shimy's export capabilities with modern 3D design elements. Built with pure HTML, CSS, and JavaScript — no frameworks, no build tools required.

### Pages

| Page | File | Description |
|------|------|-------------|
| Home | `index.html` | Hero with 3D floating product cards, export capabilities, services, testimonials, quote form |
| About | `about.html` | Company story, timeline, values, mission/vision, certifications |
| Products | `products.html` | Seasonal product catalogue with 3D flip cards, export process, global markets |
| FAQs | `faqs.html` | 18 FAQs across 5 categories with smooth accordion |
| Blog | `blogs.html` | Market intelligence articles, featured post, newsletter |

---

## Tech Stack

- **HTML5** — semantic, SEO-optimised markup with structured data (JSON-LD)
- **CSS3** — custom design system, CSS variables, `perspective`/`preserve-3d` for 3D effects
- **Vanilla JS** — IntersectionObserver, animated counters, FAQ accordion, season tabs, mobile menu
- **Google Fonts** — Manrope typeface
- **Google Material Symbols** — icon set

### 3D Effects Used

- Floating product cards in hero (CSS `rotateX/Y + translateZ + @keyframes`)
- Perspective grid floor in hero
- 3D flip cards on hover (Products page)
- Mouse-tilt effect on value/feature cards (JS `mousemove` + `perspective`)
- Spinning 3D globe (CSS `rotateY` animation)

---

## Project Structure

```
elshimy-export/
├── index.html        # Home page
├── about.html        # About page
├── products.html     # Products page
├── faqs.html         # FAQs page
├── blogs.html        # Blog page
├── style.css         # Shared design system
├── shared.js         # Shared JavaScript
└── logo/
    ├── 1.png         # Primary logo (dark text)
    ├── 2.png         # Alternate logo (light text)
    └── 3.png         # Icon mark
```

---

## Running Locally

No build step needed — just serve the files:

```bash
# Using Node.js (built-in)
node -e "require('http').createServer((req,res)=>{ require('fs').readFile('./'+req.url.slice(1)||'index.html',(e,d)=>{ res.end(d); }); }).listen(3000)"

# Or using npx serve
npx serve .
```

Then open **http://localhost:3000**

---

## Design System

| Token | Value | Usage |
|-------|-------|-------|
| `--primary` | `#9ADA44` | Accent green, CTAs |
| `--secondary` | `#2D5027` | Dark green, headings |
| `--neutral` | `#1A201B` | Near-black, footer |
| `--tertiary` | `#F4F7F0` | Light bg sections |

### Breakpoints

| Breakpoint | Width | Changes |
|------------|-------|---------|
| Desktop | > 1024px | Full layout, 3D effects active |
| Tablet | ≤ 900px | Hamburger nav, grids collapse |
| Mobile | ≤ 600px | Single column, flip cards stacked |
| Small | ≤ 380px | Minimal nav, compact buttons |

---

## Contact

- **Website:** [elshimy.com](https://elshimy.com)
- **Email:** info@elshimy.com
- **Export enquiries:** export@elshimy.com
- **WhatsApp:** [Chat with us](https://wa.me/201000000000)
- **Location:** Office 3, Mall 11, Beverly Hills, Giza, Egypt
