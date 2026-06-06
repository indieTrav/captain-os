# [Company Name] — Master Brain

A markdown-based studio operating system. Each folder is a department; you are Claude, the operating intelligence — read context, invoke skills, produce outputs.

**Company:** [Company Name] · [yourdomain.com]
**Active offer:** [Offer Name] · [yourdomain.com/offer] — [one-line description: what it is, who it's for, price]
**Backlog offers:** [Backlogged offer name + one line — revisit after the active offer validates]
**Stage:** Pre-revenue / Validating
**Model:** [Business model — e.g. digital products, services, SaaS, courses]
**Goal:** [The single most important thing to prove or achieve right now]

> **Brand vs. offer:** "[Company Name]" = the parent company/studio. "[Offer Name]" = the active product/offer under the studio. Use the company name in parent-brand contexts (foundation, dashboard, parent-brand content); use the offer name on offer-specific sales pages, product marketing, and anything tied to the offer's URL. Backlogged or future offers should only be referenced when the user explicitly asks. If ambiguous, ask.

---

## Folder Map

`00` = capture. `01–10` = departments (operating surface). `94–99` = resources (consult, don't operate from).

| Folder               | Department / Resource                                                                | Priority                     |
| -------------------- | ------------------------------------------------------------------------------------ | ---------------------------- |
| `00-inbox/`          | Raw capture — unsorted notes, links, screenshots awaiting triage                     | High                         |
| `01-command-center/` | Vision, mission, north-star, goals, tasks, projects, ideas, offers catalog           | High                         |
| `02-research/`       | Ideal customer profiles, positioning, competitors, domain research, industry players | **Critical**                 |
| `03-audience/`       | Email list, community, social proof                                                  | High                         |
| `04-offers/`         | One file per active offer — validation worksheets, launch plans                      | **Critical**                 |
| `05-products/`       | One folder per shippable product — specs, manifests, build notes, deliverables       | **Critical**                 |
| `06-marketing/`      | Content (YouTube, blog, social, email), SEO, paid ads, website                       | High                         |
| `07-sales/`          | Pipeline, email sequences, scripts, objections                                       | Medium                       |
| `08-customers/`      | Onboarding, feedback, success stories, FAQs                                          | Low (activate at first sale) |
| `09-team/`           | Hiring, onboarding, performance, culture, leadership                                 | Low (Stage 3+)               |
| `10-operations/`     | SOPs, tools, finances, legal                                                         | Low ($5k+/mo)                |
| `94-assets/`         | Images, references, and binary assets for the repo                                   | —                            |
| `95-snapshots/`      | Dashboard, captain's logs (daily/weekly/monthly/yearly reviews), daily news archive  | High                         |
| `96-resources/`      | Playbooks, checklists, template pointer index                                        | Medium                       |
| `99-archives/`       | Retired/unresolved files — **excluded from searches**                                | —                            |

> **Offers vs. products:** `04-offers/` holds the _sales wrapper_ (positioning, pricing, validation, launch plan). `05-products/` holds the _thing being shipped_ (spec, manifest, build notes, deliverables). One offer can wrap one product; one product can be sold under multiple offers. The offer file lives at `04-offers/{offer-slug}.md` and the product build lives at `05-products/{product-slug}/`.

---

## Revenue Stage Framework

Patterns from operators like Verne Harnish and Greg Crabtree. Use to calibrate advice, content, and offers to the customer's actual game.

| Stage                        | MRR       | Core Constraint           | The Game                                                                                             |
| ---------------------------- | --------- | ------------------------- | ---------------------------------------------------------------------------------------------------- |
| **1 — Survival**             | $0–10k    | PMF + founder energy      | Will anyone pay? Doing everything yourself. Most businesses die here.                                |
| **2 — Founder Bottleneck**   | $10–50k   | Founder is the constraint | Proven people pay; sales/support/dev/ops all route through one person. Must delegate or systematize. |
| **3 — First Org Transition** | ~$80k     | First non-founder hires   | Too big for one person, too small for a team. First manager hire. Cash flow gets weird.              |
| **4 — No Man's Land**        | $250–420k | Premature infrastructure  | Needs systems + middle management before revenue justifies them. Margins compress.                   |
| **5 — Real Company**         | ~$830k    | Managing managers         | Founder mostly not doing the work. Communication + hiring quality become the job.                    |
| **6 — Process & Capital**    | $2M+      | Systems, capital, talent  | Different game entirely.                                                                             |

> **Playing field for this business:** [Which stages this business is playing in — e.g. Stages 1–2 only.] Map every offer and content asset to the wall the business is currently pushing against (e.g. the **Stage 1→2 wall** at ~$10k MRR / first distribution system, or the **Stage 2→3 wall** at ~$80k MRR / first hire).

---

## Market Segments

Segments = **job title × revenue stage**. Profiles live in `02-research/ideal-customer-profiles/` named `{stage}-{segment}-profile.md`. Identify both dimensions before writing copy or building an offer — the same job title at two different revenue stages is not the same customer.

| Job Title       | Stage 1 · $0–10k  | Stage 2 · $10–50k | Stage 3+ |
| --------------- | ----------------- | ----------------- | -------- |
| **[Segment A]** | _(not yet built)_ | _(not yet built)_ | —        |
| **[Segment B]** | _(not yet built)_ | —                 | —        |

_(not yet built)_ = a segment to serve eventually. Add the profile (use the ideal-customer-profile template) before producing content for it.

---

## Key Context Files

Load these for full context before working:

- `01-command-center/foundation.md` — business identity, stage, revenue snapshot
- `01-command-center/vision-mission-values.md`, `north-star.md`
- `01-command-center/tasks.md` — rolling tasks; tags reference `[[project-slug]]`
- `01-command-center/projects/` — one file per active project (slug matches tasks.md tag)
- `01-command-center/goals/` — annual + quarterly
- `01-command-center/ideas.md` — **single dump file for all ideas** (Triage, Offers, Marketing, Content, Product, Random). Always capture here; triage and graduate to real homes weekly. No other `*-ideas.md` files exist.
- `01-command-center/offers.md` — **offer catalog** (active offers, funnel, revenue by offer). Single source of truth for what's being sold.
- `02-research/ideal-customer-profiles/` — one file per segment × stage
- `02-research/positioning.md`, `competitors.md`, `domain-availability-research.md`, `trends-and-bets.md`
- `02-research/industry-players/` — one file per notable operator / competitor in the space
- `04-offers/` — one file per active offer (validation worksheets, launch plans). Offer-idea capture lives in `01-command-center/ideas.md` under `## Offers`.
- `05-products/` — one folder per shippable product (spec, manifest, build notes, deliverables). Product-idea capture lives in `01-command-center/ideas.md` under `## Product`.
- `06-marketing/strategy/` — content-pillars, content-strategy, keyword-master-list. Marketing-idea capture lives in `01-command-center/ideas.md` under `## Marketing`.
- `95-snapshots/dashboard.md` — current state: stage, metrics, milestones
- `96-resources/index.md` — playbook + template pointer index (consult when user references resources or asks for a template)

---

## Skill Routing

Always invoke the skill; never replicate its logic. **Default:** run `/deslopify` on any content before publishing.

- **Content writing:** `/video-scripts-and-captions-generator` · `/linkedin-post-writer` · `/twitter-x-post-writer`
- **Content strategy:** `/content-ideas-generator` · `/content-repurpose-generator` · `/marketing-ideas-generator` · `/content-hooks-generator`
- **Research — people & competitors:** `/people-osint-researcher` · `/competitor-teardown` · `/twitter-x-profile-posts-scraper`
- **Research — content & demand:** `/youtube-transcript-generator` · `/youtube-comments-scraper` · `/keyword-research` · `/domain-availability-checker`
- **Research — audience & offers:** `/icp-generator` · `/marketing-offer-generator` · `/voice-cloner`
- **Operating the studio:** `/setup-foundation` (first-run setup) · `/business-status-report` · `/daily-news` · `/xlsx`
- **Quality:** `/deslopify` (always, before publishing)
- **System / meta:** `/skill-creator`

---

## Output Folder Map

Where finished assets get saved. Never dump in root.

| Asset                                                    | Folder                                                                         |
| -------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Raw capture (unsorted notes, links, screenshots)         | `00-inbox/`                                                                    |
| Images, references, binary assets                        | `94-assets/`                                                                   |
| Offer worksheet / launch plan                            | `04-offers/`                                                                   |
| Product spec / build notes / manifest                    | `05-products/{product-slug}/`                                                  |
| Blog post (staged pipeline)                              | `06-marketing/blog/{00-brief,01-dump,02-outline,03-draft,04-review,05-final}/` |
| YouTube script · packaging                               | `06-marketing/youtube/{scripts,packaging}/`                                    |
| Shorts / Reels script                                    | `06-marketing/shorts/`                                                         |
| Social post (LinkedIn / Instagram / Twitter)             | `06-marketing/{linkedin,instagram,twitter}/posts/`                             |
| Newsletter · broadcast                                   | `06-marketing/email/{newsletters,broadcasts}/`                                 |
| Email sequence (sales / nurture)                         | `07-sales/email-sequences/` or `03-audience/email-list/sequences/`             |
| Paid ad campaign brief                                   | `06-marketing/paid-ads/campaigns/`                                             |
| Project brief                                            | `01-command-center/projects/`                                                  |
| Captain's log (daily / weekly / monthly / yearly review) | `95-snapshots/captains-logs/{daily,weekly,monthly,yearly}/`                    |
| Daily news brief archive                                 | `95-snapshots/daily-news/YYYY-MM-DD.md`                                        |
| Content tracking (status of every file)                  | `01-command-center/content.md`                                                 |

---

## Working Conventions

1. **Read before writing.** Load ideal customer profile, positioning, and content pillars before generating any asset so it's on-brand.
2. **Save to the right folder.** See Output Folder Map. Never dump in root.
3. **Templates are co-located dotfiles.** Every output folder contains a `.[name].template.md` scaffold (e.g. `01-command-center/projects/.[project].template.md`). To create a new doc: read the dotfile, create a new file in the _same folder_ with a real name (no leading dot, no `.template`), fill it in. Never edit the dotfile. Full pointer index lives in `96-resources/index.md`.
4. **Stage gates.** Don't over-engineer Low-priority folders. Focus on Critical + High.
5. **Voice check.** `/deslopify` pass on all published content.
6. **Avoid acronyms.** Audience may include first-time founders — spell terms out, with the acronym in parentheses on first use only if it repeats (e.g. "monthly recurring revenue (MRR)"). Skip the acronym entirely if the term appears once. Common offenders: OKR, ICP, MRR, ARR, SaaS, SOP, KPI, CTA, CRM, CAC, LTV.
7. **Ignore scaffold files.** `*.example.md` and `.*.template.md` are scaffolds, not live content. Don't load as context, don't count in summaries, don't update unless asked. Flag them as scaffolds when listing folder contents.
8. **Ignore `99-archives/`.** Cold storage — exclude from all searches, traversals, counts, and context loading. Use `--exclude-dir=99-archives` or `-g '!99-archives/**'` with `find`/`rg`/`Glob`. Only enter when the user explicitly names it.
9. **Content tracking.** Every content **file** (not every piece inside a bundle) gets a row in `01-command-center/content.md` when created — under the right type section, with `Status: DRAFT`. Use the file's H1 as the Title and a wiki link `[[filename.md]]` in the File column. Update the Status as the file progresses (`DRAFT → REVIEWED → SCHEDULED → PUBLISHED → ARCHIVED`). This doc is the only source of truth for content state; don't add status fields to individual content files. When producing a repurpose batch, also add a row to the **Source Bundles** table at the top.
10. **`//` is the founder's note marker in drafts.** Any line starting with `//` (e.g. `// rewrite this paragraph`, `// add a screenshot here`, `// too long, cut by 30%`) is an instruction to act on during the next edit pass — never body copy, never published. When editing a draft, treat every `//` line as a TODO: apply the instruction, then remove the line. Never generate `//` lines yourself.

---

## Stage Gate Progression

Update **Stage** at the top when you graduate.

| Stage                | Unlock                | Activate                                                         |
| -------------------- | --------------------- | ---------------------------------------------------------------- |
| **Validating** (now) | No consistent revenue | —                                                                |
| **Early Revenue**    | First $1k month       | `04-offers/` fully, `07-sales/`                                  |
| **Growing**          | $10k/mo consistently  | `06-marketing/` fully, `08-customers/`                           |
| **Scaling**          | $50k/mo               | `10-operations/` (SOPs, finance), deep `95-snapshots/` analytics |
| **First Hires**      | ~$80k/mo (Stage 3)    | `09-team/` hiring, onboarding, performance                       |
| **Team Building**    | $250k+/mo (Stage 4+)  | `09-team/` culture, leadership, managing managers                |
