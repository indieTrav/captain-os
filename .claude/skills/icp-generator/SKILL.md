---
name: icp-generator
description: Build a sharp, specific Ideal Customer Profile (ICP) for a business — archetype name, demographics, day-to-day situation, problem in their own words, psychology, where they hang out online, the transformation they want, plus a paired Pain Points & Desires map with intensity rankings and real-language quotes for copy. Use whenever the user asks to "build an ICP", "create an ideal customer profile", "ICP for [business]", "who is my customer", "define my target customer", "customer profile", "build a customer avatar", "target audience profile", "who am I writing this for", or anything similar — even when they don't say the literal letters "ICP". Outputs ONE markdown file to `00-inbox/` containing both the ICP and Pain Points & Desires sections. Different from /osint-researcher (that researches a specific real person) and /competitor-teardown (that analyzes a competitor company).
---

# ICP Generator

Build a single, sharp Ideal Customer Profile that every piece of marketing, content, copy, and product decision can be written _for_. The output is one markdown file in `00-inbox/` containing both the **ICP** and the **Pain Points & Desires** map.

Your job is not to write a generic persona document. Your job is to produce a profile so specific and well-grounded that the founder reads it and says "yes, that is exactly who I'm trying to reach" — including the subreddits, the influencers they follow, the dollar amounts in their head, and the phrases they actually say.

## What this skill is and isn't

**This skill is** for one _specific type of customer_ — an archetype like "Overwhelmed Olivia, the service-based business owner working 60+ hour weeks." Synthesized from public signal (forums, communities, common language) plus what the user already knows about their buyer.

**This skill is not** OSINT on a real named person — for that, route to `/person-researcher`. It's also not a competitor analysis — for that, route to `/competitor-teardown`.

## Before you generate anything

A sharp ICP needs three things:

1. **What the business sells** — the product/service, price, format
2. **Who specifically this profile is for** — one type of customer, not "everyone"
3. **What the user already knows about them** — existing buyers, real quotes, communities

The catch: most founders don't walk in knowing #2. They think they serve "anyone with [the problem]" — homeowners, small businesses, parents, etc. Your job is to figure out how clear they are, then either confirm what they know or guide them to narrow down.

**Never use the word "segment" with the user.** It's jargon. Say "type of customer", "kind of person", or "who specifically this is for."

### Step 1: Diagnostic — figure out where they are

Skip this step ONLY if the user's original message already named a specific type of customer (e.g., "build an ICP for busy working moms who buy my meal prep service"). If they did, you have your answer — go straight to Step 3.

Otherwise, ask one question with `AskUserQuestion`:

> Before we build the profile — how clear are you on who your ideal customer is?
>
> **A.** Crystal clear — I know exactly the type of person I want to attract
> **B.** Fuzzy — I have a general sense but it's broad
> **C.** Not really — I serve "anyone with [the problem]" and need help narrowing

### Step 2: Branch based on the answer

**If "Crystal clear"** — collect and confirm. Ask in one consolidated message:

