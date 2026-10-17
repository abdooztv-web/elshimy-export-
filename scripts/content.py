# -*- coding: utf-8 -*-
"""Bilingual content for the El-Shimy website. Edit facts/config here, then run `python scripts/build.py`."""

# ───────────────────────── Configuration / verification flags ─────────────────────────
SITE = "https://elshimy.com"
BRAND = "EL-SHIMY"
LEGAL = {"en": "EL-SHIMY for Trading & Agencies", "ar": "الشيمي للتجارة والتوكيلات"}
EMAIL = "info@elshimy.com"             # from the previous README - confirm it is monitored
WHATSAPP = ""                          # digits only incl. country code, e.g. "20xxxxxxxxxx". Empty = WhatsApp links hidden.
FORM_ENDPOINT = ""                     # Formspree/Netlify/own endpoint. Empty = form opens a pre-filled email draft.
GSC_TOKEN = ""                         # Google Search Console verification token (optional)
SHOW_ISO = False                       # set True once the ISO 22000 certificate (holder, scope, validity, body) is verified
SHOW_VOLUME = False                    # set True once ~400 t exported in 2025 is verified against shipping records
ADDRESS = {"en": "Office 3, Mall 11, Beverly Hills, Giza, Egypt",
           "ar": "مكتب 3، مول 11، بيفرلي هيلز، الجيزة، مصر"}  # from previous site - confirm

# ───────────────────────── UI strings ─────────────────────────
UI = {
 "en": {
  "skip": "Skip to main content", "menu": "Menu", "close": "Close",
  "nav": {"products": "Products", "services": "Sourcing & Export", "freight": "Freight & Customs",
          "quality": "Quality & Food Safety", "markets": "Markets", "about": "About", "insights": "Insights", "contact": "Contact"},
  "quote": "Request a Quote", "lang_name": "العربية", "lang_label": "Read this page in Arabic",
  "home": "Home", "breadcrumb": "Breadcrumb", "footer_tag": "Egyptian Products. Global Markets.",
  "footer_products": "Products", "footer_company": "Company", "footer_contact": "Contact",
  "img_note": "Images are illustrative stock photography unless captioned otherwise.", "credits": "Photo credits",
  "rights": "All rights reserved.", "whatsapp": "WhatsApp", "email_us": "Email us",
  "view_all": "View all products", "learn_more": "Learn more", "request_quote_for": "Request a quote for",
  "fresh": "Fresh", "frozen": "Frozen (IQF)", "veg": "Vegetables", "fruit": "Fruits", "frozen_cat": "Frozen Products",
  "all": "All", "search": "Search products", "no_results": "No products match your filter.", "filters": "Filter products",
  "type": "Form", "season": "Indicative season", "packing": "Typical packing", "category": "Category",
  "varieties": "Varieties", "sizes": "Sizes & grading", "packaging": "Packaging", "storage": "Storage & shipping",
  "docs": "Documentation", "related": "Related products", "spec_note": "Specifications on this page are indicative industry references, not a commitment. Variety, grade, size, packing, availability and price are confirmed in a written quote for each shipment.",
  "season_note": "Indicative Egyptian harvest window from external industry references. El-Shimy availability is confirmed per order.",
  "spec_title": "Product specifications", "details_title": "Details buyers ask for",
 },
 "ar": {
  "skip": "انتقل إلى المحتوى الرئيسي", "menu": "القائمة", "close": "إغلاق",
  "nav": {"products": "المنتجات", "services": "التوريد والتصدير", "freight": "الشحن والتخليص الجمركي",
          "quality": "الجودة وسلامة الغذاء", "markets": "الأسواق", "about": "من نحن", "insights": "مقالات ودلائل", "contact": "اتصل بنا"},
  "quote": "اطلب عرض سعر", "lang_name": "English", "lang_label": "اقرأ هذه الصفحة بالإنجليزية",
  "home": "الرئيسية", "breadcrumb": "مسار التنقل", "footer_tag": "منتجات مصرية. أسواق عالمية.",
  "footer_products": "المنتجات", "footer_company": "الشركة", "footer_contact": "تواصل معنا",
  "img_note": "الصور المستخدمة توضيحية من مصادر صور مجانية ما لم يُذكر خلاف ذلك.", "credits": "حقوق الصور",
  "rights": "جميع الحقوق محفوظة.", "whatsapp": "واتساب", "email_us": "راسلنا عبر البريد",
  "view_all": "عرض كل المنتجات", "learn_more": "اعرف المزيد", "request_quote_for": "اطلب عرض سعر لـ",
  "fresh": "طازج", "frozen": "مجمد (IQF)", "veg": "الخضروات", "fruit": "الفاكهة", "frozen_cat": "المنتجات المجمدة",
  "all": "الكل", "search": "ابحث في المنتجات", "no_results": "لا توجد منتجات مطابقة.", "filters": "تصفية المنتجات",
  "type": "الحالة", "season": "الموسم التقريبي", "packing": "التعبئة المعتادة", "category": "الفئة",
  "varieties": "الأصناف", "sizes": "الأحجام والتدريج", "packaging": "التعبئة", "storage": "التخزين والشحن",
  "docs": "المستندات", "related": "منتجات ذات صلة", "spec_note": "المواصفات في هذه الصفحة مراجع إرشادية للقطاع وليست التزاماً. يتم تأكيد الصنف والدرجة والحجم والتعبئة والتوافر والسعر في عرض سعر مكتوب لكل شحنة.",
  "season_note": "فترة حصاد مصرية تقريبية من مراجع خارجية للقطاع. يتم تأكيد توافر الشيمي لكل طلب.",
  "spec_title": "مواصفات المنتج", "details_title": "تفاصيل يسأل عنها المستوردون",
 },
}

# ───────────────────────── Products ─────────────────────────
# fields: slug, cat (veg|fruit|frozen), img (photo name or None), accent, name, tag (short), intro, varieties, sizes, packing, season, form
P = []
def add(**k): P.append(k)

PACK_GEN = {
 "en": "Cartons or crates, palletised; mesh bags for dry vegetables. Exact format and weight agreed per order.",
 "ar": "كراتين أو صناديق على بالتات؛ وأجولة شبكية للخضروات الجافة. يُتفق على الشكل والوزن لكل طلب.",
}
STORE_GEN = {
 "en": "Shipped in temperature-controlled (reefer) containers or by air freight, depending on the commodity, transit time and destination. Set-points and ventilation are agreed per product.",
 "ar": "تُشحن في حاويات مبرّدة أو بالشحن الجوي بحسب المنتج ومدة الرحلة والوجهة. يُتفق على درجات الحرارة والتهوية لكل منتج.",
}
DOCS_GEN = {
 "en": "Commonly requested: commercial invoice, packing list, phytosanitary certificate, certificate of origin and any importer-specific documents. We confirm the exact set with you before shipment.",
 "ar": "المستندات المطلوبة عادةً: الفاتورة التجارية، قائمة التعبئة، شهادة صحة نباتية، شهادة المنشأ وأي مستندات يطلبها المستورد. نؤكد المجموعة المطلوبة معك قبل الشحن.",
}

add(slug="egyptian-potatoes", cat="veg", img="potatoes", accent="#C8A25B", form="fresh",
 name={"en": "Egyptian Potatoes", "ar": "البطاطس المصرية"},
 tag={"en": "Table potatoes for retail, wholesale and food service", "ar": "بطاطس مائدة للتجزئة والجملة والمطاعم"},
 title={"en": "Egyptian Potatoes Export | Fresh Table Potatoes | EL-SHIMY", "ar": "تصدير البطاطس المصرية | بطاطس طازجة | الشيمي"},
 meta={"en": "Request a quote for fresh Egyptian potatoes. Varieties, sizing, packing and shipping options coordinated by EL-SHIMY for importers and distributors.",
       "ar": "اطلب عرض سعر للبطاطس المصرية الطازجة. الأصناف والأحجام والتعبئة وخيارات الشحن بتنسيق الشيمي للمستوردين والموزعين."},
 intro={"en": "Egyptian potatoes are one of the country's most established vegetable exports, supplied to importers, wholesalers and food service buyers. EL-SHIMY sources through partner farms and packhouses and coordinates grading, packing and shipment to your specification.",
        "ar": "تُعد البطاطس المصرية من أبرز الصادرات الزراعية الراسخة، وتُورَّد للمستوردين وتجار الجملة وقطاع الضيافة. يوفرها الشيمي عبر مزارع ومحطات تعبئة شريكة وينسق الفرز والتعبئة والشحن وفق مواصفاتك."},
 varieties={"en": "Commonly requested export varieties include Spunta, Diamant and Cara; red-skinned options are also available in the market. Confirm your required variety, skin colour and intended use (fresh table, frying, processing).",
            "ar": "من الأصناف المطلوبة عادةً للتصدير: سبونتا وديامان وكارا، كما تتوفر أصناف حمراء القشرة في السوق. حدّد الصنف ولون القشرة والاستخدام (مائدة، قلي، تصنيع)."},
 sizes={"en": "Sized by diameter in millimetres (for example 35–55 mm or 45–65 mm) with limits on defects, greening and damage. Share your target size range and we will confirm what is achievable.",
        "ar": "تُصنَّف بالقطر بالمليمتر (مثلاً 35–55 أو 45–65 مم) مع حدود للعيوب والاخضرار والتلف. أرسل نطاق الحجم المطلوب لنؤكد المتاح."},
 packing=PACK_GEN, season={"en": "≈ Jan – May", "ar": "≈ يناير – مايو"})

