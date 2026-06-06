# Library Index

*Consult this index when asked to use the library or a specific entry. Scan for the relevant file, load it, then proceed.*

---

## Marketing

- `marketing/cold-outreach.md` — DM and email outreach scripts, sequences, follow-up cadence | when running direct outreach for validation, sales, or partnership
- `marketing/reddit-distribution.md` — organic traction from subreddits without getting banned | when distributing content or offers on Reddit
- `marketing/producthunt-launch.md` — full PH launch sequence: prep, launch day, follow-up | when planning or executing a Product Hunt launch

## Offers

- `offers/offer-validation.md` — validation ladder (calls → waitlist → pre-sale → manual delivery), call framework, pre-sale mechanics | before building or pricing any offer
- `offers/big-list-of-offers.md` — reference catalog of offer types (free trial, bundle, guarantee, cohort, etc.) | when brainstorming ways to package or price an offer (powers `/marketing-offer-generator`)

## Playbooks

- `playbooks/offers.md` — Offers Playbook: Grand Slam Offer structure, Value Equation, M-A-G-I-C naming | when constructing or naming an offer

## Checklists

- `checklists/github-actions-docker-deploy-checklist.md` — end-to-end checklist for shipping a containerized app to a server via GitHub Actions | when setting up CI/CD, Docker deploys, or server provisioning

## Swipe Files

- `swipe-files/x-twitter/leila-hormozi-x-posts.md` — @LeilaHormozi X/Twitter post swipe file | when studying high-performing short-form hooks and structures

## Voice Profiles

Reference voice profiles writer skills load verbatim (`/twitter-x-post-writer`, `/linkedin-post-writer`, `/video-scripts-and-captions-generator`). Build new ones with `/voice-cloner`.

- `voice-profiles/voice-alex-hormozi-tweets.md` — Alex Hormozi tweet voice (punchy, value-dense)
- `voice-profiles/voice-hrefs-blog.md` — Ahrefs blog voice (practical, SEO-savvy long-form)
- `voice-profiles/voice-paul-graham-blog-posts.md` — Paul Graham essay voice (plain, argumentative)
- `voice-profiles/voice-tim-urban-wait-but-why-blog.md` — Tim Urban / Wait But Why voice (conversational, deep-dive)

---

## Templates — Pointer Index

Templates live **co-located** with the folder they get used in, as hidden dotfiles named `.[name].template.md`. Read the template in place, then create a new file in the same folder (without the leading dot, with a real name) and fill it in. Never edit the dotfile itself.

### Command center (01)
- `01-command-center/goals/.[year]-annual.template.md` — annual goal structure
- `01-command-center/goals/.[year]-[q#].template.md` — quarterly goal structure
- `01-command-center/projects/.[project].template.md` — project brief with slug, status, milestones

### Research (02)
- `02-research/ideal-customer-profiles/.[revenue-range]-[title]-profile.template.md` — ideal customer profile by segment × stage

### Offers (04)
- `04-offers/.[offer-validation].template.md` — offer validation worksheet (calls, waitlist, pre-sale)

### Products (05)
- _(no template yet — add a `.[product].template.md` scaffold when the first product spec is authored)_

### Marketing — content (06)
- `06-marketing/blog/` — **stage-folder pipeline** for blog posts. Each stage is a top-level folder (`00-brief/ → 05-final/`) holding one file per post, prefixed with the stage and sharing a slug (`BRIEF-{slug}.md` → `DUMP-{slug}.md` → `OUTLINE-{slug}.md` → `DRAFT-{slug}.md` → `REVIEW-{slug}.md` → `FINAL-{slug}.md`). To start a new post, copy an existing `BRIEF-{slug}.md` in `00-brief/`, rename to the new slug, and rewrite it. `01-dump/` can hold either a single `DUMP-{slug}.md` file (single-note dump) or a `DUMP-{slug}/` folder (multi-file research pile).
- `06-marketing/content/email/broadcasts/.[broadcast].template.md` — one-off email broadcast
- `06-marketing/content/email/newsletters/.[newsletter].template.md` — weekly newsletter issue
- `06-marketing/content/shorts/.[shorts].template.md` — YouTube Shorts / Reels script
- `06-marketing/content/social/instagram/posts/.[instagram_post].template.md` — Instagram caption + visual notes
- `06-marketing/content/social/linkedin/posts/.[linkedin_post].template.md` — LinkedIn post
- `06-marketing/content/social/twitter/posts/.[twitter_post].template.md` — Twitter/X thread or single post
- `06-marketing/content/youtube/packaging/.[youtube_packaging].template.md` — title, thumbnail, description, tags
- `06-marketing/content/youtube/scripts/.[youtube_script].template.md` — full YouTube video script

### Marketing — paid (06)
- `06-marketing/paid-ads/campaigns/.[campaign].template.md` — paid ad campaign brief

### Customers (08)
- `08-customers/onboarding/.[onboarding].template.md` — customer onboarding flow

### Team (09) — Stage 3+
- `09-team/hiring/.[role_scorecard].template.md` — outcomes-first role scorecard
- `09-team/onboarding/checklists/.[onboarding_checklist].template.md` — per-hire onboarding checklist
- `09-team/performance/1-1s/.[one_on_one].template.md` — running 1:1 log
- `09-team/performance/reviews/.[performance_review].template.md` — quarterly performance review
- `09-team/leadership/objectives-and-key-results/.[okrs].template.md` — quarterly company + team Objectives and Key Results

### Operations (10)
- `10-operations/sops/.[sop].template.md` — standard operating procedure

### Snapshots — captain's logs (96)
- `96-snapshots/captains-logs/daily/.YYYY-MM-DD.template.md` — daily snapshot
- `96-snapshots/captains-logs/weekly/.[year]_week_[#].template.md` — weekly review snapshot
- `96-snapshots/captains-logs/monthly/.[YEAR]_[month].template.md` — monthly snapshot
- `96-snapshots/captains-logs/yearly/.YEAR.template.md` — yearly review snapshot

### Archived
Templates without a single clean output home, or that duplicated other scaffolds, are stored at `99-archives/` for reference but not actively used:
- `decision_log_entry_template.md` — paste-into-file entry, not a standalone document
- `email_sequence_template.md` — fits either `03-audience/email-list/sequences/` (nurture) or `07-sales/email-sequences/` (sales); resolve before un-archiving
- `launch_template.md` — overlaps with offer launch scaffolding (see `04-offers/`)
- `monthly_template.md`, `weekly_template.md` — superseded by the snapshot dotfile templates above
