# -*- coding: utf-8 -*-
"""Designed (non-article) page builders: home, services, freight, quality, about, markets, insights, guide.
Copy for these pages lives here (EN + AR). Shared helpers come from build.py via init()."""
import json
from icons import icon
import content as C

B = None
def init(mod):
    global B
    B = mod

# ───────────────────────── shared components ─────────────────────────
def arrow(): return icon("arrow", "arr")

def hero_lite(lang, crumbs_html, h1, lead, ctas="", media="", eyebrow="", cls=""):
    return f'''<section class="hero hero-lite {cls}"><div class="wrap hero-grid">
<div class="hero-copy">{crumbs_html}{f'<p class="eyebrow rise">{eyebrow}</p>' if eyebrow else ""}<h1 class="rise">{h1}</h1><p class="lead rise">{lead}</p>{f'<div class="hero-actions rise">{ctas}</div>' if ctas else ""}</div>
{f'<div class="hero-media rise">{media}</div>' if media else ""}</div></section>'''

def btn(href, label, kind="accent", extra=""):
    return f'<a class="btn btn-{kind}" href="{href}"{extra}>{label}</a>'

def timeline(steps, cls=""):
    lis = "".join(f'<li><span class="tl-ic">{icon(ic)}<b class="tl-n">{i + 1}</b></span><h3>{t}</h3><p>{d}</p></li>' for i, (ic, t, d) in enumerate(steps))
    return f'<ol class="tl reveal {cls}"><span class="tl-line" aria-hidden="true"></span>{lis}</ol>'

def sec_head(h, p="", cls=""):
    return f'<div class="sec-head reveal {cls}"><h2>{h}</h2>{f"<p>{p}</p>" if p else ""}</div>'

def cta_big(lang, h, p, label, href, art=None):
    ui = C.UI[lang]
    wa = f'<a class="btn btn-ghost-light" href="{B.wa_link(lang)}" target="_blank" rel="noopener">{ui["whatsapp"]}</a>' if C.WHATSAPP else ""
    img = f'<img class="cta-art" src="/assets/img/{art}" alt="" width="600" height="340" loading="lazy">' if art else ""
    return f'''<section class="cta-big"><div class="wrap cta-big-in reveal"><div><h2>{h}</h2><p>{p}</p><div class="hero-actions">{btn(href, label)}{wa}</div></div>{img}</div></section>'''

def check_list(items, cls=""):
    return f'<ul class="ticks {cls}">' + "".join(f"<li>{icon('check')}<span>{x}</span></li>" for x in items) + "</ul>"

def contact_href(lang, topic): return B.url("contact", lang) + f"?topic={topic}"

def page_trail(lang, label):
    return B.crumbs(lang, [(label, None)])

# ───────────────────────── copy ─────────────────────────
V = {"en": {}, "ar": {}}

# ---- Freight ----
V["en"]["freight"] = {
 "eyebrow": "Freight & Customs", "h1": "From Packhouse to Destination.",
 "lead": "Perishables need a shipping plan built around the product. We coordinate transport, customs arrangements and paperwork around your product and destination.",
 "cta": "Request a Shipping Quote", "cta2": "Explore shipping modes",
 "chips": ["Sea", "Air", "Land", "Customs documents"],
 "modes_h": "Choose the mode that fits the product", "modes_p": "Each mode suits different products, volumes and timings. We help you choose, then plan packing and documents around it.",
 "modes": [
  {"k": "sea", "icon": "ship", "art": "ill-reefer.svg", "t": "Sea Freight", "d": "Temperature-controlled (reefer) containers for suitable fruit, vegetable and frozen programmes, shipped from Egyptian ports where available.",
   "li": ["Reefer containers for chilled or frozen cargo, as suits the product", "Pallet loading planned with your packing specification", "Set-points and ventilation agreed per commodity"], "a": "Ask about sea freight"},
  {"k": "air", "icon": "plane", "art": "ill-plane.svg", "t": "Air Freight", "d": "Air transport for suitable time-sensitive, perishable shipments such as fresh strawberries, mangoes or stone fruit.",
   "li": ["Suited to highly perishable or urgent lines", "Packing and pre-cooling planned for air handling", "Routing and cut-offs depend on airline and airport"], "a": "Ask about air freight"},
  {"k": "land", "icon": "truck", "art": "ill-truck.svg", "t": "Land Freight", "d": "Regional overland transport where road routes are practical for the destination.",
   "li": ["Refrigerated or ventilated trucks, as the product requires", "Useful for neighbouring and regional destinations", "Border and permit requirements confirmed per route"], "a": "Ask about land freight"},
 ],
 "modes_note": "Door-to-door delivery can be arranged where available. Transit times, costs and availability are quoted per enquiry; we do not publish fixed figures.",
 "docs_h": "Customs clearance & documents", "docs_p": "We coordinate export clearance in Egypt and the paperwork your importer needs. The exact set depends on the product and the destination, and not every document applies to every shipment.",
 "docs": [("doc", "Commercial invoice", "Describes the goods and the agreed value for customs.", "Commonly requested"),
          ("list", "Packing list", "Itemises cartons, weights and pallets in the shipment.", "Commonly requested"),
          ("stamp", "Certificate of origin", "Confirms Egyptian origin where the contract or destination requires it.", "If required"),
          ("leaf", "Phytosanitary certificate", "Plant-health document for fresh produce, where the importing country requires it.", "If applicable"),
          ("ship", "Bill of lading / air waybill", "The transport document issued by the carrier for the shipment.", "Per shipment"),
          ("globe", "Destination-specific documents", "Extra certificates, permits or labels your importing authority asks for.", "Destination-specific")],
 "docs_note": "We confirm the document list with you before loading. Please also check requirements with your customs authority, as rules differ by country and can change.",
 "proc_h": "How an export shipment moves", "proc_p": "A clear sequence from first enquiry to delivery, with the documents prepared alongside.",
 "proc": [("send", "Share requirements", "Share your product and destination requirements."),
          ("clipboard", "Confirm specs & sourcing", "Confirm specifications and sourcing."),
          ("box", "Plan packing & documents", "Plan packing, shipping and required documentation."),
          ("stamp", "Dispatch & customs", "Coordinate dispatch and customs arrangements."),
          ("pin", "Track & deliver", "Track the shipment and coordinate delivery, where included in the agreed service.")],
 "inco_h": "Incoterms & planning", "inco_p": "The Incoterm you agree decides who arranges and pays for each stage of the journey. Tell us which one you use, or ask us to suggest one for your route.",
 "inco_cols": ["Export clearance", "Loading at origin", "Main carriage", "Insurance", "Delivery to destination", "Import clearance & duties"],
 "inco_rows": [("EXW", "Ex Works", "BBB-BB"), ("FOB", "Free On Board", "SSB-BB"), ("CIF", "Cost, Insurance & Freight", "SSSSBB"), ("DAP", "Delivered at Place", "SSS-SB")],
 "seller": "Seller", "buyer": "Buyer", "na": "Not required", "legend": "Who is responsible",
 "inco_note": "Illustrative summary of Incoterms® 2020. Actual obligations, risk transfer and costs depend on the term, the named place and your sales contract. FOB and CIF apply to sea freight; FCA and CIP are the usual alternatives for air and containerised transport. Always confirm in the contract.",
 "inco_plan_h": "To plan your shipment, tell us:", "inco_plan": ["Preferred Incoterm", "Destination port or airport", "Target arrival window", "Volume and packing"],
 "cta_h": "Planning a shipment?", "cta_p": "Share your product, volume, destination and preferred Incoterm. We will come back with a shipping plan and quote.",
 "title": "Freight & Customs for Egyptian Produce | EL-SHIMY", "meta": "Sea, air and land freight, customs arrangements and export documents for Egyptian fresh produce and frozen products, coordinated by EL-SHIMY.",
 "img_alt": "Illustration of a container ship, port crane and cargo aircraft",
}
V["ar"]["freight"] = {
 "eyebrow": "الشحن والتخليص الجمركي", "h1": "من محطة التعبئة إلى الوجهة.",
 "lead": "تحتاج المنتجات سريعة التلف إلى خطة شحن مبنية حول المنتج. ننسق النقل والترتيبات الجمركية والأوراق بحسب منتجك ووجهتك.",
 "cta": "اطلب عرض سعر للشحن", "cta2": "استكشف وسائل الشحن",
 "chips": ["بحري", "جوي", "بري", "مستندات جمركية"],
 "modes_h": "اختر الوسيلة المناسبة للمنتج", "modes_p": "تناسب كل وسيلة منتجات وكميات وتوقيتات مختلفة. نساعدك على الاختيار ثم نخطط التعبئة والمستندات حولها.",
 "modes": [
  {"k": "sea", "icon": "ship", "art": "ill-reefer.svg", "t": "الشحن البحري", "d": "حاويات مبرّدة (ريفر) لبرامج الفاكهة والخضروات والمنتجات المجمدة المناسبة، تُشحن من الموانئ المصرية حيثما أمكن.",
   "li": ["حاويات مبرّدة للبضائع المبردة أو المجمدة بحسب المنتج", "تخطيط تحميل البالتات وفق مواصفات التعبئة", "يُتفق على درجات الحرارة والتهوية لكل منتج"], "a": "اسأل عن الشحن البحري"},
  {"k": "air", "icon": "plane", "art": "ill-plane.svg", "t": "الشحن الجوي", "d": "نقل جوي للشحنات سريعة التلف والحساسة للوقت مثل الفراولة الطازجة والمانجو وفاكهة النواة.",
   "li": ["مناسب للأصناف شديدة القابلية للتلف أو العاجلة", "تخطيط التعبئة والتبريد المسبق للتداول الجوي", "المسارات ومواعيد القبول تعتمد على الناقل والمطار"], "a": "اسأل عن الشحن الجوي"},
  {"k": "land", "icon": "truck", "art": "ill-truck.svg", "t": "الشحن البري", "d": "نقل بري إقليمي حيثما كانت الطرق عملية للوجهة.",
   "li": ["شاحنات مبرّدة أو مهواة بحسب حاجة المنتج", "مفيد للوجهات المجاورة والإقليمية", "تُؤكَّد متطلبات الحدود والتصاريح لكل مسار"], "a": "اسأل عن الشحن البري"},
 ],
 "modes_note": "يمكن ترتيب التوصيل حتى الباب حيثما كان متاحاً. تُقدَّم مدد النقل والتكاليف والتوافر لكل استفسار، ولا ننشر أرقاماً ثابتة.",
 "docs_h": "التخليص الجمركي والمستندات", "docs_p": "ننسق التخليص الجمركي للتصدير في مصر والأوراق التي يحتاجها المستورد. تعتمد المجموعة المطلوبة على المنتج والوجهة، وليست كل المستندات مطلوبة في كل شحنة.",
 "docs": [("doc", "الفاتورة التجارية", "تصف البضاعة وقيمتها المتفق عليها لأغراض الجمارك.", "مطلوبة عادةً"),
          ("list", "قائمة التعبئة", "تفصّل الكراتين والأوزان والبالتات في الشحنة.", "مطلوبة عادةً"),
          ("stamp", "شهادة المنشأ", "تؤكد المنشأ المصري عندما يتطلب العقد أو الوجهة ذلك.", "عند الطلب"),
          ("leaf", "شهادة الصحة النباتية", "وثيقة صحة نباتية للمنتجات الطازجة عندما تشترطها الدولة المستوردة.", "عند الاقتضاء"),
          ("ship", "بوليصة الشحن البحري / الجوي", "وثيقة النقل التي يصدرها الناقل للشحنة.", "لكل شحنة"),
          ("globe", "مستندات خاصة بالوجهة", "شهادات أو تصاريح أو ملصقات إضافية تطلبها جهة الاستيراد.", "بحسب الوجهة")],
 "docs_note": "نؤكد قائمة المستندات معك قبل التحميل. يرجى أيضاً مراجعة متطلبات الجهة الجمركية لديك، فالقواعد تختلف بين الدول وقد تتغير.",
 "proc_h": "كيف تتحرك شحنة التصدير", "proc_p": "تسلسل واضح من الاستفسار الأول حتى التسليم، مع تجهيز المستندات بالتوازي.",
 "proc": [("send", "شارك المتطلبات", "شارك متطلبات المنتج والوجهة."),
          ("clipboard", "أكّد المواصفات والتوريد", "تأكيد المواصفات والتوريد."),
          ("box", "خطط التعبئة والمستندات", "تخطيط التعبئة والشحن والمستندات المطلوبة."),
          ("stamp", "الإرسال والجمارك", "تنسيق الإرسال والترتيبات الجمركية."),
          ("pin", "تتبّع وسلّم", "تتبع الشحنة وتنسيق التسليم حيثما كان ضمن الخدمة المتفق عليها.")],
 "inco_h": "الـ Incoterms والتخطيط", "inco_p": "يحدد الـ Incoterm المتفق عليه من يرتب ويتحمل كل مرحلة من الرحلة. أخبرنا بما تستخدمه أو اطلب منا اقتراح الأنسب لمسارك.",
 "inco_cols": ["التخليص للتصدير", "التحميل في بلد المنشأ", "النقل الرئيسي", "التأمين", "التسليم للوجهة", "التخليص للاستيراد والرسوم"],
 "inco_rows": [("EXW", "تسليم أرض المصنع", "BBB-BB"), ("FOB", "التسليم على ظهر السفينة", "SSB-BB"), ("CIF", "التكلفة والتأمين والشحن", "SSSSBB"), ("DAP", "التسليم في مكان محدد", "SSS-SB")],
 "seller": "البائع", "buyer": "المشتري", "na": "غير مطلوب", "legend": "من المسؤول",
 "inco_note": "ملخص توضيحي لقواعد Incoterms® 2020. تعتمد الالتزامات الفعلية ونقل المخاطر والتكاليف على الشرط والمكان المحدد وعقد البيع. ينطبق FOB وCIF على الشحن البحري، أما FCA وCIP فبديلان شائعان للشحن الجوي وبالحاويات. أكّد ذلك دائماً في العقد.",
 "inco_plan_h": "لتخطيط شحنتك أخبرنا بـ:", "inco_plan": ["الـ Incoterm المفضل", "ميناء أو مطار الوصول", "موعد الوصول المستهدف", "الكمية والتعبئة"],
 "cta_h": "تخطط لشحنة؟", "cta_p": "شارك المنتج والكمية والوجهة والـ Incoterm المفضل. سنعود إليك بخطة شحن وعرض سعر.",
 "title": "الشحن والتخليص الجمركي للمنتجات المصرية | الشيمي", "meta": "شحن بحري وجوي وبري وترتيبات جمركية ومستندات تصدير للمنتجات المصرية الطازجة والمجمدة بتنسيق الشيمي.",
 "img_alt": "رسم توضيحي لسفينة حاويات ورافعة ميناء وطائرة شحن",
}

