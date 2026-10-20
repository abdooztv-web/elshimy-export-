# -*- coding: utf-8 -*-
"""Keyword research list for elshimytrading.com (EN + AR). Search volumes are NOT included on purpose:
validate every row in Google Search Console / Keyword Planner before acting on it.

Row = (keyword, lang, intent, category, product_slug, target, priority, notes)
target: 'home' | 'products' | 'services' | 'freight' | 'quality' | 'markets' | 'about' | 'contact' | 'insights' | 'guide'
        | 'p:<slug>' (product page) | ('NEW', '<path under /{lang}>')  (page that does not exist yet)
"""
C, I, N = "commercial", "informational", "navigational"
H, M, L = "high", "medium", "low"
ROWS = []
def add(kw, lang, intent, cat, slug, target, prio, note=""):
    ROWS.append((kw, lang, intent, cat, slug, target, prio, note))

# ───────────────────────── company ─────────────────────────
for kw, t, pr, nt in [
    ("Egyptian fruit and vegetable exporter", "home", H, "core head term"),
    ("Egyptian fruit exporter", "home", H, ""),
    ("Egyptian vegetable exporter", "home", H, ""),
    ("fresh produce exporter Egypt", "home", H, ""),
    ("fresh produce supplier Egypt", "home", H, ""),
    ("fruit and vegetable export company Egypt", "home", H, ""),
    ("fresh and frozen produce supplier Egypt", "home", M, "fresh + IQF positioning"),
    ("Egyptian agricultural exporter", "about", M, ""),
    ("Egyptian agricultural products exporter", "about", M, ""),
    ("Egyptian produce supplier for importers", "services", M, "B2B phrasing"),
    ("wholesale Egyptian fruits and vegetables", "products", M, "wholesale intent"),
    ("fresh produce sourcing agent Egypt", "services", M, "matches partner-farm model; do not imply ownership of farms"),
    ("Egyptian food trading company", "about", L, ""),
    ("Egypt food export company", "home", L, ""),
]:
    add(kw, "en", C, "company", "", t, pr, nt)
for kw, intent, t, pr, nt in [
    ("EL-SHIMY", N, "home", H, "brand"),
    ("Elshimy for Trading & Agencies", N, "home", H, "brand / legal name"),
    ("El-Shimy trading Egypt", N, "home", M, "brand + country"),
]:
    add(kw, "en", intent, "company", "", t, pr, nt)

for kw, t, pr, nt in [
    ("مصدر فواكه وخضروات مصري", "home", H, "core head term"),
    ("شركة تصدير خضروات وفواكه من مصر", "home", H, ""),
    ("مورد خضروات وفواكه طازجة من مصر", "home", H, "مورد = supplier"),
    ("مصدر فاكهة مصري", "home", H, ""),
    ("مصدر خضروات مصري", "home", H, ""),
    ("شركة تصدير حاصلات زراعية مصرية", "about", M, "الحاصلات الزراعية is the formal Egyptian trade term"),
    ("تصدير الحاصلات الزراعية المصرية", "about", M, ""),
    ("مورد فواكه بالجملة في مصر", "products", M, "wholesale intent"),
    ("مصدرين مصريين للفواكه والخضار", "home", L, "خضار is the Gulf/Levant spelling of خضروات"),
    ("منتجات طازجة ومجمدة من مصر", "home", M, "fresh + IQF positioning"),
    ("شركة تجارة وتصدير مصرية", "about", L, ""),
    ("وكيل توريد فواكه وخضروات من مصر", "services", M, "partner-farm sourcing model"),
]:
    add(kw, "ar", C, "company", "", t, pr, nt)
for kw, pr, nt in [("الشيمي للتجارة والتوكيلات", H, "brand / legal name"), ("الشيمي للتصدير", M, "brand"), ("شركة الشيمي مصر", M, "brand + country")]:
    add(kw, "ar", N, "company", "", "home", pr, nt)

