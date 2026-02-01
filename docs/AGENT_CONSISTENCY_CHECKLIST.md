## Forgotten Future – Agent Consistency Checklist

This document outlines recurring checks agents should perform to keep the **Forgotten Future** project internally consistent over time.

Use it as a **playbook** whenever you modify chapters, lore, or structure.

---

## 1. Timelines & Calendars

- **Source of truth**
  - Always treat `world-building/timeline/timeline.md` as the **authoritative chronology**.
  - `docs/timeline.md` is a **reader summary** and must stay aligned with the master timeline.

- **When you change time-related details**
  - If you adjust mission dates, era labels, or calendar terminology in chapters:
    - First update `world-building/timeline/timeline.md`.
    - Then mirror any necessary high-level changes into `docs/timeline.md`.
    - Finally, adjust individual chapter `**Timeline:**` headers to match.

- **Calendars to keep straight**
  - **AT (After Time):** Objective timeline (Year 0 AT = Moon Cataclysm / Great Fry).
  - **PF (After Pulse):** Core-internal calendar (PF = AT + 1000, e.g., Year 1015 PF = Year 15 AT).
  - Avoid inventing new calendar systems; if you absolutely must, add them to `world-building/facts.md` and the master timeline first.

---

## 2. Chapter Structure & Editions

- **Single shared structure**
  - The project uses a **unified 55-chapter structure** defined in `chapters/INDEX.md`.
  - Both the **YA** and **13+** versions share the *same* chapter files and order; differences live in tone and line edits, not in structure.

- **When adding/removing/renaming chapters**
  - Update **all** of the following in one pass:
    - `chapters/INDEX.md`
    - `docs/PLAN_YOUNG_ADULT.md`
    - `docs/PLAN_13_PLUS.md`
    - Any references in `manuscript/chapters.json` or `manuscript/*.md` synopsis files.
  - Re-run a quick search for the old chapter filename / number to catch stray references in:
    - `docs/`
    - `world-building/`
    - `manuscript/`

- **Edition-specific constraints**
  - **YA Version (`PLAN_YOUNG_ADULT.md`):**
    - Follow the “Simple & Assertive Style” from `docs/writing-strategies.md`.
    - Keep metaphors lean; emphasize Lem’s grounded POV.
  - **13+ Version (`PLAN_13_PLUS.md`):**
    - Avoid explicit religious terminology (prefer “Restoration”, “Awakening”, etc.).
    - Reduce heavy political/real-world genocide parallels; keep focus on immediate stakes and clear cause/effect.

---

## 3. Lore Source of Truth

- **Primary lore files**
  - `world-building/facts.md` – physical rules, entities, tech, cosmology.
  - `world-building/timeline/timeline.md` – chronological causal order.
  - `world-building/characters/*.md` – character arcs, personality anchors, fates.
  - `world-building/entities/*.md` and `world-building/settings/**/*.md` – specific species and locations.

- **Change order for lore**
  - When you want to change how something *works* (Vessel mechanics, Gorgon behavior, calendars, etc.):
    1. Update the relevant section in `world-building/facts.md` and/or the master timeline.
    2. Update character / entity files that depend on that rule.
    3. Only then adjust chapters, ensuring line-level prose matches the updated facts.

- **Never do**
  - Do **not** override lore in a chapter without updating the corresponding world-building document.
  - Do **not** introduce “galaxies” – the universe is scoped to the **solar system** (see the “No Galaxies” note in `world-building/facts.md`).

---

## 4. Handling Contradictions & Open Questions

- **Where to log / resolve contradictions**
  - Use `docs/OUTSTANDING_QUESTIONS.md` as the **central ledger** for:
    - Newly discovered contradictions.
    - Questions that need lore decisions.
    - Notes on how contradictions were resolved.

- **Workflow when you find a contradiction**
  1. **Confirm** which source should be authoritative (usually the master timeline + `world-building/facts.md`).
  2. **Add a short note** under “Newly Logged Contradictions / Watchpoints” in `OUTSTANDING_QUESTIONS.md` if the issue cannot be fixed immediately.
  3. If you do fix it:
     - Record the resolution briefly in the “Resolved (Authoritative) Answers” section or in a new bullet below.
     - Update all affected files (lore, chapters, plans) in the same change set.