# ---- Quality ----
V["en"]["quality"] = {
 "eyebrow": "Quality & Food Safety", "h1": "Quality Starts with Clear Specifications.",
 "lead": "We agree the specification with you, pass it to partner farms and packhouses, and coordinate the checks and documents agreed for your order before it ships.",
 "cta": "See the quality process", "cta2": "Discuss Your Quality Requirements",
 "scope": [("users", "Partner-based sourcing"), ("clipboard", "Checks agreed per order"), ("doc", "Specifications confirmed in writing")],
 "proc_h": "Our quality process", "proc_p": "Five steps from the buyer's requirements to a documented shipment.",
 "steps": [("clipboard", "Define Specifications", "Agree variety, size, grade, packaging, labelling and buyer requirements in writing."),
           ("users", "Select Suppliers", "Coordinate with suitable partner farms and packhouses for your product and season."),
           ("search", "Inspect and Verify", "Coordinate the checks and records agreed for your order, at packing and before loading."),
           ("thermo", "Plan Handling and Transport", "Coordinate pre-cooling and cold-chain requirements when they apply to the product and route."),
           ("doc", "Prepare Documentation", "Confirm the required documents and destination-specific requirements before shipment.")],
 "trace_h": "Specifications, records and shipment documents, in one place",
 "trace_p": "Buyer confidence comes from clear information. For each order we can organise the following, as agreed:",
 "trace": [("tag", "Written product specification", "Variety, size, grade, packing and labelling."), ("users", "Supplier information", "Which partner farm and packhouse supplies the order."),
           ("camera", "Inspection records", "Check results or photos, where agreed for the order."), ("doc", "Shipment documents", "Invoice, packing list and certificates as required.")],
 "trace_note": "What you receive depends on the order and what we agree with you in advance.",
 "sheet_t": "Product Specification", "sheet_ribbon": "Illustrative example, not a real record",
 "sheet": [("Product", "Navel oranges (example)"), ("Origin", "Egypt"), ("Size", "Count 56–72 (example)"), ("Grade", "Class I (example)"),
           ("Packing", "15 kg carton, palletised (example)"), ("Labelling", "Buyer brand and country of origin"), ("Checks agreed", "Size, colour and defect check at packing; pre-shipment check"),
           ("Cold chain", "Reefer container, set-point agreed"), ("Documents", "Invoice, packing list, certificates if required")],
 "trace_img_alt": "Fresh produce ready for packing (illustrative stock photo)",
 "cert_h": "Certifications", "cert_p": "Certificates are shown only when their documents have been verified.",
 "iso_t": "ISO 22000", "iso_s": "Food safety management", "iso_p": "Certificate documentation is available for confirmation on request. Please ask our team for the current certificate details relevant to your order.", "iso_btn": "Request certificate details",
 "ext_t": "Third-party inspection & additional standards", "ext_p": "If your programme needs an independent inspection company, retailer requirements or other standards, tell us at enquiry stage so it can be built into the plan and costed. We discuss additional standards only where they can be evidenced.",
 "honest_t": "What this means in practice",
 "honest": ["We coordinate with partner farms and packhouses; we do not operate our own farms or packhouses.", "We do not operate our own laboratory.", "We do not guarantee zero defects. Tolerances are agreed in the specification for each order."],
 "cta_h": "Discuss Your Quality Requirements", "cta_p": "Tell us the product, specification and any standards or inspections you need. We will confirm what can be arranged.",
 "title": "Quality & Food Safety Coordination | EL-SHIMY", "meta": "How EL-SHIMY coordinates specifications, inspection, traceability documents and cold-chain planning for Egyptian produce exports.",
 "hero_alt": "Egyptian oranges with leaves (illustrative stock photo)",
}
V["ar"]["quality"] = {
 "eyebrow": "الجودة وسلامة الغذاء", "h1": "الجودة تبدأ بمواصفات واضحة.",
 "lead": "نتفق معك على المواصفة، ونمررها إلى المزارع ومحطات التعبئة الشريكة، وننسق الفحوص والمستندات المتفق عليها لطلبك قبل الشحن.",
 "cta": "اطّلع على عملية الجودة", "cta2": "ناقش متطلبات الجودة لديك",
 "scope": [("users", "توريد عبر شركاء"), ("clipboard", "فحوص يُتفق عليها لكل طلب"), ("doc", "مواصفات مؤكدة كتابةً")],
 "proc_h": "عملية الجودة لدينا", "proc_p": "خمس خطوات من متطلبات المشتري إلى شحنة موثّقة.",
 "steps": [("clipboard", "تحديد المواصفات", "نتفق كتابةً على الصنف والحجم والدرجة والتعبئة والملصقات ومتطلبات المشتري."),
           ("users", "اختيار الموردين", "ننسق مع مزارع ومحطات تعبئة شريكة مناسبة لمنتجك وموسمه."),
           ("search", "الفحص والتحقق", "ننسق الفحوص والسجلات المتفق عليها لطلبك، عند التعبئة وقبل التحميل."),
           ("thermo", "تخطيط التداول والنقل", "ننسق التبريد المسبق ومتطلبات سلسلة التبريد عندما تنطبق على المنتج والمسار."),
           ("doc", "تجهيز المستندات", "نؤكد المستندات المطلوبة ومتطلبات الوجهة قبل الشحن.")],
 "trace_h": "المواصفات والسجلات ومستندات الشحن في مكان واحد",
 "trace_p": "تأتي ثقة المشتري من وضوح المعلومات. لكل طلب يمكننا تنظيم ما يلي بحسب الاتفاق:",
 "trace": [("tag", "مواصفة مكتوبة للمنتج", "الصنف والحجم والدرجة والتعبئة والملصقات."), ("users", "معلومات المورّد", "المزرعة ومحطة التعبئة الشريكة التي تورّد الطلب."),
           ("camera", "سجلات الفحص", "نتائج الفحص أو الصور عند الاتفاق عليها للطلب."), ("doc", "مستندات الشحن", "الفاتورة وقائمة التعبئة والشهادات بحسب المطلوب.")],
 "trace_note": "ما تحصل عليه يعتمد على الطلب وعلى ما نتفق عليه معك مسبقاً.",
 "sheet_t": "مواصفة المنتج", "sheet_ribbon": "مثال توضيحي وليس سجلاً حقيقياً",
 "sheet": [("المنتج", "برتقال أبو سرة (مثال)"), ("المنشأ", "مصر"), ("الحجم", "عدد 56–72 (مثال)"), ("الدرجة", "الدرجة الأولى (مثال)"),
           ("التعبئة", "كرتونة 15 كجم على بالتات (مثال)"), ("الملصقات", "علامة المشتري وبلد المنشأ"), ("الفحوص المتفق عليها", "فحص الحجم واللون والعيوب عند التعبئة؛ وفحص قبل الشحن"),
           ("سلسلة التبريد", "حاوية مبرّدة بدرجة حرارة متفق عليها"), ("المستندات", "الفاتورة وقائمة التعبئة والشهادات إن لزم")],
 "trace_img_alt": "منتجات طازجة جاهزة للتعبئة (صورة توضيحية)",
 "cert_h": "الشهادات", "cert_p": "لا تُعرض الشهادات إلا بعد التحقق من مستنداتها.",
 "iso_t": "ISO 22000", "iso_s": "نظام إدارة سلامة الغذاء", "iso_p": "مستندات الشهادة متاحة للتأكد منها عند الطلب. يرجى مراسلة فريقنا للحصول على تفاصيل الشهادة الحالية المرتبطة بطلبك.", "iso_btn": "اطلب تفاصيل الشهادة",
 "ext_t": "الفحص المستقل والمعايير الإضافية", "ext_p": "إذا احتاج برنامجك إلى شركة فحص مستقلة أو متطلبات سلاسل التجزئة أو معايير أخرى فأخبرنا عند الاستفسار ليُدرج ذلك في الخطة والتكلفة. نناقش المعايير الإضافية فقط حيثما أمكن إثباتها.",
 "honest_t": "ماذا يعني ذلك عملياً",
 "honest": ["ننسق مع مزارع ومحطات تعبئة شريكة، ولا نملك مزارع أو محطات تعبئة خاصة بنا.", "لا نشغّل مختبراً خاصاً بنا.", "لا نضمن خلوّ الشحنة من العيوب تماماً؛ تُتفق حدود التفاوت في المواصفة لكل طلب."],
 "cta_h": "ناقش متطلبات الجودة لديك", "cta_p": "أخبرنا بالمنتج والمواصفة وأي معايير أو فحوص تحتاجها، وسنؤكد ما يمكن ترتيبه.",
 "title": "تنسيق الجودة وسلامة الغذاء | الشيمي", "meta": "كيف ينسق الشيمي المواصفات والفحص ومستندات التتبع وتخطيط سلسلة التبريد لصادرات المنتجات المصرية.",
 "hero_alt": "برتقال مصري بأوراقه (صورة توضيحية)",
}

