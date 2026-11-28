# ARRON website: hosting, domain, email, security and search

*Internal documentation, updated 28 November 2026.*

This is the same content as the formatted page at **https://arrontechnologies.com/documentation/** (the file `index.html` in this folder). GitHub shows HTML files as code, so this README repeats everything in a form GitHub displays directly. If the two ever differ, check the live settings in Wix and GitHub.

## Contents

1. [Summary](#1-summary)
2. [Costs](#2-what-it-cost)
3. [Email](#3-email)
4. [How the pieces fit together](#4-how-the-pieces-fit-together)
5. [DNS records](#5-dns-records-final-state)
6. [How the site was put online](#6-how-the-site-was-put-online-step-by-step)
7. [Laptop fix](#7-why-the-site-did-not-open-on-one-laptop-and-the-fix)
8. [Repository protection](#8-who-can-change-the-website-repository-protection)
9. [Site security](#9-site-security)
10. [Search visibility (SEO)](#10-search-visibility-seo)
11. [LinkedIn company page](#11-linkedin-company-page)
12. [Updating the site](#12-how-to-change-the-website-later)
13. [Maintenance checklist](#13-maintenance-checklist)

---

## 1. Summary

The ARRON website is a static site (plain HTML, CSS and JavaScript) stored in this GitHub repository and published for free with GitHub Pages. The domain **arrontechnologies.com** and three company mailboxes were bought from Wix on 22 November 2026. On 27 November 2026 the domain was pointed at GitHub Pages, so the site loads at that address with HTTPS. Since then the site has been hardened, prepared for search engines, and a LinkedIn company page has been created.

| | |
|---|---|
| Website address | https://arrontechnologies.com |
| Source code | github.com/yashgupta67/ARRON (public) |
| Hosting | GitHub Pages, free |
| Domain registrar | Wix (the domain is not at GoDaddy) |
| DNS provider | Wix name servers |
| Email | 3 mailboxes, Google Workspace via Wix Business Email |
| LinkedIn page | linkedin.com/company/arron-technologies |
| Site size | 36 pages, plain HTML, built by a Python script |

> The domain and the email live in one Wix account, but the website itself is **not** on Wix. Wix only supplies the domain name, its DNS settings and the mailboxes. The pages are served by GitHub.

## 2. What it cost

Figures come from the Wix billing history and Premium Subscriptions pages. Taxes may be added by Wix, and prices can change at renewal.

| Item | Provider | Billing | Amount (USD) | Paid / next payment |
|---|---|---|---|---|
| Domain `arrontechnologies.com` | Wix | Once for 3 years | $88.11 | Paid 22 Nov 2026, covers to 22 Nov 2029 (Wix lists the next payment as 23 Oct 2029) |
| Business Email, 3 users (Starter plan) | Wix (Google Workspace) | Monthly | $27.27 / month | First month paid 22 Nov 2026, next payment 22 Dec 2026 |
| Website hosting (GitHub Pages) | GitHub | None | $0 | Free for public repositories |
| HTTPS certificate | GitHub / Let's Encrypt | None | $0 | Automatic |

| Period | Calculation | Approx. total |
|---|---|---|
| Paid so far (22 Nov 2026) | $88.11 domain + $27.27 first month of email | $115.38 |
| First 12 months | $88.11 + 12 × $27.27 | $415.35 |
| Each following year | 12 × $27.27 (domain already paid to Nov 2029) | $327.24 |
| Domain per year, spread over 3 years | $88.11 ÷ 3 | $29.37 |

The email is the main running cost. Removing a mailbox in Wix Business Email lowers the monthly charge.

## 3. Email

Wix Business Email (Starter) gives **3 users** on **@arrontechnologies.com**, delivered by Google Workspace. The addresses published on the website are RajitM@arrontechnologies.com and Annad@arrontechnologies.com. The third mailbox is an administrator mailbox. The website's contact buttons and forms open an email draft to the two published addresses, because the site cannot send mail itself.

### Email protection (anti-spoofing)

| Record | What it does | Status |
|---|---|---|
| SPF | Says Google's servers may send mail for the domain | In place |
| DMARC | `_dmarc` TXT: `v=DMARC1; p=quarantine; pct=25; rua=mailto:admin@arrontechnologies.com`. Sends 25% of mail that fails the checks to spam and emails daily summary reports to the admin mailbox | Added 28 Nov 2026 |
| DKIM | A digital signature on outgoing mail | **Not yet on.** Turn it on in Google Admin: Apps → Google Workspace → Gmail → Authenticate email, then add the DNS record Google shows |

**Next step for email:** after DKIM is on and a few weeks pass with no problems in the DMARC reports, raise `pct` to 100, and later change `p=quarantine` to `p=reject`.

Email and website use different DNS records. The website records were changed on 27 November 2026. The mail records (MX and SPF) were left untouched, so email kept working.

## 4. How the pieces fit together

**Website path:** browser → Wix DNS (A and CNAME records) → GitHub Pages → site files.

**Email path:** sender → Wix DNS (MX records) → Google Workspace → mailbox.

## 5. DNS records (final state)

Managed in Wix: *Domains → arrontechnologies.com → ⋯ → Manage DNS records*. The name servers are `ns2.wixdns.net` and `ns3.wixdns.net`, and DNSSEC is switched on by Wix. **Do not change the name servers**: moving them elsewhere would break the domain until DNSSEC is removed.

### Changed on 27 November 2026

| Type | Host | Before (Wix) | After (GitHub Pages) |
|---|---|---|---|
| A | @ | 185.230.63.171 | 185.199.108.153 |
| A | @ | 185.230.63.186 | 185.199.109.153 |
| A | @ | 185.230.63.107 | 185.199.110.153 |
| A (new) | @ | none | 185.199.111.153 |
| CNAME | www | cdn3.wixdns.net | yashgupta67.github.io |

GitHub publishes four server addresses for Pages, and listing all four gives redundancy. The `www` record makes `www.arrontechnologies.com` work and GitHub redirects it to the main address.

### Email records (MX and TXT)

| Type | Value | Priority |
|---|---|---|
| MX | aspmx.l.google.com | 10 |
| MX | alt1.aspmx.l.google.com | 20 |
| MX | alt2.aspmx.l.google.com | 30 |
| MX | alt3.aspmx.l.google.com | 40 |
| MX | alt4.aspmx.l.google.com | 50 |
| TXT | `v=spf1 include:_spf.google.com ~all` (SPF) | |
| TXT `_dmarc` (added 28 Nov 2026) | `v=DMARC1; p=quarantine; pct=25; rua=mailto:admin@arrontechnologies.com` | |

## 6. How the site was put online, step by step

### A. Finding where the domain lives

1. **Checked the public registry (RDAP).** It showed the domain was registered on 22 Nov 2026 at *Wix.com Ltd.*, with name servers at Wix and mail records at Google. So all DNS changes had to be made in Wix, not GoDaddy.

   ```bash
   curl -s "https://rdap.verisign.com/com/v1/domain/arrontechnologies.com"
   dig +short arrontechnologies.com MX
   ```

   *Why:* DNS can only be edited where the name servers are hosted. Checking first avoided editing the wrong account.

2. **Found the right Wix account.** The domain was listed under Domains as "Not assigned to a site", so there was no Wix website to disconnect. *Why:* a connected Wix site locks the website records.

### B. Editing DNS in Wix (27 Nov 2026)

1. Opened Domains → arrontechnologies.com → Manage DNS records and checked the existing records, leaving the five Google MX records alone.
2. Edited the three existing A records to 185.199.108.153, .109.153 and .110.153, and added a fourth, 185.199.111.153. (Wix warns that this can take a Wix site offline, which is expected.)
3. Edited the `www` CNAME from `cdn3.wixdns.net` to `yashgupta67.github.io`.
4. Verified:

   ```bash
   dig +short @ns2.wixdns.net arrontechnologies.com A
   dig +short @8.8.8.8 arrontechnologies.com A
   dig +short www.arrontechnologies.com CNAME
   ```

   *Why:* asking Wix's own server proves the change was saved, and asking Google's public resolver shows it has spread.

### C. Telling GitHub about the domain (terminal, GitHub CLI)

1. Added a file named `CNAME` containing the domain, and pushed it.

   ```bash
   printf 'arrontechnologies.com\n' > CNAME
   git add CNAME
   git commit -m "Add custom domain arrontechnologies.com"
   git push
   ```

   *Why:* GitHub Pages reads this file to know which domain the site answers for.

2. Set the custom domain in the Pages settings:

   ```bash
   gh api -X PUT repos/yashgupta67/ARRON/pages -f cname=arrontechnologies.com
   ```

   *Why:* this switches the domain on and starts the automatic HTTPS certificate request. It was done after DNS was ready so the existing address did not break first.

3. Waited for the certificate to become "approved" (about a minute), then enforced HTTPS:

   ```bash
   gh api repos/yashgupta67/ARRON/pages --jq '.https_certificate.state'
   gh api -X PUT repos/yashgupta67/ARRON/pages -F https_enforced=true
   ```

   *Why:* HTTPS encrypts the connection (the padlock). Enforcing it redirects `http://` to `https://`.

4. Tested the live site by asking GitHub's server directly (avoids stale DNS on the testing computer):

   ```bash
   curl -s --resolve arrontechnologies.com:443:185.199.108.153 https://arrontechnologies.com/ | grep -o "<title>[^<]*"
   curl -s -o /dev/null -w "%{http_code}\n" https://arrontechnologies.com/
   ```

**Result:** https://arrontechnologies.com serves the site, `www` redirects to it, and the old address (yashgupta67.github.io/ARRON) forwards to the new domain.

## 7. Why the site did not open on one laptop, and the fix

Right after the change, the site opened for some people but not others. DNS answers are saved ("cached") by routers and providers for the record's lifetime (1 hour here). A home router that had saved the old Wix addresses kept handing them out, so one laptop saw a Wix "This domain isn't connected to a site" page. Public resolvers such as Cloudflare (1.1.1.1), Google (8.8.8.8) and Quad9 (9.9.9.9) already had the new addresses.

Commands used on the laptop (macOS):

| Command | What it does | Safe? |
|---|---|---|
| `networksetup -setdnsservers Wi-Fi 1.1.1.1 9.9.9.9` | Makes Wi-Fi ask Cloudflare and Quad9 for addresses instead of the router | Yes, only changes which lookup service Wi-Fi uses |
| `networksetup -getdnsservers Wi-Fi` | Shows the current setting | Yes, read-only |
| `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder` | Clears the Mac's saved list of recent lookups | Yes, deletes no files |
| `networksetup -setdnsservers Wi-Fi empty` | Undo: back to the router's own DNS | Yes |

The setting can reset when Wi-Fi reconnects. A router restart, or waiting a few hours, also clears the stale copy. It only affects networks that cached the old records.

## 8. Who can change the website? (repository protection)

The repository is **public**: anyone can read and copy it, but only the owner and invited collaborators can change it. Checked on 28 November 2026:

| Check | Result |
|---|---|
| People with write access | Only the owner (`yashgupta67`) |
| Pending invitations, deploy keys, webhooks | None |
| Branch protection on `main` | Force-pushes and branch deletion blocked |
| Wiki and Projects | Switched off |
| Forks | Allowed, but a fork is a separate copy and cannot alter the original |
| Pull requests | Strangers can propose changes, but nothing is merged or published unless the owner approves |

```bash
gh api repos/yashgupta67/ARRON/collaborators
gh api -X PUT repos/yashgupta67/ARRON/branches/main/protection --input protection.json
gh api -X PATCH repos/yashgupta67/ARRON -F has_wiki=false -F has_projects=false
```

**Extra safeguards:** two-factor sign-in on GitHub and Wix (a stolen password is the real risk), never commit passwords or keys (everything is public), and review collaborators from time to time.

> This documentation is published with the site (at `/documentation/`) and marked "noindex", but anyone with the link can read it. It deliberately omits passwords, account emails, card details and invoice numbers.

## 9. Site security

The site is static files: no database, login, server code or admin area, so there is little to attack. The realistic risks are account takeover (GitHub, Wix, Google) and faked email, so those are covered too.

| Protection | What it does | Status |
|---|---|---|
| HTTPS enforced | Encrypts visits and redirects http to https | On |
| Content security policy | Every page may only load its own files and Google Fonts, blocking injected scripts (set in `page()` in `_src/build.py`) | On |
| Clickjacking protection | A script in `assets/main.js` stops the site being shown inside another page | On |
| Referrer policy | Limits what other sites learn about where visitors came from | On |
| Safe external links | Open in a new tab with `noopener noreferrer` | On |
| `security.txt` | Tells researchers where to report problems (`/.well-known/security.txt`) | Published |
| Secrets scan | Repository searched for passwords, keys and tokens, none found | Clean |
| Repository access | Owner only, no force-push (section 8) | On |
| DNS and domain | Transfer lock and DNSSEC on at Wix | On |
| Email spoofing protection | SPF and DMARC on, DKIM still to enable (section 3) | Partly |
| Two-factor sign-in | Must be enabled by the account owners for GitHub, Wix and Google | To do |

**Limit to remember:** because scripts may only come from the site itself, never add an outside script (analytics, chat widget) without updating the policy in `_src/build.py`, or it will be blocked.

## 10. Search visibility (SEO)

Nobody can guarantee a top ranking, because Google decides. Brand searches ("arron technologies") are realistic to win within weeks once Google has indexed the site. Broad searches such as "AI services" are very competitive and take months plus links from other sites. Local searches such as "AI services Dallas" are the realistic target.

**Built into the site**

| Item | Where |
|---|---|
| Keyword-focused titles and descriptions (home, Offerings and AI pages mention "AI Services" and Dallas) | `_src/build.py` |
| Canonical link on every page (avoids duplicates) | `page()` |
| Link previews for LinkedIn, WhatsApp etc. (Open Graph image `assets/img/og-image.png`) | `page()` |
| Structured data (JSON-LD): organization name, alternative spellings ARRON / Arron Technology / Arron Tech, Dallas address, LinkedIn page, founding year | home page |
| `sitemap.xml` rebuilt on every build | site root |
| `robots.txt` pointing at the sitemap and skipping `/documentation/` | site root |
| Custom 404 page | `404.html` |

**Still to do by the account owner**

1. **Google Search Console** (search.google.com/search-console): add `arrontechnologies.com` as a domain property, verify with the DNS TXT record Google gives, then submit `https://arrontechnologies.com/sitemap.xml`.
2. **Bing Webmaster Tools:** import the site from Google Search Console.
3. **Google Business Profile** for ARRON in Dallas (matters most for local searches).
4. **Links from other sites:** the LinkedIn page (done), team profiles, partner and directory listings.
5. **Fresh content:** the Our Insights section is empty. A few real articles on AI, ERP and ITSM would help a lot.

## 11. LinkedIn company page

Created on 28 November 2026: **https://www.linkedin.com/company/arron-technologies/**. It is linked from the website's contact section and footer.

| Field | Value |
|---|---|
| Name | ARRON Technologies |
| Tagline | Ahead of Now. Building AI-native enterprises. |
| Industry, size, type | IT Services and IT Consulting · 11–50 employees · Privately held |
| Founded | 2026 |
| Website and button | https://arrontechnologies.com with a "Visit website" button |
| Locations | Dallas TX (HQ), Louisville KY, Houston TX, Delhi NCR, Pune, Bangalore (cities only) |
| Specialties | Artificial Intelligence, AI Strategy, ERP, ITSM, Customer Experience, Digital Workplace, Digital Transformation, Product as a Service |
| Public contact | admin@arrontechnologies.com in the About text |

Page admins are not shown publicly. A person appears on the page only if they add ARRON Technologies as an employer on their own LinkedIn profile.

The logo (300×300 dark square) and cover banner (1128×191, key content inside a safe zone because LinkedIn crops the edges) are kept in the project's local `linkedin` folder, not in the repository.

## 12. How to change the website later

The pages are generated by a small Python script so the design stays consistent.

1. **Edit the content** in `_src/build.py` (page text) or `assets/styles.css` (design).
2. **Rebuild** from the project folder:

   ```bash
   python3 _src/build.py
   ```

3. **Publish:**

   ```bash
   git add -A
   git commit -m "Describe the change"
   git push
   ```

GitHub Pages republishes in one or two minutes. Hard-refresh the browser (Cmd+Shift+R) to see it.

The build also regenerates `sitemap.xml`, `robots.txt`, `404.html` and `.well-known/security.txt`. Team photos are in `assets/img/team/`, general photos in `assets/img/photos/`, partner logos in `assets/img/partners/`, and logo files in `assets/img/`.

## 13. Maintenance checklist

- **Monthly:** Wix charges $27.27 for the three mailboxes on the 22nd (plus any taxes). Keep the payment method valid or email stops.
- **Before November 2029:** renew the domain in Wix and consider auto-renew. If it lapses, both website and email stop.
- **Email protection:** switch on DKIM in Google Admin, then tighten DMARC from 25% to 100% and later to reject.
- **Search:** add the site to Google Search Console and Bing and submit the sitemap.
- **Two-factor sign-in:** switch it on for GitHub, Wix and Google.
- **Never delete** the MX, SPF or `_dmarc` records in Wix DNS.
- **Never change** the Wix name servers without a plan for DNSSEC.
- **Never delete** the `CNAME` file in the repository.
- **Do not add outside scripts** without updating the content security policy.
- **After any Wix or LinkedIn session,** sign out, especially on shared computers.
- **Still to decide:** a contact form that stores messages needs a service such as Formspree, because the site has no server. Today the forms open an email draft.