add(slug="yellow-onions", cat="veg", img="yellow-onions", accent="#D9A441", form="fresh",
 name={"en": "Yellow / Golden Onions", "ar": "البصل الأصفر (الذهبي)"},
 tag={"en": "Dry golden onions, graded and bagged for export", "ar": "بصل ذهبي جاف، مفروز ومعبأ للتصدير"},
 title={"en": "Yellow Onions from Egypt | Golden Onion Exporter | EL-SHIMY", "ar": "البصل الأصفر المصري | مُصدّر البصل الذهبي | الشيمي"},
 meta={"en": "Egyptian yellow (golden) onions for export: sizing, bagging and shipping coordinated by EL-SHIMY. Request a specification-based quote.",
       "ar": "بصل أصفر (ذهبي) مصري للتصدير: الفرز والتعبئة والشحن بتنسيق الشيمي. اطلب عرض سعر وفق مواصفاتك."},
 intro={"en": "Golden onions are a staple dry-vegetable export from Egypt: firm bulbs with papery yellow-brown skin and a strong, pungent flavour that suits cooking and processing. EL-SHIMY coordinates sourcing, sizing and packing for importers and distributors.",
        "ar": "البصل الذهبي من أهم الخضروات الجافة المصدّرة من مصر: أبصال متماسكة بقشرة ورقية صفراء مائلة للبني ونكهة قوية تناسب الطهي والتصنيع. ينسق الشيمي التوريد والفرز والتعبئة للمستوردين والموزعين."},
 varieties={"en": "Yellow/golden onions in round to globe shapes. Specify dry-matter needs, skin quality and neck dryness if they matter for storage on your side.",
            "ar": "بصل أصفر/ذهبي بأشكال كروية. حدّد المادة الجافة وجودة القشرة وجفاف الرقبة إن كانت مهمة للتخزين لديك."},
 sizes={"en": "Sized by diameter in millimetres, commonly in bands such as 40–60, 50–70 or 60–80 mm. Tell us your preferred band and tolerance.",
        "ar": "تُصنَّف بالقطر بالمليمتر، وغالباً بنطاقات مثل 40–60 أو 50–70 أو 60–80 مم. أخبرنا بالنطاق والتفاوت المطلوبين."},
 packing={"en": "Mesh bags (commonly 10–25 kg), palletised and loaded in ventilated or reefer containers. Bag weight and labelling agreed per order.",
          "ar": "أجولة شبكية (غالباً 10–25 كجم) على بالتات وتُحمَّل في حاويات مهواة أو مبرّدة. يُتفق على الوزن والملصقات لكل طلب."},
 season={"en": "≈ Jan – Aug", "ar": "≈ يناير – أغسطس"})

add(slug="red-onions", cat="veg", img="red-onions", accent="#9C2F4F", form="fresh",
 name={"en": "Red Onions", "ar": "البصل الأحمر"},
 tag={"en": "Mild to sweet red onions for retail and food service", "ar": "بصل أحمر معتدل إلى حلو للتجزئة والمطاعم"},
 title={"en": "Egyptian Red Onions Export | Red Onion Supplier | EL-SHIMY", "ar": "تصدير البصل الأحمر المصري | مورّد البصل الأحمر | الشيمي"},
 meta={"en": "Red onions from Egypt for importers and distributors. Sizing, packing and shipment arranged by EL-SHIMY. Ask for a quote.",
       "ar": "بصل أحمر مصري للمستوردين والموزعين. الفرز والتعبئة والشحن بترتيب الشيمي. اطلب عرض سعر."},
 intro={"en": "Red onions are valued for their colour and milder, sweeter taste, which suits salads, grilling and fresh-cut applications. EL-SHIMY coordinates supply from partner farms and packhouses, graded to your size and quality requirements.",
        "ar": "يتميز البصل الأحمر بلونه ونكهته الأخف والأحلى التي تناسب السلطات والشواء والتقطيع الطازج. ينسق الشيمي التوريد من مزارع ومحطات تعبئة شريكة بدرجات تناسب متطلبات الحجم والجودة لديك."},
 varieties={"en": "Medium to large red onions with deep skin colour. State preferred colour intensity, shape and whether you need tight-skinned bulbs for longer transit.",
            "ar": "بصل أحمر متوسط إلى كبير بلون قشرة عميق. حدّد شدة اللون والشكل وهل تحتاج أبصالاً محكمة القشرة لرحلات أطول."},
 sizes={"en": "Sized by diameter in millimetres (for example 40–60 or 50–80 mm). Confirm your band and defect tolerance in the enquiry.",
        "ar": "تُصنَّف بالقطر بالمليمتر (مثلاً 40–60 أو 50–80 مم). أكّد النطاق وحدود العيوب في طلبك."},
 packing=PACK_GEN, season={"en": "≈ Jan – Aug", "ar": "≈ يناير – أغسطس"})

add(slug="tomatoes", cat="veg", img="tomatoes", accent="#C8402B", form="fresh",
 name={"en": "Egyptian Tomatoes", "ar": "الطماطم المصرية"},
 tag={"en": "Fresh round tomatoes, packed for export", "ar": "طماطم مستديرة طازجة معبأة للتصدير"},
 title={"en": "Egyptian Tomatoes Export | Fresh Tomato Supplier | EL-SHIMY", "ar": "تصدير الطماطم المصرية | مورّد طماطم طازجة | الشيمي"},
 meta={"en": "Fresh tomatoes from Egypt for importers and wholesalers. Maturity, size and packing coordinated by EL-SHIMY. Request a quote.",
       "ar": "طماطم مصرية طازجة للمستوردين وتجار الجملة. النضج والحجم والتعبئة بتنسيق الشيمي. اطلب عرض سعر."},
 intro={"en": "Tomatoes are a perishable, quality-sensitive product where harvest maturity, handling and transit time matter. EL-SHIMY works with partner growers and packhouses to match maturity and packing to your destination and shipping mode.",
        "ar": "الطماطم منتج سريع التلف وحساس للجودة، ويتوقف أداؤه على درجة النضج عند الحصاد والتداول ومدة الرحلة. يعمل الشيمي مع مزارعين ومحطات تعبئة شريكة لمطابقة النضج والتعبئة مع وجهتك ووسيلة الشحن."},
 varieties={"en": "Round (slicing) tomatoes in firm, uniform grades. Specify colour stage, firmness and whether you need air or sea freight, which affects the maturity we recommend.",
            "ar": "طماطم مستديرة بدرجات متماسكة ومتجانسة. حدّد مرحلة اللون والتماسك ووسيلة الشحن الجوية أو البحرية لأنها تحدد النضج الموصى به."},
 sizes={"en": "Sized by diameter in millimetres in bands set per order, with limits on blemishes and soft fruit.",
        "ar": "تُصنَّف بالقطر بالمليمتر بنطاقات تُحدد لكل طلب مع حدود للعيوب والثمار الطرية."},
 packing={"en": "Cartons or ventilated crates, palletised; net weight and carton type agreed per order.",
          "ar": "كراتين أو صناديق مهواة على بالتات؛ يُتفق على الوزن الصافي ونوع الكرتون لكل طلب."},
 season={"en": "≈ Nov – Apr", "ar": "≈ نوفمبر – أبريل"})

add(slug="egyptian-oranges", cat="fruit", img="oranges", accent="#E8892B", form="fresh",
 name={"en": "Egyptian Oranges", "ar": "البرتقال المصري"},
 tag={"en": "Navel and Valencia oranges for fresh and juice markets", "ar": "برتقال أبو سرة وفالنسيا للاستهلاك الطازج والعصير"},
 title={"en": "Egyptian Oranges Export | Navel & Valencia Oranges | EL-SHIMY", "ar": "تصدير البرتقال المصري | أبو سرة وفالنسيا | الشيمي"},
 meta={"en": "Navel and Valencia oranges from Egypt for Gulf, Asian and other importers. Count sizes, packing and shipping coordinated by EL-SHIMY.",
       "ar": "برتقال أبو سرة وفالنسيا مصري لمستوردي الخليج وآسيا وغيرها. الأحجام والتعبئة والشحن بتنسيق الشيمي."},
 intro={"en": "Oranges are Egypt's best-known citrus export. Navel oranges are prized for easy peeling and sweet, seedless flesh, while Valencia suits juicing and later-season supply. EL-SHIMY coordinates sourcing, grading and shipment from partner farms and packhouses.",
        "ar": "البرتقال أشهر صادرات مصر من الحمضيات. يتميز أبو سرة بسهولة التقشير ولبّه الحلو الخالي من البذور، بينما تناسب الفالنسيا العصير والموسم المتأخر. ينسق الشيمي التوريد والفرز والشحن من مزارع ومحطات تعبئة شريكة."},
 varieties={"en": "Navel (early season), Valencia (later season, juicing and fresh) and Baladi. Tell us the variety, colour and Brix expectations for your market.",
            "ar": "أبو سرة (بداية الموسم)، فالنسيا (موسم متأخر للعصير والاستهلاك الطازج) وبلدي. أخبرنا بالصنف واللون وتوقعات البريكس لسوقك."},
 sizes={"en": "Citrus is sized by count per carton (e.g. 48, 56, 64, 72, 80, 88, 100). Share the count range you sell and we will confirm availability.",
        "ar": "تُصنَّف الحمضيات بالعدد في الكرتونة (مثل 48 و56 و64 و72 و80 و88 و100). أرسل نطاق العدد الذي تبيعه لنؤكد التوافر."},
 packing={"en": "Cartons (commonly 7.5–15 kg), open-top or telescopic, palletised in reefer containers. Waxing, labelling and private-label options on request.",
          "ar": "كراتين (غالباً 7.5–15 كجم) مفتوحة أو تلسكوبية على بالتات في حاويات مبرّدة. التشميع والملصقات والعلامة الخاصة عند الطلب."},
 season={"en": "≈ Dec – Jun", "ar": "≈ ديسمبر – يونيو"})

add(slug="mandarins", cat="fruit", img="mandarins", accent="#E8892B", form="fresh",
 name={"en": "Egyptian Mandarins", "ar": "اليوسفي المصري"},
 tag={"en": "Easy-peel mandarins from the winter citrus season", "ar": "يوسفي سهل التقشير من موسم الحمضيات الشتوي"},
 title={"en": "Egyptian Mandarins Export | Fresh Mandarin Supplier | EL-SHIMY", "ar": "تصدير اليوسفي المصري | مورّد يوسفي طازج | الشيمي"},
 meta={"en": "Fresh mandarins from Egypt for importers and distributors. Sizing, packing and shipping options arranged by EL-SHIMY.",
       "ar": "يوسفي مصري طازج للمستوردين والموزعين. الأحجام والتعبئة وخيارات الشحن بترتيب الشيمي."},
 intro={"en": "Mandarins are a winter citrus favourite: small, easy to peel and sweet. EL-SHIMY coordinates supply from partner farms and packhouses with sizing and packing matched to your retail or wholesale programme.",
        "ar": "اليوسفي من أحب حمضيات الشتاء: صغير الحجم وسهل التقشير وحلو المذاق. ينسق الشيمي التوريد من مزارع ومحطات تعبئة شريكة مع أحجام وتعبئة تناسب برنامجك للتجزئة أو الجملة."},
 varieties={"en": "Seedless, easy-peel mandarin types. Ask about the specific variety, colour and seed expectations for your market.",
            "ar": "أنواع يوسفي خالية من البذور وسهلة التقشير. اسأل عن الصنف واللون وتوقعات البذور في سوقك."},
 sizes={"en": "Sized by count per carton in bands agreed per order (for example 72–125).", "ar": "تُصنَّف بالعدد في الكرتونة بنطاقات تُتفق لكل طلب (مثلاً 72–125)."},
 packing=PACK_GEN, season={"en": "≈ Nov – Feb", "ar": "≈ نوفمبر – فبراير"})