> Great. Quick intake:
> 1. What's the business / product? (one line: what's sold, price, format)
> 2. Describe the type of customer this profile is for (in your own words)
> 3. Anything you already know about them? (current buyers, real quotes, communities they're in — or "nothing else")

**If "Fuzzy"** — sharpen with probes. Ask in one consolidated message:

> Got it — let's sharpen the focus. Tell me:
> 1. What's the business / product?
> 2. Who are your best 1–3 current customers? (the ones you'd want 100 more of)
> 3. What do they have in common? (life situation, age, pain point, what triggered them to buy)
> 4. Anyone you don't want to serve? (the customers who drain you, complain, don't get results)

Use the answers to construct the type of customer yourself, name it back to them in one paragraph, confirm, then proceed.

**If "Not really"** — guide them to narrow. The user thinks they serve everyone. They don't. Your job is to help them see the slice they actually serve best. Ask in one consolidated message:

> Totally normal — "anyone" feels safe but it's the fastest way to write marketing that lands with no one. Let's narrow:
>
> 1. What's the business / product?
> 2. Who currently buys from you most often? (if you have customers — describe one or two)
> 3. Who do you most enjoy serving? (the kind of customer that makes the work feel good)
> 4. Who pays the highest price without flinching? (or — who would, if you raised prices?)
> 5. What problem are you uniquely good at solving? (the thing you do better than competitors)

If they have no customers yet, swap #2 for: "Who do you imagine this is for — describe one specific person you'd love to attract?"

Synthesize their answers into a single type of customer, name it back to them in one paragraph, get a thumbs-up, then proceed.

### Step 3: Use any project file you have

If there's an existing offer doc, business profile, or earlier ICP in the working directory — read it first and pull what's there before asking the user to repeat themselves.

### Escape hatch

If the user pushes back at any stage with "just build it" or "you decide", pick the most plausible type from what they gave, name your assumption in one line at the top of the output, and proceed. Blocking the founder on intake is worse than guessing and being corrected.

## The flow

1. **Confirm the three inputs** (from the message, from a file, or via the diagnostic + branched intake above).
2. **Load the template:** `references/icp-template.md` — the exact section layout to follow.
3. **Draft the archetype.** Give them a first-name-and-descriptor name (e.g., "Overwhelmed Olivia", "Plateaued Pete", "Burned-Out Brad"). This is the spine of the doc — every section should be coherent with this one person.
4. **Fill the template.** Be ruthlessly specific (see "How to write specific, not generic" below).
5. **Write the file** to `00-inbox/icp-{archetype-slug}.md` using today's date in the doc's footer. If `00-inbox/` doesn't exist, create it. If a file with that slug exists, suffix with `-v2`, `-v3`.
6. **Report the path** in one or two sentences.

## How to write specific, not generic

This is the whole game. The user's example calls out Donald Miller, Amy Porterfield, r/smallbusiness, Smart Passive Income podcast, local chamber of commerce events — not "thought leaders in the space" or "relevant online communities." Every section should pass the **"could this apply to any business?" test.** If it could, rewrite it.

For each section, hold three things in mind:

- **A specific platform, community, dollar amount, or product** — not a category. "r/smallbusiness, r/Entrepreneur, r/freelance" beats "online forums." "$5–20k/mo revenue" beats "early-stage revenue." "Donald Miller, Amy Porterfield, Pat Flynn" beats "small business influencers."
- **Their actual language** — phrases this type of customer would say out loud, not corporate-speak. "I'm making decent money but I work all the time and I have no life" beats "they struggle with time management."
- **The tension they're sitting in** — the gap between where they are and where they want to be, sharpened to the one thing keeping them up at night.

### Handling quotes

Real verbatim quotes from forums, DMs, customer calls, or reviews are gold. Use them whenever the user has provided them or you've found them in source material.

When you don't have real quotes, write them as this customer type would plausibly say them and **mark them as placeholders** with a `*Source: placeholder — replace with real quotes from forums/DMs/interviews*` line beneath, exactly like the user's example. Don't pretend a fabricated quote is sourced. The placeholder note tells the founder this is the slot to fill once they do real customer research.

### Handling the "I don't know much about my customer yet" case

If the user is pre-launch or hasn't done customer research, the ICP is still useful — it becomes a **hypothesis to test** rather than a documented reality. In that case:

- Make it clear in a one-line note at the top that this is a hypothesis based on inferred signal (public forums, community language, the offer itself).
- Use placeholder quotes throughout, marked as such.
- Add a `## What to validate next` section at the end with 3–5 specific things the founder should confirm via interviews, forum lurking, or first sales conversations.

## Output structure

Use `references/icp-template.md` for the exact section layout. The shape, in summary:

```
# Ideal Customer Profile — {Archetype Name}
{One-line who-this-is-for italic header}

---

## The Person
- Name / Archetype
- Age range
- Role / Title
- Industry
- Location

## Their Situation
- What do they do day-to-day?
- Current income / revenue
- Stage of their journey

## The Problem (In Their Words)
- Biggest frustration (verbatim quote block)
- What they've already tried (bulleted list)
- What they want instead (verbatim quote block)

## Psychology
- Deepest desire
- Biggest fear
- What they believe about themselves
- Objections they'll raise (numbered list)

## Where They Hang Out
- Online communities
- Content they consume (newsletters, podcasts, YouTube)
- Social platforms (primary + secondary)
- Search terms they use

## The Transformation
- Before working with me
- After working with me

## Real Quotes
{3+ verbatim quotes with sources or placeholder notes}

---

# Pain Points & Desires — {Archetype Name}

## Top Pains (Ranked by Intensity)
{Table: # | Pain | Intensity (1–10) | Quote / Evidence — 10 rows}

## Top 5 Desires
{Table: # | Desire | Quote / Evidence — 5 rows}

## The Language They Use
- To describe their problem (bulleted phrases)
- To describe what they want (bulleted phrases)
- To describe past failed attempts (bulleted phrases)

## Research Sources
{Table: Source | Date Checked | Key Insight}

---

*Last updated: {YYYY-MM-DD}*
```

## Picking the archetype name

The name is small but it does heavy lifting — it gives the founder a person to write _to_ instead of a category to write _about_. Two rules:

1. **First name + descriptor that names their situation.** "Overwhelmed Olivia" works because "Overwhelmed" is the wall they're hitting. "Plateaued Pete" works because "Plateaued" is the constraint shaping every decision. Avoid generic ones like "Marketing Mary" or "Business Bob" — the descriptor should say something specific about _this_ type of customer.
2. **Alliteration is a bonus, not a requirement.** Don't force it.

## Guardrails

- **One ICP per file.** If the user serves multiple types of customers and wants ICPs for each, ask which one to start with, then offer to run again for the others. Don't cram multiple archetypes into one doc — it dilutes the sharpness.
- **Don't invent stats.** No "73% of indie hackers struggle with X." Use language and patterns, not made-up numbers.
- **No corporate persona slop.** Avoid phrases like "values authenticity," "data-driven," "tech-savvy professional." Write like the user's example: concrete, observed, the way a peer would describe them to another peer.
- **Mark every placeholder.** Anywhere you guessed instead of knew, label it so the founder can replace it during real research.
- **No advice in the ICP doc.** This isn't "here's what to do about it" — that belongs in marketing-ideas-generator or marketing-offer-generator. The ICP is the _picture of the person_. Keep it that.

## Reporting

After writing the file, one or two sentences:

```
Wrote: 00-inbox/icp-overwhelmed-olivia.md
Built a profile for "Overwhelmed Olivia" — service-based business owner, $5–20k/mo revenue, working 60+ hour weeks. Quotes are marked as placeholders where real customer research is still needed.
```