# ---- Home ----
V["en"]["home"] = {
 "why_h": "Why buyers work with EL‑SHIMY", "why_p": "A trading partner built around clear specifications and one point of contact.",
 "why": [("clipboard", "Specification first", "Variety, size, grade and packing agreed in writing before sourcing."), ("users", "Partner-farm sourcing", "We match growers and packhouses to each product and season."),
         ("globe", "Gulf first, then Asia", "Our priority markets, with documentation planned for each destination."), ("snow", "Fresh and frozen range", "Egyptian fruit and vegetables, plus selected IQF strawberries and berries."),
         ("mail", "English and Arabic", "Enquiries and documents handled in both languages.")],
 "freight_h": "Shipping planned around the product", "freight_p": "Sea, air and land freight with customs arrangements and export documents coordinated by one team.", "freight_a": "Explore freight & customs",
 "markets_h": "Our priority markets", "mk": [("Gulf countries", "First focus"), ("Asia", "Second focus")], "markets_a": "See markets",
 "cat_sub": {"veg": "Potatoes, onions, tomatoes", "fruit": "Citrus, grapes, mangoes, strawberries and more", "frozen": "IQF strawberries and berries"},
}
V["ar"]["home"] = {
 "why_h": "لماذا يتعامل المشترون مع الشيمي", "why_p": "شريك تجاري قائم على مواصفات واضحة وجهة اتصال واحدة.",
 "why": [("clipboard", "المواصفات أولاً", "يُتفق كتابةً على الصنف والحجم والدرجة والتعبئة قبل التوريد."), ("users", "توريد عبر مزارع شريكة", "نطابق المزارعين ومحطات التعبئة مع كل منتج وموسم."),
         ("globe", "الخليج أولاً ثم آسيا", "أسواقنا ذات الأولوية، مع تخطيط المستندات لكل وجهة."), ("snow", "منتجات طازجة ومجمدة", "فاكهة وخضروات مصرية، إضافة إلى فراولة وتوت مجمد IQF مختار."),
         ("mail", "العربية والإنجليزية", "نتعامل مع الاستفسارات والمستندات بكلتا اللغتين.")],
 "freight_h": "شحن مخطط حول المنتج", "freight_p": "شحن بحري وجوي وبري مع ترتيبات جمركية ومستندات تصدير ينسقها فريق واحد.", "freight_a": "استكشف الشحن والتخليص",
 "markets_h": "أسواقنا ذات الأولوية", "mk": [("دول الخليج", "التركيز الأول"), ("آسيا", "التركيز الثاني")], "markets_a": "اطّلع على الأسواق",
 "cat_sub": {"veg": "بطاطس وبصل وطماطم", "fruit": "حمضيات وعنب ومانجو وفراولة وغيرها", "frozen": "فراولة وتوت مجمد IQF"},
}