add(slug="lemons", cat="fruit", img="lemons", accent="#E3C53B", form="fresh",
 name={"en": "Egyptian Lemons & Limes", "ar": "الليمون المصري"},
 tag={"en": "Adalia lemons and green limes", "ar": "ليمون أداليا وليمون أخضر"},
 title={"en": "Egyptian Lemons Export | Adalia Lemon & Lime Supplier | EL-SHIMY", "ar": "تصدير الليمون المصري | أداليا والليمون الأخضر | الشيمي"},
 meta={"en": "Adalia lemons and limes from Egypt for importers. Count sizes, packing and shipping coordinated by EL-SHIMY.",
       "ar": "ليمون أداليا وليمون أخضر مصري للمستوردين. الأحجام والتعبئة والشحن بتنسيق الشيمي."},
 intro={"en": "Lemons and limes are steady-demand citrus items for retail, food service and processing. EL-SHIMY coordinates sourcing and packing of juicy, bright-yellow lemons and thin-skinned green limes.",
        "ar": "الليمون والليمون الأخضر من الحمضيات ذات الطلب المستقر للتجزئة والمطاعم والتصنيع. ينسق الشيمي توريد وتعبئة ليمون أصفر زاهٍ وعصيري وليمون أخضر رقيق القشرة."},
 varieties={"en": "Adalia lemon (medium to large, smooth skin, high juice) and small green lime. State colour, juice content and skin-finish requirements.",
            "ar": "ليمون أداليا (متوسط إلى كبير، قشرة ناعمة، عصير وفير) وليمون أخضر صغير. حدّد اللون ومحتوى العصير ومواصفات القشرة."},
 sizes={"en": "Sized by count per carton (e.g. 80–138 for lemons). Confirm your required range.", "ar": "تُصنَّف بالعدد في الكرتونة (مثلاً 80–138 للّيمون). أكّد النطاق المطلوب."},
 packing=PACK_GEN, season={"en": "≈ Sep – Feb", "ar": "≈ سبتمبر – فبراير"})

add(slug="strawberries", cat="fruit", img="strawberries", accent="#C8283C", form="fresh",
 name={"en": "Fresh Egyptian Strawberries", "ar": "الفراولة المصرية الطازجة"},
 tag={"en": "Fresh strawberries for air and sea freight", "ar": "فراولة طازجة للشحن الجوي والبحري"},
 title={"en": "Fresh Egyptian Strawberries Export | Strawberry Supplier | EL-SHIMY", "ar": "تصدير الفراولة المصرية الطازجة | مورّد الفراولة | الشيمي"},
 meta={"en": "Fresh strawberries from Egypt for Gulf and Asian importers. Pre-cooling, punnet packing and air or sea freight coordinated by EL-SHIMY.",
       "ar": "فراولة مصرية طازجة لمستوردي الخليج وآسيا. التبريد المسبق والتعبئة في عبوات وشحن جوي أو بحري بتنسيق الشيمي."},
 intro={"en": "Fresh strawberries are highly perishable, so cold-chain discipline and short transit matter. EL-SHIMY coordinates harvesting-to-shipment planning with partner growers and packhouses, and can advise on air versus sea freight for your destination. Frozen (IQF) strawberries are available as a separate product.",
        "ar": "الفراولة الطازجة سريعة التلف، لذا تتطلب انضباطاً في سلسلة التبريد ومدة نقل قصيرة. ينسق الشيمي التخطيط من الحصاد حتى الشحن مع مزارعين ومحطات تعبئة شريكة، ويقدم المشورة بين الشحن الجوي والبحري لوجهتك. الفراولة المجمدة (IQF) متاحة كمنتج منفصل."},
 varieties={"en": "Firm, red, aromatic strawberry varieties suited to export. Specify variety preferences, colour coverage and Brix targets.",
            "ar": "أصناف فراولة حمراء متماسكة وعطرية مناسبة للتصدير. حدّد الصنف المفضل وتغطية اللون وهدف البريكس."},
 sizes={"en": "Graded by fruit diameter and quality class (e.g. Class I). Share your required size and defect tolerance.", "ar": "تُفرز بحسب قطر الثمرة ودرجة الجودة (مثل الدرجة الأولى). أرسل الحجم المطلوب وحدود العيوب."},
 packing={"en": "Punnets or clamshells packed into cartons and palletised; pre-cooled before loading. Weights and labelling agreed per order.",
          "ar": "عبوات أو علب بلاستيكية في كراتين على بالتات؛ وتُبرَّد مسبقاً قبل التحميل. يُتفق على الأوزان والملصقات لكل طلب."},
 season={"en": "≈ Nov – Feb", "ar": "≈ نوفمبر – فبراير"})

add(slug="pomegranates", cat="fruit", img="pomegranates", accent="#A3203A", form="fresh",
 name={"en": "Egyptian Pomegranates", "ar": "الرمان المصري"},
 tag={"en": "Red pomegranates with good colour and juice", "ar": "رمان أحمر بلون وعصير جيدين"},
 title={"en": "Egyptian Pomegranates Export | Pomegranate Supplier | EL-SHIMY", "ar": "تصدير الرمان المصري | مورّد الرمان | الشيمي"},
 meta={"en": "Pomegranates from Egypt for importers and distributors. Varieties, sizes and packing coordinated by EL-SHIMY.",
       "ar": "رمان مصري للمستوردين والموزعين. الأصناف والأحجام والتعبئة بتنسيق الشيمي."},
 intro={"en": "Egyptian pomegranates are exported for their deep-red colour, juicy arils and good keeping quality. EL-SHIMY coordinates sourcing and packing from partner farms to match your size and quality requirements.",
        "ar": "يُصدَّر الرمان المصري لما يتميز به من لون أحمر عميق وحبوب عصيرية وجودة تخزين جيدة. ينسق الشيمي التوريد والتعبئة من مزارع شريكة بما يطابق متطلبات الحجم والجودة لديك."},
 varieties={"en": "Commonly Wonderful and Baladi types, plus early varieties at the start of the season. Specify variety, skin colour and aril colour.",
            "ar": "عادةً أصناف وندرفول والبلدي، إضافة إلى أصناف مبكرة في بداية الموسم. حدّد الصنف ولون القشرة ولون الحبوب."},
 sizes={"en": "Sized by count per carton (larger fruit has a lower count). Confirm your required size range.", "ar": "تُصنَّف بالعدد في الكرتونة (الثمرة الأكبر عددها أقل). أكّد نطاق الحجم المطلوب."},
 packing={"en": "Cartons or plastic boxes (commonly 4–5 kg), palletised in reefer containers.", "ar": "كراتين أو صناديق بلاستيكية (غالباً 4–5 كجم) على بالتات في حاويات مبرّدة."},
 season={"en": "≈ Aug – Dec", "ar": "≈ أغسطس – ديسمبر"})

add(slug="grapes", cat="fruit", img="grapes", accent="#6B3F7B", form="fresh",
 name={"en": "Egyptian Grapes", "ar": "العنب المصري"},
 tag={"en": "Seedless green, red and black table grapes", "ar": "عنب مائدة أخضر وأحمر وأسود بدون بذور"},
 title={"en": "Egyptian Grapes Export | Seedless Table Grapes | EL-SHIMY", "ar": "تصدير العنب المصري | عنب مائدة بدون بذور | الشيمي"},
 meta={"en": "Seedless Egyptian table grapes for importers: green, red and black. Packing and shipping coordinated by EL-SHIMY.",
       "ar": "عنب مائدة مصري بدون بذور للمستوردين: أخضر وأحمر وأسود. التعبئة والشحن بتنسيق الشيمي."},
 intro={"en": "Egyptian table grapes reach international shelves in green, red and black seedless types. EL-SHIMY coordinates the supply chain with partner growers and packhouses, including packing style, pre-cooling and shipping mode.",
        "ar": "يصل العنب المصري إلى الأسواق العالمية بأنواعه الأخضر والأحمر والأسود الخالي من البذور. ينسق الشيمي سلسلة التوريد مع مزارعين ومحطات تعبئة شريكة، بما في ذلك نمط التعبئة والتبريد المسبق ووسيلة الشحن."},
 varieties={"en": "Green seedless (e.g. Superior, Sugraone, Flame types), red (e.g. Crimson types) and black seedless. Specify variety, berry size and Brix expectations.",
            "ar": "أخضر بدون بذور (مثل سوبيريور وشوغراون وفلايم)، وأحمر (مثل كريمسون) وأسود بدون بذور. حدّد الصنف وحجم الحبة وتوقعات البريكس."},
 sizes={"en": "Graded by berry diameter and bunch weight, with limits on shatter and blemish. Confirm your requirements.", "ar": "تُفرز بحسب قطر الحبة ووزن العنقود مع حدود لتساقط الحبات والعيوب. أكّد متطلباتك."},
 packing={"en": "Cartons (commonly around 4.5–5 kg) with liners or punnets, palletised and pre-cooled.", "ar": "كراتين (غالباً نحو 4.5–5 كجم) مع بطانة أو عبوات، على بالتات ومبرّدة مسبقاً."},
 season={"en": "≈ May – Oct", "ar": "≈ مايو – أكتوبر"})