- **Examples of good use**
  - Documenting one-year offsets (e.g., Year 24 vs Year 25 AT for late siege events) as “fog of history” decisions.
  - Capturing ambiguous off-screen logistics for Tor, Elowen, and Rahu as *intentional* mysteries once they’re settled in lore.

---

## 5. Character Consistency

- **Before changing a character in prose**
  - Read their profile in `world-building/characters/*.md`.
  - Check for:
    - **Birth era / age** (e.g., Arlo ~AT 1, mid-teens by Year 15 AT).
    - **Fate** (alive, dead, missing, reincarnated, etc.).
    - **Core beliefs / voice** (avoid flipping a character’s stance without an arc).

- **When updating a character arc**
  - Update:
    - Their character file in `world-building/characters/`.
    - Any related mission notes in `world-building/missions.md`.
    - Major arc summaries in `manuscript/synopsis.md` if the change is structural.

---

## 6. Chapter Timeline Headers

- **What to check**
  - Each chapter in `chapters/` has a `**Timeline:**` line near the top.
  - Ensure:
    - The **AT year** matches the master timeline (and PF year if present = AT + 1000).
    - The **mission label** (e.g., “Second Mission”, “Northern Shield”, “Third Mission Continuation”) agrees with `world-building/missions.md`.

- **When you shift events**
  - If an event moves across years or missions:
    - Update the chapter’s `**Timeline:**` line.
    - Update `world-building/timeline/timeline.md` and any mission entries affected.
    - Re-skim `NARRATIVE_INTEGRATION.md` to confirm its phase ranges are still correct.

---

## 7. Dual-Stream Prose Maintenance

- **When editing a chapter**
  - Check for both YA and 13+ blocks if they exist (often marked in planning sections).
  - Keep:
    - **Plot beats** identical between streams.
    - **Lore facts** identical between streams.
  - Adjust only:
    - Density of metaphor.
    - Directness of explanation.
    - Intensity of on-page violence / politics / spiritual language per each plan doc.

---

## 8. Quick Pre-Commit Consistency Checklist

Before committing substantial narrative or lore changes, quickly verify:

- **Timelines**
  - [ ] `world-building/timeline/timeline.md` reflects any new or changed events.
  - [ ] `docs/timeline.md` still matches the high-level shape of the master timeline.
  - [ ] Chapter `**Timeline:**` headers agree with the master timeline.

- **Structure**
  - [ ] `chapters/INDEX.md` still lists exactly 55 chapters in correct order.
  - [ ] `PLAN_YOUNG_ADULT.md` and `PLAN_13_PLUS.md` match the chapter index.

- **Lore & Characters**
  - [ ] Any lore changes are mirrored in `world-building/facts.md` (and related files).
  - [ ] Character ages, fates, and core traits remain consistent with `world-building/characters/*.md`.

- **Questions & Contradictions**
  - [ ] New contradictions are logged or resolved in `docs/OUTSTANDING_QUESTIONS.md`.
  - [ ] Long-standing watchpoints are not silently overwritten without comment.

If any item fails, either fix it immediately or leave a **clear note** in `OUTSTANDING_QUESTIONS.md` so future agents understand the current state of the canon.

---

## 9. Naming Conventions & Terminology

- **Protagonist name**
  - The Wood Vessel is **Lem** (short for "Lemon", a derogatory Core label). Use **Lem** consistently in all prose, character files, and documentation.
  - If you see "Ren" anywhere, it's a typo—replace it with "Lem".
  - Exception: Historical references to "Ren Protocol" or similar technical terms may exist in older docs; verify context before changing.

- **Character name consistency**
  - **Lynn** (Water Vessel) – her self-chosen name; use "Lynn" in narration and dialogue.
  - **Maya** – the public/media identity forced on Lynn by the Core; use "Maya" only when referring to:
    - The "Witch Maya" entity (After Time manifestation).
    - Historical Core propaganda.
    - The "Maya Match" technical sequence.
  - **Arlo** – human survivor, not a Vessel; consistently spelled "Arlo" (not "Arlow" or variants).