# ---- Services ----
V["en"]["services"] = {
 "eyebrow": "Sourcing & Export", "h1": "Sourcing & Export Services",
 "lead": "One point of contact for buying Egyptian produce. We source from partner farms and packhouses and coordinate quality, documents and shipping to your specification.",
 "model_h": "A partner-based model", "model_p": "EL-SHIMY was established in 2016. We do not own farms or packing facilities: we work with partner farms and packhouses and manage the buying process on your behalf, so you deal with a single trading partner.",
 "what_h": "What we coordinate", "what": [("leaf", "Product & variety sourcing", "Fresh fruits and vegetables, plus selected IQF-frozen strawberries and berries."), ("clipboard", "Specification", "Variety, size, grade, packing, labelling and private-label needs."),
          ("search", "Quality coordination", "Inspection at packing and pre-shipment checks agreed with you."), ("doc", "Export documentation", "Commercial and shipping documents, phytosanitary and origin certificates as required."),
          ("ship", "Shipping", "Sea, air and land freight with customs arrangements.")],
 "who_h": "Who we work with", "who": ["Importers", "Wholesalers", "Hotels & hospitality", "Food distributors", "Food manufacturers"], "who_p": "Gulf countries are our first priority, followed by Asia.",
 "proc_h": "How a quote works", "proc_p": "Prices are quoted per request because they depend on season, volume, packing and freight.",
 "proc": [("send", "Send your enquiry", "Product, variety, size, packing, quantity, destination port and Incoterm."), ("search", "We confirm availability", "Matching partner farms and packhouses to your specification."),
          ("doc", "Receive a written offer", "Specification, packing, terms and price in one document."), ("ship", "Plan the shipment", "Packing, freight and documents coordinated to your schedule.")],
 "cta_h": "Tell us what you are looking for", "cta_p": "Send the product, quantity and destination and we will come back with a specification-based offer.",
 "title": "Sourcing & Export Services from Egypt | EL-SHIMY", "meta": "How EL-SHIMY sources Egyptian produce through partner farms and packhouses and coordinates export documentation, quality checks and shipment.",
}
V["ar"]["services"] = {
 "eyebrow": "التوريد والتصدير", "h1": "خدمات التوريد والتصدير",
 "lead": "جهة اتصال واحدة لشراء المنتجات المصرية. نوفّر من مزارع ومحطات تعبئة شريكة وننسق الجودة والمستندات والشحن وفق مواصفاتك.",
 "model_h": "نموذج قائم على الشراكات", "model_p": "تأسس الشيمي عام 2016. لا نمتلك مزارع أو محطات تعبئة، بل نعمل مع مزارع ومحطات تعبئة شريكة وندير عملية الشراء نيابةً عنك، لتتعامل مع شريك تجاري واحد.",
 "what_h": "ما الذي ننسقه", "what": [("leaf", "توريد المنتجات والأصناف", "فاكهة وخضروات طازجة، إضافة إلى فراولة وتوت مجمد IQF مختار."), ("clipboard", "المواصفات", "الصنف والحجم والدرجة والتعبئة والملصقات والعلامة الخاصة."),
          ("search", "تنسيق الجودة", "فحص عند التعبئة وفحوص قبل الشحن يُتفق عليها معك."), ("doc", "مستندات التصدير", "المستندات التجارية ومستندات الشحن وشهادات الصحة النباتية والمنشأ بحسب المطلوب."),
          ("ship", "الشحن", "شحن بحري وجوي وبري مع الترتيبات الجمركية.")],
 "who_h": "مع من نعمل", "who": ["المستوردون", "تجار الجملة", "الفنادق والضيافة", "موزعو الأغذية", "مصنّعو الأغذية"], "who_p": "دول الخليج أولويتنا الأولى، ثم آسيا.",
 "proc_h": "كيف يتم عرض السعر", "proc_p": "تُقدَّم الأسعار عند الطلب لأنها تعتمد على الموسم والكمية والتعبئة والشحن.",
 "proc": [("send", "أرسل استفسارك", "المنتج والصنف والحجم والتعبئة والكمية وميناء الوصول والـ Incoterm."), ("search", "نؤكد التوافر", "مطابقة المزارع ومحطات التعبئة الشريكة مع مواصفاتك."),
          ("doc", "استلم عرضاً مكتوباً", "المواصفات والتعبئة والشروط والسعر في وثيقة واحدة."), ("ship", "خطط الشحنة", "تنسيق التعبئة والشحن والمستندات وفق جدولك.")],
 "cta_h": "أخبرنا بما تبحث عنه", "cta_p": "أرسل المنتج والكمية والوجهة وسنعود إليك بعرض مبني على المواصفات.",
 "title": "خدمات التوريد والتصدير من مصر | الشيمي", "meta": "كيف يوفّر الشيمي المنتجات المصرية عبر مزارع ومحطات تعبئة شريكة وينسق مستندات التصدير وفحوص الجودة والشحن.",
}

# ---- About ----
V["en"]["about"] = {
 "eyebrow": "About EL-SHIMY", "h1": "An Egyptian trading partner for international food buyers.",
 "lead": "Established in 2016, EL-SHIMY for Trading & Agencies handles import/export trading and supply-chain coordination for Egyptian fruits, vegetables and selected frozen products.",
 "flow_h": "How the supply chain fits together", "flow_p": "We do not own farms or packing facilities. We coordinate the chain around your order.",
 "flow": [("sprout", "Partner farms", "Growers matched to the product and season"), ("box", "Partner packhouses", "Sorting, grading and packing to specification"),
          ("clipboard", "EL-SHIMY coordination", "Specifications, checks, documents, one contact"), ("ship", "Freight & customs", "Sea, air or land with clearance"), ("pin", "Your market", "Importers, wholesalers, manufacturers")],
 "mv": [("Mission", "To deliver fresh, healthy products that meet agreed quality standards while strengthening the reputation of Egyptian agricultural products abroad."),
        ("Vision", "To be a trusted partner for buyers in the fruit and vegetable export industry, offering dependable solutions that support local farming and the wider supply chain.")],
 "pr_h": "How we work", "pr": [("users", "Long-term relationships", "With buyers and with partner farms and packhouses."), ("tag", "Quality and fair pricing", "A balance between specification and competitive prices."),
        ("sprout", "Supporting Egyptian farming", "Strengthening the local economy through trade."), ("shield", "Say only what we can deliver", "Specifications, availability and prices are confirmed in writing.")],
 "cta_h": "Let's talk about your next order", "cta_p": "Send us the product and destination and we will tell you what we can arrange.",
 "title": "About EL-SHIMY | Egyptian Food Trading & Export Partner", "meta": "EL-SHIMY for Trading & Agencies, established in 2016, is an Egyptian food trading, import/export and supply-chain coordination company.",
 "hero_alt": "Egyptian mangoes (illustrative stock photo)",
}
V["ar"]["about"] = {
 "eyebrow": "عن الشيمي", "h1": "شريك تجاري مصري للمشترين الدوليين في قطاع الأغذية.",
 "lead": "تأسست الشيمي للتجارة والتوكيلات عام 2016، وتدير تجارة الاستيراد والتصدير وتنسيق سلاسل الإمداد للفاكهة والخضروات المصرية ومنتجات مجمدة مختارة.",
 "flow_h": "كيف تتكامل سلسلة الإمداد", "flow_p": "لا نمتلك مزارع أو محطات تعبئة، بل ننسق السلسلة حول طلبك.",
 "flow": [("sprout", "مزارع شريكة", "مزارعون مطابقون للمنتج والموسم"), ("box", "محطات تعبئة شريكة", "فرز وتدريج وتعبئة وفق المواصفات"),
          ("clipboard", "تنسيق الشيمي", "المواصفات والفحوص والمستندات وجهة اتصال واحدة"), ("ship", "الشحن والتخليص", "بحري أو جوي أو بري مع التخليص"), ("pin", "سوقك", "مستوردون وتجار جملة ومصنّعون")],
 "mv": [("رسالتنا", "تقديم منتجات طازجة وصحية تلبي معايير الجودة المتفق عليها مع تعزيز سمعة المنتجات الزراعية المصرية في الخارج."),
        ("رؤيتنا", "أن نكون شريكاً موثوقاً للمشترين في قطاع تصدير الفاكهة والخضروات بحلول يُعتمد عليها تدعم الزراعة المحلية وسلسلة الإمداد الأوسع.")],
 "pr_h": "كيف نعمل", "pr": [("users", "علاقات طويلة الأمد", "مع المشترين ومع المزارع ومحطات التعبئة الشريكة."), ("tag", "جودة وأسعار عادلة", "توازن بين المواصفات والأسعار التنافسية."),
        ("sprout", "دعم الزراعة المصرية", "تعزيز الاقتصاد المحلي من خلال التجارة."), ("shield", "نقول فقط ما نستطيع الوفاء به", "تُؤكَّد المواصفات والتوافر والأسعار كتابةً.")],
 "cta_h": "لنتحدث عن طلبك القادم", "cta_p": "أرسل لنا المنتج والوجهة وسنخبرك بما يمكننا ترتيبه.",
 "title": "عن الشيمي | شريك مصري في تجارة وتصدير الأغذية", "meta": "الشيمي للتجارة والتوكيلات، تأسست عام 2016، شركة مصرية لتجارة الأغذية والاستيراد والتصدير وتنسيق سلاسل الإمداد.",
 "hero_alt": "مانجو مصري (صورة توضيحية)",
}