add(slug="mangoes", cat="fruit", img="mangoes", accent="#E7A33A", form="fresh",
 name={"en": "Egyptian Mangoes", "ar": "المانجو المصري"},
 tag={"en": "Egyptian mango varieties for air and sea freight", "ar": "أصناف المانجو المصري للشحن الجوي والبحري"},
 title={"en": "Egyptian Mangoes Export | Mango Supplier | EL-SHIMY", "ar": "تصدير المانجو المصري | مورّد المانجو | الشيمي"},
 meta={"en": "Egyptian mangoes for importers: Keitt, Kent, Tommy Atkins and local varieties. Maturity, packing and shipping coordinated by EL-SHIMY.",
       "ar": "مانجو مصري للمستوردين: كيت وكنت وتومي أتكنز وأصناف محلية. النضج والتعبئة والشحن بتنسيق الشيمي."},
 intro={"en": "Egyptian mango season runs through late summer and autumn. Choosing the right maturity for your shipping mode is the key to arriving fruit in good condition; EL-SHIMY coordinates this with partner growers and packhouses.",
        "ar": "يمتد موسم المانجو المصري من أواخر الصيف إلى الخريف. اختيار درجة النضج المناسبة لوسيلة الشحن هو مفتاح وصول الثمار بحالة جيدة، وينسق الشيمي ذلك مع مزارعين ومحطات تعبئة شريكة."},
 varieties={"en": "Commonly Keitt, Kent, Tommy Atkins, plus local varieties such as Zebdia and Ewais. Specify variety, colour and maturity stage.",
            "ar": "عادةً كيت وكنت وتومي أتكنز، إضافة إلى أصناف محلية مثل الزبدية وعويس. حدّد الصنف واللون ودرجة النضج."},
 sizes={"en": "Sized by fruit weight in grams per class, set per order.", "ar": "تُصنَّف بوزن الثمرة بالجرام لكل فئة، وتُحدد لكل طلب."},
 packing={"en": "Cartons (commonly 4–5 kg) with protective liners, palletised; heat or other treatments per destination rules.", "ar": "كراتين (غالباً 4–5 كجم) ببطانة واقية على بالتات؛ مع معالجات حرارية أو غيرها وفق متطلبات الوجهة."},
 season={"en": "≈ Jul – Oct", "ar": "≈ يوليو – أكتوبر"})

add(slug="dates", cat="fruit", img="dates", accent="#8A5A2B", form="fresh",
 name={"en": "Egyptian Dates", "ar": "البلح والتمور المصرية"},
 tag={"en": "Barhi (fresh) and other Egyptian date varieties", "ar": "بلح برحي طازج وأصناف تمور مصرية أخرى"},
 title={"en": "Egyptian Dates Export | Barhi & Fresh Dates Supplier | EL-SHIMY", "ar": "تصدير التمور المصرية | بلح برحي وتمور طازجة | الشيمي"},
 meta={"en": "Egyptian dates, including fresh Barhi, for importers and distributors. Packing and shipping coordinated by EL-SHIMY.",
       "ar": "تمور مصرية، ومنها البرحي الطازج، للمستوردين والموزعين. التعبئة والشحن بتنسيق الشيمي."},
 intro={"en": "Egyptian dates are exported both fresh (such as the golden, soft Barhi) and as semi-dry or dry varieties. Ask us which type and ripeness stage suits your market and shipping time.",
        "ar": "تُصدَّر التمور المصرية طازجة (مثل البرحي الذهبي الطري) وكذلك بأنواعها نصف الجافة والجافة. اسألنا عن النوع ودرجة النضج الأنسب لسوقك ومدة الشحن."},
 varieties={"en": "Barhi (fresh), plus Zaghloul, Samany and other Egyptian varieties as available. Confirm variety and ripeness stage.", "ar": "برحي (طازج)، إضافة إلى زغلول وسماني وأصناف مصرية أخرى حسب التوافر. أكّد الصنف ودرجة النضج."},
 sizes={"en": "Graded by size, colour and moisture; defined per variety and order.", "ar": "تُفرز بحسب الحجم واللون والرطوبة، وتُحدد لكل صنف وطلب."},
 packing=PACK_GEN, season={"en": "Barhi ≈ Jul – Sep", "ar": "البرحي ≈ يوليو – سبتمبر"})

add(slug="guava", cat="fruit", img="guava", accent="#7DB264", form="fresh",
 name={"en": "Egyptian Guava", "ar": "الجوافة المصرية"},
 tag={"en": "Fragrant guava, rich in vitamin C", "ar": "جوافة عطرية غنية بفيتامين C"},
 title={"en": "Egyptian Guava Export | Fresh Guava Supplier | EL-SHIMY", "ar": "تصدير الجوافة المصرية | مورّد جوافة طازجة | الشيمي"},
 meta={"en": "Fresh guava from Egypt for importers. Grading, packing and shipping coordinated by EL-SHIMY.", "ar": "جوافة مصرية طازجة للمستوردين. الفرز والتعبئة والشحن بتنسيق الشيمي."},
 intro={"en": "Guava is a fragrant tropical-style fruit grown in Egypt and in growing demand in export markets. EL-SHIMY coordinates sorting, packing and shipping with partner farms and packhouses, with care for the fruit's delicate skin.",
        "ar": "الجوافة فاكهة عطرية تُزرع في مصر وطلبها متزايد في أسواق التصدير. ينسق الشيمي الفرز والتعبئة والشحن مع مزارع ومحطات تعبئة شريكة مع عناية بقشرتها الرقيقة."},
 varieties={"en": "White- and pink-fleshed guava types. Specify flesh colour, firmness and ripeness stage.", "ar": "جوافة بيضاء ووردية اللب. حدّد لون اللب والتماسك ودرجة النضج."},
 sizes={"en": "Graded by weight/diameter and by external quality; defined per order.", "ar": "تُفرز بحسب الوزن/القطر والجودة الخارجية، وتُحدد لكل طلب."},
 packing={"en": "Small cartons (commonly 2–3 kg) with protective padding, palletised.", "ar": "كراتين صغيرة (غالباً 2–3 كجم) مع حشو واقٍ، على بالتات."},
 season={"en": "≈ Aug – May", "ar": "≈ أغسطس – مايو"})

add(slug="watermelon", cat="fruit", img="watermelon", accent="#3F8F4E", form="fresh",
 name={"en": "Egyptian Watermelon", "ar": "البطيخ المصري"},
 tag={"en": "Summer watermelon, bulk or packed", "ar": "بطيخ صيفي سائب أو معبأ"},
 title={"en": "Egyptian Watermelon Export | Fresh Watermelon Supplier | EL-SHIMY", "ar": "تصدير البطيخ المصري | مورّد بطيخ طازج | الشيمي"},
 meta={"en": "Watermelon from Egypt for importers and wholesalers. Sizing, packing and shipping coordinated by EL-SHIMY.", "ar": "بطيخ مصري للمستوردين وتجار الجملة. الأحجام والتعبئة والشحن بتنسيق الشيمي."},
 intro={"en": "Watermelon is a high-volume summer commodity. EL-SHIMY coordinates supply from partner farms with sizing and loading plans that suit your destination and container type.",
        "ar": "البطيخ سلعة صيفية بكميات كبيرة. ينسق الشيمي التوريد من مزارع شريكة بخطط للفرز والتحميل تناسب وجهتك ونوع الحاوية."},
 varieties={"en": "Round and oval types, seeded and seedless where available. Specify variety, flesh colour and Brix expectations.", "ar": "أنواع كروية وبيضاوية، بذور أو بدون بذور حسب التوافر. حدّد الصنف ولون اللب وتوقعات البريكس."},
 sizes={"en": "Sized by fruit weight in kilograms (for example 5–8 kg bands), set per order.", "ar": "تُصنَّف بوزن الثمرة بالكيلوجرام (مثلاً نطاقات 5–8 كجم) وتُحدد لكل طلب."},
 packing={"en": "Loose in bulk bins or packed in cartons/crates and palletised, depending on shipping mode.", "ar": "سائبة في صناديق كبيرة أو معبأة في كراتين/صناديق على بالتات بحسب وسيلة الشحن."},
 season={"en": "≈ May – Jul", "ar": "≈ مايو – يوليو"})

add(slug="pears", cat="fruit", img="pears", accent="#A9B84A", form="fresh",
 name={"en": "Egyptian Pears", "ar": "الكمثرى المصرية"},
 tag={"en": "Autumn pears for fresh markets", "ar": "كمثرى خريفية للأسواق الطازجة"},
 title={"en": "Egyptian Pears Export | Fresh Pear Supplier | EL-SHIMY", "ar": "تصدير الكمثرى المصرية | مورّد كمثرى طازجة | الشيمي"},
 meta={"en": "Pears from Egypt for importers and distributors. Variety, size and packing coordinated by EL-SHIMY.", "ar": "كمثرى مصرية للمستوردين والموزعين. الصنف والحجم والتعبئة بتنسيق الشيمي."},
 intro={"en": "Egypt's autumn pear crop supplies importers looking for regional-origin fruit during the late-summer to autumn window. EL-SHIMY coordinates grading and packing with partner farms and packhouses.",
        "ar": "يغذي محصول الكمثرى المصري الخريفي مستوردين يبحثون عن فاكهة إقليمية المنشأ في نافذة أواخر الصيف والخريف. ينسق الشيمي الفرز والتعبئة مع مزارع ومحطات تعبئة شريكة."},
 varieties={"en": "Pear varieties grown in Egypt vary by region; confirm the variety, shape and firmness stage you need.", "ar": "تختلف أصناف الكمثرى المزروعة في مصر بحسب المنطقة؛ أكّد الصنف والشكل ودرجة التماسك المطلوبة."},
 sizes={"en": "Graded by diameter or weight, defined per order.", "ar": "تُفرز بحسب القطر أو الوزن وتُحدد لكل طلب."},
 packing=PACK_GEN, season={"en": "≈ Aug – Nov", "ar": "≈ أغسطس – نوفمبر"})