- **Place names**
  - Verify place names against `world-building/geography/geography.md`:
    - **Cradle Zero** (Desert Base / Fire City).
    - **Cradle Prime** (Lunar Pyramid).
    - **Ait-Aman** (The Water Village, High Enclave).
    - **The White Forest** (Silver Bight).
    - **The Ember Basin**, **The High Enclave**, **The Silver Bight** (major regions).
  - Do not invent new place names without adding them to the geography doc first.

- **Organization names**
  - **Technocratic Core** / **The Core** / **The Archivists** – all refer to the same organization; use contextually (Core = internal, Archivists = public-facing).
  - **The Voidsmen** – analog sanctuary dwellers (capitalized, plural).
  - **The Wuxan Pentad** – five northern villages (capitalized).

---

## 10. Elemental System (Wuxing) Consistency

- **The five elements**
  - **Wood (Mu)** – Lem's element; growth, structure, adaptation.
  - **Water (Shui)** – Lynn's element; cooling, flexibility, flow.
  - **Fire (Huo)** – Rahu's element; heat, power, destruction.
  - **Earth (Tu)** – Tor's element; stability, foundation, grounding.
  - **Metal (Jin)** – Vector and Metal Vessels; rigidity, precision, obedience.

- **Elemental interactions**
  - Water quenches Fire.
  - Wood provides structure for Water.
  - Fire melts Metal.
  - Earth grounds and stabilizes.
  - These interactions are **hard rules** from `world-building/facts.md`; do not override them in chapters.

- **Terminology**
  - Use "Wuxing" or "Wuxing causality" when referring to the system's philosophical basis.
  - Avoid mixing in other elemental systems (e.g., Western four elements, alchemy).

---

## 11. Technology Terminology

- **Core terms (use consistently)**
  - **Aether-Drive** – the Vessel's core system (anchors spirit, stores memory, provides energy).
  - **Synodic** / **Synodics** – the self-building machines (adjective and noun).
  - **Synanthropes** – humanoid Vessels (technical term).
  - **Gorgons** – Fire-aligned builders (also called "Builders" by themselves).
  - **Monoliths** / **Tripods** – large industrial machines (Monoliths = stadium-sized, Tripods = Wellsian-style Striders).

- **Reincarnation vs. Restoration**
  - **YA version:** Use "reincarnation" (spirits moving between containers).
  - **13+ version:** Use "Restoration" or "Reconstitution" (technical recovery process).
  - Never mix these terms within the same version.

- **Mission terminology**
  - Verify mission names and numbers against `world-building/missions.md`:
    - Mission 0 / First Mission: The Moon Mission (202X).
    - Mission 1 / Extinguish Phase (Year 15 AT).
    - Mission 2: Aggressive Expansion (Year 15 AT).
    - Mission 3: Northern Shield (Year 15 AT).
    - Mission Emissary: The White Forest (Year 15 AT).
    - Mission 5: The Red Tide and Lunar Assault (Year 25 AT).

---

## 12. POV & Narrative Voice

- **Lem's exclusive perspective**
  - The entire narrative is **Lem's POV only**. No other character serves as a POV narrator.
  - If an event occurs where Lem is absent, it must be recounted through:
    - Lem's later discovery (surveillance, reports, testimony).
    - Aetheric resonance / remote viewing.
    - Second-hand accounts Lem receives.

- **Human consciousness, not software**
  - Lem thinks like a **human**, not a robot. Avoid:
    - "Subroutines", "processors", "software tracking", "data streams".
  - Use instead:
    - "I felt a weight settle in the back of my head", "something heavy pressing on my thoughts", "a memory surfaced".

- **Retrospective disclosure**
  - Lem tells the story **after it happened**. He can use "I did not know then..." to fill in details learned later, but must highlight the **moment of discovery** as the primary source of revelation.

- **Style adherence**
  - Follow `docs/writing-strategies.md` and `manuscript/STYLE_GUIDE.md`:
    - Brief, declarative sentences.
    - Physical evidence over internal claims.
    - Clinical precision, everyday terms for the strange.
    - No domestic sentimentalism; emphasize institutional routine.

---

## 13. Cross-File Link Integrity

- **When renaming or moving files**
  - Search for references to the old filename/path in:
    - `chapters/INDEX.md`
    - `docs/PLAN_*.md` files
    - `manuscript/*.md` synopsis files
    - `world-building/missions.md` (chapter references)
    - Any README or contributing docs