# ---- Markets ----
V["en"]["markets"] = {
 "eyebrow": "Markets", "h1": "Gulf first, then Asia.",
 "lead": "Our priority markets are the Gulf countries, followed by Asia. We also discuss other destinations on request.",
 "panels": [
  {"n": "01", "t": "Gulf countries", "s": "First focus", "p": "Typical programmes include citrus, onions, potatoes and grapes for wholesalers, hotels and food distributors, with air freight for the most perishable lines.", "slugs": ["egyptian-oranges", "yellow-onions", "egyptian-potatoes", "grapes"]},
  {"n": "02", "t": "Asia", "s": "Second focus", "p": "Long transit times make variety choice, maturity and cold-chain planning especially important. IQF strawberries and berries suit manufacturers who need consistent, free-flowing product.", "slugs": ["iqf-strawberries", "iqf-berries", "egyptian-oranges", "grapes"]}],
 "tab_h": "What usually matters, by region", "tab_cols": ["", "Gulf countries", "Asia"],
 "tab": [("Priority", "First focus", "Second focus"), ("Typical lines", "Citrus, onions, potatoes, grapes; air freight for the most perishable", "Fresh lines chosen carefully for transit; IQF strawberries and berries for manufacturers"),
         ("Planning point", "Labelling and documentation required by the importing country", "Longer transit: variety, maturity and cold-chain planning")],
 "tab_note": "Requirements differ by country and product, and can change. We confirm them with you before shipment.",
 "other_h": "Another destination?", "other_p": "If your market is not listed, send us the product and destination. We will tell you whether we can support it and what the documentation and shipping route would involve.",
 "cta_h": "Tell us your market", "cta_p": "Share the product, volume and destination for a specification-based offer.",
 "title": "Markets We Serve: Gulf & Asia | EL-SHIMY", "meta": "EL-SHIMY prioritises Gulf countries, followed by Asia, supplying Egyptian fruits, vegetables and IQF-frozen products to importers and manufacturers.",
 "view": "View product",
}
V["ar"]["markets"] = {
 "eyebrow": "الأسواق", "h1": "الخليج أولاً ثم آسيا.",
 "lead": "أسواقنا ذات الأولوية هي دول الخليج ثم آسيا. كما نبحث وجهات أخرى عند الطلب.",
 "panels": [
  {"n": "01", "t": "دول الخليج", "s": "التركيز الأول", "p": "تشمل البرامج المعتادة الحمضيات والبصل والبطاطس والعنب لتجار الجملة والفنادق وموزعي الأغذية، مع الشحن الجوي لأكثر الأصناف قابلية للتلف.", "slugs": ["egyptian-oranges", "yellow-onions", "egyptian-potatoes", "grapes"]},
  {"n": "02", "t": "آسيا", "s": "التركيز الثاني", "p": "تجعل مدة الرحلة الطويلة اختيار الصنف ودرجة النضج وتخطيط سلسلة التبريد أمراً بالغ الأهمية. والفراولة والتوت المجمد IQF مناسبان للمصنّعين الذين يحتاجون منتجاً متجانساً منفصل الحبات.", "slugs": ["iqf-strawberries", "iqf-berries", "egyptian-oranges", "grapes"]}],
 "tab_h": "ما يهم عادةً بحسب المنطقة", "tab_cols": ["", "دول الخليج", "آسيا"],
 "tab": [("الأولوية", "التركيز الأول", "التركيز الثاني"), ("الأصناف المعتادة", "حمضيات وبصل وبطاطس وعنب؛ وشحن جوي لأكثرها قابلية للتلف", "أصناف طازجة تُختار بعناية للرحلة؛ وفراولة وتوت IQF للمصنّعين"),
         ("نقطة التخطيط", "الملصقات والمستندات التي تتطلبها الدولة المستوردة", "رحلة أطول: تخطيط الصنف والنضج وسلسلة التبريد")],
 "tab_note": "تختلف المتطلبات بحسب الدولة والمنتج وقد تتغير. نؤكدها معك قبل الشحن.",
 "other_h": "وجهة أخرى؟", "other_p": "إن لم تكن سوقك مذكورة فأرسل لنا المنتج والوجهة. سنخبرك إن كان بإمكاننا دعمها وما يتطلبه المسار من مستندات وشحن.",
 "cta_h": "أخبرنا بسوقك", "cta_p": "شارك المنتج والكمية والوجهة لتحصل على عرض مبني على المواصفات.",
 "title": "الأسواق التي نخدمها: الخليج وآسيا | الشيمي", "meta": "يعطي الشيمي الأولوية لدول الخليج ثم آسيا في توريد الفاكهة والخضروات المصرية والمنتجات المجمدة IQF للمستوردين والمصنّعين.",
 "view": "عرض المنتج",
}

# ---- Insights / guide ----
V["en"]["insights"] = {"eyebrow": "Insights", "h1": "Insights & Export Guides", "lead": "Practical, plain-language guides for buyers sourcing Egyptian produce.",
 "read": "Read the guide", "tag": "Buyer guide", "time": "5 min read",
 "title": "Export Guides & Insights | EL-SHIMY", "meta": "Practical guides for importers buying Egyptian fruits and vegetables: what to specify, which documents to expect and how to request a quote."}
V["ar"]["insights"] = {"eyebrow": "مقالات", "h1": "مقالات وأدلة التصدير", "lead": "أدلة عملية بلغة واضحة للمشترين الذين يوردون المنتجات المصرية.",
 "read": "اقرأ الدليل", "tag": "دليل المشتري", "time": "قراءة 5 دقائق",
 "title": "أدلة ومقالات التصدير | الشيمي", "meta": "أدلة عملية للمستوردين الذين يشترون الفاكهة والخضروات المصرية: ماذا تحدد وما المستندات المتوقعة وكيف تطلب عرض سعر."}

V["en"]["guide"] = {"eyebrow": "Buyer guide", "h1": "How to Request a Produce Quote from an Egyptian Exporter",
 "lead": "A precise enquiry gets a precise offer. Use this checklist so an exporter can quote accurately without back-and-forth.",
 "items": [("tag", "Product and variety", "Name the product and, if you know it, the variety (for example Navel or Valencia oranges). If you are flexible, say so: an exporter can suggest the best option for the season."),
           ("search", "Size, grade and quality", "State the size band (diameter in mm, count per carton or weight), quality class and tolerances for defects, colour and sugar (Brix) if relevant."),
           ("box", "Packing and labelling", "Specify carton or bag type, net weight, pallet configuration, and any private-label printing, barcodes or label languages."),
           ("clipboard", "Quantity and schedule", "Give volume per shipment and delivery frequency or target dates. Container loads and air consignments are planned differently."),
           ("anchor", "Incoterm and destination", "Say whether you want FOB, CFR, CIF or another term, and name the destination port or airport."),
           ("doc", "Documents and import rules", "List what your customs authority requires, such as phytosanitary or origin certificates and any import permits. Rules differ by country and change, so confirm them with your authority."),
           ("mail", "Payment terms", "Mention preferred payment terms so they can be discussed early with your offer.")],
 "tpl_h": "Enquiry template", "tpl_p": "Copy this into an email or into our quote form and fill in the gaps.",
 "tpl": "Product / variety:\nSize / grade:\nPacking / labelling:\nQuantity and schedule:\nIncoterm and destination port:\nDocuments required:\nPayment terms:",
 "copy": "Copy template", "copied": "Copied", "use": "Use in the quote form",
 "faq_h": "Frequently asked questions",
 "faq": [("Do you publish fixed prices?", "No. Prices depend on season, volume, packing and freight, so we quote per enquiry."),
         ("Do you own the farms?", "No. We source through partner farms and packhouses and coordinate quality, documents and shipping."),
         ("Can different products share a container?", "Sometimes, if their temperature and ventilation needs are compatible. Tell us your products and volumes and we will confirm what is feasible."),
         ("Can you handle private label or specific labelling?", "Labelling and private-label needs can be discussed. Include them in your enquiry."),
         ("Which documents will I receive?", "It depends on the product and destination. Commonly an invoice, packing list, shipping document and, where required, phytosanitary and origin certificates.")],
 "title": "Checklist: How to Request a Produce Quote from an Egyptian Exporter", "meta": "What to include when asking an Egyptian exporter for a fruit or vegetable quote: product, size, packing, quantity, Incoterm, documents and shipping."}