add(slug="stone-fruits", cat="fruit", img="stone-fruits", accent="#E58A5B", form="fresh",
 name={"en": "Stone Fruits: Apricots, Peaches, Nectarines & Plums", "ar": "الفاكهة ذات النواة: مشمش وخوخ ونكتارين وبرقوق"},
 tag={"en": "Spring and summer stone fruit, grouped on one page", "ar": "فاكهة النواة الربيعية والصيفية في صفحة واحدة"},
 title={"en": "Egyptian Stone Fruit Export | Apricots, Peaches, Plums | EL-SHIMY", "ar": "تصدير الفاكهة ذات النواة المصرية | مشمش وخوخ وبرقوق | الشيمي"},
 meta={"en": "Egyptian apricots, peaches, nectarines and plums for importers. Packing and shipping options coordinated by EL-SHIMY.",
       "ar": "مشمش وخوخ ونكتارين وبرقوق مصري للمستوردين. التعبئة وخيارات الشحن بتنسيق الشيمي."},
 intro={"en": "Stone fruits are short-season, delicate products where timing and handling decide quality on arrival. We group apricots, peaches, nectarines and plums here because they share harvest windows, packing styles and shipping considerations. Tell us which fruit you need and EL-SHIMY will confirm what can be sourced.",
        "ar": "الفاكهة ذات النواة منتجات قصيرة الموسم وحساسة، ويحدد التوقيت والتداول جودتها عند الوصول. جمعنا المشمش والخوخ والنكتارين والبرقوق هنا لتشابه مواسم الحصاد وأنماط التعبئة واعتبارات الشحن. أخبرنا بما تحتاجه وسيؤكد الشيمي المتاح توريده."},
 varieties={"en": "Apricots, peaches (yellow and white flesh), nectarines and plums. Varieties change through the season; specify colour, firmness and sugar targets.", "ar": "مشمش وخوخ (لب أصفر وأبيض) ونكتارين وبرقوق. تتغير الأصناف خلال الموسم؛ حدّد اللون والتماسك والسكر المستهدف."},
 sizes={"en": "Graded by diameter in millimetres or count per carton; defined per fruit and order.", "ar": "تُفرز بالقطر بالمليمتر أو العدد في الكرتونة وتُحدد لكل فاكهة وطلب."},
 packing={"en": "Single- or double-layer trays in cartons, palletised and pre-cooled; air freight is often preferred for long routes.", "ar": "صواني بطبقة أو طبقتين في كراتين على بالتات ومبرّدة مسبقاً؛ وغالباً يُفضَّل الشحن الجوي للمسافات الطويلة."},
 season={"en": "≈ Apr/May – Aug (varies by fruit)", "ar": "≈ أبريل/مايو – أغسطس (بحسب الفاكهة)"})

add(slug="prickly-pear", cat="fruit", img="prickly-pear", accent="#C3417A", form="fresh",
 name={"en": "Prickly Pear (Cactus Pear)", "ar": "التين الشوكي"},
 tag={"en": "De-spined prickly pear for specialty markets", "ar": "تين شوكي منزوع الأشواك للأسواق المتخصصة"},
 title={"en": "Egyptian Prickly Pear Export | Cactus Pear Supplier | EL-SHIMY", "ar": "تصدير التين الشوكي المصري | مورّد التين الشوكي | الشيمي"},
 meta={"en": "Prickly (cactus) pear from Egypt for importers and specialty distributors. Packing and shipping coordinated by EL-SHIMY.", "ar": "تين شوكي مصري للمستوردين وموزعي الأسواق المتخصصة. التعبئة والشحن بتنسيق الشيمي."},
 intro={"en": "Prickly pear is a distinctive late-summer fruit popular in specialty and ethnic retail. Handling matters because of the skin's glochids; EL-SHIMY coordinates de-spined, carefully packed fruit through partner suppliers.",
        "ar": "التين الشوكي فاكهة مميزة في أواخر الصيف ومطلوبة في الأسواق المتخصصة. يتطلب تداولاً حذراً بسبب أشواك القشرة الدقيقة؛ وينسق الشيمي توفير ثمار منزوعة الأشواك ومعبأة بعناية عبر موردين شركاء."},
 varieties={"en": "Orange-, yellow-, red- and green-skinned types. Specify colour and ripeness.", "ar": "أنواع بقشرة برتقالية وصفراء وحمراء وخضراء. حدّد اللون ودرجة النضج."},
 sizes={"en": "Graded by weight per fruit; defined per order.", "ar": "تُفرز بوزن الثمرة وتُحدد لكل طلب."},
 packing={"en": "Cartons with padding, palletised; air or sea depending on shelf-life needs.", "ar": "كراتين بحشو واقٍ على بالتات؛ جواً أو بحراً بحسب مدة الصلاحية المطلوبة."},
 season={"en": "≈ Jul – Oct", "ar": "≈ يوليو – أكتوبر"})

add(slug="iqf-strawberries", cat="frozen", img="strawberries", accent="#C8283C", form="frozen",
 name={"en": "IQF Strawberries", "ar": "الفراولة المجمدة (IQF)"},
 tag={"en": "Individually quick-frozen strawberries for food manufacturers", "ar": "فراولة مجمدة فردياً لمصنّعي الأغذية"},
 title={"en": "IQF Strawberries from Egypt | Frozen Strawberry Supplier | EL-SHIMY", "ar": "فراولة IQF مصرية | مورّد الفراولة المجمدة | الشيمي"},
 meta={"en": "IQF frozen strawberries from Egypt for manufacturers, distributors and food service. Grades, packing and shipping coordinated by EL-SHIMY.",
       "ar": "فراولة مجمدة IQF مصرية لمصنّعي الأغذية والموزعين وقطاع الضيافة. الدرجات والتعبئة والشحن بتنسيق الشيمي."},
 intro={"en": "IQF (individually quick frozen) strawberries stay free-flowing, so buyers can take only what they need for yoghurt, dairy, bakery, beverage and dessert production. EL-SHIMY coordinates supply of frozen strawberries and shipping under frozen cold-chain conditions.",
        "ar": "الفراولة المجمدة فردياً (IQF) تبقى منفصلة الحبات، فيأخذ المشتري ما يحتاجه فقط لإنتاج الزبادي والألبان والمخبوزات والمشروبات والحلويات. ينسق الشيمي توريد الفراولة المجمدة وشحنها في سلسلة تبريد مجمدة."},
 varieties={"en": "Whole, cut or crown-cut strawberries are typical formats. Specify variety, colour, Brix, calibre and whether you need whole or sliced fruit.", "ar": "الأشكال المعتادة: ثمار كاملة أو مقطعة. حدّد الصنف واللون والبريكس والقياس وهل تحتاج ثمراً كاملاً أو شرائح."},
 sizes={"en": "Calibre bands (e.g. by diameter in millimetres) and grade (defects, broken fruit) agreed per order.", "ar": "نطاقات القياس (مثلاً بالقطر بالمليمتر) والدرجة (العيوب والثمار المكسورة) تُتفق لكل طلب."},
 packing={"en": "Poly-lined cartons or bulk bags on pallets; retail packs on request.", "ar": "كراتين ببطانة بلاستيكية أو أكياس كبيرة على بالتات؛ وعبوات تجزئة عند الطلب."},
 season={"en": "Frozen format: availability depends on production and stock", "ar": "منتج مجمد: يعتمد التوافر على الإنتاج والمخزون"},
 storage={"en": "Stored and shipped frozen at −18 °C or below in reefer containers. Cold-chain records and temperature set-points are agreed with you per shipment.",
          "ar": "تُخزَّن وتُشحن مجمدة عند −18 °م أو أقل في حاويات مبرّدة. تُتفق سجلات سلسلة التبريد ودرجات الحرارة معك لكل شحنة."})

add(slug="iqf-berries", cat="frozen", img="iqf-berries", accent="#3C4E8F", form="frozen",
 name={"en": "IQF Berries: Blueberries, Raspberries & Blackberries", "ar": "التوت المجمد IQF: توت أزرق وتوت العُليق والتوت الأسود"},
 tag={"en": "Frozen berries for manufacturing and food service", "ar": "توت مجمد للتصنيع وقطاع الضيافة"},
 title={"en": "IQF Berries from Egypt | Frozen Blueberries, Raspberries | EL-SHIMY", "ar": "توت IQF مصري | توت أزرق وعُليق مجمد | الشيمي"},
 meta={"en": "IQF frozen blueberries, raspberries and blackberries on enquiry. Specification, packing and shipping coordinated by EL-SHIMY.",
       "ar": "توت أزرق وعُليق وتوت أسود مجمد IQF عند الطلب. المواصفات والتعبئة والشحن بتنسيق الشيمي."},
 intro={"en": "Alongside IQF strawberries, EL-SHIMY can discuss frozen blueberries, raspberries and blackberries for manufacturers and distributors. Availability and origin vary by crop and season, so please send your specification and quantity and we will confirm what can be offered.",
        "ar": "إلى جانب الفراولة المجمدة، يمكن للشيمي بحث توفير التوت الأزرق والعُليق والتوت الأسود المجمد للمصنّعين والموزعين. يختلف التوافر والمنشأ بحسب المحصول والموسم، لذا أرسل مواصفاتك وكميتك لنؤكد ما يمكن عرضه."},
 varieties={"en": "Blueberries, raspberries and blackberries, whole fruit. Specify berry type, size and any organic or other claims you require.", "ar": "توت أزرق وعُليق وتوت أسود، ثمار كاملة. حدّد النوع والحجم وأي ادعاءات مثل العضوي."},
 sizes={"en": "Calibre and grade agreed per order.", "ar": "يُتفق على القياس والدرجة لكل طلب."},
 packing={"en": "Poly-lined cartons or bulk bags on pallets.", "ar": "كراتين ببطانة بلاستيكية أو أكياس كبيرة على بالتات."},
 season={"en": "Frozen format: availability on enquiry", "ar": "منتج مجمد: التوافر عند الطلب"},
 storage={"en": "Stored and shipped frozen at −18 °C or below in reefer containers.", "ar": "تُخزَّن وتُشحن مجمدة عند −18 °م أو أقل في حاويات مبرّدة."})

for p in P:
    p.setdefault("storage", STORE_GEN)
    p["docs"] = DOCS_GEN

CATS = {"veg": ("veg", "#2F6B3C"), "fruit": ("fruit", "#E8892B"), "frozen": ("frozen_cat", "#3C6E8F")}

# ───────────────────────── Static pages ─────────────────────────
# Each page: title, meta, h1, lead, sections=[(heading, [paragraphs] or html)], cta
PAGES = {}

PAGES["home"] = {
 "en": {"title": "EL-SHIMY | Egyptian Fruit & Vegetable Exporter | Fresh & IQF Frozen", "meta": "Egyptian fresh fruits, vegetables and IQF-frozen berries for international buyers. Sourcing via partner farms, quality coordination and export logistics. Est. 2016.",
        "h1": "Egyptian Products. Global Markets.",
        "lead": "We connect international food buyers with Egyptian agricultural products through reliable sourcing, quality coordination, export expertise and international shipping solutions."},
 "ar": {"title": "الشيمي | مُصدّر خضروات وفاكهة مصرية | طازج ومجمد IQF", "meta": "الشيمي للتجارة والتوكيلات تربط المشترين الدوليين بالفاكهة والخضروات المصرية الطازجة والتوت المجمد IQF عبر مزارع شريكة وتنسيق للجودة ولوجستيات التصدير. تأسست عام 2016.",
        "h1": "منتجات مصرية. أسواق عالمية.",
        "lead": "نربط مشتري الأغذية الدوليين بالمنتجات الزراعية المصرية عبر توريد موثوق وتنسيق للجودة وخبرة في التصدير وحلول للشحن الدولي."},
}