# ───────────────────────── products ─────────────────────────
# slug: (en rows, ar rows); each row (keyword, priority, note)
PRODUCTS = {
 "egyptian-potatoes": (
  [("Egyptian potatoes", H, ""), ("Egyptian potato exporter", H, ""), ("potatoes supplier Egypt", H, ""), ("Egypt potatoes export", M, ""),
   ("Spunta potatoes Egypt", M, "variety"), ("Diamant potatoes Egypt", L, "variety"), ("fresh table potatoes wholesale", L, "")],
  [("بطاطس مصرية", H, "Egypt spelling"), ("بطاطا مصرية", H, "Gulf/Levant spelling of potato"), ("تصدير البطاطس المصرية", H, ""), ("مورد بطاطس مصري", H, ""),
   ("مصدر بطاطس في مصر", M, ""), ("بطاطس سبونتا مصرية", M, "variety"), ("بطاطس للتصدير", M, "")]),
 "yellow-onions": (
  [("Egyptian yellow onions", H, ""), ("golden onions Egypt", M, ""), ("yellow onion exporter Egypt", H, ""), ("onions supplier Egypt", H, ""), ("Egyptian onions export", H, "")],
  [("بصل أصفر مصري", H, ""), ("بصل ذهبي مصري", M, ""), ("تصدير البصل المصري", H, ""), ("مورد بصل مصري", H, ""), ("مصدر بصل في مصر", M, "")]),
 "red-onions": (
  [("Egyptian red onions", H, ""), ("red onion exporter Egypt", M, ""), ("red onions supplier Egypt", M, "")],
  [("بصل أحمر مصري", H, ""), ("تصدير البصل الأحمر", M, ""), ("مورد بصل أحمر", M, "")]),
 "tomatoes": (
  [("Egyptian tomatoes", M, ""), ("tomato exporter Egypt", M, ""), ("fresh tomatoes supplier Egypt", M, "")],
  [("طماطم مصرية", M, "Egypt/Gulf spelling"), ("بندورة مصرية", L, "Levant spelling"), ("تصدير الطماطم المصرية", M, ""), ("مورد طماطم من مصر", M, "")]),
 "egyptian-oranges": (
  [("Egyptian oranges", H, ""), ("Egyptian orange exporter", H, ""), ("oranges supplier Egypt", H, ""), ("Egypt oranges export", H, ""),
   ("Navel oranges Egypt", H, "variety"), ("Valencia oranges Egypt", H, "variety"), ("Egyptian citrus exporter", H, "category term")],
  [("برتقال مصري", H, ""), ("تصدير البرتقال المصري", H, ""), ("مصدر برتقال في مصر", H, ""), ("برتقال أبو سرة", H, "Navel in Egypt/Gulf"),
   ("برتقال فالنسيا مصري", H, ""), ("مورد برتقال بالجملة", M, ""), ("مصدر حمضيات مصري", H, "citrus category")]),
 "mandarins": (
  [("Egyptian mandarins", H, ""), ("mandarin exporter Egypt", H, ""), ("Egyptian tangerines", M, "US/UK variant"), ("Egypt mandarin oranges export", M, "")],
  [("يوسفي مصري", H, "Egypt term"), ("ماندرين مصري", M, "Gulf term"), ("تصدير اليوسفي المصري", H, ""), ("مورد يوسفي", M, ""), ("مندرين للتصدير", L, "alt spelling")]),
 "lemons": (
  [("Egyptian lemons", H, ""), ("lemon exporter Egypt", H, ""), ("Adalia lemons Egypt", M, "variety"), ("Egyptian limes", M, ""), ("lemons supplier Egypt", M, "")],
  [("ليمون مصري", H, ""), ("تصدير الليمون المصري", H, ""), ("ليمون أضاليا", M, "variety"), ("ليمون أخضر مصري", M, "limes"), ("مورد ليمون", M, "")]),
 "strawberries": (
  [("Egyptian strawberries", H, ""), ("fresh strawberries exporter Egypt", H, ""), ("strawberries supplier Egypt", H, ""), ("Egypt strawberry export air freight", M, "")],
  [("فراولة مصرية", H, ""), ("تصدير الفراولة المصرية", H, ""), ("مورد فراولة طازجة", H, ""), ("فريز مصري", M, "Levant/Gulf term for strawberry"), ("مصدر فراولة في مصر", M, "")]),
 "pomegranates": (
  [("Egyptian pomegranates", H, ""), ("pomegranate exporter Egypt", H, ""), ("pomegranate supplier Egypt", M, ""), ("Wonderful pomegranate Egypt", M, "variety")],
  [("رمان مصري", H, ""), ("تصدير الرمان المصري", H, ""), ("مورد رمان", M, ""), ("رمان وندرفول", M, "variety")]),
 "grapes": (
  [("Egyptian grapes", H, ""), ("grape exporter Egypt", H, ""), ("seedless grapes Egypt", H, ""), ("Egyptian red seedless grapes", M, ""), ("table grapes supplier Egypt", M, "")],
  [("عنب مصري", H, ""), ("تصدير العنب المصري", H, ""), ("عنب بدون بذور مصري", H, ""), ("عنب أحمر بدون بذور", M, ""), ("مورد عنب", M, "")]),
 "mangoes": (
  [("Egyptian mangoes", M, ""), ("mango exporter Egypt", M, ""), ("Keitt mango Egypt", M, "variety"), ("Kent mango Egypt", L, "variety")],
  [("مانجو مصري", M, "Egypt/Gulf spelling"), ("مانجا مصرية", M, "Levant spelling"), ("تصدير المانجو المصري", M, ""), ("مانجو كيت", L, "variety"), ("مانجو عويس", L, "Egyptian variety")]),
 "dates": (
  [("Egyptian dates", M, ""), ("Barhi dates Egypt", M, ""), ("fresh dates exporter Egypt", M, "")],
  [("بلح مصري", M, "Egypt term for fresh dates"), ("تمور مصرية", M, ""), ("بلح برحي", M, ""), ("تصدير البلح المصري", M, ""), ("تمر مصري للتصدير", L, "")]),
 "guava": (
  [("Egyptian guava", M, ""), ("guava exporter Egypt", M, "")],
  [("جوافة مصرية", M, ""), ("تصدير الجوافة المصرية", M, "")]),
 "watermelon": (
  [("Egyptian watermelon", M, ""), ("watermelon exporter Egypt", M, "")],
  [("بطيخ مصري", M, ""), ("تصدير البطيخ المصري", M, "")]),
 "pears": (
  [("Egyptian pears", L, ""), ("pear exporter Egypt", L, "")],
  [("كمثرى مصرية", L, "Egypt/Gulf term"), ("إجاص مصري", L, "Levant term")]),
 "stone-fruits": (
  [("Egyptian apricots", M, ""), ("Egyptian peaches", M, ""), ("Egyptian plums", L, ""), ("Egyptian nectarines", L, ""), ("stone fruit exporter Egypt", M, "")],
  [("مشمش مصري", M, ""), ("خوخ مصري", M, "Egypt term for peach"), ("دراق مصري", L, "Gulf/Levant term for peach"), ("برقوق مصري", L, ""), ("تصدير الفاكهة ذات النواة", L, "")]),
 "prickly-pear": (
  [("Egyptian prickly pear", L, ""), ("cactus pear exporter Egypt", L, "")],
  [("تين شوكي مصري", L, ""), ("تصدير التين الشوكي", L, "")]),
 "iqf-strawberries": (
  [("IQF strawberries Egypt", H, ""), ("frozen strawberries supplier Egypt", H, ""), ("IQF strawberries supplier", H, "manufacturer intent"), ("Egyptian frozen strawberries", H, ""), ("frozen strawberries for food manufacturers", M, "")],
  [("فراولة مجمدة مصرية", H, ""), ("فراولة IQF", H, "IQF is used in Latin letters in Arabic trade searches"), ("مورد فراولة مجمدة", H, ""), ("تصدير الفراولة المجمدة", M, ""), ("فراولة مجمدة للمصانع", M, "")]),
 "iqf-berries": (
  [("IQF blueberries supplier", M, ""), ("frozen raspberries supplier Egypt", M, ""), ("IQF berries Egypt", M, ""), ("frozen blackberries supplier", L, "")],
  [("توت مجمد", M, ""), ("توت أزرق مجمد IQF", M, "blueberry"), ("توت العليق المجمد", L, "raspberry"), ("مورد توت مجمد", M, "")]),
}
for slug, (en, ar) in PRODUCTS.items():
    for kw, pr, nt in en: add(kw, "en", C, "product", slug, "p:" + slug, pr, nt)
    for kw, pr, nt in ar: add(kw, "ar", C, "product", slug, "p:" + slug, pr, nt)