V["ar"]["guide"] = {"eyebrow": "دليل المشتري", "h1": "كيف تطلب عرض سعر للمنتجات الزراعية من مُصدّر مصري",
 "lead": "الاستفسار الدقيق يعطي عرضاً دقيقاً. استخدم هذه القائمة ليتمكن المُصدّر من التسعير بدقة دون تبادل رسائل متكرر.",
 "items": [("tag", "المنتج والصنف", "اذكر المنتج والصنف إن عرفته (مثل برتقال أبو سرة أو فالنسيا). وإذا كنت مرناً فاذكر ذلك ليقترح المُصدّر أفضل خيار للموسم."),
           ("search", "الحجم والدرجة والجودة", "حدّد نطاق الحجم (القطر بالمليمتر أو العدد في الكرتونة أو الوزن) ودرجة الجودة وحدود العيوب واللون والسكر (البريكس) إن لزم."),
           ("box", "التعبئة والملصقات", "حدّد نوع الكرتون أو الجوال والوزن الصافي وتكوين البالتة، وأي طباعة لعلامة خاصة أو باركود أو لغات الملصقات."),
           ("clipboard", "الكمية والجدول", "اذكر الكمية لكل شحنة وتكرار التوريد أو المواعيد المستهدفة. فشحنات الحاويات والشحن الجوي تُخطَّط بشكل مختلف."),
           ("anchor", "الـ Incoterm والوجهة", "اذكر هل تريد FOB أو CFR أو CIF أو غيره، وسمِّ ميناء أو مطار الوصول."),
           ("doc", "المستندات وقواعد الاستيراد", "اذكر ما تطلبه جهة الجمارك لديك مثل شهادات الصحة النباتية أو المنشأ وأي تصاريح استيراد. تختلف القواعد بين الدول وتتغير، فتأكد منها مع الجهة المختصة."),
           ("mail", "شروط الدفع", "اذكر شروط الدفع المفضلة لتُناقش مبكراً مع العرض.")],
 "tpl_h": "نموذج الاستفسار", "tpl_p": "انسخ هذا النموذج إلى رسالة بريد أو إلى نموذج عرض السعر لدينا واملأ الفراغات.",
 "tpl": "المنتج / الصنف:\nالحجم / الدرجة:\nالتعبئة / الملصقات:\nالكمية والجدول:\nالـ Incoterm وميناء الوصول:\nالمستندات المطلوبة:\nشروط الدفع:",
 "copy": "انسخ النموذج", "copied": "تم النسخ", "use": "استخدمه في نموذج عرض السعر",
 "faq_h": "الأسئلة الشائعة",
 "faq": [("هل تنشرون أسعاراً ثابتة؟", "لا. تعتمد الأسعار على الموسم والكمية والتعبئة والشحن، لذا نسعّر لكل استفسار."),
         ("هل تملكون المزارع؟", "لا. نوفّر عبر مزارع ومحطات تعبئة شريكة وننسق الجودة والمستندات والشحن."),
         ("هل يمكن لمنتجات مختلفة مشاركة حاوية واحدة؟", "أحياناً، إذا كانت احتياجاتها من الحرارة والتهوية متوافقة. أخبرنا بمنتجاتك وكمياتك لنؤكد المتاح."),
         ("هل يمكنكم التعامل مع العلامة الخاصة أو ملصقات محددة؟", "يمكن مناقشة الملصقات والعلامة الخاصة. أدرجها في استفسارك."),
         ("ما المستندات التي سأستلمها؟", "يعتمد ذلك على المنتج والوجهة. عادةً فاتورة وقائمة تعبئة ومستند شحن، وشهادات صحة نباتية ومنشأ عند اللزوم.")],
 "title": "قائمة تحقق: كيف تطلب عرض سعر للفاكهة والخضروات من مُصدّر مصري", "meta": "ما الذي تدرجه عند طلب عرض سعر لفاكهة أو خضروات من مُصدّر مصري: المنتج والحجم والتعبئة والكمية والـ Incoterm والمستندات والشحن."}

# contact-form topic prefill messages
TOPICS = {
 "en": {"freight": "Shipping quote request. Product, volume, destination and preferred Incoterm:", "sea": "Sea freight enquiry. Product, volume, destination port and Incoterm:",
        "air": "Air freight enquiry. Product, volume, destination airport and target arrival date:", "land": "Land freight enquiry. Product, volume and destination:",
        "quality": "Quality requirements. Product, specification and any standards or inspections needed:", "certificate": "Please share the current certificate details (ISO 22000) relevant to my order.",
        "guide": ""},
 "ar": {"freight": "طلب عرض سعر للشحن. المنتج والكمية والوجهة والـ Incoterm المفضل:", "sea": "استفسار عن الشحن البحري. المنتج والكمية وميناء الوصول والـ Incoterm:",
        "air": "استفسار عن الشحن الجوي. المنتج والكمية ومطار الوصول وتاريخ الوصول المستهدف:", "land": "استفسار عن الشحن البري. المنتج والكمية والوجهة:",
        "quality": "متطلبات الجودة. المنتج والمواصفات وأي معايير أو فحوص مطلوبة:", "certificate": "يرجى مشاركة تفاصيل الشهادة الحالية (ISO 22000) المرتبطة بطلبي.",
        "guide": ""},
}

# ───────────────────────── builders ─────────────────────────
def build_freight(lang):
    d = V[lang]["freight"]; ui = C.UI[lang]; a = B.url("freight", B.other(lang))
    bc, ld = page_trail(lang, ui["nav"]["freight"])
    chips = "".join(f"<li>{x}</li>" for x in d["chips"])
    hero = hero_lite(lang, bc, d["h1"], d["lead"],
                     btn(contact_href(lang, "freight"), d["cta"]) + btn("#modes", d["cta2"], "ghost-light"),
                     f'<img class="hero-art" src="/assets/img/ill-port.svg" width="1200" height="700" alt="{d["img_alt"]}" fetchpriority="high">',
                     eyebrow=d["eyebrow"], cls="hero-freight") + f'<section class="strip"><ul class="wrap">{chips}</ul></section>'
    panels = ""
    for m in d["modes"]:
        panels += f'''<article class="mode mode-{m["k"]} reveal"><div class="mode-art"><img src="/assets/img/{m["art"]}" alt="" width="600" height="380" loading="lazy"></div>
<div class="mode-body"><span class="mode-ic">{icon(m["icon"])}</span><h3>{m["t"]}</h3><p>{m["d"]}</p>{check_list(m["li"])}
<a class="more" href="{contact_href(lang, m["k"])}">{m["a"]} {arrow()}</a></div></article>'''
    modes = f'<section class="section" id="modes"><div class="wrap">{sec_head(d["modes_h"], d["modes_p"])}<div class="modes">{panels}</div><p class="note center-note">{d["modes_note"]}</p></div></section>'
    docs = "".join(f'<li class="paper reveal"><span class="paper-ic">{icon(ic)}</span><div><span class="paper-tag">{tag}</span><h3>{t}</h3><p>{p}</p></div></li>' for ic, t, p, tag in d["docs"])
    docsec = f'''<section class="section dark" id="documents"><div class="wrap"><div class="docs-grid"><div class="docs-intro reveal"><h2>{d["docs_h"]}</h2><p>{d["docs_p"]}</p><div class="callout">{icon("shield")}<p>{d["docs_note"]}</p></div></div>
<ul class="papers">{docs}</ul></div></div></section>'''
    proc = f'<section class="section" id="process"><div class="wrap">{sec_head(d["proc_h"], d["proc_p"])}{timeline(d["proc"])}</div></section>'
    # incoterm matrix
    lab = {"S": d["seller"], "B": d["buyer"], "-": d["na"]}
    head = "".join(f"<th scope='col'>{c}</th>" for c in d["inco_cols"])
    rows = ""
    for code, name, marks in d["inco_rows"]:
        cells = "".join(f'<td><span class="pill pill-{"na" if m == "-" else m}">{lab[m]}</span></td>' for m in marks)
        rows += f'<tr><th scope="row"><b>{code}</b><small>{name}</small></th>{cells}</tr>'
    legend = "".join(f'<li><span class="pill pill-{k}">{lab[k2]}</span></li>' for k, k2 in (("S", "S"), ("B", "B"), ("na", "-")))
    plan = "".join(f"<li>{icon('check')}{x}</li>" for x in d["inco_plan"])
    inco = f'''<section class="section alt" id="incoterms"><div class="wrap">{sec_head(d["inco_h"], d["inco_p"])}
<div class="matrix-wrap reveal" tabindex="0" role="region" aria-label="{d["inco_h"]}"><table class="matrix"><caption class="sr">{d["inco_h"]}</caption><thead><tr><th scope="col"><span class="sr">Incoterm</span></th>{head}</tr></thead><tbody>{rows}</tbody></table></div>
<div class="matrix-foot reveal"><ul class="legend" aria-label="{d["legend"]}">{legend}</ul><p class="note">{d["inco_note"]}</p></div>
<div class="plan reveal"><h3>{d["inco_plan_h"]}</h3><ul>{plan}</ul></div></div></section>'''
    cta = cta_big(lang, d["cta_h"], d["cta_p"], d["cta"], contact_href(lang, "freight"), art="ill-truck.svg")
    return B.page(lang, "freight", B.url("freight", lang), a, d["title"], d["meta"], hero + modes + docsec + proc + inco + cta, ld=[ld])

