# Output Template

The exact structure each generated file follows.

---

```markdown
# Offer Variations — {Offer Name}

**Date:** {YYYY-MM-DD}
**ICP:** {Segment × Stage — e.g. Indie Hacker · $0–10k MRR}
**Stage:** {Validating / Early Revenue / etc.}
**Current offer:** {one-line — what's being sold, the headline price, current structure}

---

## Inputs Loaded

- Offer file: `{host path to active offer}`
- ICP: `{host path to ideal-customer-profile file}`
- Big List of Offers: `.claude/skills/marketing-offer-generator/references/big-list-of-offers.md`
- Offers Playbook: `.claude/skills/marketing-offer-generator/references/offers-playbook.md`

---

## Variation 1 — {M-A-G-I-C Styled Name}

- **Type:** {one item from big-list — e.g. Pre-Order Discount, Cohort, Performance/Revshare, Bundle, Founding Member, Lifetime Deal, Free Trial, Paid Trial}
- **Hook:** {one-line pitch the operator would actually say out loud}
- **Mechanic:** {how it works in practice — pricing tiers, what's delivered, payment flow, duration}
- **Value Equation Lens:** {Dream Outcome ↑ / Perceived Likelihood ↑ / Time Delay ↓ / Effort & Sacrifice ↓ — pick the primary lever}
- **Price:** {$ + structure — one-time, monthly, deposit + payment plan, performance fee, etc.}
- **Guarantee:** {type from playbook — Unconditional / Conditional / Anti / Implied — with the specific terms}
- **Scarcity / Urgency:** {which play from the playbook — Cohort Cap / Total Business Cap / Rolling Seasonal / Exploding Opportunity / none}
- **Why this fits the ICP:** {quote a pain or trigger from the ICP file. If you can't tie it to something specific in the ICP doc, this variation isn't sharp enough — sharpen or drop.}
- **Operational cost:** {Low / Medium / High — what it would take to fulfill if 10 people bought today}

---

## Variation 2 — {Name}
...

(Continue for 10–15 variations. Span the offer-type menu — don't cluster.)

---

## Top 3 to Test First

Pick from above based on: (1) fit to the founder's current stage, (2) fit to the ICP's stated pains, (3) lowest operational cost / fastest signal.

1. **{Variation N — Name}** — {2–3 sentences on why this is the highest-leverage first test. What you learn if it works. What you learn if it doesn't.}
2. **{Variation N — Name}** — {same shape}
3. **{Variation N — Name}** — {same shape}

---

## What I'd Skip (and Why)

A short list of variations from above that look interesting but probably aren't worth testing first. One-line reasoning each.

- **{Variation N — Name}** — {why it's a poor first test for this founder right now}
- ...

---

## Notes & Next Moves

- {Any variation that requires a prerequisite the founder doesn't have yet — partnerships, an audience size, a hire — gets flagged here with the prereq.}
- {Any variation that's a clear v2 idea after the first test gets parked here.}
```

---

## Notes on using this template

- **Span the menu.** If 10 of 12 variations are "discount + free trial", you've failed at variety. Force yourself across at least 6–8 distinct offer types from `big-list-of-offers.md`.
- **No filler.** A variation without a sharp ICP tie-in is worse than not generating that variation. Better 10 strong than 15 mixed.
- **The hook is the test.** If the hook reads like AI marketing slop ("transform your business with our revolutionary…"), the variation is dead on arrival. Rewrite or drop.
- **Operational cost matters more than it sounds.** A six-figure performance deal is "exciting" but useless if the founder is solo at Stage 1. Score honestly.
- **Top 3 should span risk levels.** One conservative (closest to current offer), one moderate (a real reframe), one ambitious (could 5x the price if it works). Don't pick three flavors of the same thing.