# ───────────────────────── markets ─────────────────────────
GULF = ("NEW", "/markets/gulf-countries/")
for kw, t, pr, nt in [
    ("Egyptian produce for Gulf importers", GULF, H, "priority market #1"),
    ("export fruit from Egypt to Saudi Arabia", GULF, H, ""),
    ("Egyptian vegetables exporter to UAE", GULF, H, ""),
    ("Egyptian oranges Saudi Arabia importers", GULF, M, ""),
    ("Egyptian fruit suppliers Kuwait Qatar Oman", GULF, L, "only target countries once real orders exist; do not claim customers"),
    ("Egyptian produce exporter to Asia", "markets", M, "priority market #2"),
    ("Egypt fresh produce export markets", "markets", M, ""),
    ("fresh produce supplier for hotels and food distributors", "services", M, ""),
]:
    add(kw, "en", C, "market", "", t, pr, nt)
for kw, t, pr, nt in [
    ("تصدير فواكه مصرية إلى السعودية", GULF, H, ""),
    ("مصدر خضروات مصري للإمارات", GULF, H, ""),
    ("موردين فواكه وخضروات لدول الخليج", GULF, H, "دول الخليج"),
    ("مستورد فواكه مصرية في الخليج", GULF, M, "importer-side search"),
    ("تصدير برتقال مصري للسعودية", GULF, M, ""),
    ("تصدير خضروات وفواكه إلى آسيا", "markets", M, ""),
    ("أسواق تصدير الخضروات والفواكه المصرية", "markets", M, ""),
    ("مورد فواكه وخضروات للفنادق والموزعين", "services", M, ""),
]:
    add(kw, "ar", C, "market", "", t, pr, nt)

