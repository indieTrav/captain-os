# Captain OS

A markdown-based studio operating system. Every folder is a department; Claude is the operating intelligence that reads context, invokes skills, and produces outputs. You run the business by talking to Claude inside this repo.

---

## Getting Started

### 1. Set the foundation

**Fastest way — run `/setup-foundation`.** It asks a handful of quick questions, then drafts and writes your whole foundation for you: the `CLAUDE.md` header, business identity, vision/mission/values, north-star metric, and offer catalog. Go from blank boilerplate to a live system in a few minutes.

Prefer to do it by hand? Open `CLAUDE.md` and fill in the header placeholders — company name, active offer, stage, model, and goal (this is the context every skill reads first) — then fill in:

- `01-command-center/foundation.md` — business identity, stage, revenue snapshot
- `01-command-center/vision-mission-values.md` and `north-star.md`

### 2. Learn the folder map

- `00-inbox/` — raw capture; dump anything here, triage later
- `01-command-center/` — vision, goals, tasks, projects, ideas, offers catalog
- `02-research/` — customer profiles, positioning, competitors
- `04-offers/` — the sales wrapper (positioning, pricing, launch plan)
- `05-products/` — the thing being shipped (specs, build notes, deliverables)
- `06-marketing/` — content across blog, YouTube, social, email
- `95-snapshots/` — dashboard + captain's logs (daily/weekly/monthly reviews)
- `96-resources/` — playbooks, checklists, template index

Folders `00`–`10` are your operating surface. `94`–`99` are resources you consult, not operate from. `99-archives/` is cold storage and excluded from all searches.

### 3. Work the system

Just ask Claude in plain language. A few starting points:

- **"Catch me up"** or `/business-status-report` — pulse on stage, metrics, tasks, and what to do next
- **"Build an ICP for [customer]"** (`/icp-generator`) — sharp ideal customer profile
- **"Give me offer ideas for [product]"** (`/marketing-offer-generator`) — ranked offer variations
- **Write content** — `/linkedin-post-writer`, `/twitter-x-post-writer`, video scripts, and more
- **"Capture this idea: …"** — Claude files it in `01-command-center/ideas.md`

Run `/deslopify` on any content before publishing.

### 4. Follow the conventions

- **Read before writing.** Claude loads your profile, positioning, and pillars so output stays on-brand.
- **Save to the right folder.** See the Output Folder Map in `CLAUDE.md` — never dump in root.
- **Templates are co-located dotfiles** (`.[name].template.md`). Copy them to a real filename to create a new doc; never edit the dotfile.
- **`//` marks founder notes** in drafts — instructions for Claude's next edit pass, never published copy.

---

For the full operating manual — skill routing, revenue-stage framework, market segments, and stage gates — see `CLAUDE.md`.
