# -*- coding: utf-8 -*-
"""Inline SVG icon sprite (24px, stroke-based) used across the site."""
_P = {
 "check": '<path d="M5 13l4 4L19 7"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "ship": '<path d="M3 16l2 4h14l2-4z"/><path d="M7 16V9h10v7"/><path d="M10 9V6h4v3"/>',
 "plane": '<path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 00-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z"/>',
 "truck": '<path d="M2 6h11v10H2zM13 9h4l4 4v3h-8z"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
 "doc": '<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h8"/>',
 "list": '<path d="M8 6h12M8 12h12M8 18h12M3.5 6h.01M3.5 12h.01M3.5 18h.01"/>',
 "award": '<circle cx="12" cy="9" r="6"/><path d="M8.5 14.5L7 22l5-3 5 3-1.5-7.5"/>',
 "leaf": '<path d="M5 19C5 10 10 4 20 4c0 10-6 15-15 15z"/><path d="M5 19c3-5 6-8 10-10"/>',
 "clipboard": '<path d="M9 3h6v3H9zM7 5H5v16h14V5h-2"/><path d="M9 14l2 2 4-4"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "thermo": '<path d="M10 14V5a2 2 0 014 0v9a4 4 0 11-4 0z"/><path d="M12 9v7"/>',
 "search": '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4-4"/>',
 "box": '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
 "pin": '<path d="M12 21s7-6 7-12a7 7 0 10-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "users": '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-4 3-6 6-6s6 2 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14c3 0 5 2 5 5"/>',
 "mail": '<path d="M3 5h18v14H3z"/><path d="M3 6l9 7 9-7"/>',
 "tag": '<path d="M3 12V3h9l9 9-9 9z"/><circle cx="7.5" cy="7.5" r="1"/>',
 "snow": '<path d="M12 2v20M3 7l18 10M21 7L3 17"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 "anchor": '<circle cx="12" cy="5" r="2"/><path d="M12 7v14M5 12H3c0 5 4 9 9 9s9-4 9-9h-2M8 12h8"/>',
 "camera": '<path d="M3 8h4l2-3h6l2 3h4v12H3z"/><circle cx="12" cy="13" r="4"/>',
 "copy": '<path d="M9 9h11v11H9zM5 15V4h11"/>',
 "chevron": '<path d="M6 9l6 6 6-6"/>',
 "stamp": '<path d="M4 20h16M6 16h12v4H6zM9 16c0-4-2-4-2-7a5 5 0 0110 0c0 3-2 3-2 7"/>',
 "link": '<path d="M10 14a4 4 0 005.7 0l3-3a4 4 0 00-5.7-5.7l-1 1M14 10a4 4 0 00-5.7 0l-3 3a4 4 0 005.7 5.7l1-1"/>',
 "sprout": '<path d="M12 21V11"/><path d="M12 11C12 7 9 5 5 5c0 4 3 6 7 6zM12 13c0-3 2-5 6-5 0 3-2 5-6 5z"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>',
 "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 11v6M8 7.5v.01M12 17v-6M12 13a3 3 0 016 0v4"/>',
 "chat": '<path d="M4 20l1.5-4A8 8 0 1112 20a8 8 0 01-4-1z"/>',
 "send": '<path d="M22 2L11 13M22 2l-7 20-4-9-9-4z"/>',
}
SPRITE = '<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">' + "".join(
    f'<symbol id="i-{k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{v}</symbol>'
    for k, v in _P.items()) + "</svg>"

def icon(name, cls=""):
    return f'<svg class="ic {cls}" aria-hidden="true" focusable="false"><use href="#i-{name}"/></svg>'
