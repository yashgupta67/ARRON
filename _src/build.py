#!/usr/bin/env python3
"""Generates the ARRON static site into the parent folder. Run: python3 _src/build.py"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import visuals as V

VER = str(int(__import__('time').time()))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL_1 = "RajitM@arrontechnologies.com"
EMAIL_2 = "Annad@arrontechnologies.com"
MAILTO = f"mailto:{EMAIL_1},{EMAIL_2}?subject=Enquiry%20from%20the%20ARRON%20website"
import re as _re

def _svg_path(fname):
    s = open(os.path.join(ROOT, "assets", "img", "partners", fname)).read()
    m = _re.search(r' d="([^"]+)"', s)
    return m.group(1)


_BRANDS = {
    "SAP": ("sap.svg", "#0FAAFF"), "Oracle": ("oracle.svg", "#F80000"), "Salesforce": ("salesforce.svg", "#00A1E0"),
    "Zoho": ("zoho.svg", "#E42527"), "OpenAI": ("openai.svg", "#111111"), "Anthropic": ("anthropic.svg", "#D97757"),
    "Google Cloud": ("googlecloud.svg", "#4285F4"), "AWS": ("amazonaws.svg", "#FF9900"),
}


def plogo(name):
    """Logo (brand icon + name) for a partner, or a plain text wordmark when no icon is available."""
    if name == "Microsoft":
        ico = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="1.5" y="1.5" width="10" height="10" fill="#F25022"/><rect x="12.5" y="1.5" width="10" height="10" fill="#7FBA00"/><rect x="1.5" y="12.5" width="10" height="10" fill="#00A4EF"/><rect x="12.5" y="12.5" width="10" height="10" fill="#FFB900"/></svg>'
        return f'<span class="plg">{ico}<span class="wm">Microsoft</span></span>'
    if name in _BRANDS:
        f, col = _BRANDS[name]
        return f'<span class="plg"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="{col}" d="{_svg_path(f)}"/></svg><span class="wm">{name}</span></span>'
    if name == "ServiceNow":
        return '<span class="plg"><span class="wm">service<i style="color:#3fae2a">now</i></span></span>'
    if name == "Workday":
        return '<span class="plg"><span class="wm" style="color:#0875E1">workday<i style="color:#F5A31A">.</i></span></span>'
    if name == "NetSuite":
        return '<span class="plg"><span class="wm" style="color:#1F4E85">NetSuite</span></span>'
    return f'<span class="plg"><span class="wm">{name}</span></span>'


ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHEV = '<svg width="10" height="7" viewBox="0 0 12 8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M1 1.5l5 5 5-5"/></svg>'
LI = '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.1c.6-1 1.9-2 3.9-2 4 0 4.7 2.6 4.7 6V21h-4v-5c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7V21h-4z"/></svg>'

ICONS = {
    "bank": '<path d="M3 21h18M5 21V10M10 21V10M14 21V10M19 21V10M2 10l10-6 10 6"/>',
    "factory": '<path d="M3 21V8l6 4V8l6 4V4h6v17z"/>',
    "heart": '<path d="M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.5-7 10-7 10z"/>',
    "cart": '<path d="M6 6h15l-2 9H8zM6 6L5 3H2"/><circle cx="9" cy="20" r="1.2"/><circle cx="18" cy="20" r="1.2"/>',
    "signal": '<path d="M5 12a10 10 0 0 1 14 0M8 15a6 6 0 0 1 8 0M12 19h.01"/>',
    "code": '<path d="M8 8l-5 4 5 4M16 8l5 4-5 4M14 5l-4 14"/>',
    "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    "gov": '<path d="M3 10l9-6 9 6M5 10v9h14v-9M9 19v-5h6v5"/>',
    "server": '<rect x="3" y="4" width="18" height="6" rx="2"/><rect x="3" y="14" width="18" height="6" rx="2"/><path d="M7 7h.01M7 17h.01"/>',
    "truck": '<path d="M2 6h12v10H2zM14 10h5l3 3v3h-8"/><circle cx="6" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/>',
    "brief": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V4h6v3M3 13h18"/>',
    "plane": '<path d="M2 14l20-8-8 20-3-9z"/>',
    "map": '<path d="M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2z"/><path d="M9 4v14M15 6v14"/>',
    "doc": '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
    "chart": '<path d="M4 20V4M4 20h16M8 16v-5M13 16V8M18 16v-8"/>',
    "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.6 2.7-6 6-6s6 2.4 6 6M16 5.2a3.2 3.2 0 0 1 0 5.6M18 14.4c2 .8 3 2.6 3 5.6"/>',
    "shield": '<path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/>',
    "cog": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
}


def icon(k):
    return f'<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[k]}</svg>'


def photo(name, alt=""):
    return f'<img src="assets/img/photos/{name}.jpg" alt="{alt}" loading="lazy">'


def part(name, cls="art ph", extra=""):
    return f'<div class="{cls}">{photo(name)}{extra}</div>'


PLATFORMS = ["ServiceNow", "SAP", "Oracle", "Microsoft", "Salesforce", "Workday", "NetSuite", "Zoho", "AWS", "Google Cloud", "OpenAI", "Anthropic"]

# ------------------------------------------------------------------ NAV
INDUSTRY_PAGES = [("banking.html", "Banking & Financial Services", "Compliance, resilience and customer trust"),
                  ("manufacturing.html", "Manufacturing", "Connected plants, planning and supply chains"),
                  ("retail.html", "Retail & Consumer", "Omnichannel experience and demand sensing"),
                  ("telecom.html", "Telecom", "Proactive service on always-on networks"),
                  ("healthcare.html", "Healthcare", "Access, operations and secure data")]
MENUS = {
    "offerings.html": dict(groups=[(None, [
        ("ai.html", "AI / Super Intelligence", "AI built for impact, architected for autonomy"),
        ("erp.html", "ERP", "A smarter core for the AI-native enterprise"),
        ("itsm.html", "ITSM", "Service built for efficiency, engineered for resilience"),
        ("cx.html", "Customer Experience", "Every interaction, elevated"),
        ("digital-workplace.html", "Digital Workplace", "Work designed around people")])],
        foot=("offerings.html", "View all offerings"), wide=False),
    "capabilities.html": dict(groups=[(None, [
        ("consulting.html", "Consulting", "Strategy and advice you can execute"),
        ("services.html", "Services", "Implementation, integration and managed support"),
        ("partnerships.html", "Partnerships", "A certified ecosystem on your side")])],
        foot=("capabilities.html", "How we work with you"), wide=False),
    "products.html": dict(groups=[(None, [
        ("arron-ai.html", "ARRON AI", "Agentic AI for customer and employee experience"),
        ("record-vault-ai.html", "Record Vault AI", "An AI-powered evidence vault"),
        ("connect-ai.html", "Connect AI", "AI for nonprofit and volunteer organizations")])],
        foot=("products.html", "Product as a Service"), wide=False),
    "industry.html": dict(groups=[(None, [(h, t, d) for h, t, d in INDUSTRY_PAGES])],
        foot=("industry.html", "All industries"), wide=False),
    "insights.html": dict(groups=[(None, [
        ("technology-insights.html", "Technology Insights", "What is changing in enterprise technology"),
        ("perspectives.html", "Perspectives", "Points of view from our leaders"),
        ("playbooks.html", "Playbooks", "Practical guides you can put to work"),
        ("blog.html", "Blog / Newsletter", "Articles and our newsletter")])],
        foot=("insights.html", "All our insights"), wide=False),
    "proven-experience.html": dict(groups=[(None, [
        ("client-stories.html", "Client Stories", "In our clients' own words and numbers"),
        ("case-studies.html", "Case Studies", "Challenge, approach and outcome"),
        ("testimonials.html", "Testimonials", "What clients say about working with us")])],
        foot=("proven-experience.html", "All proven experience"), wide=False),
    "about.html": dict(groups=[(None, [
        ("about.html", "Our Purpose", "Why ARRON exists"),
        ("delivery-landscape.html", "Delivery Landscape", "Offices across the U.S. and India"),
        ("consultants.html", "Leadership & Consultants", "The people you will work with"),
        ("partners.html", "Our Partners", "The platform ecosystem we work across")])],
        foot=("about.html", "About ARRON"), wide=False),
}
NAV = [("index.html", "Home"), ("offerings.html", "Offerings"), ("capabilities.html", "Capabilities"), ("products.html", "Products"),
       ("industry.html", "Industry Expertise"), ("insights.html", "Our Insights"), ("proven-experience.html", "Proven Experience"),
       ("about.html", "About ARRON"), ("careers.html", "Careers")]
SECTION = {}
for sec, m in MENUS.items():
    SECTION[sec] = sec
    for g, items in m["groups"]:
        for h, *_ in items:
            SECTION.setdefault(h, sec)

def header(fname):
    active = SECTION.get(fname, fname)
    items = ''
    for href, label in NAV:
        if href in MENUS:
            m = MENUS[href]
            body = ''
            for g, its in m["groups"]:
                col = ''
                if g:
                    col += f'<h5>{g}</h5>'
                col += ''.join(f'<a href="{h}"><b>{t}</b><span>{d}</span></a>' for h, t, d in its)
                body += f'<div class="mcol">{col}</div>'
            foot = f'<a class="foot" href="{m["foot"][0]}">{m["foot"][1]} →</a>'
            cls = "menu wide" if m["wide"] else "menu"
            on = "active" if active == href else ""
            items += f'<div class="dd"><a class="{on}" href="{href}">{label}{CHEV}</a><div class="{cls}">{body}{foot}</div></div>'
        else:
            on = ' class="active"' if href == active else ''
            items += f'<a href="{href}"{on}>{label}</a>'
    return f'''<header class="site-header"><div class="wrap bar">
<a class="logo" href="index.html" aria-label="ARRON home"><img src="assets/img/logo.png" alt="ARRON — Ahead of now" width="693" height="210" style="height:58px;width:auto;max-width:none;flex:none;aspect-ratio:693/210"></a>
<button class="burger" aria-label="Menu"><span></span><span></span></button>
<nav class="nav">{items}<a class="btn btn-red" href="about.html#contact">Talk to us {ARROW}</a></nav></div></header>'''


def footer():
    def col(title, links):
        return f'<div><h4>{title}</h4><ul>' + ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in links) + '</ul></div>'
    return f'''<footer class="site-footer"><div class="wrap"><div class="ft" style="grid-template-columns:1.5fr repeat(4,1fr)">
<div><img src="assets/img/logo-stacked-light.png" alt="ARRON — ahead of now"><p style="max-width:34ch">An AI-ready technology company building AI-native enterprises. Headquartered in Dallas, Texas.</p></div>
{col("Offerings", [("ai.html", "AI / Super Intelligence"), ("erp.html", "ERP"), ("itsm.html", "ITSM"), ("cx.html", "Customer Experience"), ("digital-workplace.html", "Digital Workplace")])}
{col("Capabilities & Products", [("consulting.html", "Consulting"), ("services.html", "Services"), ("partnerships.html", "Partnerships"), ("arron-ai.html", "ARRON AI"), ("record-vault-ai.html", "Record Vault AI"), ("connect-ai.html", "Connect AI")])}
{col("Industries", [(h, t) for h, t, d in INDUSTRY_PAGES])}
{col("Company", [("about.html", "About ARRON"), ("proven-experience.html", "Proven Experience"), ("insights.html", "Our Insights"), ("careers.html", "Careers"), (f"mailto:{EMAIL_1}", EMAIL_1), (f"mailto:{EMAIL_2}", EMAIL_2)])}</div>
<div class="fb"><span>© 2026 ARRON Technologies. All rights reserved.</span><span>Dallas, Texas · Louisville · Houston · Delhi NCR · Pune · Bangalore</span></div></div></footer>'''


def marquee(label="The platforms and ecosystems we work across", names=PLATFORMS):
    items = ''.join(f'<div class="it">{plogo(n)}</div>' for n in names)
    return f'<div class="marq"><div class="lab">{label}</div><div class="roll"><div class="track">{items}{items}</div></div></div>'


def page(fname, title, desc, body):
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="icon" href="assets/img/mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=Manrope:wght@500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css?v={VER}"></head>
<body>{header(fname)}
{body}
{footer()}
<script src="assets/main.js?v={VER}"></script></body></html>'''
    html = html.replace('href="about.html#contact"', f'href="{MAILTO}"') if fname != "about.html" else html.replace('<a class="btn btn-red" href="about.html#contact">', f'<a class="btn btn-red" href="{MAILTO}">')
    with open(os.path.join(ROOT, fname), "w") as f:
        f.write(html)


def hero(crumb, h1, lead, stage, stage_cls="", cta=True, cta_html=None):
    c = cta_html if cta_html else f'<div class="hero-cta rv" data-delay=".5"><a class="btn btn-red" href="about.html#contact">Talk to an expert {ARROW}</a><a class="btn btn-ghost" href="#more">Explore below</a></div>' if cta else ''
    return f'''<section class="hero"><div class="wrap hero-grid"><div>
<div class="crumbs rv">{crumb}</div><h1 data-split>{h1}</h1><p class="lead rv" data-delay=".35">{lead}</p>{c}</div>
<div class="stage {stage_cls} rv" data-delay=".25">{stage}</div></div></section>'''


def photo_stage(name, title, sub):
    return f'{photo(name)}<div class="cap"><b>{title}</b><span>{sub}</span></div>'


def sh(kicker, h2, p):
    return f'<div class="sh"><div><span class="kicker rv">{kicker}</span><h2 data-split>{h2}</h2></div><p class="rv" data-delay=".2">{p}</p></div>'


def rows(items, cls=''):
    return f'<div class="rows {cls}" data-stagger>' + ''.join(
        f'<div class="row"><span class="n">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(items)) + '</div>'


def proc(steps):
    return '<div class="proc" data-stagger>' + ''.join(f'<div class="pstep"><span class="n">{i+1}</span><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(steps)) + '</div>'


def cta_band(h, p, label="Start a conversation", href="about.html#contact"):
    return f'<section style="padding:70px 0 110px"><div class="wrap"><div class="cta rv"><div><h2>{h}</h2><p>{p}</p><a class="btn btn-red" href="{href}">{label} {ARROW}</a></div></div></div></section>'


def tile(href, k, title, desc, art_html):
    return f'<a class="tile" href="{href}"><div class="art">{art_html}</div><div class="tb"><span class="k">{k}</span><h3>{title}</h3><p>{desc}</p><span class="more">Explore {ARROW}</span></div></a>'



# =========================================================== DETAIL PAGES (offerings + capabilities)
D = {}
D["ai"] = dict(
    file="ai.html", parent=("offerings.html", "Offerings"), name="Artificial & Super Intelligence", short="AI / SI", visual=V.v_ai, mini="ai",
    tile_tag="Evolve or Beyond AI",
    tile_desc="Beyond AI assistance toward adaptive, autonomous systems that transform decisions, operations and experiences into impact.",
    platforms=["OpenAI", "Anthropic", "Google Cloud", "AWS", "Microsoft", "ServiceNow", "SAP", "Salesforce", "Zoho", "Databricks", "Snowflake"],
    plat_label="AI platforms and ecosystems we work with")
D["erp"] = dict(
    file="erp.html", parent=("offerings.html", "Offerings"), name="Enterprise Resource Planning", short="ERP", visual=V.v_erp, mini="erp",
    tile_tag="A smarter core",
    tile_desc="Modernized enterprise core and processes, on a platform that simplifies operations, accelerates decisions and enables continuous change.",
    plat_label="ERP platforms we work with",
    platforms=["SAP", "Oracle", "Microsoft", "NetSuite", "Workday", "Zoho", "Infor", "Epicor", "IFS"])
D["itsm"] = dict(
    file="itsm.html", parent=("offerings.html", "Offerings"), name="IT Service Management", short="ITSM", visual=V.v_itsm, mini="itsm",
    tile_tag="Service, before it's needed",
    tile_desc="Proactive, automated services that resolve faster, reduce disruption and improve the support experience.",
    h1='Service built for efficiency, <span class="r">engineered for resilience.</span>',
    lead="We design and deploy ITIL-aligned service management on leading platforms, combining AI-led self-service, knowledge, prediction and automation to lower cost-to-serve, accelerate resolution and free teams to focus on higher-value work.",
    what_h="Service management that anticipates, not just responds.", what_p="Four disciplines that take support from reactive to proactive.",
    what=[("Process Optimization & Automation", "Standardize ITIL-aligned workflows with AI and automation for faster, lower-effort service."),
          ("Incident & Problem Management", "Combine AI-assisted diagnosis, prediction and root-cause analysis to resolve faster and reduce repeat issues."),
          ("Change, Release & Service Improvement", "Risk-based controls and service insights to deliver safer change and continuously improve performance."),
          ("Asset, Knowledge & Self-Service", "A lifecycle-aware CMDB, connected knowledge and AI-led self-service that people actually use.")],
    steps_h="From assessment to continuous improvement.", steps_p="Four stages, each with a defined output, so you always know where the program stands.",
    steps=[("Assess", "Measure maturity across tools, workflows and skills."), ("Roadmap", "Choose the platform, integrations, KPIs and timeline."),
           ("Implement", "Configure portal, SLAs and automation, and migrate from legacy tools."), ("Optimize", "Use analytics to predict breaches and extend to HR and Finance.")],
    get_h="Better service. Lower cost. Less disruption.", get_p="What changes for your users, your team and your budget.",
    get=[("bolt", "Faster resolution", "AI-assisted triage and routing get issues to the right resolution faster."),
         ("chart", "Lower cost-to-serve", "Self-service, knowledge and automation reduce avoidable support effort."),
         ("cog", "Higher productivity", "Automates repetitive work so teams can focus on higher-value service."),
         ("refresh", "Fewer repeat incidents", "Root-cause insights help eliminate recurring issues and reduce demand."),
         ("users", "Better service experience", "Simpler self-service and more consistent support reduce user effort."),
         ("target", "More proactive operations", "Predictive insights help identify risks earlier and act before service is impacted.")],
    plat_label="ITSM platforms and tools we work with",
    platforms=["ServiceNow", "Zoho", "BMC Helix", "Freshservice", "Microsoft", "Slack", "Zendesk", "PagerDuty"])
D["cx"] = dict(
    file="cx.html", parent=("offerings.html", "Offerings"), name="Customer Experience", short="CX", visual=V.v_cx, mini="cx",
    tile_tag="Every interaction, elevated",
    tile_desc="Connected journeys and insight that deliver premium experiences, driving loyalty and growth.",
    h1='Turn every interaction into <span class="r">loyalty, advocacy and growth.</span>',
    lead="We connect data, journeys, channels, platforms and people behind every touchpoint to anticipate needs and deliver consistent, personalized experiences.",
    what_h="Fix the moments that matter most.", what_p="Four disciplines that connect what customers feel to the systems behind it.",
    what=[("Experience Design", "Map the customer journey and fix the moments that matter most."),
          ("CX Platforms", "CRM, contact center and digital engagement, implemented well for a consistent experience."),
          ("Insight & Personalization", "Unified data that drives the next best action."),
          ("Service Excellence", "AI-assisted agents, knowledge and self-service that get it right the first time.")],
    steps_h="Listen first, then build.", steps_p="Experience programs start with evidence and end with measured improvement.",
    steps=[("Listen", "Gather feedback, data and journey evidence."), ("Design", "Define target experience and the business case."),
           ("Build", "Implement platforms, integrations and automations."), ("Optimize", "Measure satisfaction and keep improving.")],
    get_h="Turning every interaction into insight. Every insight into value.", get_p="What customers notice, and what the business sees.",
    get=[("network", "Seamless journeys", "Consistent interactions across channels and touchpoints."),
         ("spark", "Personalized experiences", "Every interaction shaped by customer context, preferences and needs."),
         ("leaf", "Lower customer effort", "Simpler journeys with fewer handoffs and repetitions."),
         ("bolt", "Faster resolution", "AI-assisted service and self-service resolve needs quicker."),
         ("shield", "Stronger loyalty", "Better experiences build trust and lasting relationships."),
         ("chart", "Growth & advocacy", "Stronger engagement supports retention, advocacy and growth.")],
    plat_label="CX platforms and tools we work with",
    platforms=["Salesforce", "Microsoft", "Zoho", "Adobe Experience Cloud", "Twilio", "Genesys", "Zendesk", "HubSpot", "Qualtrics"])
D["dw"] = dict(
    file="digital-workplace.html", parent=("offerings.html", "Offerings"), name="Digital Workplace", short="Digital Workplace", visual=V.v_dw, mini="dw",
    tile_tag="Work, without friction",
    tile_desc="A secure and seamless workplace that improves how people connect, work and experience technology.",
    h1='Work designed around people, <span class="r">built for productivity.</span>',
    lead="We help organizations create connected digital workplaces where collaboration, service, knowledge, devices, AI and intelligence work around the employee, making every day work simpler and more productive.",
    what_h="Everything that shapes a day at work.", what_p="Four building blocks, designed as one connected employee experience.",
    what=[("Modern collaboration", "Messaging, meetings, documents and knowledge brought together on platforms your people already know."),
          ("Employee service portal", "One front door for IT, HR and facilities requests, with intelligent routing and self-service."),
          ("Device & endpoint experience", "Secure, well-managed devices with support that resolves issues before they interrupt work."),
          ("Intelligent workplace", "Copilots and agents that answer questions, automate requests and personalize each employee's day.")],
    steps_h="Rolled out in waves, adopted by people.", steps_p="A workplace only works when people use it, so adoption is part of every stage.",
    steps=[("Assess", "Understand how people work today and where friction sits."), ("Design", "Define the target employee experience and platform choices."),
           ("Deploy", "Roll out platforms, portals and automation in managed waves."), ("Adopt", "Train, measure and keep improving based on real usage.")],
    get_h="A workplace people actually enjoy using.", get_p="Outcomes we design for, measured against targets set up front.",
    get=[("bolt", "Faster support", "Requests resolved quickly with less back-and-forth."), ("chart", "Higher productivity", "Less time lost to tools, searching and waiting."),
         ("users", "Better employee experience", "One consistent experience across IT, HR and facilities."), ("shield", "Consistent security", "Access and data protected without slowing people down."),
         ("cog", "Less tool sprawl", "Fewer overlapping tools and lower running costs."), ("check", "Measurable adoption", "Clear usage and satisfaction data to guide improvement.")],
    plat_label="Digital workplace platforms we work with",
    platforms=["Microsoft", "Google Cloud", "Zoho", "ServiceNow", "Slack", "Zoom", "Okta", "Jamf"])
D["consulting"] = dict(
    file="consulting.html", parent=("capabilities.html", "Capabilities"), name="Consulting", short="Consulting", visual=V.v_consult, photo="sticky-notes",
    tile_desc="Technology and operating-model advice tied to financial outcomes.",
    h1='Strategy you can <span class="r">actually execute.</span>',
    lead="Technology and operating-model advice tied to financial outcomes. We clarify the decision, build the case and map the path, then stay close while it gets done.",
    what_h="Advice across the decisions that matter.", what_p="Independent guidance across the choices that shape how your enterprise runs.",
    what=[("Digital & AI strategy", "A prioritized roadmap linking technology bets to business results."),
          ("Vendor selection", "Unbiased evaluation and negotiation across platforms and partners."),
          ("Process & operating model", "Redesign how work flows across finance, supply chain and service."),
          ("Change & adoption", "People-first planning so new systems and ways of working stick.")],
    steps_h="From first conversation to first delivery wave.", steps_p="Every engagement follows the same four stages.",
    steps=[("Listen", "Interview stakeholders and review the current state."), ("Frame", "Define the problem, options and success measures."),
           ("Recommend", "Present a costed, sequenced plan with clear trade-offs."), ("Enable", "Support leaders through decisions and the first delivery wave.")],
    get_h="Deliverables you can act on Monday.", get_p="Every consulting engagement ends with tangible work product, not slideware.",
    get=[("map", "Roadmap", "A sequenced plan with owners and milestones."), ("chart", "Business case", "Costs, benefits and risk in plain numbers."),
         ("doc", "Vendor scorecards", "Transparent comparison against your requirements."), ("cog", "Target operating model", "Roles, processes and governance defined."),
         ("users", "Change plan", "Communication, training and adoption tactics."), ("shield", "Risk register", "Known risks with mitigations and triggers.")],
    plat_label="Frameworks and methods we use",
    platforms=["ITIL 4", "TOGAF", "Prince2", "Agile / SAFe", "COBIT", "Lean Six Sigma", "ADKAR", "Value stream mapping", "OKRs"])
D["services"] = dict(
    file="services.html", parent=("capabilities.html", "Capabilities"), name="Services", short="Services", visual=V.v_services, photo="dev-team",
    tile_desc="Implementation, integration and managed support from certified teams.",
    h1='Delivery and run, <span class="r">handled.</span>',
    lead="Implementation, integration and managed support from certified teams, so your platforms stay stable, secure and continuously improving.",
    what_h="Hands-on delivery, then steady-state operations.", what_p="From first configuration to the day-to-day running of your platforms.",
    what=[("Implementation", "Design, configure and launch your platforms on a proven delivery method."),
          ("Integration", "Connect ERP, service and customer systems through reliable interfaces."),
          ("Managed support", "Tiered support and monitoring against agreed service levels."),
          ("Optimization", "Regular releases, tuning and enhancements that keep value growing.")],
    steps_h="From mobilization to run.", steps_p="Short build cycles, a managed transition and clear service levels once live.",
    steps=[("Mobilize", "Set up the team, governance and plan."), ("Build", "Configure, integrate and test in short cycles."),
           ("Transition", "Train users, cut over and stabilize."), ("Run", "Operate, support and improve against service levels.")],
    get_h="Service you can measure.", get_p="Clear commitments, transparent reporting and a team that knows your landscape.",
    get=[("check", "Defined SLAs", "Response and resolution targets in writing."), ("chart", "Monthly reporting", "Performance, risks and improvement ideas."),
         ("users", "Named team", "Consistent people who know your business."), ("shield", "Security first", "Access, audit and data-protection controls."),
         ("cog", "Continuous improvement", "A standing backlog of enhancements."), ("doc", "Full documentation", "Runbooks and knowledge you own.")],
    plat_label="Delivery tools and platforms",
    platforms=["ServiceNow", "Azure DevOps", "GitHub", "Jenkins", "Terraform", "Datadog", "Splunk", "Zoho"])
D["partnerships"] = dict(
    file="partnerships.html", parent=("capabilities.html", "Capabilities"), name="Partnerships", short="Partnerships", visual=V.v_partners, photo="handshake",
    tile_desc="A certified ecosystem of platform vendors and specialist firms.",
    h1='An ecosystem <span class="r">on your side.</span>',
    lead="We work alongside leading enterprise platform vendors and specialist firms, and bring the right ones into each engagement so you get depth without the sprawl.",
    what_h="Alliances that make projects better.", what_p="Partnerships are only useful when they improve your outcome. Ours are built around that.",
    what=[("Platform alliances", "Working relationships with the vendors behind your core systems."),
          ("Certified expertise", "Consultants certified on the platforms we recommend and deliver."),
          ("Joint solutions", "Pre-built accelerators and reference architectures with partners."),
          ("Co-innovation", "Pilots and early access to new platform capabilities.")],
    steps_h="Aligned from day one.", steps_p="However many partners join, you deal with one accountable lead.",
    steps=[("Align", "Match your goals to the right partner capabilities."), ("Certify", "Ensure the team holds current platform credentials."),
           ("Co-build", "Deliver together under one accountable lead."), ("Grow", "Share learning and extend into new use cases.")],
    get_h="A network, with one point of accountability.", get_p="We stay your single lead, whichever partners join the work.",
    get=[("shield", "Vendor-neutral advice", "We recommend what fits, not what we resell."), ("users", "Right-sized teams", "Specialists on demand, not permanent overhead."),
         ("bolt", "Faster starts", "Accelerators and templates from partner ecosystems."), ("check", "Aligned delivery", "One plan, one governance, one lead."),
         ("chart", "Better commercial terms", "Partner programs that benefit you."), ("map", "Roadmap access", "Early insight into platform direction.")],
    plat_label="Technology partner ecosystem",
    platforms=["ServiceNow", "SAP", "Microsoft", "Oracle", "Salesforce", "Workday", "Zoho", "AWS", "Google Cloud", "OpenAI", "Anthropic"])
OFFER_KEYS = ["ai", "erp", "itsm", "cx", "dw"]
CAP_KEYS = ["consulting", "services", "partnerships"]


def art_for(d):
    if "mini" in d:
        return V.mini(d["mini"])
    return f'{photo(d["photo"])}'


def tile_for(d, photo_art=False):
    art_html = f'{photo(d["photo"])}' if "photo" in d else V.mini(d["mini"])
    cls = " ph" if "photo" in d else ""
    tag = f'<em class="tg">{d["tile_tag"]}</em>' if d.get("tile_tag") else ''
    return f'<a class="tile" href="{d["file"]}"><div class="art{cls}">{art_html}</div><div class="tb"><span class="k">{d["short"]}</span><h3>{d["name"]}</h3>{tag}<p>{d["tile_desc"]}</p><span class="more">Explore {ARROW}</span></div></a>'


def emph(*parts):
    return '<div class="emph rv">' + '<i></i>'.join(f'<span>{p}</span>' for p in parts) + '</div>'


def get_block(kicker, h, p, items):
    return '<section><div class="wrap">' + sh(kicker, h, p) + '<div class="inds c3" data-stagger>' + ''.join(
        f'<div class="ind">{icon(i)}<h3>{t}</h3><p>{x}</p></div>' for i, t, x in items) + '</div></div></section>'


def steps_block(kicker, h, p, steps, tag=None):
    t = f'<p class="flowline rv">{tag}</p>' if tag else ''
    return '<section class="navy"><div class="wrap">' + sh(kicker, h, p) + proc(steps) + t + '</div></section>'


def explore_block(d, keys):
    others = [D[k] for k in keys if k != d_key(d)]
    par = d["parent"]
    return '<section class="paper"><div class="wrap">' + sh("Explore further", f'Other {par[1].lower()} to explore.', "Each one stands alone, and together they close the gaps between your systems, service and customers.") + \
        f'<div class="tiles" style="grid-template-columns:repeat({len(others)},1fr)" data-stagger>' + ''.join(tile_for(o) for o in others) + '</div></div></section>'


def d_key(d):
    return [k for k, v in D.items() if v is d][0]


def detail_hero(d, h1, lead):
    par = d["parent"]
    return hero(f'<a href="index.html">Home</a> / <a href="{par[0]}">{par[1]}</a> / {d["short"]}', h1, lead, d["visual"]())


def build_detail(key):
    if key == "ai":
        return build_ai()
    if key == "erp":
        return build_erp()
    d = D[key]
    keys = OFFER_KEYS if key in OFFER_KEYS else CAP_KEYS
    b = detail_hero(d, d["h1"], d["lead"])
    b += marquee(d["plat_label"], d["platforms"] * 2)
    b += f'<section id="more"><div class="wrap">{sh("What we do", d["what_h"], d["what_p"])}{rows(d["what"], "c4w")}</div></section>'
    b += steps_block("How we deliver", d["steps_h"], d["steps_p"], d["steps"])
    b += get_block("What you get", d["get_h"], d["get_p"], d["get"])
    b += explore_block(d, keys)
    b += cta_band(f"Ready to talk {d['short']}?", "Tell us the outcome you want. We will tell you honestly how to get there.", "Start a conversation")
    page(d["file"], f'{d["name"]} — ARRON', d["lead"][:150], b)


def build_erp():
    d = D["erp"]
    b = detail_hero(d, 'Enterprise Resource Planning for the <span class="r">AI-Native Enterprise</span>',
                    "We help organizations transform their operational core through ERP strategy, implementation, and modernization. Our approach combines clean-core architecture, connected enterprise data, and embedded AI to create agile businesses that can respond quickly to market shifts and emerging opportunities. Our long-term ambition is to enable AI-native enterprises, where intelligent agents continuously support, optimize, and adapt business processes, allowing organizations ahead of now.")
    b += marquee(d["plat_label"], d["platforms"] * 2)
    b += f'''<section id="more"><div class="wrap"><div class="statement rv">Replacement as a product, not a project. Guidance generated from the system's own definitions. Scenario branches on the live business. Everything replaceable, plus an exit door. One product from AI Agents to several continents, across finance, logistics, operations and regulations.</div></div></section>'''
    b += f'''<section class="paper"><div class="wrap">{sh("What we do", "Evolve core systems to a smarter enterprise.", "From strategy and implementation to run and evolve, we modernize the operational core of the business.")}
<div class="split2" style="align-items:start;margin-bottom:64px"><div><span class="kicker rv" style="color:var(--red)">AI-Native ERP</span><h3 class="rv" style="font:600 clamp(1.5rem,2.6vw,2.1rem)/1.25 var(--fd);color:var(--ink);margin-top:10px">The core that thinks, acts and improves.</h3></div>
<div><p class="lead rv" style="margin-top:0">Traditional ERP records what happened. AI-native ERP helps decide what happens next.</p><p class="rv" data-delay=".15" style="margin-top:16px">Most enterprises add AI on top of their ERP as a separate layer. ARRON builds intelligence into the core itself, so processes can sense, decide and act, with people kept in control.</p></div></div>
<span class="kicker rv">What AI-native ERP delivers</span>
<div class="tiles five" data-stagger style="margin-top:18px">''' + ''.join(f'<div class="kcard"><span class="ic">{icon(i)}</span><h3>{t}</h3><p>{x}</p></div>' for i, t, x in [
        ("cog", "Autonomous Processes", "AI agents run routine work across finance, supply chain, procurement and order-to-cash, from matching and reconciling to replenishing and resolving exceptions."),
        ("chart", "Predictive Operations", "Forecasting and early-warning signals for demand, cash, inventory and supply risk, so the business acts before issues hit."),
        ("spark", "Conversational ERP", "People ask, approve and act in natural language instead of moving between screens and transactions."),
        ("check", "Intelligent Close & Control", "Continuous reconciliation, anomaly detection and automated compliance checks for a faster, cleaner close."),
        ("db", "Connected Data Foundation", "One trusted data layer across ERP and the wider enterprise, which gives AI the context it needs to reason and act.")]) + '</div></div></section>'
    b += steps_block("How we get there", "From transaction to autonomous action.", "Four stages that move each process from assisted to autonomous as trust grows.",
                     [("Assess", "Find the high-value processes and check how ready the data, platform and organization are for AI."),
                      ("Architect", "Design a clean, AI-ready core with clear integration, governance and points where people make the decision."),
                      ("Embed", "Build agents, automation and insight into live ERP processes, whatever the platform."),
                      ("Evolve", "Move each process from assisted to autonomous as trust, controls and adoption grow.")], "From Transaction → Insight → Autonomous Action.")
    b += f'''<section><div class="wrap">{sh("ERP services", "Four services across the ERP lifecycle.", "Choose one, or let us run the whole journey with you.")}''' + rows([
        ("ERP Advisory & Roadmap", "Assess processes, landscape and business priorities to choose the right platform, deployment model and path to value."),
        ("Transformation & Implementation", "Greenfield, brownfield or phased moves to modern cloud ERP on any leading platform, with fit-to-standard processes and clean data migration."),
        ("Intelligent ERP & Integration", "Embed AI, automation and analytics into core processes, and connect ERP smoothly with the wider enterprise landscape."),
        ("Run, Optimize & Evolve", "Application management and continuous improvement that keep the core stable, current and in step with the business.")], "c4w") + '</div></section>'
    b += get_block("What you get", "An ERP that makes the business easier to run.", "Outcomes we design for from the first workshop.", [
        ("bolt", "Operational efficiency", "Simpler processes and fewer manual steps."), ("cog", "Higher productivity", "Automation across core business processes."),
        ("chart", "Better decisions", "Connected data and timely insight for informed action."), ("refresh", "Greater agility", "Processes and platforms that adapt as the business changes."),
        ("shield", "Stronger control", "Better visibility, robust governance and consistent processes."), ("network", "Operational simplicity", "Harmonized processes and connected systems make the business easier to run and scale.")])
    b += explore_block(d, OFFER_KEYS)
    b += cta_band("Ready to build a smarter core?", "Tell us where your ERP is today. We'll help shape where it goes next.", "Start a conversation")
    page(d["file"], "ERP for the AI-Native Enterprise — ARRON", "ARRON helps organizations transform their operational core through ERP strategy, implementation and modernization, with AI built into the core.", b)


def tiles_for(keys):
    cls = " five" if len(keys) == 5 else ""
    return f'<div class="tiles{cls}" data-stagger>' + ''.join(tile_for(D[k]) for k in keys) + '</div>'



# =========================================================== ARRON AURA diagram
ICONS.update({
    "brain": '<path d="M9 4a3 3 0 0 0-3 3v1a3 3 0 0 0-2 2.8A3 3 0 0 0 6 14v1a3 3 0 0 0 3 3h.5V4z"/><path d="M15 4a3 3 0 0 1 3 3v1a3 3 0 0 1 2 2.8A3 3 0 0 1 18 14v1a3 3 0 0 1-3 3h-.5V4z"/>',
    "network": '<circle cx="12" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><path d="M11 7l-5 10M13 7l5 10M7 19h10"/>',
    "cloud": '<path d="M7 18a4 4 0 0 1-.5-7.97A5.5 5.5 0 0 1 17 9.5 4.3 4.3 0 0 1 17 18z"/>',
    "lock": '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "spark": '<path d="M12 3l2 6 6 2-6 2-2 6-2-6-6-2 6-2z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
    "loop": '<path d="M12 12c-2-3-4-4-6-4a4 4 0 0 0 0 8c2 0 4-1 6-4zm0 0c2 3 4 4 6 4a4 4 0 0 0 0-8c-2 0-4 1-6 4z"/>',
    "db": '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v12c0 1.7 3.1 3 7 3s7-1.3 7-3V6M5 12c0 1.7 3.1 3 7 3s7-1.3 7-3"/>',
    "laptop": '<rect x="4" y="5" width="16" height="11" rx="2"/><path d="M2 20h20"/>',
    "leaf": '<path d="M5 19c0-8 5-13 14-14 0 9-5 14-13 14M5 19l7-7"/>',
    "refresh": '<path d="M4 4v6h6M20 20v-6h-6"/><path d="M20 10a8 8 0 0 0-14-3M4 14a8 8 0 0 0 14 3"/>',
})


def _at(ic, title, sub, logo=None):
    top = plogo(logo) if logo else f'<span class="ic">{icon(ic)}</span>'
    name = '' if logo else f'<b>{title}</b>'
    return f'<div class="at">{top}{name}<span>{sub}</span></div>'


def _row(title, desc, tiles, cls="", n=5):
    return f'<div class="ar"><div class="ar-l"><h4>{title}</h4><p>{desc}</p></div><div class="ar-c {cls}" style="--n:{n}">{"".join(tiles)}</div></div>'


def _flow(labels=None, n=5):
    arrow = '<svg viewBox="0 0 14 34" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 2v30M3 6l4-4 4 4M3 28l4 4 4-4"/></svg>'
    cells = ''.join(f'<div>{arrow}{(l if l else "")}</div>' for l in (labels or [""] * n))
    return f'<div class="flow"><div></div><div class="fr" style="--n:{n}">{cells}</div></div>'


def aura_diagram():
    people = _row("People & Experiences", "Empower every user with Artificial Intelligence copilots and intelligent experiences", [
        _at("users", "Employees", "Artificial Intelligence Copilots"), _at("users", "Customers", "Personalized Experiences"), _at("chart", "Leaders", "Insights & Decisions"),
        _at("network", "Partners", "Connected Ecosystem"), _at("globe", "Communities", "Greater Impact")])
    agents = _row("Artificial Intelligence Agents & Digital Workforce", "Autonomous agents that execute, collaborate and deliver outcomes", [
        _at("cog", "Service Agent", "Information Technology | Human Resources | Facilities"), _at("chart", "Finance Agent", "Plan | Analyze | Optimize"),
        _at("users", "Human Resources Agent", "Recruit | Engage | Develop"), _at("spark", "Customer Experience Agent", "Assist | Resolve | Delight"),
        _at("refresh", "Operations Agent", "Monitor | Heal | Optimize"), _at("factory", "Industry Agent", "Domain Specific"),
        '<div class="at more">+ More Specialized Agents</div>'], "agents", 7)
    apps = _row("Enterprise Applications", "Seamless integration across your enterprise ecosystem", [
        _at("", "", "IT Service Management | IT Operations Management | Customer Service Management", "ServiceNow"),
        _at("", "", "Human Capital Management | Finance", "Workday"), _at("", "", "Microsoft 365 | Azure | Dynamics", "Microsoft"),
        _at("", "", "Sales | Service | Marketing", "Salesforce"), _at("", "", "Enterprise Resource Planning | Supply Chain", "SAP"),
        '<div class="at more">+ Other Enterprise Systems</div>'], "", 6)
    caps = [("brain", "Reasoning<br>Engine"), ("network", "Agent<br>Orchestration"), ("cog", "Workflow<br>Automation"), ("chart", "Real-time<br>Insights"), ("target", "Decision<br>Intelligence"), ("loop", "Continuous<br>Learning")]
    core = f'''<div class="ar"><div class="ar-l"><h4>ARRON AURA Intelligence Layer</h4><p>Reasoning, orchestration and intelligence at the core</p></div>
<div class="core"><div class="core-top"><img src="assets/img/mark.png" alt=""><div><h4>ARRON <em>AURA</em><sup>™</sup></h4><span>ARTIFICIAL INTELLIGENCE UNIFIED REASONING ARCHITECTURE</span></div></div>
<div class="core-caps">{''.join(f'<div>{icon(i)}<span>{l}</span></div>' for i, l in caps)}<div class="out">From Data<br>to Decisions<br>to Impact</div></div></div></div>'''
    data = _row("Data & Knowledge Foundation", "Unified, real-time access to all enterprise knowledge", [
        _at("db", "Structured Data", "Enterprise Resource Planning, Customer Relationship Management, Human Resources, IT Service Management"), _at("doc", "Unstructured Data", "Documents, Email, Content"),
        _at("brain", "Enterprise Knowledge", "Policies, Manuals, Expertise"), _at("bolt", "Real-time Data", "Events, Internet of Things, Logs"), _at("globe", "External Data", "Market, Industry, Web")])
    gov = _row("Governance & Security", "Responsible Artificial Intelligence for a trusted and compliant enterprise", [
        _at("shield", "Security", "Zero Trust"), _at("lock", "Compliance", "Global Standards"), _at("shield", "Responsible Artificial Intelligence", "Ethical & Transparent"),
        _at("lock", "Privacy", "Data Protection"), _at("users", "Risk Management", "Identify | Monitor | Mitigate")], "gov")
    infra = _row("Infrastructure & Cloud", "Scalable, secure and resilient by design", [
        _at("cloud", "Multi-Cloud", "Azure | AWS | Google Cloud"), _at("cloud", "Hybrid & On-Premises", "Flexible Deployment"), _at("server", "Scalable Architecture", "High Performance"),
        _at("shield", "Resilient & Secure", "Business Continuity"), _at("leaf", "Sustainable", "A Greener Tomorrow")], "gov")
    return f'''<div class="aura rv" id="aura"><div class="aura-head"><h3>ARRON <em>AURA</em><sup>™</sup></h3><span class="sub">ARTIFICIAL INTELLIGENCE UNIFIED REASONING ARCHITECTURE</span><p>A unified intelligence layer for the Autonomous Enterprise</p></div>
{people}{_flow()}{agents}{_flow(["Execute", "Collaborate", "Learn", "Adapt", "Deliver Outcomes"])}{apps}{_flow(n=6)}{core}{_flow(n=5)}{data}{gov}{infra}
<div class="aura-foot"><b>INTELLIGENCE EVERYWHERE. IMPACT FASTER.</b><span>People + Artificial Intelligence Agents + Data + Applications = A More Human, Autonomous Enterprise</span></div></div>'''


def aura_mini():
    def row(title, chips):
        return f'<div class="am"><div class="t">{title}</div><div class="c">{"".join(f"<span>{c}</span>" for c in chips)}</div></div>'
    return f'''<a class="amini rv" href="ai.html#aura" data-delay=".5" style="display:block"><div class="am-h"><b>ARRON <em>AURA</em>™</b><span>ARTIFICIAL INTELLIGENCE UNIFIED REASONING ARCHITECTURE</span></div>
{row("People & Experiences", ["Employees", "Customers", "Leaders", "Partners", "Communities"])}
{row("Artificial Intelligence Agents", ["Service", "Finance", "Human Resources", "Customer Experience", "Operations", "Industry"])}
{row("Enterprise Applications", ["ServiceNow", "Workday", "Microsoft", "Salesforce", "SAP"])}
<div class="am core">ARRON AURA INTELLIGENCE LAYER<small>Reasoning · Orchestration · Automation · Insights · Decisions · Learning</small></div>
{row("Data & Knowledge Foundation", ["Structured", "Unstructured", "Knowledge", "Real-time", "External"])}
{row("Governance & Security", ["Security", "Compliance", "Responsible AI", "Privacy", "Risk"])}
{row("Infrastructure & Cloud", ["Multi-Cloud", "Hybrid", "Scalable", "Resilient", "Sustainable"])}</a>'''


def build_ai():
    d = D["ai"]
    lead = "From augmenting people to autonomously orchestrating work, ARRON embeds AI across the enterprise to accelerate innovation, elevate decisions and reimagine customer and employee experiences."
    b = hero('<a href="index.html">Home</a> / <a href="offerings.html">Offerings</a> / AI / Super Intelligence',
             'AI built for impact, <span class="r">architected for autonomy.</span>', lead + ' <b style="color:#fff">Built AI-Native. Designed for Ahead of Now.</b>', V.v_ai())
    b += marquee(d["plat_label"], d["platforms"] * 2)
    b += f'''<section id="more"><div class="wrap">{sh("What we do", "From AI potential to enterprise impact.", "AI capabilities that turn data, knowledge and workflows into better decisions, smarter actions and new experiences.")}''' + rows([
        ("Generative AI", "Transform how people create, discover and interact with enterprise knowledge through contextual AI experiences."),
        ("Agentic & Autonomous AI", "Build AI systems that reason, coordinate and act across workflows with increasing levels of autonomy."),
        ("AI Engineering", "Design, build and integrate production-ready AI across enterprise applications, data and processes."),
        ("Decision Intelligence", "Combine data, context and AI to surface insights, guide decisions and trigger timely action.")], "c4w") + '</div></section>'
    b += f'''<section class="paper"><div class="wrap">{sh("AI-Native by design", "Traditional enterprises bolt AI onto existing systems. ARRON takes a fundamentally different approach.", "We design AI-native architectures that embed intelligence into the core of business operations, enabling autonomous decision-making, continuous learning, and seamless collaboration between people, processes, and AI from day one.")}
<div class="rv" style="padding:34px 40px;border-radius:24px;background:#fff;border-left:4px solid var(--red);max-width:900px"><span class="kicker" style="margin-bottom:12px">Definition</span><h3 style="font-size:1.35rem;margin-bottom:12px">What is AI-Native Architecture?</h3><p style="color:var(--text)">AI-native architecture is an enterprise framework where AI agents, business applications, automation, and data operate as a unified intelligence ecosystem. Every layer is designed to enable intelligent orchestration, predictive insights, adaptive workflows, and autonomous execution at scale.</p></div></div></section>'''
    b += f'''<section id="aura-sec"><div class="wrap">{sh("Introducing ARRON AURA™", "Artificial Intelligence Unified Reasoning Architecture", "ARRON AURA is our AI-native enterprise platform that connects intelligent agents, enterprise systems, data, and human expertise to create a unified operational intelligence layer across the organization.")}{aura_diagram()}</div></section>'''
    caps = [("brain", "Adaptive AI & Agent Ecosystem", "AI agents and emerging autonomous systems that reason, coordinate and act across enterprise tasks and functions."),
            ("network", "Intelligent Enterprise Workflows", "Orchestration and automation that connect AI, people, applications and processes around end-to-end outcomes."),
            ("db", "Data & Decision Intelligence", "A connected data and knowledge foundation that turns enterprise context into real-time insight and better-informed action."),
            ("refresh", "Autonomous Operations", "Adaptive operations that detect, respond, optimize and increasingly self-correct with appropriate controls."),
            ("users", "Human + AI Experience", "AI copilots, agents and contextual experiences that augment people across work, service and decision-making.")]
    b += '<section class="paper"><div class="wrap">' + sh("What AURA delivers", "One framework. Connected enterprise intelligence.", "AURA brings the capabilities required to connect AI, data, workflows, enterprise systems and people, from reasoning and orchestration through action and continuous improvement.") + \
         '<div class="tiles five" data-stagger>' + ''.join(f'<div class="kcard"><span class="ic">{icon(i)}</span><h3>{ti}</h3><p>{tx}</p></div>' for i, ti, tx in caps) + '</div></div></section>'
    pil = [("AI Agents", "Purpose-built digital workers that automate processes, execute actions, and drive intelligent outcomes."),
           ("Enterprise Platforms", "Seamless integration across ServiceNow, Workday, Microsoft, Salesforce, SAP, and other enterprise ecosystems."),
           ("Data & Knowledge Fabric", "Unified access to structured data, unstructured content, enterprise knowledge, and real-time insights."),
           ("Governance & Security", "Responsible AI frameworks delivering transparency, compliance, privacy, security, and trust."),
           ("Continuous Intelligence", "Adaptive systems that learn, evolve, and improve through every interaction and outcome.")]
    b += '<section class="navy"><div class="wrap">' + sh("The ARRON Architecture Pillars", "Built on foundations that scale with what's next.", "Five foundations designed to keep enterprise AI connected, governed and ready to evolve.") + \
         '<div class="pillars" data-stagger>' + ''.join(f'<div class="pillar"><span class="n">{i+1:02d}</span><h3>{ti}</h3><p>{tx}</p></div>' for i, (ti, tx) in enumerate(pil)) + '</div></div></section>'
    b += steps_block("How we deliver", "From ambition to AI that works.", "A structured path to take AI from opportunity to enterprise adoption, with scalability, trust and measurable value built in.",
                     [("Assess", "Identify high-value opportunities and understand data, technology, governance and organizational readiness."),
                      ("Architect", "Define the AI-native architecture, experience, integrations, controls and human decision points."),
                      ("Engineer", "Build and integrate AI, agents and automation into enterprise applications and workflows."),
                      ("Scale", "Operationalize, govern and evolve AI as adoption grows and technology advances.")], "From Data → Decision → Impact.")
    b += get_block("What you get", "AI that moves from promise to performance.", "Outcomes focused on turning AI investment into enterprise value, with trust and control built in.", [
        ("chart", "Value at scale", "Move beyond isolated AI success to meaningful impact across functions and the enterprise."),
        ("bolt", "Faster, stronger decisions", "Help people act sooner and with greater confidence when opportunities and issues emerge."),
        ("cog", "Higher productivity", "Reduce effort, delay and repetitive work so people can focus on where they add the most value."),
        ("spark", "Better experiences", "Make customer and employee interactions simpler, faster and more relevant."),
        ("refresh", "More resilient operations", "Respond faster to change, reduce disruption and strengthen operational continuity."),
        ("shield", "Autonomy with control", "Progress toward greater enterprise autonomy while retaining governance, security and human oversight.")])
    b += explore_block(d, OFFER_KEYS)
    b += cta_band("Ready to move beyond AI experimentation?", "Tell us where you want AI to create impact. We'll help shape the path forward.", "Start a conversation")
    page(d["file"], "AI / Super Intelligence — ARRON AURA | ARRON Technologies", "AI built for impact, architected for autonomy. Meet ARRON AURA, our AI-native enterprise platform.", b)


# =========================================================== Products (Product as a Service)
PRODUCTS = [
    dict(no="01", slug="arron-ai", file="arron-ai.html", name="ARRON AI", tag="Enterprise-grade agentic AI for customer and employee experience",
         h1='Agentic AI for <span class="r">customer and employee experience.</span>',
         desc="ARRON AI is an enterprise-grade Agentic AI platform that automates customer experience (CX) and employee experience (EX) interactions across chat, voice, email, and social channels.",
         feats=[("Chat", "Automated CX and EX interactions over chat."), ("Voice", "Automated CX and EX interactions by voice."), ("Email", "Automated CX and EX interactions over email."), ("Social channels", "Automated CX and EX interactions on social channels.")],
         vis=V.v_prod_arron, flip=False, photo="dashboard"),
    dict(no="02", slug="record-vault-ai", file="record-vault-ai.html", name="Record Vault AI", tag="AI-powered evidence vault",
         h1='An AI-powered <span class="r">evidence vault.</span>',
         desc="Record Vault AI is an AI-powered evidence vault for securely managing family litigation documents, records, and case history.",
         feats=[("Documents", "Family litigation documents, securely managed in one place."), ("Records", "Records kept organized and protected."), ("Case history", "The full case history, ready when you need it.")],
         vis=V.v_prod_vault, flip=True, photo="laptop-dark"),
    dict(no="03", slug="connect-ai", file="connect-ai.html", name="Connect AI", tag="AI for nonprofit and volunteer organizations",
         h1='AI that grows the impact of <span class="r">nonprofits and volunteer groups.</span>',
         desc="Connect AI empowers nonprofit and volunteer organizations with AI-driven tools to grow their impact, engage communities, and strengthen member participation.",
         feats=[("Grow impact", "AI-driven tools that extend what your organization can achieve."), ("Engage communities", "AI-driven tools to reach and engage the people you serve."), ("Member participation", "Tools that strengthen participation across your membership.")],
         vis=V.v_prod_connect, flip=False, photo="highfive"),
]


def demo_link(name):
    return MAILTO.replace("Enquiry%20from%20the%20ARRON%20website", "Request%20a%20demo%3A%20" + name.replace(" ", "%20"))


def product_tile(p):
    return f'<a class="tile" href="{p["file"]}"><div class="art">{p["vis"]()}</div><div class="tb"><span class="k">Product {p["no"]}</span><h3>{p["name"]}</h3><p>{p["tag"]}</p><span class="more">Explore {ARROW}</span></div></a>'


def build_products():
    b = hero('<a href="index.html">Home</a> / Products', 'Products built AI-native, <span class="r">delivered as a service.</span>',
             "We design, build and run software with AI at its core, then operate it as a subscription-style service with continuous releases, so you get outcomes without carrying the engineering burden.", V.v_product())
    b += marquee("Technology we build with", ["Python", "TypeScript", "Kubernetes", "Microsoft", "AWS", "Google Cloud", "PostgreSQL", "Snowflake", "OpenAI", "Anthropic"] * 2)
    b += f'<section id="more"><div class="wrap">{sh("Our products", "Three products, one delivery model.", "From enterprise agents to purpose-built tools for people and communities.")}<div class="tiles" data-stagger>' + ''.join(product_tile(p) for p in PRODUCTS) + '</div></div></section>'
    b += '<section class="paper"><div class="wrap">' + sh("Product as a Service", "A product, not a project.", "From first idea to a live product, with the team that built it staying to run it.") + rows([
        ("Product discovery & design", "Validate the problem, the users and the value before building."),
        ("AI-native engineering", "Software designed around models and agents from the first line."),
        ("Hosted & operated", "We run the platform, security and uptime on your behalf."),
        ("Continuous releases", "Regular improvements shaped by real usage and your feedback.")], "c4w") + '</div></section>'
    b += get_block("What you get", "Subscription-style delivery that keeps improving after launch.", "Outcomes of buying a product instead of commissioning a build.", [
        ("bolt", "Fast time to value", "Working software in weeks, not quarters."), ("cog", "No platform burden", "We handle hosting, scaling and security."),
        ("chart", "Usage-led roadmap", "Features driven by data, not guesswork."), ("shield", "Enterprise-grade controls", "Governance for AI and data from day one."),
        ("users", "Embedded team", "Product, design and engineering in one squad."), ("check", "Predictable cost", "A simple recurring fee against agreed outcomes.")])
    b += cta_band("Want to see a product in action?", "Tell us which one interests you and we will arrange a demo.", "Request a demo", MAILTO.replace("Enquiry%20from%20the%20ARRON%20website", "Request%20a%20demo"))
    page("products.html", "Products — Product as a Service | ARRON", "ARRON AI, Record Vault AI and Connect AI: AI-native products delivered as a service.", b)


def build_product(p):
    b = hero(f'<a href="index.html">Home</a> / <a href="products.html">Products</a> / {p["name"]}', p["h1"], p["desc"], p["vis"](),
             cta_html=f'<div class="hero-cta rv" data-delay=".5"><a class="btn btn-red" href="{demo_link(p["name"])}">Request a demo {ARROW}</a><a class="btn btn-ghost" href="#more">What it covers</a></div>')
    icons = ["chat", "voice", "email", "globe"]
    b += f'<section id="more"><div class="wrap">{sh(f"Product {p["no"]}", p["tag"] + ".", "Delivered as a service: we host it, run it and keep improving it.")}' + rows(p["feats"], "c4w" if len(p["feats"]) == 4 else "c3") + '</div></section>'
    others = [q for q in PRODUCTS if q is not p]
    b += '<section class="paper"><div class="wrap">' + sh("Explore further", "More from ARRON Products.", "Each product is delivered as a service, with continuous releases.") + \
         f'<div class="tiles" style="grid-template-columns:repeat(2,1fr)" data-stagger>' + ''.join(product_tile(q) for q in others) + '</div></div></section>'
    b += cta_band(f"Interested in {p['name']}?", "Tell us about your use case and we will set up a demo.", "Request a demo", demo_link(p["name"]))
    page(p["file"], f'{p["name"]} — ARRON', p["desc"][:150], b)


# =========================================================== HOME
def build_home():
    b = f'''<section class="hero home-hero"><div class="wrap">
<div class="tagpill rv"><i></i>ARRON Technologies · Ahead of Now</div>
<h1 data-split>Building AI-native enterprises, <span class="r">ahead of now.</span></h1>
<p class="lead rv" data-delay=".4">ARRON Technologies is an AI-ready technology company building the future enterprise on AI-native foundations. We help organizations transform operations, elevate customer and employee experiences, and accelerate growth through AI, automation, enterprise platforms, and intelligent services designed for what's ahead of now.</p>
<div class="hero-cta rv" data-delay=".55"><a class="btn btn-red" href="about.html#contact">Talk to us {ARROW}</a><a class="btn btn-ghost" href="ai.html#aura">Explore ARRON AURA™</a></div>
<div class="hero-stats rv" data-delay=".7"><div><b>100+</b><span>Projects delivered</span></div><div><b>5</b><span>AI-native applications</span></div><div><b>Up to 30%</b><span>Operational cost savings</span></div><div><b>25+ yrs</b><span>Combined experience</span></div></div>
{aura_mini()}</div></section>'''
    b += marquee()
    b += f'''<section id="who"><div class="wrap split2"><div><span class="kicker rv">Who are we</span><h2 data-split>Operating ahead of now.</h2>
<p class="lead rv" data-delay=".2">ARRON Technologies exists to help organizations operate ahead of now. As an AI-ready technology company, we help businesses evolve into AI-native enterprises through intelligent technology, modern platforms, and human ingenuity.</p>
<p class="rv" data-delay=".25" style="margin-top:18px">Our team of seasoned industry consultants brings proven experience designing and delivering solutions that drive operational efficiency, reduce costs, enhance customer and employee experiences, and create measurable business value.</p>
{emph("AI-Native by design", "Built for what comes next.")}
<a class="more rv" style="margin-top:34px" href="about.html">More about ARRON {ARROW}</a></div>
<div class="collage rv rv-r"><div class="c1">{photo("team-room", "Consultants working with a client team")}</div><div class="c2">{photo("dashboard", "Analytics dashboard")}</div>
<div class="badge"><b>25+ years</b><span>of combined experience in technology leadership and transformation</span></div></div></div></section>'''
    b += f'''<section id="intro" class="paper"><div class="wrap"><div class="center-head"><span class="kicker rv">What we believe</span><h2 data-split>What leads tomorrow must be built differently today.</h2></div>
<div class="split2" style="align-items:start;margin-top:48px"><p class="lead rv" style="margin-top:0">We believe enterprises must move beyond traditional transformation to become AI-native, adaptive and continuously evolving. That means reimagining intelligence through AI, modernizing the operational core through ERP, transforming how services run through ITSM, elevating Customer Experience, and creating a Digital Workplace built around people.</p>
<p class="rv" data-delay=".15" style="margin-top:0">By bringing these together with human ingenuity, intelligent automation and data-driven decision-making, enterprises can respond faster, decide better and continuously create new value.</p></div>
<div style="margin-top:44px">{emph("Operate Smarter", "Evolve Faster", "Lead What's Next")}</div></div></section>'''
    b += f'<section id="offer"><div class="wrap">{sh("What we offer", "Five practices. One intelligent enterprise experience.", "Each practice stands on its own. Together they close the gaps between your systems, your people and your customers.")}{tiles_for(OFFER_KEYS)}</div></section>'
    b += f'<section class="paper" id="products"><div class="wrap">{sh("Products", "Product as a Service.", "AI-native products from ARRON, delivered as a service and improved continuously.")}<div class="tiles" data-stagger>' + ''.join(product_tile(p) for p in PRODUCTS) + '</div></div></section>'
    why = [("100+", "Projects delivered", "100+ transformation and technology projects delivered across enterprise platforms, service management, workplace transformation, customer experience, and automation initiatives."),
           ("5", "AI-native applications", "5 AI-native applications successfully designed and delivered, helping organizations accelerate innovation and unlock new business capabilities."),
           ("30%", "Operational cost savings", "Up to 30% operational cost savings achieved through process optimization, automation, AI adoption, and service modernization."),
           ("04", "Deep expertise", "Deep expertise in AI, ERP, ITSM, Digital Workplace, and Customer Experience (CX) to help organizations accelerate transformation and maximize business outcomes."),
           ("05", "Business-first approach", "Business-first approach focused on measurable value, operational efficiency, and sustainable growth."),
           ("06", "AI-ready, AI-native", "AI-ready strategies and AI-native foundations designed to help organizations thrive in the age of intelligent enterprises.")]
    cells = ''
    for i, (m, ti, tx) in enumerate(why):
        if i == 0:
            head = '<span class="metric">100<i>+</i></span>'
        elif i == 1:
            head = '<span class="metric">5</span>'
        elif i == 2:
            head = '<span class="metric"><small style="font-size:.4em;letter-spacing:0;font-weight:500">Up to </small>30<i>%</i></span>'
        else:
            head = f'<span class="n">{m}</span>'
        cells += f'<div>{head}<h3>{ti}</h3><p>{tx}</p></div>'
    b += '<section class="navy" id="why"><div class="wrap">' + sh("Why ARRON", "Enterprise experience. AI-native thinking. Value from day one.", "ARRON combines deep enterprise expertise with a future-ready technology mindset to solve the right problems, move faster from idea to impact, and build solutions designed to evolve.") + \
         f'<div class="why6" data-stagger>{cells}</div><div style="margin:48px 0 0" class="emph-dark">{emph("Practical expertise", "Measurable outcomes", "Built for what's next.")}</div><div class="closing rv"><b>ARRON. Ahead of Now. Building AI-Native Enterprises.</b><div style="margin-top:26px;display:flex;gap:26px;justify-content:center;flex-wrap:wrap"><a class="more" href="proven-experience.html">Proven experience {ARROW}</a><a class="more" href="industry.html">Industries we serve {ARROW}</a></div></div></div></section>'
    nxt = [("STEP 01", "Talk to us", "Reach the team directly by email. A senior consultant will reply within one business day.", "about.html#contact", "Contact us"),
           ("STEP 02", "See how we work", "Understand our consulting, services and partnership models and which fits you.", "capabilities.html", "Capabilities"),
           ("STEP 03", "Explore ARRON AURA", "See how our AI-native architecture connects agents, data and enterprise systems.", "ai.html#aura", "ARRON AURA")]
    b += '<section><div class="wrap">' + sh("What should you do next", "Pick the starting point that fits you.", "No forms to fill and no sales script. Just a useful conversation.") + \
         '<div class="nexts" data-stagger>' + ''.join(f'<a class="nx" href="{h}"><span class="n">{n}</span><b>{t}</b><p>{p}</p><span class="more">{l} {ARROW}</span></a>' for n, t, p, h, l in nxt) + '</div></div></section>'
    b += cta_band("ARRON. Ahead of Now.", "Building AI-Native Enterprises. Tell us where you are headed and we will tell you honestly how to get there.", "Talk to us")
    page("index.html", "ARRON Technologies — Ahead of Now | AI-Native Enterprise Technology", "ARRON Technologies is an AI-ready technology company building AI-native enterprises through AI, ERP, ITSM, Customer Experience and Digital Workplace.", b)


# =========================================================== HUBS
def build_offerings():
    b = hero('<a href="index.html">Home</a> / Offerings', 'Five practices that power <span class="r">the AI-native enterprise.</span>',
             "Intelligence, operations, service and experience. Start with one, or run them as a single connected program.", V.v_stack())
    b += marquee()
    b += f'<section id="more"><div class="wrap">{sh("What we offer", "Five practices. One intelligent enterprise experience.", "Each practice has its own team, playbook and platform expertise.")}{tiles_for(OFFER_KEYS)}</div></section>'
    qs = [("ai.html", "We're investing in AI, but the business impact isn't clear", "Turn fragmented AI initiatives into scalable, governed business outcomes.", "AI / SI: AI built for impact, architected for autonomy.", "01"),
          ("erp.html", "Outgrown your ERP, or choosing a new one?", "", "ERP: The right ERP, chosen and delivered right.", "02"),
          ("itsm.html", "Drowning in tickets and missed SLAs?", "", "ITSM: Service built for efficiency, engineered for resilience.", "03"),
          ("cx.html", "Customers leaving between touchpoints?", "", "CX: Turn every interaction into loyalty, advocacy and growth.", "04"),
          ("digital-workplace.html", "Employees losing time to clunky tools?", "", "Digital Workplace: Work designed around people, built for productivity.", "05")]
    b += '<section class="navy"><div class="wrap">' + sh("Start where it hurts", "Bring us the challenge. We'll map the way ahead.", "A shortcut if you know the pain but not the label.") + \
         '<div style="border-top:1px solid rgba(255,255,255,.14)" data-stagger>' + ''.join(
             f'<a href="{h}" class="qrow"><span class="n">{n}</span><b>{q}{f"<small>{s}</small>" if s else ""}</b><span class="a">{a}</span><span class="go">{ARROW}</span></a>' for h, q, s, a, n in qs) + '</div></div></section>'
    b += cta_band("Not sure where to start?", "Bring us the challenge and we will recommend the lightest path to it.")
    page("offerings.html", "Offerings — ARRON | AI, ERP, ITSM, CX & Digital Workplace", "ARRON offerings: Artificial & Super Intelligence, ERP, IT Service Management, Customer Experience and Digital Workplace.", b)


def build_cap():
    b = hero('<a href="index.html">Home</a> / Capabilities', 'However you need us, <span class="r">we plug in.</span>',
             "Advise, deliver or partner. Three ways to work with ARRON, designed around how much of the journey you want us to own.", V.v_ladder())
    b += marquee()
    b += '<section id="more"><div class="wrap">' + sh("Engagement spectrum", "From advice to full ownership.", "Pick the lightest model that gets the job done. You can move along the spectrum as needs change.") + \
         '''<div class="spec rv"><div><span class="lv">You lead</span><h3>Advise</h3><p>Independent guidance and expert oversight while your team drives delivery.</p></div><div><span class="lv">We co-deliver</span><h3>Deliver together</h3><p>Blended teams run programs end to end, with knowledge transfer built in.</p></div><div><span class="lv">We own it</span><h3>Operate</h3><p>Managed services delivered against agreed outcomes, with your platforms kept stable and improving.</p></div></div></div></section>'''
    b += f'<section class="paper"><div class="wrap">{sh("Our capabilities", "Three ways to work with us.", "Each capability has its own page with the detail.")}{tiles_for(CAP_KEYS)}</div></section>'
    b += '<section class="navy"><div class="wrap">' + sh("How an engagement runs", "Clear stages. No surprises.", "Whatever the model, the rhythm is the same.") + \
         proc([("Discover", "Listen, assess and define the outcome and success measures."), ("Design", "Agree architecture, plan and business case."), ("Deliver", "Build in short cycles with visible progress every sprint."), ("Sustain", "Hand over, train and keep improving.")]) + '</div></section>'
    b += cta_band("Find the model that fits.", "We will recommend the lightest engagement that gets the job done.")
    page("capabilities.html", "Capabilities — ARRON | Consulting, Services, Partnerships", "How ARRON works with you: consulting, managed services and technology partnerships.", b)


# =========================================================== INDUSTRY EXPERTISE
INDUSTRIES = {
    "banking": dict(file="banking.html", name="Banking & Financial Services", short="Banking", photo="skyline", icon="bank",
        card="Compliance, resilience and customer trust, with governed AI.",
        h1='Trusted finance, <span class="r">built for what comes next.</span>',
        lead="Banks and financial institutions must modernize while staying compliant and resilient. We help them modernize core and finance platforms, strengthen service operations and bring governed AI into the work, without giving up control.",
        focus=[("Core & finance modernization", "Modern ERP and finance platforms that shorten close cycles and improve reporting and control."),
               ("Compliance & audit readiness", "Auditable change, access and service processes, with evidence captured as the work happens."),
               ("Resilient service operations", "ITSM and automation that keep critical systems available and resolve issues before customers notice."),
               ("Responsible AI", "Governed AI for monitoring, documentation and decision support, with human oversight designed in.")],
        offers=[("ai", "Governed AI for risk signals, monitoring and decision support."), ("itsm", "Audit-ready change and incident management for critical systems."), ("cx", "Simpler onboarding and servicing across every channel.")],
        platforms=["SAP", "Oracle", "ServiceNow", "Microsoft", "Salesforce", "Workday", "AWS", "Google Cloud"]),
    "manufacturing": dict(file="manufacturing.html", name="Manufacturing", short="Manufacturing", photo="dashboard", icon="factory",
        card="Connected plants, planning and supply chains.",
        h1='Connected operations, <span class="r">from plant to planner.</span>',
        lead="Plants, planners and suppliers all depend on the same data. We connect ERP, supply chain and shop-floor systems so manufacturers can plan with confidence, respond to disruption and keep production moving.",
        focus=[("Connected planning & ERP", "One system of record across finance, planning, inventory and production."),
               ("Supply chain visibility", "Inventory, logistics and demand signals brought together for earlier, better decisions."),
               ("Predictive operations", "Forecasting and early-warning signals for demand, maintenance and supply risk."),
               ("Quality & compliance", "Consistent processes and traceable records across plants and suppliers.")],
        offers=[("erp", "A clean-core ERP that connects planning, shop floor and finance."), ("ai", "Predictive and agentic AI for demand, supply and maintenance."), ("itsm", "Reliable service operations for plant and enterprise systems.")],
        platforms=["SAP", "Oracle", "Microsoft", "NetSuite", "Infor", "Epicor", "IFS", "ServiceNow"]),
    "retail": dict(file="retail.html", name="Retail & Consumer", short="Retail & Consumer", photo="highfive", icon="cart",
        card="Omnichannel experience, personalization and demand sensing.",
        h1='One customer, <span class="r">every channel.</span>',
        lead="Customers move between stores, apps, websites and contact centers without thinking about it. We help retail and consumer brands join up data, journeys and operations so every interaction feels consistent and every sale is supported.",
        focus=[("Omnichannel experience", "Consistent service and journeys across stores, digital and contact center."),
               ("Personalization", "Unified customer data that drives the next best action."),
               ("Demand sensing & inventory", "Connected ERP and supply data that keep the right products in the right place."),
               ("Peak-season resilience", "Service and platform operations that hold up when volumes surge.")],
        offers=[("cx", "Connected journeys, CRM and service that customers feel."), ("erp", "Inventory, finance and supply chain on one connected core."), ("ai", "AI for personalization, service and demand sensing.")],
        platforms=["Salesforce", "SAP", "Oracle", "Microsoft", "NetSuite", "Zoho", "Twilio", "Adobe Experience Cloud"]),
    "telecom": dict(file="telecom.html", name="Telecom", short="Telecom", photo="servers", icon="signal",
        card="Proactive service on always-on networks.",
        h1='Service that keeps up with <span class="r">always-on networks.</span>',
        lead="Telecom operators run on scale and uptime. We help them move from reactive to proactive: predicting incidents, routing work intelligently and giving customers a simpler, more connected experience.",
        focus=[("Proactive service assurance", "Event correlation and prediction that find issues before customers do."),
               ("Intelligent incident routing", "AI-assisted triage that gets each issue to the right team faster."),
               ("Customer lifecycle & churn", "Connected data and journeys that improve retention."),
               ("Digital operations", "Modern ERP and service platforms behind billing, field and back-office work.")],
        offers=[("itsm", "AI-assisted service management for network and enterprise operations."), ("cx", "Proactive customer service and retention journeys."), ("ai", "Predictive and agentic AI for network and service operations.")],
        platforms=["ServiceNow", "Salesforce", "Microsoft", "Oracle", "SAP", "AWS", "Google Cloud", "Genesys"]),
    "healthcare": dict(file="healthcare.html", name="Healthcare", short="Healthcare", photo="office", icon="heart",
        card="Access, operations and secure data for care organizations.",
        h1='Care that runs on <span class="r">connected, secure systems.</span>',
        lead="Healthcare organizations need time back for patients and staff, and trust in how data is handled. We help them simplify operations, improve access and apply AI carefully, with privacy and human review built in.",
        focus=[("Patient access & engagement", "Connected journeys and service that make care easier to reach."),
               ("Documentation & operational support", "Governed AI assistants embedded in existing workflows, with human review."),
               ("Secure data & compliance", "Data, access and audit controls designed around privacy and regulatory needs."),
               ("Resilient support for critical systems", "Service management that keeps clinical and operational systems available.")],
        offers=[("ai", "Governed AI for documentation and operational support."), ("dw", "A secure, simple workplace for clinical and administrative staff."), ("itsm", "SLA-driven support for systems that cannot go down.")],
        platforms=["ServiceNow", "Microsoft", "SAP", "Oracle", "Workday", "Salesforce", "AWS", "Google Cloud"]),
}


def ind_tile(i):
    return f'<a class="tile" href="{i["file"]}"><div class="art ph">{photo(i["photo"])}</div><div class="tb"><span class="k">Industry</span><h3>{i["name"]}</h3><p>{i["card"]}</p><span class="more">Explore {ARROW}</span></div></a>'


def build_industry():
    b = hero('<a href="index.html">Home</a> / Industry Expertise', 'Sector knowledge that <span class="r">shortens the learning curve.</span>',
             "Five industries where our consultants have deep, hands-on experience, and the practices we bring to each.", V.v_industries())
    b += marquee("Technology partners across our client work")
    b += '<section id="more"><div class="wrap">' + sh("Industries", "Where we work.", "Choose your sector to see where we help and which practices apply.") + \
         '<div class="tiles five" data-stagger>' + ''.join(ind_tile(i) for i in INDUSTRIES.values()) + '</div></div></section>'
    b += '<section class="paper"><div class="wrap">' + sh("Our approach", "What we bring to every sector.", "The same discipline, applied to the realities of your industry.") + rows([
        ("Sector knowledge", "Consultants who know the regulations, processes and vocabulary of your industry."),
        ("Platform depth", "Certified expertise across the ERP, service and customer platforms the sector runs on."),
        ("AI with governance", "Practical AI use cases with the controls your regulators and customers expect."),
        ("Outcome focus", "Success measures agreed up front and tracked through delivery.")], "c4w") + '</div></section>'
    b += cta_band("Working in one of these sectors?", "We will bring people who have done it before.")
    page("industry.html", "Industry Expertise — ARRON | Banking, Manufacturing, Retail, Telecom, Healthcare", "ARRON's industry expertise across banking and financial services, manufacturing, retail and consumer, telecom and healthcare.", b)


def build_industry_page(key):
    i = INDUSTRIES[key]
    b = hero(f'<a href="index.html">Home</a> / <a href="industry.html">Industry Expertise</a> / {i["short"]}', i["h1"], i["lead"],
             photo_stage(i["photo"], i["name"], "Industry expertise"), "photo")
    b += marquee("Platforms we work with in this sector", i["platforms"] * 2)
    b += f'<section id="more"><div class="wrap">{sh("Where we help", "What we do for " + i["name"] + ".", "Four areas where our teams bring the most value.")}{rows(i["focus"], "c4w")}</div></section>'
    b += '<section class="paper"><div class="wrap">' + sh("Our practices", "How our offerings apply.", "Each practice adapted to the realities of the sector.") + '<div class="inds c3" data-stagger>' + ''.join(
        f'<a class="ind" href="{D[k]["file"]}">{icon({"ai":"brain","erp":"cog","itsm":"server","cx":"users","dw":"laptop"}[k])}<h3>{D[k]["name"]}</h3><p>{t}</p></a>' for k, t in i["offers"]) + '</div></div></section>'
    others = [v for k, v in INDUSTRIES.items() if k != key][:3]
    b += '<section><div class="wrap">' + sh("Explore further", "Other industries we serve.", "Experience from one sector often improves the work in another.") + '<div class="tiles" data-stagger>' + ''.join(ind_tile(o) for o in others) + '</div></div></section>'
    b += cta_band(f"Working in {i['short'].lower()}?", "Tell us what you are trying to achieve and we will bring the right people.")
    page(i["file"], f'{i["name"]} — ARRON', i["lead"][:150], b)


# =========================================================== EMPTY-STATE SECTIONS (insights, proven experience, careers)
def build_soon(file, parent, name, h1, lead, ph, blurb, subject, cta_html=None):
    crumb = f'<a href="index.html">Home</a> / <a href="{parent[0]}">{parent[1]}</a> / {name}'
    b = hero(crumb, h1, lead, photo_stage(ph, name, "Coming soon"), "photo", cta_html=cta_html)
    mail = MAILTO.replace("Enquiry%20from%20the%20ARRON%20website", "Notify%20me%3A%20" + subject.replace(" ", "%20"))
    b += f'''<section id="more"><div class="wrap"><div class="soon rv"><span class="soon-ic">{icon("doc")}</span><span class="kicker">Coming soon</span><h2>Nothing published here yet.</h2>
<p>{blurb}</p><div class="soon-cta"><a class="btn btn-red" href="{mail}">Notify me when it is live {ARROW}</a><a class="btn btn-ghost" href="{parent[0]}">Back to {parent[1]}</a></div></div></div></section>'''
    b += '<section class="paper"><div class="wrap">' + sh("In the meantime", "Explore what is live.", "Start with our practices, or meet the team.") + '<div class="tiles" data-stagger>' + \
         tile_for(D["ai"]) + tile_for(D["erp"]) + f'<a class="tile" href="about.html"><div class="art ph">{photo("team-room")}</div><div class="tb"><span class="k">About ARRON</span><h3>Our Purpose</h3><p>Why ARRON exists and how we work.</p><span class="more">Explore {ARROW}</span></div></a>' + '</div></div></section>'
    page(file, f'{name} — ARRON', lead[:150], b)


def build_soon_hub(file, name, h1, lead, ph, sh_t, items, sub):
    b = hero(f'<a href="index.html">Home</a> / {name}', h1, lead, photo_stage(ph, name, "Being prepared"), "photo")
    b += f'<section id="more"><div class="wrap">{sh(name, sh_t, sub)}<div class="tiles" style="grid-template-columns:repeat({len(items)},1fr)" data-stagger>' + ''.join(
        f'<a class="tile" href="{h}"><div class="art ph">{photo(p)}</div><div class="tb"><span class="k">Coming soon</span><h3>{t}</h3><p>{d}</p><span class="more">Open {ARROW}</span></div></a>' for h, t, d, p in items) + '</div></div></section>'
    b += cta_band("Want to hear when we publish?", "Tell us what you would like to read first and we will let you know.", "Notify me", MAILTO.replace("Enquiry%20from%20the%20ARRON%20website", "Notify%20me%3A%20" + name.replace(" ", "%20")))
    page(file, f'{name} — ARRON', lead[:150], b)


def build_insights():
    build_soon_hub("insights.html", "Our Insights", 'Thinking worth <span class="r">acting on.</span>', "Technology insights, perspectives, playbooks and articles from the ARRON team. This section is being prepared.", "laptop-dark",
                   "Four ways to read us.", [("technology-insights.html", "Technology Insights", "What is changing in enterprise technology, and what to do about it.", "dashboard"),
                                             ("perspectives.html", "Perspectives", "Points of view from our leaders on the AI-native enterprise.", "boardroom"),
                                             ("playbooks.html", "Playbooks", "Practical, step-by-step guides you can put to work.", "sticky-notes"),
                                             ("blog.html", "Blog / Newsletter", "Articles and updates from the ARRON team, plus our newsletter.", "meeting-table")], "We are preparing our first publications.")
    s = [("technology-insights.html", "Technology Insights", ("Technology Insights", 'Enterprise technology, <span class="r">explained.</span>', "Clear, practical analysis of the technology shifts that matter to enterprise leaders.", "dashboard", "We are preparing our first technology insights on AI, ERP, ITSM, customer experience and the digital workplace.")),
         ("perspectives.html", "Perspectives", ("Perspectives", 'Points of view <span class="r">from our leaders.</span>', "How ARRON's leaders see the road from digital transformation to the AI-native enterprise.", "boardroom", "Our leaders' first perspectives are being prepared.")),
         ("playbooks.html", "Playbooks", ("Playbooks", 'Guides you can <span class="r">put to work.</span>', "Practical playbooks for adopting AI, modernizing the core and improving service and experience.", "sticky-notes", "Our first playbooks are being prepared.")),
         ("blog.html", "Blog / Newsletter", ("Blog / Newsletter", 'Notes from <span class="r">the field.</span>', "Articles and updates from the people doing the work at ARRON, delivered to your inbox.", "meeting-table", "Our first articles are being prepared."))]
    for f, n, (nm, h1, lead, ph, blurb) in s:
        sig = None
        if f == "blog.html":
            sig = f'''<div class="hero-signup rv" data-delay=".5"><span class="hs-label">Get the blog and newsletter by email</span>
<form data-demo data-mailto="{EMAIL_1},{EMAIL_2}" data-subject="Subscribe me to the ARRON blog and newsletter" onsubmit="return false"><div class="news"><input type="email" name="email" required placeholder="you@company.com" aria-label="Email address"><button class="btn btn-red" type="submit">Subscribe {ARROW}</button></div></form>
<div class="ok">Your email app should open with the request ready to send. Just press send and we will add you.</div><p class="hs-note">Be first to read our articles when they are published. Free, and you can unsubscribe any time.</p></div>'''
        build_soon(f, ("insights.html", "Our Insights"), nm, h1, lead, ph, blurb, n, sig)


def build_proven():
    build_soon_hub("proven-experience.html", "Proven Experience", 'Results you can <span class="r">point to.</span>', "Client stories, case studies and testimonials. This section is being prepared as we receive client approvals.", "highfive",
                   "Evidence of the work.", [("client-stories.html", "Client Stories", "How clients describe the journey, in their own words.", "team-room"),
                                            ("case-studies.html", "Case Studies", "The challenge, the approach and the outcome.", "boardroom"),
                                            ("testimonials.html", "Testimonials", "What clients say about working with ARRON.", "meeting-table")], "We will publish these once clients have approved them.")
    s = [("client-stories.html", "Client Stories", 'Our clients, <span class="r">in their words.</span>', "Stories of the journeys we have shared with clients.", "team-room", "Client stories will appear here once clients have approved them."),
         ("case-studies.html", "Case Studies", 'The challenge, the approach, <span class="r">the outcome.</span>', "Detailed engagements across AI, ERP, ITSM, customer experience and the digital workplace.", "boardroom", "Case studies will appear here once clients have approved them."),
         ("testimonials.html", "Testimonials", 'What clients <span class="r">say about us.</span>', "Straight feedback from the leaders we have worked alongside.", "meeting-table", "Testimonials will appear here once clients have approved them.")]
    for f, n, h1, lead, ph, blurb in s:
        build_soon(f, ("proven-experience.html", "Proven Experience"), n, h1, lead, ph, blurb, n)


PEOPLE = [
    ("Rajit Mohan", "Growth Accelerator | Digital Solutions & Modern Workplaces", "", "Entrepreneurial executive who advises clients in healthcare, retail, manufacturing, banking and technology on large-scale modernization, digital strategy, automation and AI, and has led large multi-year global deals.", ["Digital workplace", "Cloud", "AIOps"], "Dallas-Fort Worth, Texas", "rajit.jpg", "https://www.linkedin.com/in/rajit-mohan-22197732/"),
    ("Gourav Gupta", "SAP Enterprise Architect", "", "Designs how manufacturing and distribution companies run on SAP, from greenfield S/4HANA implementations to ECC conversions. Sets clean-core direction on SAP BTP and leads SAP Business AI. Certified SAP Enterprise Architect.", ["S/4HANA", "SAP BTP", "Business AI"], "Louisville, Kentucky", "gourav.jpg", "https://www.linkedin.com/in/sap-gourav-gupta/"),
    ("Manjot Sohal", "Oracle HCM Architect", "", "Oracle Human Capital Management architect based in the Dallas-Fort Worth area, helping organizations design and deliver HCM solutions that support their people and processes.", ["Oracle HCM", "Architecture", "HR transformation"], "Dallas-Fort Worth, Texas", "manjot.jpg", "https://www.linkedin.com/in/manjot-sohal-107a22187/"),
    ("Yash Gupta", "AI & Data Science", "", "AI and data science graduate focused on generative AI, analytics and business intelligence, with a foundation in machine learning, Python and web development.", ["GenAI", "Analytics", "Business Intelligence"], "Delhi, India", "yash.jpg", "https://www.linkedin.com/in/yash-gupta-73b9281b1/"),
]
LI_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.07 2.07 0 1 1 0-4.13 2.07 2.07 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>'



def build_consultants():
    stage = photo_stage("team-room", "Senior practitioners on every engagement", "Leadership and consultants")
    b = hero('<a href="index.html">Home</a> / <a href="about.html">About ARRON</a> / Leadership & Consultants', 'The people you <span class="r">will work with.</span>',
             "Practitioners with decades of enterprise delivery behind them, who stay close to clients and to the work.", stage, "photo")
    b += '<section id="more" class="paper"><div class="wrap">' + sh("Leadership & consultants", "Meet the team.", "Profiles of the practitioners who lead our engagements.") + \
         '<div class="people" data-stagger>' + ''.join(f'<article class="person"><div class="ph real">{f'<span class="yrs">{y}</span>' if y else ''}<img src="assets/img/team/{img}" alt="{n}" loading="lazy" width="480" height="480"></div><div class="pi"><h3>{n}</h3><div class="role">{r}</div><p>{bio}</p><div class="chips">{"".join(f"<span>{c}</span>" for c in ch)}</div><div class="loc">{loc}</div><a class="li" href="{url}" target="_blank" rel="noopener noreferrer" aria-label="{n} on LinkedIn">{LI_SVG} LinkedIn profile</a></div></article>' for n, r, y, bio, ch, loc, img, url in PEOPLE) + '</div></div></section>'
    b += f'''<section class="band">{photo("team-laptop", "Team collaborating")}<div class="wrap"><span class="kicker">Join ARRON</span><h2>Do the best work of your career.</h2><p style="margin:20px 0 32px;max-width:48ch;font-size:1.1rem;color:#cfdcff">We hire experienced consultants and architects who want to stay close to clients and to the work.</p><a class="btn btn-red" href="careers.html">Careers at ARRON {ARROW}</a></div></section>'''
    page("consultants.html", "Leadership & Consultants — ARRON", "Meet the ARRON leadership and consultants.", b)


def build_partners():
    b = hero('<a href="index.html">Home</a> / <a href="about.html">About ARRON</a> / Our Partners', 'Strong platforms. <span class="r">Stronger together.</span>',
             "Certified expertise across the enterprise ecosystems our clients already run on, from ERP and service management to cloud and AI.", V.v_partners())
    pl = [("ServiceNow", "IT Service Management"), ("SAP", "Enterprise Resource Planning"), ("Microsoft", "Azure · Dynamics · 365"), ("Oracle", "ERP · Cloud"),
          ("Salesforce", "Customer Relationship Management"), ("Workday", "Human Capital · Finance"), ("NetSuite", "ERP · Cloud"), ("Zoho", "Business applications"),
          ("AWS", "Cloud · Artificial Intelligence"), ("Google Cloud", "Data · Artificial Intelligence"), ("OpenAI", "Generative AI"), ("Anthropic", "Generative AI")]
    b += '<section id="more"><div class="wrap">' + sh("Our partners", "The ecosystem we work across.", "We recommend what fits your needs and bring the right partners into each engagement.") + \
         '<div class="plogos" data-stagger>' + ''.join(f'<div class="plogo">{plogo(n)}<small>{s}</small></div>' for n, s in pl) + '</div>' \
         f'<p style="margin-top:44px"><a class="more" href="partnerships.html">How our partnerships work {ARROW}</a></p></div></section>'
    b += cta_band("Working on one of these platforms?", "Tell us what you run today and where you want to take it.")
    page("partners.html", "Our Partners — ARRON", "The enterprise platform ecosystem ARRON works across.", b)


def build_delivery():
    b = hero('<a href="index.html">Home</a> / <a href="about.html">About ARRON</a> / Delivery Landscape', 'U.S. leadership. <span class="r">Global delivery.</span>',
             "ARRON combines U.S. leadership with global delivery capabilities, giving clients access to experienced consultants, architects, engineers, and transformation specialists.", V.v_offices())
    b += '<section id="more"><div class="wrap">' + sh("Global Delivery, Local Partnership", "Six offices across two countries.", "Headquartered in Dallas, Texas, with delivery teams across the U.S. and India.")
    b += '<div class="offices" data-stagger><div class="ofc"><h3>United States</h3><ul><li class="hq"><i></i>Dallas, Texas <small>Headquarters</small></li><li><i></i>Louisville, Kentucky</li><li><i></i>Houston, Texas</li></ul></div><div class="ofc"><h3>India</h3><ul><li><i></i>National Capital Region (Delhi NCR)</li><li><i></i>Pune</li><li><i></i>Bangalore</li></ul></div></div>'
    b += '<p class="rv" style="margin-top:34px;max-width:80ch;font-size:1.05rem">This distributed presence enables us to deliver the responsiveness of a local partner with the scale, expertise, and innovation capabilities of a global technology organization.</p></div></section>'
    b += cta_band("Need a team close to you?", "Tell us where you operate and we will tell you how we would deliver.")
    page("delivery-landscape.html", "Delivery Landscape — ARRON", "ARRON offices in Dallas, Louisville, Houston, Delhi NCR, Pune and Bangalore.", b)


def build_careers():
    stage = photo_stage("team-laptop", "Join ARRON", "Senior practitioners, real clients, room to grow")
    b = hero('<a href="index.html">Home</a> / Careers', 'Join ARRON. Do the best work <span class="r">of your career.</span>',
             "Join a team where senior practitioners shape the work, learn from each other and stay close to clients.", stage, "photo")
    b += f'<section id="more"><div class="wrap">{sh("Why ARRON", "What it is like to work here.", "A senior team with the ambition of a much larger firm.")}' + rows([
        ("Meaningful work", "AI, ERP, service and experience programs for organizations that depend on them."),
        ("Senior colleagues", "Learn directly from people with decades of delivery experience."),
        ("Funded learning", "Certification support and protected time to build new skills."),
        ("Global team", "Work with colleagues across the U.S. and India.")], "c4w") + '</div></section>'
    mail = MAILTO.replace("Enquiry%20from%20the%20ARRON%20website", "Careers%20at%20ARRON")
    b += f'''<section class="paper"><div class="wrap"><div class="soon rv"><span class="soon-ic">{icon("users")}</span><span class="kicker">Open roles</span><h2>No roles listed right now.</h2><p>We are always glad to hear from experienced consultants, architects and engineers. Send us your profile and tell us what you want to work on, and we will be in touch when a role fits.</p><div class="soon-cta"><a class="btn btn-red" href="{mail}">Send your profile {ARROW}</a></div></div></div></section>'''
    b += '<section class="navy"><div class="wrap">' + sh("How we hire", "A process that respects your time.", "Four steps, usually completed within three weeks.") + \
         proc([("Apply", "Send your profile or a short note."), ("Conversation", "Meet a senior consultant to discuss your experience."), ("Case discussion", "Talk through a real engagement scenario."), ("Offer", "Meet the leadership team and receive your offer.")]) + '</div></section>'
    page("careers.html", "Careers — Join ARRON", "Careers at ARRON: join a team building AI-native enterprises.", b)



def build_about():
    b = hero('<a href="index.html">Home</a> / About ARRON / Our Purpose', 'Building the Future Enterprise. <span class="r">Today.</span>',
             "Headquartered in Dallas, Texas, ARRON Technologies is an AI-ready technology consulting and services company dedicated to helping organizations operate ahead of now.", V.v_offices())
    b += '''<section id="more" class="navy"><div class="wrap split2" style="align-items:start"><div><span class="kicker rv">Our Purpose</span><h2 class="pull" data-split>We believe the next generation of successful enterprises will not simply use AI. They will be built around it.</h2></div>
<div><p class="lead rv" style="margin-top:0;color:#c3cee6">ARRON exists to help organizations create that future by building AI-native foundations that empower people, accelerate innovation, and create sustainable competitive advantage.</p>
<p class="rv" data-delay=".2" style="margin-top:28px;font:500 1.3rem var(--fd);color:#fff">ARRON. Ahead of Now. Building AI-Native Enterprises.</p></div></div></section>'''
    b += f'''<section><div class="wrap split2" style="align-items:start"><div class="collage rv" ><div class="c1">{photo("office", "ARRON office")}</div><div class="c2">{photo("team-laptop", "Team at work")}</div><div class="badge"><b>Dallas, TX</b><span>Headquarters, with delivery teams across the U.S. and India</span></div></div>
<div><span class="kicker rv">Building the Future Enterprise. Today.</span><h2 data-split>An AI-ready company for an AI-driven world.</h2>
<p class="lead rv" data-delay=".2">Headquartered in Dallas, Texas, ARRON Technologies is an AI-ready technology consulting and services company dedicated to helping organizations operate ahead of now. We enable businesses to transition from traditional operating models to AI-native enterprises by combining intelligent technology, modern platforms, and human ingenuity.</p>
<p class="rv" data-delay=".25" style="margin-top:18px">With more than 25 years of combined experience in technology leadership, digital transformation, enterprise architecture, customer experience, service management, and business operations, our team has helped organizations reimagine how they work, serve customers, and create value in an increasingly AI-driven world.</p>
<p class="rv" data-delay=".3" style="margin-top:18px">Our consultants have designed and delivered transformational solutions across industries, helping organizations modernize operations, improve service experiences, accelerate innovation, and realize significant business value through technology. From AI and automation to ERP, ITSM, Digital Workplace, and Customer Experience (CX), we focus on solutions that drive measurable outcomes and sustainable growth.</p></div></div></section>'''
    b += '<section class="paper"><div class="wrap"><div class="stats rv" style="grid-template-columns:repeat(4,1fr)"><div class="stat"><b data-count="25" data-suffix="+">0</b><span>Years of combined experience</span></div><div class="stat"><b data-count="100" data-suffix="+">0</b><span>Projects delivered</span></div><div class="stat"><b data-count="5">0</b><span>AI-native applications</span></div><div class="stat"><b data-count="6">0</b><span>Offices across two countries</span></div></div></div></section>'
    b += f'''<section class="paper" id="contact"><div class="wrap cgrid"><div><span class="kicker rv">Contact us</span><h2 data-split>Let's talk about what is next.</h2>
<p class="rv" data-delay=".2" style="margin-top:22px;font-size:1.1rem">Tell us a little about your challenge. A senior member of the team will reply within one business day.</p>
<div class="cinfo rv" data-delay=".3"><div><b>Email</b><span><a href="mailto:{EMAIL_1}">{EMAIL_1}</a></span></div><div><b>Email</b><span><a href="mailto:{EMAIL_2}">{EMAIL_2}</a></span></div><div><b>Headquarters</b><span>Dallas, Texas, USA</span></div></div></div>
<div class="rv rv-r"><form class="f" data-demo data-mailto="{EMAIL_1},{EMAIL_2}" onsubmit="return false"><div class="two"><label>Name<input name="name" required placeholder="Jane Smith"></label><label>Work email<input name="email" type="email" required placeholder="jane@company.com"></label></div>
<div class="two"><label>Company<input name="company" placeholder="Company name"></label><label>Interested in<select name="topic"><option>Artificial Intelligence / ARRON AURA</option><option>ERP</option><option>ITSM</option><option>Customer Experience</option><option>Digital Workplace</option><option>Products</option><option>Careers</option><option>Something else</option></select></label></div>
<label>How can we help?<textarea name="msg" placeholder="A few lines about your goals or challenge"></textarea></label>
<button class="btn btn-red" type="submit" style="justify-content:center">Send message {ARROW}</button><div class="ok">Your email app should open with the message ready to send. If it does not, write to us directly at the addresses shown.</div></form></div></div></section>'''
    page("about.html", "About ARRON — Our Purpose | ARRON Technologies, Dallas, Texas", "ARRON Technologies is an AI-ready technology consulting and services company headquartered in Dallas, Texas, with delivery teams in the U.S. and India.", b)



if __name__ == "__main__":
    build_home(); build_offerings(); build_cap(); build_industry(); build_insights(); build_proven(); build_consultants(); build_partners(); build_delivery()
    build_products(); build_careers(); build_about()
    for p in PRODUCTS:
        build_product(p)
    for k in INDUSTRIES:
        build_industry_page(k)
    for k in OFFER_KEYS + CAP_KEYS:
        build_detail(k)
    print("built", len([f for f in os.listdir(ROOT) if f.endswith('.html')]), "pages")