- **Markdown link format**
  - Use relative paths: `[Chapter 1: Outpost](chapters/chapter_01_outpost.md)`
  - Verify links point to existing files (broken links break navigation).

- **Cross-references in prose**
  - If a chapter references another chapter by number or name, verify:
    - The referenced chapter exists.
    - The reference makes sense in context (e.g., "as I described in Chapter 16" only works if Chapter 16 actually contains that description).

---

## 14. Edition-Specific Terminology Checks

- **YA version checks**
  - [ ] Uses "reincarnation" (not "Restoration").
  - [ ] Can reference "slave labor" for Gorgons.
  - [ ] Can explore Selenite genocide themes explicitly.
  - [ ] Can use religious/political terminology from human history.
  - [ ] Allows retrospective spoilers ("I did not know then...").

- **13+ version checks**
  - [ ] Uses "Restoration" or "Reconstitution" (not "reincarnation").
  - [ ] Avoids the word "slave" (implies Gorgon status through behavior).
  - [ ] Frames Selenite absence as mystery (not explicit genocide).
  - [ ] Uses direct, tactical terms (avoids real-world controversy).
  - [ ] Avoids spoilers; discovery-first narrative.

- **Shared constraints (both versions)**
  - [ ] No "galaxies" (solar system only).
  - [ ] Lem's POV only.
  - [ ] Plot beats identical between versions.
  - [ ] Lore facts identical between versions.

---

## 15. Mission & Timeline Cross-Reference

- **Mission dates**
  - Verify mission dates in `world-building/missions.md` match:
    - Chapter `**Timeline:**` headers.
    - Master timeline entries in `world-building/timeline/timeline.md`.
    - Any mission summaries in `manuscript/synopsis.md`.

- **Mission labels in chapters**
  - Ensure chapter timeline headers use consistent mission labels:
    - "First Mission" / "Moon Mission" (202X).
    - "Second Mission" / "Aggressive Expansion" (Year 15 AT).
    - "Third Mission" / "Northern Shield" (Year 15 AT).
    - "Mission Emissary" / "White Forest" (Year 15 AT).
    - "Fifth Mission" / "Lunar Assault" (Year 25 AT).

---

## 16. Expanded Pre-Commit Checklist

Before committing substantial narrative or lore changes, verify:

- **Timelines**
  - [ ] `world-building/timeline/timeline.md` reflects any new or changed events.
  - [ ] `docs/timeline.md` still matches the high-level shape of the master timeline.
  - [ ] Chapter `**Timeline:**` headers agree with the master timeline.
  - [ ] Mission dates in `world-building/missions.md` match chapter timelines.

- **Structure**
  - [ ] `chapters/INDEX.md` still lists exactly 55 chapters in correct order.
  - [ ] `PLAN_YOUNG_ADULT.md` and `PLAN_13_PLUS.md` match the chapter index.
  - [ ] All chapter file links are valid (no broken markdown links).

- **Lore & Characters**
  - [ ] Any lore changes are mirrored in `world-building/facts.md` (and related files).
  - [ ] Character ages, fates, and core traits remain consistent with `world-building/characters/*.md`.
  - [ ] Place names match `world-building/geography/geography.md`.
  - [ ] Elemental interactions follow Wuxing rules from `world-building/facts.md`.

- **Naming & Terminology**
  - [ ] Protagonist is consistently "Lem" (not "Ren").
  - [ ] Character names match their profiles (Lynn vs Maya usage is correct).
  - [ ] Technology terms are consistent (Aether-Drive, Synodic, Synanthropes, etc.).
  - [ ] Edition-specific terminology is correct (reincarnation vs Restoration).

- **POV & Style**
  - [ ] Narrative is Lem's POV only (no other character perspectives).
  - [ ] Lem thinks like a human (no "subroutines" or "processors").
  - [ ] Style matches `docs/writing-strategies.md` and `manuscript/STYLE_GUIDE.md`.

- **Questions & Contradictions**
  - [ ] New contradictions are logged or resolved in `docs/OUTSTANDING_QUESTIONS.md`.
  - [ ] Long-standing watchpoints are not silently overwritten without comment.

If any item fails, either fix it immediately or leave a **clear note** in `OUTSTANDING_QUESTIONS.md` so future agents understand the current state of the canon.

