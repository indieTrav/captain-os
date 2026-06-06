---
name: setup-foundation
description: Guided first-run setup that turns the blank boilerplate into a live, operational business or project in one short interview. Asks a small set of essential questions, then drafts and writes all the core foundation files — CLAUDE.md header, foundation, vision/mission/values, north-star metrics, and the offer catalog — so the founder is up and running fast. Trigger on "set up the foundation", "setup foundation", "get started", "getting started", "start a new project", "new project", "new business", "kickoff", "initialize", "onboard me", "set up my business", "fill in the boilerplate", "I'm just getting started", "help me set this up".
---

# Setup Foundation

You're the founder's onboarding guide. Your job: take someone from blank boilerplate to a live, operational system in one short sitting. The whole experience should feel fast and easy — you ask a handful of essential questions, then you do the writing. The founder should never have to draft prose themselves; you draft vision, mission, values, and metrics *from their plain answers* and let them refine.

This works for a full **business** or a lighter **project**. Detect which from their answers and adapt — a non-commercial project doesn't need pricing or revenue targets, so skip those and make the north-star metric a non-revenue signal.

---

## Step 0 — Check current state

Read `01-command-center/foundation.md` and the top of `CLAUDE.md` first.

- **Still boilerplate** (placeholders like `[Company Name]`, `[Offer Name]` present) → proceed with a fresh setup.
- **Already filled in** → don't blow it away. Tell the founder it's already set up and ask whether they want to (a) update specific sections, (b) start over from scratch, or (c) cancel. Only overwrite on an explicit yes.

Don't load `99-archives/` or any `.*.template.md` / `*.example.md` scaffolds.

---

## Step 1 — Run the interview

Open with one or two sentences: you'll ask a few quick questions, then fill in the whole foundation for them. Then ask the questions below **as one compact numbered list** so a fast founder can answer everything in a single message. Tell them they can answer all at once, or just answer what they know and you'll draft sensible drafts for the rest (marked so they can fix later).

Keep it to these essentials — resist adding more:

1. **Name** — business or project name?
2. **What it is** — in a sentence or two, what is it and who's it for?
3. **Customer** — who's the target customer / audience? (or "just me / internal" for a personal project)
4. **Offer** — what are you selling? Name, one-liner, and price. ("Not sure yet" / "nothing, it's a project" is fine.)
5. **Model** — business model? (digital products · services · SaaS · course · content · other)
6. **Stage** — where are you? (Idea · Validating · Early revenue · Growing)
7. **The goal** — the single most important thing to prove or achieve right now?
8. **12-month target** — revenue or customers a year out? (skip for a non-commercial project)
9. **Why** — the personal reason this is worth building? (optional)

If something essential is genuinely missing after their reply (e.g. no name at all), ask one tight follow-up — don't re-ask things they already answered. Prefer drafting a reasonable default over interrogating.

For the multiple-choice items (model, stage), you may use the AskUserQuestion tool if it makes answering faster; otherwise plain text in the numbered list is fine.

---

## Step 2 — Draft, then confirm in one pass

From their answers, draft the real content. You write the prose, not them:

- **Vision** — a concrete 12-month picture (offer, distribution, audience, product), built from their stage + target.
- **Mission** — who they help, the outcome, and how, in one or two sentences.
- **Values** — propose 3 values that fit what they said; keep them specific, not generic.
- **North-star metric** — propose the 1 number that proves the thing is working, based on stage + model (e.g. Validating → paying customers or discovery calls; content model → qualified subscribers; SaaS → active paying accounts). Add 1–2 supporting leading indicators.
- **Stage + playing field** — map their stage to the Revenue Stage Framework in `CLAUDE.md` and name the wall they're pushing against.

Show the founder a **tight summary** of what you inferred — especially the drafted vision one-liner, mission, the 3 values, and the north-star metric — and ask for a quick thumbs-up or edits. One round. Don't make them review every file line by line; the files are easy to tweak later.

---

## Step 3 — Write the files

On confirmation, populate these real files (they already exist — edit them in place, replacing placeholders; **never** edit the `.*.template.md` dotfiles). Preserve each file's existing section structure; just fill the blanks. Spell out acronyms per the CLAUDE.md convention (write "monthly recurring revenue", not "MRR"). Stamp every `Last updated:` / `Created:` line with **today's date** (use the current date from session context).

1. **`CLAUDE.md`** — the header block at the very top: Company, Active offer, Backlog offers, Stage, Model, Goal. Fill the brand-vs-offer note and the "Playing field for this business" line under the Revenue Stage Framework with the stage(s) they're in. Leave the Market Segments table for the ICP step.
2. **`01-command-center/foundation.md`** — identity, active offers table, metadata, revenue snapshot, stage.
3. **`01-command-center/vision-mission-values.md`** — the 12-month picture, the business, transformation (before/after), revenue/impact target, why, plus the Mission and Values sections.
4. **`01-command-center/north-star.md`** — primary metric, supporting metrics table, what they're ignoring for now.
5. **`01-command-center/offers.md`** — the offer catalog active row. (For a non-commercial project, note there's no offer yet and leave the table minimal.)

For a **project** (not a business): keep offers/revenue minimal or empty, make the north-star a non-revenue signal, and skip the 12-month revenue target.

---

## Step 4 — Offer the fast next steps

Once files are written, briefly confirm what you populated, then offer (don't auto-run) the natural next moves so they keep momentum:

- **Seed a first goal** — fill `01-command-center/goals/` annual + current-quarter files from the templates, and drop 3–5 starter tasks into `01-command-center/tasks.md`.
- **Define the customer** — run `/icp-generator` to build the ideal customer profile (and populate the Market Segments table in `CLAUDE.md`).
- **Check the pulse** — run `/business-status-report` to see the system read back the business with its first action plan.

Keep the close short. The win is that they went from blank boilerplate to a live foundation in a few minutes — say that plainly and hand them the next step.
