---
name: marketing-offer-generator
description: Generate a ranked list of concrete offer variations for the user's product — different ways to package, price, guarantee, or bundle the same core thing. Cross-references the bundled big-list of offer types (free trial, bundle, guarantee, cohort, etc.) and the offers playbook (Grand Slam structure, Value Equation, M-A-G-I-C naming). Use whenever the user asks for "offer ideas", "offer variations", "different offers I could run", "ways to package my product", "how should I price/bundle/promote [offer]", "marketing offer generator", "give me offer angles", "test offers for [product]", or anything similar. Different from /marketing-ideas-generator — that one is about *how to market* (channels, growth moves); this one is about *what offer to present* (the wrapping around the same core product). Outputs a markdown file to 00-inbox/ by default, with 10–15 variations and a "Top 3 to test first" recommendation.
---

# Marketing Offer Generator

Take the user's product (or offer they name) and generate a ranked list of **offer variations** — different ways to package, present, price, or guarantee the same core thing. Each variation must be specific to _this_ product × _this_ audience, not generic playbook advice.

Output is a single markdown file in `00-inbox/`. That's it.

## What this skill is and isn't

**This skill is** about offer-level variation: should it be a $99 digital download, or a $499 cohort with a guarantee, or a $0 free trial that converts at month two, or a bundle with a partner's product? It generates concrete offer SKUs the user could actually run.

**This skill is not** the marketing channel skill. If the user asks "how do I get more leads" or "what channels should I post on", route them to `/marketing-ideas-generator` instead. The line: if the answer involves changing the _wrapping_ of what's sold, it's this skill. If the answer involves changing _where it's distributed_ or _what content runs around it_, it's marketing-ideas-generator.

## Before you generate anything

You need two things to produce variations that aren't generic:

1. **The offer** — what's being sold, current price, current format
2. **The ICP** — who it's for, in one line (role + the pain it solves)

### How to get them

**First, check the user's original message.** If they said _"give me offer variations for my $497 Notion template course aimed at remote PMs,"_ that's both — don't ask. Just go.

**If a project file is available, use it.** If the user points to an offer doc, ICP file, or business profile (or you can see one in the working directory), read it first. Pull what's there. Only ask about gaps.

**Ask only for what's missing — in one combined message.** If you have to ask, batch the missing pieces into a single short prompt:

> Quick — before I generate offer variations:
>
> 1. What are you selling? (offer + current price + format)
> 2. Who's it for? (one line: who they are + the pain it solves)

That's the whole intake. No "what have you tried", no funnel diagnosis, no fifteen-question discovery. Don't drip-feed follow-ups. If they push back or say "just generate it," make smart assumptions from whatever they did give, name the assumptions in one line at the top of the output, and proceed.

## The flow

1. **Confirm the inputs** above are in hand (from the message, a file, or the one-shot intake).
2. **Load both bundled reference files:**
   - `references/big-list-of-offers.md` — the menu of offer _types_ (discounts, free trials, bundles, guarantees, cohorts, payment plans, etc.).
   - `references/offers-playbook.md` — the theory: Grand Slam Offer build, Value Equation, M-A-G-I-C naming, guarantee taxonomy, scarcity/urgency plays.
3. **Generate 10–15 variations.** Each is a distinct offer SKU (not a tweak on the last one). Span the full menu — don't cluster all 12 around "discount + free trial". Aim for genuine variety: at least one performance-based, one bundle, one cohort, one no-money/access-based, one extreme premium, etc.
4. **Score and rank.** Pick a Top 3 the user should test first, based on fit-to-ICP, leverage, and operational cost.
5. **Write the file** to `00-inbox/{offer-slug}-offer-variations-{YYYY-MM-DD}.md`. Use today's date from system context. If `00-inbox/` doesn't exist, create it. Report the path in one sentence.

## How to generate variations that actually fit

For each variation, hold three things in your head at once:

- **A specific offer type from `references/big-list-of-offers.md`.** Don't invent a category — use one of the named types (Free Trial, Cohort, Bundle, Performance/Revshare, Pre-Order, etc.). This forces variety and grounds the suggestion.
- **A specific lever from the Value Equation** (Dream Outcome ↑, Perceived Likelihood ↑, Time Delay ↓, Effort & Sacrifice ↓). Which one is this variation primarily pulling? If you can't answer that cleanly, the variation is fuzzy — sharpen or drop it.
- **A specific pain or trigger from the ICP.** Tie it to language the user gave you (or, if working from a file, quote the doc). A variation that doesn't connect to a real pain is generic — drop it.

A variation without all three legs is filler. Better to ship 10 sharp variations than 15 with three duds.

## Output structure

Use `references/output-template.md` for the exact section layout. The shape, in summary:

```
# Offer Variations — {Offer Name}
Date · ICP · Current price/structure

## Inputs
(offer summary, ICP summary — plus any assumptions made if intake was partial)

## Variation 1 — {M-A-G-I-C styled name}
- Type: {from big-list}
- Hook: {one-line pitch}
- Mechanic: {how it works in practice}
- Value Equation Lens: {which lever}
- Price: {$ + structure}
- Guarantee: {type from playbook}
- Scarcity / Urgency: {which play}
- Why this fits the ICP: {pain or trigger}
- Operational cost: {low / medium / high — what it'd take to run}

## Variation 2 — ...
...

## Top 3 to Test First
1. **{Variation N}** — {why this is the highest-leverage first test}
2. ...
3. ...

## What I'd Skip (and Why)
{1–3 variations from the list I'd deprioritize, with one-line reasoning}
```

## Naming

Every variation gets a M-A-G-I-C-styled name (see `references/offers-playbook.md` — the M-A-G-I-C section). The Goal slot should hit the ICP's actual outcomes in their own words — what _they_ would call winning. Avoid generic SaaS-marketing names ("The Ultimate Founder Kit", "The Complete System").

## Guardrails

- **No more than 15 variations.** More is noise. Ten well-differentiated variations beats fifteen mediocre ones.
- **Don't propose offers the user can't actually fulfill.** If a variation depends on a team they don't have, partnerships not yet in place, or infrastructure that doesn't exist, flag it as "requires X first." When in doubt, assume solo operator and surface team-dependent variations with a clear flag.
- **Respect the user's voice.** No "transform your life" copy. The hook should sound like something the operator would actually say to a peer.
- **One file out, dated.** If a file with the same name exists, append a `-v2`, `-v3` suffix rather than overwriting — past variations are useful as a record.

## Reporting

After writing the file, one or two sentences:

```
Wrote: 00-inbox/{offer-slug}-offer-variations-{YYYY-MM-DD}.md
Generated 12 variations across 8 offer types. Top 3 recommended: #4 (Pre-Sale Cohort), #7 (Performance-Tied Membership), #9 (Founding Member Lifetime Deal).
```