def build_quality(lang):
    d = V[lang]["quality"]; ui = C.UI[lang]; a = B.url("quality", B.other(lang))
    bc, ld = page_trail(lang, ui["nav"]["quality"])
    scope = "".join(f"<li>{icon(i)}{t}</li>" for i, t in d["scope"])
    media = B.picture("oranges", d["hero_alt"], cls="hero-photo", sizes="(min-width:900px) 40vw, 100vw", eager=True)
    hero = hero_lite(lang, bc, d["h1"], d["lead"], btn("#process", d["cta"]) + btn(contact_href(lang, "quality"), d["cta2"], "ghost-light"), media, eyebrow=d["eyebrow"], cls="hero-quality")
    hero += f'<section class="strip strip-icons"><ul class="wrap">{scope}</ul></section>'
    steps = "".join(f'<li class="alt-step reveal"><span class="alt-ic">{icon(ic)}</span><div class="alt-card"><span class="alt-n">0{i + 1}</span><h3>{t}</h3><p>{p}</p></div></li>' for i, (ic, t, p) in enumerate(d["steps"]))
    proc = f'<section class="section" id="process"><div class="wrap">{sec_head(d["proc_h"], d["proc_p"], "center")}<ol class="alt-tl">{steps}</ol></div></section>'
    sheet = "".join(f"<tr><th scope='row'>{k}</th><td>{v}</td></tr>" for k, v in d["sheet"])
    tr = "".join(f'<li>{icon(ic)}<div><h3>{t}</h3><p>{p}</p></div></li>' for ic, t, p in d["trace"])
    trace = f'''<section class="section alt" id="traceability"><div class="wrap trace">
<div class="trace-copy reveal"><h2>{d["trace_h"]}</h2><p>{d["trace_p"]}</p><ul class="iconlist">{tr}</ul><p class="note">{d["trace_note"]}</p></div>
<div class="trace-vis reveal">{B.picture("grapes", d["trace_img_alt"], cls="trace-img", sizes="(min-width:900px) 45vw, 100vw")}
<figure class="sheet" aria-label="{d["sheet_t"]}"><span class="ribbon">{d["sheet_ribbon"]}</span><figcaption><img src="/assets/img/logo.png" width="96" height="28" alt=""> <b>{d["sheet_t"]}</b></figcaption><table><tbody>{sheet}</tbody></table></figure></div></div></section>'''
    honest = "".join(f"<li>{icon('check')}{x}</li>" for x in d["honest"])
    cert = f'''<section class="section" id="certifications"><div class="wrap">{sec_head(d["cert_h"], d["cert_p"])}
<div class="cert-grid"><article class="iso reveal"><div class="iso-ring" aria-hidden="true">{icon("award")}</div><div><h3>{d["iso_t"]}</h3><p class="iso-s">{d["iso_s"]}</p><p>{d["iso_p"]}</p>{btn(contact_href(lang, "certificate"), d["iso_btn"], "primary")}</div></article>
<div class="cert-side reveal"><h3>{d["ext_t"]}</h3><p>{d["ext_p"]}</p><div class="honest"><h4>{d["honest_t"]}</h4><ul class="ticks">{honest}</ul></div></div></div></div></section>'''
    cta = cta_big(lang, d["cta_h"], d["cta_p"], d["cta2"], contact_href(lang, "quality"), art="ill-reefer.svg")
    return B.page(lang, "quality", B.url("quality", lang), a, d["title"], d["meta"], hero + proc + trace + cert + cta, ld=[ld])

def build_home(lang):
    ui = C.UI[lang]; d = C.PAGES["home"][lang]; h = C.HOME[lang]; v = V[lang]["home"]; fr = V[lang]["freight"]; a = B.url("home", B.other(lang))
    P = B.PBY
    featured = [P[s] for s in ("egyptian-oranges", "egyptian-potatoes", "yellow-onions", "grapes", "strawberries", "iqf-strawberries")]
    wa = f'<a class="btn btn-ghost-light" href="{B.wa_link(lang)}" target="_blank" rel="noopener">{ui["whatsapp"]}</a>' if C.WHATSAPP else ""
    cap = {"en": "Illustrative stock photos", "ar": "صور توضيحية"}[lang]
    mosaic = f'''<div class="mosaic">{B.picture("strawberries", {"en": "Fresh strawberries", "ar": "فراولة طازجة"}[lang], cls="m1", sizes="(min-width:900px) 30vw, 60vw", eager=True)}
{B.picture("oranges", {"en": "Egyptian oranges", "ar": "برتقال مصري"}[lang], cls="m2", sizes="(min-width:900px) 18vw, 40vw")}{B.picture("grapes", {"en": "Table grapes", "ar": "عنب مائدة"}[lang], cls="m3", sizes="(min-width:900px) 18vw, 40vw")}<span class="m-cap">{cap}</span></div>'''
    hero = f'''<section class="hero"><div class="wrap hero-grid"><div class="hero-copy"><p class="eyebrow rise">{C.LEGAL[lang]}</p><h1 class="rise">{d["h1"]}</h1><p class="lead rise">{d["lead"]}</p>
<div class="hero-actions rise">{btn(B.url("contact", lang), ui["quote"])}{btn(B.url("products", lang), ui["view_all"], "ghost-light")}{wa}</div></div><div class="hero-media rise">{mosaic}</div></div></section>
<section class="strip"><ul class="wrap">{"".join(f"<li>{s}</li>" for s in h["strip"])}</ul></section>'''
    tiles = ""
    for cat, key, img in (("veg", "veg", "vegetables"), ("fruit", "fruit", "oranges"), ("frozen", "frozen_cat", "strawberries")):
        bg = B.picture(img, "", cls="tile-img", sizes="(min-width:900px) 33vw, 100vw") if img else f'<span class="tile-img tile-plain tile-{cat}"></span>'
        tiles += f'<a class="tile tile-c-{cat} reveal" href="{B.url("products", lang)}?cat={cat}">{bg}<span class="tile-txt"><b>{ui[key]}</b><small>{v["cat_sub"][cat]}</small><span class="more-w">{ui["view_all"]} {arrow()}</span></span></a>'
    cats = f'<section class="section"><div class="wrap">{sec_head(h["cats_h"], h["cats_lead"])}<div class="tiles">{tiles}</div></div></section>'
    why = "".join(f'<li class="reveal">{icon(ic)}<div><h3>{t}</h3><p>{p}</p></div></li>' for ic, t, p in v["why"])
    whysec = f'<section class="section dark"><div class="wrap why"><div class="why-h reveal"><h2>{v["why_h"]}</h2><p>{v["why_p"]}</p></div><ul class="why-list">{why}</ul></div></section>'
    feat = f'<section class="section"><div class="wrap">{sec_head(h["feat_h"])}<div class="cards">{"".join(B.card(p, lang) for p in featured)}</div><p class="center"><a class="btn btn-primary" href="{B.url("products", lang)}">{ui["view_all"]}</a></p></div></section>'
    steps = [("send", *h["how"][0]), ("clipboard", *h["how"][1]), ("box", *h["how"][2]), ("ship", *h["how"][3])]
    proc = f'<section class="section alt"><div class="wrap">{sec_head(h["how_h"], h["model"])}{timeline(steps, "tl-4")}</div></section>'
    frt = f'''<section class="band"><div class="wrap band-in"><div class="reveal"><h2>{v["freight_h"]}</h2><p>{v["freight_p"]}</p><ul class="modes-mini"><li>{icon("ship")}{fr["modes"][0]["t"]}</li><li>{icon("plane")}{fr["modes"][1]["t"]}</li><li>{icon("truck")}{fr["modes"][2]["t"]}</li></ul>{btn(B.url("freight", lang), v["freight_a"], "accent")}</div>
<img class="band-art reveal" src="/assets/img/ill-port.svg" width="1200" height="700" alt="{fr["img_alt"]}" loading="lazy"></div></section>'''
    mk = "".join(f'<a class="mk reveal" href="{B.url("markets", lang)}"><b>{t}</b><span>{s}</span></a>' for t, s in v["mk"])
    markets = f'<section class="section"><div class="wrap mk-wrap"><div class="reveal"><h2>{v["markets_h"]}</h2><p>{ui["nav"]["markets"]}: {v["mk"][0][0]} · {v["mk"][1][0]}</p><a class="more" href="{B.url("markets", lang)}">{v["markets_a"]} {arrow()}</a></div><div class="mks">{mk}</div></div></section>'
    org = {"@context": "https://schema.org", "@type": "Organization", "name": C.LEGAL["en"], "alternateName": C.BRAND, "url": B.abs_url("/"), "logo": B.abs_url("/assets/img/logo.png"),
           "foundingDate": "2016", "email": C.EMAIL, "telephone": C.PHONE, "sameAs": [C.LINKEDIN], "address": {"@type": "PostalAddress", "addressLocality": "Cairo", "addressCountry": "EG"},
           "description": C.PAGES["home"]["en"]["lead"]}
    return B.page(lang, "home", B.url("home", lang), a, d["title"], d["meta"], hero + cats + whysec + feat + proc + frt + markets + B.cta_band(lang), ld=[org])