PAGES["services"] = {
 "en": {"title": "Sourcing & Export Services from Egypt | EL-SHIMY", "meta": "How EL-SHIMY sources Egyptian produce through partner farms and packhouses and coordinates export documentation, quality checks and shipment for international buyers.",
        "h1": "Sourcing & Export Services",
        "lead": "One point of contact for buying Egyptian produce: we source from partner farms and packhouses and coordinate quality, documents and shipping to your specification.",
        "sections": [
          ("How we work", ["EL-SHIMY is an Egyptian food trading and export company established in 2016. We do not own farms or packing facilities: we work with partner farms and packhouses and manage the buying process on your behalf.",
                          "That model lets us match growers and packers to each product and season, while you deal with a single trading partner for specification, pricing, documents and shipment."]),
          ("What we coordinate", ["<ul><li><strong>Product and variety sourcing</strong> – fresh fruits and vegetables, plus selected IQF-frozen strawberries and berries.</li><li><strong>Specification</strong> – variety, size, grade, packing, labelling and private-label needs.</li><li><strong>Quality coordination</strong> – inspection at packing and pre-shipment checks agreed with you.</li><li><strong>Export documentation</strong> – commercial and shipping documents, phytosanitary and origin certificates as required by the destination.</li><li><strong>Shipping</strong> – sea, air and land freight with customs clearance. See <a href=\"/en/freight-customs/\">Freight &amp; Customs</a>.</li></ul>"]),
          ("Who we work with", ["International importers, wholesalers, hotels and hospitality groups, food distributors and food manufacturers, with Gulf countries as our first priority market, followed by Asia."]),
          ("How a quote works", ["Send us your product, variety, size, packing, quantity, destination port and preferred Incoterm. We confirm availability and revert with a written offer. Prices are quoted per request because they depend on season, volume, packing and freight."]),
        ]},
 "ar": {"title": "خدمات التوريد والتصدير من مصر | الشيمي", "meta": "كيف يوفّر الشيمي المنتجات المصرية عبر مزارع ومحطات تعبئة شريكة وينسق مستندات التصدير وفحوص الجودة والشحن للمشترين الدوليين.",
        "h1": "خدمات التوريد والتصدير",
        "lead": "جهة اتصال واحدة لشراء المنتجات المصرية: نوفّر من مزارع ومحطات تعبئة شريكة وننسق الجودة والمستندات والشحن وفق مواصفاتك.",
        "sections": [
          ("طريقة عملنا", ["الشيمي شركة مصرية للتجارة والتصدير في مجال الأغذية، تأسست عام 2016. لا نمتلك مزارع أو محطات تعبئة، بل نعمل مع مزارع ومحطات تعبئة شريكة وندير عملية الشراء نيابةً عنك.",
                          "يتيح لنا هذا النموذج مطابقة المزارعين والمعبّئين لكل منتج وموسم، بينما تتعامل أنت مع شريك تجاري واحد للمواصفات والأسعار والمستندات والشحن."]),
          ("ما الذي ننسقه", ["<ul><li><strong>توريد المنتجات والأصناف</strong> – فاكهة وخضروات طازجة، إضافة إلى فراولة وتوت مجمد IQF مختار.</li><li><strong>المواصفات</strong> – الصنف والحجم والدرجة والتعبئة والملصقات والعلامة الخاصة.</li><li><strong>تنسيق الجودة</strong> – فحص عند التعبئة وفحوص قبل الشحن يُتفق عليها معك.</li><li><strong>مستندات التصدير</strong> – المستندات التجارية ومستندات الشحن وشهادات الصحة النباتية والمنشأ بحسب الوجهة.</li><li><strong>الشحن</strong> – شحن بحري وجوي وبري مع التخليص الجمركي. راجع <a href=\"/ar/freight-customs/\">الشحن والتخليص الجمركي</a>.</li></ul>"]),
          ("مع من نعمل", ["المستوردون الدوليون وتجار الجملة والفنادق ومجموعات الضيافة وموزعو الأغذية ومصنّعو الأغذية، مع أولوية لدول الخليج أولاً ثم آسيا."]),
          ("كيف يتم عرض السعر", ["أرسل لنا المنتج والصنف والحجم والتعبئة والكمية وميناء الوصول والـ Incoterm المفضل. نؤكد التوافر ونرد بعرض مكتوب. تُقدَّم الأسعار عند الطلب لأنها تعتمد على الموسم والكمية والتعبئة والشحن."]),
        ]},
}

PAGES["freight"] = {
 "en": {"title": "Freight & Customs for Egyptian Produce | EL-SHIMY", "meta": "Sea, air and land freight, customs clearance and export documentation for Egyptian fresh produce and frozen products, coordinated by EL-SHIMY.",
        "h1": "Freight & Customs",
        "lead": "Perishables need a shipping plan built around the product. We coordinate transport, clearance and paperwork so your order moves from packhouse to port or airport on schedule.",
        "sections": [
          ("Shipping modes", ["<ul><li><strong>Sea freight</strong> – temperature-controlled (reefer) containers for most fruit and vegetable programmes and frozen products, from Egyptian ports.</li><li><strong>Air freight</strong> – for highly perishable or time-critical items such as fresh strawberries, mangoes and stone fruit.</li><li><strong>Land freight</strong> – for regional destinations where road transport is practical.</li></ul>","Door-to-door delivery can be arranged where available; ask us about your destination."]),
          ("Customs clearance & documents", ["We coordinate export customs clearance in Egypt and the documents your importer needs. These commonly include the commercial invoice, packing list, bill of lading or air waybill, phytosanitary certificate and certificate of origin, plus any destination-specific requirements.","Document requirements differ by country and product, so we confirm the list with you before loading."]),
          ("Incoterms and planning", ["Tell us your preferred Incoterm (for example FOB, CFR or CIF), destination port or airport, and target arrival window. Transit times and costs depend on route and carrier, so we quote them per enquiry rather than publish fixed figures."]),
        ]},
 "ar": {"title": "الشحن والتخليص الجمركي للمنتجات المصرية | الشيمي", "meta": "شحن بحري وجوي وبري وتخليص جمركي ومستندات تصدير للمنتجات الطازجة والمجمدة المصرية بتنسيق الشيمي.",
        "h1": "الشحن والتخليص الجمركي",
        "lead": "تحتاج المنتجات سريعة التلف إلى خطة شحن مبنية حول المنتج. ننسق النقل والتخليص والأوراق ليصل طلبك من محطة التعبئة إلى الميناء أو المطار في موعده.",
        "sections": [
          ("وسائل الشحن", ["<ul><li><strong>الشحن البحري</strong> – حاويات مبرّدة لمعظم برامج الفاكهة والخضروات والمنتجات المجمدة من الموانئ المصرية.</li><li><strong>الشحن الجوي</strong> – للمنتجات شديدة القابلية للتلف أو المرتبطة بالوقت مثل الفراولة الطازجة والمانجو وفاكهة النواة.</li><li><strong>الشحن البري</strong> – للوجهات الإقليمية التي يناسبها النقل البري.</li></ul>","يمكن ترتيب التوصيل حتى الباب حيثما كان متاحاً؛ اسألنا عن وجهتك."]),
          ("التخليص الجمركي والمستندات", ["ننسق التخليص الجمركي للتصدير في مصر والمستندات التي يحتاجها المستورد. وتشمل عادةً الفاتورة التجارية وقائمة التعبئة وبوليصة الشحن البحري أو الجوي وشهادة الصحة النباتية وشهادة المنشأ، إضافة إلى متطلبات خاصة بكل وجهة.",
                                         "تختلف المتطلبات بحسب الدولة والمنتج، لذا نؤكد القائمة معك قبل التحميل."]),
          ("الـ Incoterms والتخطيط", ["أخبرنا بالـ Incoterm المفضل (مثل FOB أو CFR أو CIF) وميناء أو مطار الوصول وموعد الوصول المستهدف. تعتمد مدة الرحلة والتكلفة على المسار وشركة النقل، لذا نقدمها لكل طلب بدل نشر أرقام ثابتة."]),
        ]},
}

PAGES["quality"] = {
 "en": {"title": "Quality & Food Safety Coordination | EL-SHIMY", "meta": "How EL-SHIMY coordinates specifications, inspection, traceability documents and cold-chain planning for Egyptian produce exports.",
        "h1": "Quality & Food Safety",
        "lead": "Quality starts with a clear specification. We agree it with you, pass it to partner farms and packhouses, and coordinate checks before the shipment leaves Egypt.",
        "sections": [
          ("Our approach", ["<ol><li><strong>Written specification</strong> – variety, size, grade, packing, labelling and any importer standards.</li><li><strong>Source selection</strong> – matching your product to suitable partner farms and packhouses.</li><li><strong>Inspection</strong> – checks at packing and before loading, with photos or reports where agreed.</li><li><strong>Cold-chain planning</strong> – pre-cooling and temperature set-points matched to the product and route.</li><li><strong>Documentation</strong> – certificates and records the destination requires.</li></ol>"]),
          ("Third-party inspection and standards", ["If your programme needs an independent inspection company or specific standards (for example retailer requirements), tell us at enquiry stage so it can be built into the plan and costed."]),
          ("Certifications", ["Certification details are published here only once the documents have been verified. Please ask our team for current certificates relevant to your order."]),
        ]},
 "ar": {"title": "تنسيق الجودة وسلامة الغذاء | الشيمي", "meta": "كيف ينسق الشيمي المواصفات والفحص ومستندات التتبع وتخطيط سلسلة التبريد لصادرات المنتجات المصرية.",
        "h1": "الجودة وسلامة الغذاء",
        "lead": "تبدأ الجودة بمواصفة واضحة. نتفق عليها معك ونمررها إلى المزارع ومحطات التعبئة الشريكة وننسق الفحوص قبل مغادرة الشحنة مصر.",
        "sections": [
          ("منهجنا", ["<ol><li><strong>مواصفة مكتوبة</strong> – الصنف والحجم والدرجة والتعبئة والملصقات وأي معايير للمستورد.</li><li><strong>اختيار المصدر</strong> – مطابقة منتجك مع مزارع ومحطات تعبئة شريكة مناسبة.</li><li><strong>الفحص</strong> – فحوص عند التعبئة وقبل التحميل مع صور أو تقارير عند الاتفاق.</li><li><strong>تخطيط سلسلة التبريد</strong> – تبريد مسبق ودرجات حرارة تناسب المنتج والمسار.</li><li><strong>المستندات</strong> – الشهادات والسجلات التي تتطلبها الوجهة.</li></ol>"]),
          ("الفحص المستقل والمعايير", ["إذا احتاج برنامجك إلى شركة فحص مستقلة أو معايير محددة (مثل متطلبات سلاسل التجزئة) فأخبرنا عند الاستفسار ليُدرج ذلك في الخطة والتكلفة."]),
          ("الشهادات", ["لا تُنشر تفاصيل الشهادات هنا إلا بعد التحقق من مستنداتها. يرجى مراسلة فريقنا للحصول على الشهادات الحالية المناسبة لطلبك."]),
        ]},
}