# ───────────────────────── logistics ─────────────────────────
IMPORT_GUIDE = ("NEW", "/insights/import-fresh-produce-from-egypt/")
for kw, intent, t, pr, nt in [
    ("how to import fruit and vegetables from Egypt", I, IMPORT_GUIDE, H, "guide proposal; ties to freight + quote pages"),
    ("import fresh produce from Egypt", C, IMPORT_GUIDE, H, ""),
    ("reefer container Egypt fresh produce", C, "freight", H, ""),
    ("sea freight fresh fruit from Egypt", C, "freight", M, ""),
    ("air freight fresh strawberries Egypt", C, "freight", M, ""),
    ("Egypt export customs clearance fresh produce", I, "freight", M, ""),
    ("phytosanitary certificate Egypt fruit export", I, "freight", M, ""),
    ("export documents for fresh produce from Egypt", I, "freight", M, ""),
    ("Incoterms for fresh produce FOB CIF", I, "freight", M, "EXW/FOB/CIF/DAP table already on the page"),
    ("door to door delivery fruit from Egypt", C, "freight", L, "only where available; do not promise"),
    ("Egyptian produce quote request", C, "contact", M, ""),
]:
    add(kw, "en", intent, "logistics", "", t, pr, nt)
for kw, intent, t, pr, nt in [
    ("كيفية استيراد الفواكه والخضروات من مصر", I, IMPORT_GUIDE, H, "guide proposal"),
    ("استيراد فواكه طازجة من مصر", C, IMPORT_GUIDE, H, ""),
    ("حاويات مبردة لشحن الفواكه من مصر", C, "freight", H, "حاويات مبردة / ريفر"),
    ("شحن بحري مبرد من مصر", C, "freight", M, ""),
    ("شحن جوي فراولة طازجة من مصر", C, "freight", M, ""),
    ("التخليص الجمركي لصادرات الفواكه والخضروات", I, "freight", M, ""),
    ("شهادة صحة نباتية للتصدير من مصر", I, "freight", M, ""),
    ("مستندات تصدير الخضروات والفواكه", I, "freight", M, ""),
    ("شروط التسليم FOB وCIF للخضروات والفواكه", I, "freight", L, ""),
    ("طلب عرض سعر خضروات وفواكه مصرية", C, "contact", M, "never publish fixed prices; quote per enquiry"),
]:
    add(kw, "ar", intent, "logistics", "", t, pr, nt)

# ───────────────────────── quality ─────────────────────────
IQF_GUIDE = ("NEW", "/insights/what-is-iqf-frozen-fruit/")
for kw, intent, t, pr, nt in [
    ("fruit export specifications size grade packing", I, "quality", M, ""),
    ("quality control for fresh produce export", I, "quality", M, ""),
    ("pre-shipment inspection fresh fruit", I, "quality", L, ""),
    ("fresh produce traceability documents", I, "quality", L, ""),
    ("food safety fresh produce Egypt", I, "quality", L, ""),
    ("ISO 22000 certified exporter Egypt", C, "quality", L, "BLOCKED: do not target or claim until SHOW_ISO is verified"),
    ("what is IQF frozen fruit", I, IQF_GUIDE, M, "guide proposal; feeds the two IQF product pages"),
    ("IQF vs block frozen strawberries", I, IQF_GUIDE, L, ""),
]:
    add(kw, "en", intent, "quality", "", t, pr, nt)
for kw, intent, t, pr, nt in [
    ("مواصفات تصدير الفواكه والخضروات", I, "quality", M, ""),
    ("مراقبة الجودة في تصدير المنتجات الطازجة", I, "quality", M, ""),
    ("فحص الشحنات قبل التصدير", I, "quality", L, ""),
    ("سلامة الغذاء في تصدير الفواكه", I, "quality", L, ""),
    ("ما هو التجميد السريع IQF للفواكه", I, IQF_GUIDE, M, "guide proposal"),
    ("الفرق بين IQF والتجميد العادي", I, IQF_GUIDE, L, ""),
]:
    add(kw, "ar", intent, "quality", "", t, pr, nt)