def build_services(lang):
    d = V[lang]["services"]; ui = C.UI[lang]; a = B.url("services", B.other(lang))
    bc, ld = page_trail(lang, ui["nav"]["services"])
    media = B.picture("mandarins", {"en": "Mandarins ready for export (illustrative stock photo)", "ar": "يوسفي جاهز للتصدير (صورة توضيحية)"}[lang], cls="hero-photo", sizes="(min-width:900px) 40vw, 100vw", eager=True)
    hero = hero_lite(lang, bc, d["h1"], d["lead"], btn(B.url("contact", lang), ui["quote"]) + btn("#what", d["what_h"], "ghost-light"), media, eyebrow=d["eyebrow"])
    model = f'<section class="section"><div class="wrap model reveal"><h2>{d["model_h"]}</h2><p>{d["model_p"]}</p></div></section>'
    what = "".join(f'<li class="reveal">{icon(ic)}<div><h3>{t}</h3><p>{p}</p></div></li>' for ic, t, p in d["what"])
    whatsec = f'<section class="section dark" id="what"><div class="wrap">{sec_head(d["what_h"])}<ul class="feat-grid">{what}</ul></div></section>'
    who = "".join(f"<li>{x}</li>" for x in d["who"])
    whosec = f'<section class="section"><div class="wrap who reveal"><h2>{d["who_h"]}</h2><ul class="chips-static">{who}</ul><p>{d["who_p"]}</p></div></section>'
    proc = f'<section class="section alt"><div class="wrap">{sec_head(d["proc_h"], d["proc_p"])}{timeline(d["proc"], "tl-4")}</div></section>'
    return B.page(lang, "services", B.url("services", lang), a, d["title"], d["meta"], hero + model + whatsec + whosec + proc + cta_big(lang, d["cta_h"], d["cta_p"], ui["quote"], B.url("contact", lang), art="ill-plane.svg"), ld=[ld])

def build_about(lang):
    d = V[lang]["about"]; ui = C.UI[lang]; a = B.url("about", B.other(lang))
    bc, ld = page_trail(lang, ui["nav"]["about"])
    media = B.picture("mangoes", d["hero_alt"], cls="hero-photo hero-photo-tall", sizes="(min-width:900px) 35vw, 100vw", eager=True)
    hero = hero_lite(lang, bc, d["h1"], d["lead"], btn(B.url("contact", lang), ui["quote"]) + btn(B.url("services", lang), ui["nav"]["services"], "ghost-light"), media, eyebrow=d["eyebrow"])
    flow = "".join(f'<li class="reveal"><span class="flow-ic">{icon(ic)}</span><h3>{t}</h3><p>{p}</p></li>' for ic, t, p in d["flow"])
    flowsec = f'<section class="section"><div class="wrap">{sec_head(d["flow_h"], d["flow_p"])}<ol class="flow">{flow}</ol></div></section>'
    mv = f'<section class="mv"><div class="mv-a reveal"><div><h2>{d["mv"][0][0]}</h2><p>{d["mv"][0][1]}</p></div></div><div class="mv-b reveal"><div><h2>{d["mv"][1][0]}</h2><p>{d["mv"][1][1]}</p></div></div></section>'
    pr = "".join(f'<li class="reveal">{icon(ic)}<h3>{t}</h3><p>{p}</p></li>' for ic, t, p in d["pr"])
    prsec = f'<section class="section"><div class="wrap">{sec_head(d["pr_h"])}<ul class="principles">{pr}</ul></div></section>'
    return B.page(lang, "about", B.url("about", lang), a, d["title"], d["meta"], hero + flowsec + mv + prsec + cta_big(lang, d["cta_h"], d["cta_p"], ui["quote"], B.url("contact", lang), art="ill-truck.svg"), ld=[ld])

def build_markets(lang):
    d = V[lang]["markets"]; ui = C.UI[lang]; a = B.url("markets", B.other(lang))
    bc, ld = page_trail(lang, ui["nav"]["markets"])
    hero = hero_lite(lang, bc, d["h1"], d["lead"], btn(B.url("contact", lang), ui["quote"]), f'<img class="hero-art" src="/assets/img/ill-port.svg" width="1200" height="700" alt="" fetchpriority="high">', eyebrow=d["eyebrow"])
    panels = ""
    for i, p in enumerate(d["panels"]):
        links = "".join(f'<a class="chip-link" href="{B.url("product", lang, s)}">{B.esc(B.PBY[s]["name"][lang].split(":")[0])}</a>' for s in p["slugs"])
        panels += f'<article class="mkt mkt-{i + 1} reveal"><span class="mkt-n">{p["n"]}</span><p class="eyebrow">{p["s"]}</p><h2>{p["t"]}</h2><p>{p["p"]}</p><div class="chip-links">{links}</div></article>'
    rows = "".join(f"<tr><th scope='row'>{r[0]}</th><td>{r[1]}</td><td>{r[2]}</td></tr>" for r in d["tab"])
    tab = f'''<section class="section alt"><div class="wrap">{sec_head(d["tab_h"])}<div class="matrix-wrap reveal" tabindex="0" role="region" aria-label="{d["tab_h"]}"><table class="cmp"><thead><tr><th scope="col"><span class="sr">&nbsp;</span></th><th scope="col">{d["tab_cols"][1]}</th><th scope="col">{d["tab_cols"][2]}</th></tr></thead><tbody>{rows}</tbody></table></div><p class="note">{d["tab_note"]}</p></div></section>'''
    other = f'<section class="section"><div class="wrap other reveal">{icon("globe")}<div><h2>{d["other_h"]}</h2><p>{d["other_p"]}</p></div>{btn(B.url("contact", lang), ui["quote"], "primary")}</div></section>'
    return B.page(lang, "markets", B.url("markets", lang), a, d["title"], d["meta"], hero + f'<section class="section"><div class="wrap mkts">{panels}</div></section>' + tab + other, ld=[ld])

def build_insights(lang):
    d = V[lang]["insights"]; g = V[lang]["guide"]; ui = C.UI[lang]; a = B.url("insights", B.other(lang))
    bc, ld = page_trail(lang, ui["nav"]["insights"])
    hero = hero_lite(lang, bc, d["h1"], d["lead"], eyebrow=d["eyebrow"])
    feat = f'''<section class="section"><div class="wrap"><a class="feature reveal" href="{B.url("guide", lang)}"><div class="feature-vis">{icon("clipboard")}<ol>{"".join(f"<li>{icon('check')}{t}</li>" for _, t, _ in g["items"][:5])}</ol></div>
<div class="feature-txt"><span class="badge-o">{d["tag"]}</span><h2>{g["h1"]}</h2><p>{g["lead"]}</p><span class="more">{d["read"]} {arrow()}</span><small>{d["time"]}</small></div></a></div></section>'''
    return B.page(lang, "insights", B.url("insights", lang), a, d["title"], d["meta"], hero + feat + B.cta_band(lang), ld=[ld])

def build_guide(lang):
    g = V[lang]["guide"]; ui = C.UI[lang]; a = B.url("guide", B.other(lang))
    bc, ld = B.crumbs(lang, [(ui["nav"]["insights"], B.url("insights", lang)), (g["h1"], None)])
    hero = hero_lite(lang, bc, g["h1"], g["lead"], eyebrow=g["eyebrow"])
    items = "".join(f'<li class="gi reveal"><span class="gi-n">{i + 1}</span><span class="gi-ic">{icon(ic)}</span><div><h3>{t}</h3><p>{p}</p></div></li>' for i, (ic, t, p) in enumerate(g["items"]))
    tpl = f'''<section class="section alt"><div class="wrap tpl reveal"><div><h2>{g["tpl_h"]}</h2><p>{g["tpl_p"]}</p><div class="hero-actions"><button class="btn btn-primary" type="button" data-copy="#tpl-text" data-done="{g["copied"]}">{icon("copy")} {g["copy"]}</button>{btn(contact_href(lang, "guide") + "&tpl=1", g["use"], "ghost")}</div></div><pre id="tpl-text" class="tpl-box" dir="{"rtl" if lang == "ar" else "ltr"}">{B.esc(g["tpl"])}</pre></div></section>'''
    faq = "".join(f'<details class="reveal"><summary>{q}</summary><p>{an}</p></details>' for q, an in g["faq"])
    faqsec = f'<section class="section"><div class="wrap faq">{sec_head(g["faq_h"])}<div class="acc">{faq}</div></div></section>'
    return B.page(lang, "insights", B.url("guide", lang), a, g["title"], g["meta"], hero + f'<section class="section"><div class="wrap"><ol class="gis">{items}</ol></div></section>' + tpl + faqsec + B.cta_band(lang), ld=[ld])

def build_products_hero(lang, bc, h1, lead):
    media = f'''<div class="mosaic mosaic-s">{B.picture("oranges", "", cls="m1", sizes="25vw")}{B.picture("strawberries", "", cls="m2", sizes="20vw")}{B.picture("grapes", "", cls="m3", sizes="20vw")}</div>'''
    return hero_lite(lang, bc, h1, lead, media=media)