PAGES["about"] = {
 "en": {"title": "About EL-SHIMY | Egyptian Food Trading & Export Partner", "meta": "EL-SHIMY for Trading & Agencies, established in 2016, is an Egyptian food trading, import/export and supply-chain coordination company serving international buyers.",
        "h1": "About EL-SHIMY",
        "lead": "EL-SHIMY for Trading & Agencies is an Egyptian food trading and export partner for international buyers, established in 2016.",
        "sections": [
          ("Who we are", ["We specialise in Egyptian agricultural products: fresh fruits and vegetables, with selected IQF-frozen strawberries and berries. We handle import/export trading and supply-chain coordination, working through partner farms and packhouses rather than owning production facilities."]),
          ("Mission", ["To deliver fresh, healthy products that meet agreed quality standards while strengthening the reputation of Egyptian agricultural products abroad."]),
          ("Vision", ["To be a trusted partner for buyers in the fruit and vegetable export industry, offering dependable solutions that support local farming and the wider supply chain."]),
          ("Principles", ["<ul><li>Build long-term relationships with buyers and partners.</li><li>Balance quality with competitive pricing.</li><li>Support Egyptian farmers and the local economy.</li><li>Say only what we can deliver: specifications, availability and prices are confirmed in writing.</li></ul>"]),
        ]},
 "ar": {"title": "عن الشيمي | شريك مصري في تجارة وتصدير الأغذية", "meta": "الشيمي للتجارة والتوكيلات، تأسست عام 2016، شركة مصرية لتجارة الأغذية والاستيراد والتصدير وتنسيق سلاسل الإمداد للمشترين الدوليين.",
        "h1": "عن الشيمي",
        "lead": "الشيمي للتجارة والتوكيلات شريك مصري في تجارة وتصدير الأغذية للمشترين الدوليين، تأسست عام 2016.",
        "sections": [
          ("من نحن", ["نتخصص في المنتجات الزراعية المصرية: فاكهة وخضروات طازجة، مع فراولة وتوت مجمد IQF مختار. ندير تجارة الاستيراد والتصدير وتنسيق سلاسل الإمداد، ونعمل عبر مزارع ومحطات تعبئة شريكة دون امتلاك منشآت إنتاج."]),
          ("رسالتنا", ["تقديم منتجات طازجة وصحية تلبي معايير الجودة المتفق عليها مع تعزيز سمعة المنتجات الزراعية المصرية في الخارج."]),
          ("رؤيتنا", ["أن نكون شريكاً موثوقاً للمشترين في قطاع تصدير الفاكهة والخضروات بحلول يُعتمد عليها تدعم الزراعة المحلية وسلسلة الإمداد الأوسع."]),
          ("مبادئنا", ["<ul><li>بناء علاقات طويلة الأمد مع المشترين والشركاء.</li><li>الموازنة بين الجودة والأسعار التنافسية.</li><li>دعم المزارع المصري والاقتصاد المحلي.</li><li>نقول فقط ما نستطيع الوفاء به: تُؤكَّد المواصفات والتوافر والأسعار كتابةً.</li></ul>"]),
        ]},
}

PAGES["markets"] = {
 "en": {"title": "Markets We Serve: Gulf & Asia | EL-SHIMY", "meta": "EL-SHIMY prioritises Gulf countries, followed by Asia, supplying Egyptian fruits, vegetables and IQF-frozen products to importers, wholesalers and manufacturers.",
        "h1": "Markets",
        "lead": "Our priority markets are the Gulf countries, followed by Asia. We also discuss other destinations on request.",
        "sections": [
          ("Gulf countries", ["The Gulf is our first focus. Typical programmes include citrus, onions, potatoes and grapes for wholesalers, hotels and food distributors, with air freight for the most perishable lines. Importers in the region commonly have specific labelling and documentation requirements, which we confirm before shipment."]),
          ("Asia", ["We supply importers and distributors in Asian markets, where long transit times make variety choice, maturity and cold-chain planning especially important. IQF-frozen strawberries and berries suit manufacturers who need consistent, free-flowing product."]),
          ("Other destinations", ["If your market is not listed, send us the product and destination. We will tell you whether we can support it and what the documentation and shipping route would involve."]),
        ]},
 "ar": {"title": "الأسواق التي نخدمها: الخليج وآسيا | الشيمي", "meta": "يعطي الشيمي الأولوية لدول الخليج ثم آسيا في توريد الفاكهة والخضروات المصرية والمنتجات المجمدة IQF للمستوردين وتجار الجملة والمصنّعين.",
        "h1": "الأسواق",
        "lead": "أسواقنا ذات الأولوية هي دول الخليج ثم آسيا. كما نبحث وجهات أخرى عند الطلب.",
        "sections": [
          ("دول الخليج", ["الخليج هو محور تركيزنا الأول. تشمل البرامج المعتادة الحمضيات والبصل والبطاطس والعنب لتجار الجملة والفنادق وموزعي الأغذية، مع الشحن الجوي لأكثر الأصناف قابلية للتلف. وللمستوردين في المنطقة عادةً متطلبات خاصة للملصقات والمستندات نؤكدها قبل الشحن."]),
          ("آسيا", ["نورّد للمستوردين والموزعين في الأسواق الآسيوية، حيث تجعل مدة الرحلة الطويلة اختيار الصنف ودرجة النضج وتخطيط سلسلة التبريد أمراً بالغ الأهمية. والفراولة والتوت المجمد IQF مناسبان للمصنّعين الذين يحتاجون منتجاً متجانساً منفصل الحبات."]),
          ("وجهات أخرى", ["إن لم تكن سوقك مذكورة فأرسل لنا المنتج والوجهة. سنخبرك إن كان بإمكاننا دعمها وما يتطلبه المسار من مستندات وشحن."]),
        ]},
}

GUIDE_SLUG = "produce-quote-checklist"
PAGES["insights"] = {
 "en": {"title": "Export Guides & Insights | EL-SHIMY", "meta": "Practical guides for importers buying Egyptian fruits and vegetables: what to specify, which documents to expect and how to request a quote.",
        "h1": "Insights & Export Guides", "lead": "Practical, plain-language guides for buyers sourcing Egyptian produce."},
 "ar": {"title": "أدلة ومقالات التصدير | الشيمي", "meta": "أدلة عملية للمستوردين الذين يشترون الفاكهة والخضروات المصرية: ماذا تحدد وما المستندات المتوقعة وكيف تطلب عرض سعر.",
        "h1": "مقالات وأدلة التصدير", "lead": "أدلة عملية بلغة واضحة للمشترين الذين يوردون المنتجات المصرية."},
}
PAGES["guide"] = {
 "en": {"title": "Checklist: How to Request a Produce Quote from an Egyptian Exporter", "meta": "What to include when asking an Egyptian exporter for a fruit or vegetable quote: product, size, packing, quantity, Incoterm, documents and shipping.",
        "h1": "How to Request a Produce Quote from an Egyptian Exporter",
        "lead": "A precise enquiry gets a precise offer. Use this checklist to include everything an exporter needs to quote accurately and avoid back-and-forth.",
        "sections": [
          ("1. Product and variety", ["Name the product and, if you know it, the variety (for example Navel or Valencia oranges). If you are flexible, say so: an exporter can then suggest the best option for the season."]),
          ("2. Size, grade and quality", ["State the size band (diameter in mm, count per carton or weight), quality class and tolerances for defects, colour and sugar (Brix) if relevant."]),
          ("3. Packing and labelling", ["Specify carton or bag type, net weight, pallet configuration, and whether you need private-label printing, barcodes or specific language on labels."]),
          ("4. Quantity and schedule", ["Give the volume per shipment and the delivery frequency or target dates. Container loads and air-freight consignments are planned differently."]),
          ("5. Incoterm and destination", ["Say whether you want FOB, CFR, CIF or another term, and name the destination port or airport. This decides who arranges and pays for each part of transport."]),
          ("6. Documents and import rules", ["List the documents your customs authority requires, such as the phytosanitary certificate, certificate of origin or conformity certificates, and any import permits you hold. Rules differ by country and can change, so confirm them with your authority."]),
          ("7. Payment terms", ["Mention preferred payment terms so they can be discussed early with your offer."]),
        ]},
 "ar": {"title": "قائمة تحقق: كيف تطلب عرض سعر للفاكهة والخضروات من مُصدّر مصري", "meta": "ما الذي تدرجه عند طلب عرض سعر لفاكهة أو خضروات من مُصدّر مصري: المنتج والحجم والتعبئة والكمية والـ Incoterm والمستندات والشحن.",
        "h1": "كيف تطلب عرض سعر للمنتجات الزراعية من مُصدّر مصري",
        "lead": "الاستفسار الدقيق يعطي عرضاً دقيقاً. استخدم هذه القائمة لتضمين كل ما يحتاجه المُصدّر ليسعّر بدقة ويتجنب تبادل الرسائل المتكرر.",
        "sections": [
          ("1. المنتج والصنف", ["اذكر المنتج والصنف إن عرفته (مثل برتقال أبو سرة أو فالنسيا). وإذا كنت مرناً فاذكر ذلك ليقترح المُصدّر أفضل خيار للموسم."]),
          ("2. الحجم والدرجة والجودة", ["حدّد نطاق الحجم (القطر بالمليمتر أو العدد في الكرتونة أو الوزن) ودرجة الجودة وحدود العيوب واللون والسكر (البريكس) إن لزم."]),
          ("3. التعبئة والملصقات", ["حدّد نوع الكرتون أو الجوال والوزن الصافي وتكوين البالتة، وهل تحتاج طباعة علامة خاصة أو باركود أو لغة معينة على الملصقات."]),
          ("4. الكمية والجدول", ["اذكر الكمية لكل شحنة وتكرار التوريد أو المواعيد المستهدفة. فشحنات الحاويات تُخطَّط بشكل مختلف عن الشحن الجوي."]),
          ("5. الـ Incoterm والوجهة", ["اذكر هل تريد FOB أو CFR أو CIF أو غيره، وسمِّ ميناء أو مطار الوصول. فهذا يحدد من يرتب ويتحمل كل جزء من النقل."]),
          ("6. المستندات وقواعد الاستيراد", ["اذكر المستندات التي تطلبها جهة الجمارك لديك مثل شهادة الصحة النباتية وشهادة المنشأ وشهادات المطابقة وأي تصاريح استيراد لديك. تختلف القواعد بين الدول وقد تتغير، فتأكد منها مع الجهة المختصة."]),
          ("7. شروط الدفع", ["اذكر شروط الدفع المفضلة لتُناقش مبكراً مع العرض."]),
        ]},
}

PAGES["contact"] = {
 "en": {"title": "Request a Quote | Contact EL-SHIMY", "meta": "Send your product, quantity and destination to EL-SHIMY and request a quote for Egyptian fresh produce or IQF-frozen berries.",
        "h1": "Request a Quote", "lead": "Tell us what you need. The more detail you give about product, size, packing, quantity and destination, the more accurate our offer will be."},
 "ar": {"title": "اطلب عرض سعر | تواصل مع الشيمي", "meta": "أرسل المنتج والكمية والوجهة إلى الشيمي واطلب عرض سعر للمنتجات المصرية الطازجة أو التوت المجمد IQF.",
        "h1": "اطلب عرض سعر", "lead": "أخبرنا بما تحتاجه. كلما زادت التفاصيل عن المنتج والحجم والتعبئة والكمية والوجهة كان عرضنا أدق."},
}

PAGES["products"] = {
 "en": {"title": "Egyptian Fruits, Vegetables & Frozen Products for Export | EL-SHIMY", "meta": "Browse Egyptian fresh vegetables, fruits and IQF-frozen strawberries and berries available for export through EL-SHIMY. Filter by category and request a quote.",
        "h1": "Egyptian Products for Export", "lead": "Fresh vegetables and fruits, plus selected IQF-frozen products. Open any product for specifications, packing and shipping notes, then request a quote."},
 "ar": {"title": "فاكهة وخضروات ومنتجات مجمدة مصرية للتصدير | الشيمي", "meta": "تصفح الخضروات والفاكهة المصرية الطازجة والفراولة والتوت المجمد IQF المتاحة للتصدير عبر الشيمي. صفِّ بحسب الفئة واطلب عرض سعر.",
        "h1": "منتجات مصرية للتصدير", "lead": "خضروات وفاكهة طازجة إضافة إلى منتجات مجمدة IQF مختارة. افتح أي منتج لتعرف المواصفات والتعبئة وملاحظات الشحن ثم اطلب عرض سعر."},
}

NOTFOUND = {
 "en": {"title": "Page not found | EL-SHIMY", "h1": "Page not found", "lead": "The page you are looking for does not exist or has moved.", "links": "Try one of these instead"},
 "ar": {"title": "الصفحة غير موجودة | الشيمي", "h1": "الصفحة غير موجودة", "lead": "الصفحة التي تبحث عنها غير موجودة أو تم نقلها.", "links": "جرّب أحد هذه الروابط"},
}

HOME = {
 "en": {
  "strip": ["Established 2016", "Gulf first, then Asia", "Fresh produce & IQF-frozen berries", "Sourced via partner farms & packhouses"],
  "cats_h": "What we supply", "cats_lead": "Egyptian fruits and vegetables are our core business. Selected frozen products complete the range.",
  "feat_h": "Featured products",
  "how_h": "How an order works",
  "how": [("Specify", "Send product, size, packing, quantity and destination."), ("Source & check", "We match partner farms and packhouses and agree quality checks."), ("Pack & document", "Packing, labelling and export documents prepared to your requirements."), ("Ship & deliver", "Sea, air or land freight with customs clearance; door-to-door where available.")],
  "svc_h": "Beyond the product", "svc_lead": "Sourcing, quality coordination and logistics from one trading partner.",
  "svc": [("services", "Sourcing & Export", "Product sourcing, specification and export coordination."), ("freight", "Freight & Customs", "Sea, air and land freight with clearance and documents."), ("quality", "Quality & Food Safety", "Specifications, inspections and cold-chain planning.")],
  "cta_h": "Ready to discuss your next order?", "cta_p": "Send your product, quantity and destination and we will come back with a specification-based offer.",
  "model": "We source through partner farms and packhouses.",
 },
 "ar": {
  "strip": ["تأسست عام 2016", "الخليج أولاً ثم آسيا", "منتجات طازجة وتوت مجمد IQF", "توريد عبر مزارع ومحطات تعبئة شريكة"],
  "cats_h": "ما نورّده", "cats_lead": "الفاكهة والخضروات المصرية هي نشاطنا الأساسي، وتكمل المنتجات المجمدة المختارة المجموعة.",
  "feat_h": "منتجات مميزة",
  "how_h": "كيف يتم الطلب",
  "how": [("حدّد", "أرسل المنتج والحجم والتعبئة والكمية والوجهة."), ("وفّر وافحص", "نطابق المزارع ومحطات التعبئة الشريكة ونتفق على فحوص الجودة."), ("عبّئ ووثّق", "تجهيز التعبئة والملصقات ومستندات التصدير وفق متطلباتك."), ("اشحن وسلّم", "شحن بحري أو جوي أو بري مع التخليص الجمركي؛ وحتى الباب حيثما أمكن.")],
  "svc_h": "أكثر من المنتج", "svc_lead": "التوريد وتنسيق الجودة واللوجستيات من شريك تجاري واحد.",
  "svc": [("services", "التوريد والتصدير", "توريد المنتجات والمواصفات وتنسيق التصدير."), ("freight", "الشحن والتخليص الجمركي", "شحن بحري وجوي وبري مع التخليص والمستندات."), ("quality", "الجودة وسلامة الغذاء", "المواصفات والفحوص وتخطيط سلسلة التبريد.")],
  "cta_h": "هل أنت مستعد لمناقشة طلبك القادم؟", "cta_p": "أرسل المنتج والكمية والوجهة وسنعود إليك بعرض مبني على المواصفات.",
  "model": "نوفّر عبر مزارع ومحطات تعبئة شريكة.",
 },
}

FORM = {
 "en": {"name": "Full name", "company": "Company", "email": "Work email", "phone": "Phone / WhatsApp (optional)", "country": "Destination country",
        "product": "Product of interest", "choose": "Choose a product", "other": "Other / multiple products",
        "qty": "Estimated quantity (optional)", "msg": "Specification & message", "msg_ph": "Variety, size, packing, Incoterm, destination port, timing…",
        "send": "Send enquiry", "required": "required", "privacy": "We use your details only to respond to your enquiry.",
        "e_required": "Please fill in this field.", "e_email": "Please enter a valid email address.",
        "summary": "Please correct the highlighted fields:", "sending": "Sending…",
        "ok_endpoint": "Thank you. Your enquiry has been sent and our team will reply by email.",
        "ok_mailto": "Your email app should now open with your enquiry pre-filled. If it did not, please email us at",
        "fail": "Sorry, we could not send your enquiry. Please email us directly at",
        "direct": "Prefer to write directly?", "address": "Office"},
 "ar": {"name": "الاسم الكامل", "company": "الشركة", "email": "البريد الإلكتروني للعمل", "phone": "الهاتف / واتساب (اختياري)", "country": "دولة الوجهة",
        "product": "المنتج المطلوب", "choose": "اختر منتجاً", "other": "أخرى / عدة منتجات",
        "qty": "الكمية التقديرية (اختياري)", "msg": "المواصفات والرسالة", "msg_ph": "الصنف، الحجم، التعبئة، الـ Incoterm، ميناء الوصول، التوقيت…",
        "send": "إرسال الاستفسار", "required": "مطلوب", "privacy": "نستخدم بياناتك فقط للرد على استفسارك.",
        "e_required": "يرجى تعبئة هذا الحقل.", "e_email": "يرجى إدخال بريد إلكتروني صحيح.",
        "summary": "يرجى تصحيح الحقول المحددة:", "sending": "جارٍ الإرسال…",
        "ok_endpoint": "شكراً لك. تم إرسال استفسارك وسيرد فريقنا عبر البريد الإلكتروني.",
        "ok_mailto": "يجب أن يفتح تطبيق البريد الآن برسالة معبأة مسبقاً. إن لم يحدث ذلك فراسلنا على",
        "fail": "عذراً، تعذر إرسال استفسارك. يرجى مراسلتنا مباشرة على",
        "direct": "تفضّل المراسلة المباشرة؟", "address": "المكتب"},
}

CREDITS = {
 "en": {"title": "Photo Credits | EL-SHIMY", "meta": "Credits and licences for the photographs used on the EL-SHIMY website.", "h1": "Photo credits",
        "lead": "Product photographs are illustrative and come from Wikimedia Commons under the licences shown. They are not photographs of EL-SHIMY shipments.",
        "cols": ["Image", "Photographer", "Licence", "Source"], "unsplash": "Strawberries, oranges, mandarins, mangoes, watermelon and grapes: illustrative stock photographs from Unsplash, used under the Unsplash Licence.", "view": "File page"},
 "ar": {"title": "حقوق الصور | الشيمي", "meta": "بيانات المصور والترخيص للصور المستخدمة في موقع الشيمي.", "h1": "حقوق الصور",
        "lead": "صور المنتجات توضيحية ومأخوذة من ويكيميديا كومنز بموجب التراخيص الموضحة. وهي ليست صوراً لشحنات الشيمي.",
        "cols": ["الصورة", "المصوّر", "الترخيص", "المصدر"], "unsplash": "الفراولة والبرتقال واليوسفي والمانجو والبطيخ والعنب: صور توضيحية من Unsplash مستخدمة بموجب ترخيص Unsplash.", "view": "صفحة الملف"},
}
