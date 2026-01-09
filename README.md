# Forgotten Future: The Story

This repository contains the narrative foundation and manuscript for **Forgotten Future**, an AI-driven science fiction epic. This project is a companion to the `ff-teaser` and the upcoming game project.

## Vision: AI-Driven & Open Source

This is an **AI-Driven Story**. This means the bar for narrative depth, consistency, and descriptive fidelity is set extremely high. We leverage AI to maintain complex world-building "facts," simulate character motivations, and ensure causality is never sacrificed for convenience.

**Current Stage: Chapter Planning (Phase V)**
The chapters in this repository are **planning documents**, not prose. They function like detailed chapter synopses or "for dummies" outlines—structured narratives that define plot, character arcs, world-building integration, and key scenes. These planning documents will be used as source material for generative AI agents to produce the full prose manuscript in Phase VI.

**Workflow:**
1. **Phase V (Complete):** Create comprehensive chapter planning documents
2. **Lore Hardening:** Use `QUESTION_RESOLUTION_PROMPT.md` to resolve plot holes and ambiguities through iterative AI dialogue.
3. **Phase VI (Next):** Use AI agents to generate full prose narrative from chapter plans using `CHAPTER_PLANNING_PROMPT.md`.
3. **Phase VII:** QA/refinement and editorial review
4. **Release:** First edition hardcopy publication
5. **Evolution:** The book will continue to receive refinements, corrections, and expansions over time—like software with regular updates and new editions

**Perpetual Early Release:** This project is open-source and public-access from day one. Anyone can watch the story evolve, contribute lore, fix inconsistencies, or even refine chapters.

**Community Rewards:**
- All contributors are credited.
- Significant contributions earn a share of publishing returns (details to be finalized in a future `CONTRIBUTING.md`).
- Helping is easy: use GitHub to add files or send pull requests.

## Project Roadmap (Waterfall Phases)

1.  **Phase I: Foundation (The Lore):** ✅ Define the universe "Facts", history, and the state of physics/technology.
2.  **Phase II: Dramatis Personae (The Cast):** ✅ Define characters, motivations, and arcs.
3.  **Phase III: Cartography & Chronology (The Stage):** ✅ Map out settings and the timeline.
4.  **Phase IV: Structural Outline (The Skeleton):** ✅ Divide the story into major Acts/Arcs.
5.  **Phase V: Detail Refinement (The Pulse):** ✅ Complete chapter-by-chapter planning documents.
6.  **Phase VI: Narrative Composition (The Meat):** 🚧 **IN PROGRESS** — Drafting the manuscript.
7.  **Phase VII: Polish & Review (The Skin):** Scheduled after Phase VI completion.

## Story Connections

This story is directly linked to the teaser found in [ff-teaser](../ff-teaser). The events of "Stars Die" (the destruction of the moon, the arrival of the Tripods) are the catalyst for our narrative.

## Manuscript Progress

**Current Stage:** Phase V Complete — Chapter Planning Documents Finished (13 chapters)
**Next Stage:** Phase VI — AI-Generated Prose Composition

The 13 chapters listed below are **planning documents** (structured synopses with plot beats, character arcs, world-building notes, and critical questions). These will be fed to AI generative agents to produce full prose narrative with descriptions, dialogue, and sensory detail.

**Chapter Planning Complete (Phase V ✅):**
- Chapter 1: An Ordinary Distance — Lem's suburban life shatters
- Chapter 2: Lynn — Lynn arrives and forces activation
- Chapter 3: The Doorway — Lem discovers his nature; compulsion installed
- Chapter 4: Drafted — Lem embedded with soldiers; anti-gravity tech revealed
- Chapter 5: The Briefing He Never Had — Soldiers discuss psychological warfare
- Chapter 6: The Near Moon — Moon's true nature confirmed
- Chapter 7: Zenith — Soldier crisis; Lynn's ruthless authority; Novak executes
- Chapter 8: The Shattered Approach — Tor broadcasts; Moon fragments; The Caucasian Eagle destroyed
- Chapter 9: Waking in the Dream and the Rescue — Lem survives; Aether-Drive activated; isolated on lunar surface
- Chapter 10: Alone on the Moon — Lem joins strike team; plasma cannon engagement; Rahu emerges as threat
- Chapter 11: Rahu — Lem recognizes Rahu; Tor sacrifices Hermes; Novak assumes command; mission continues
- Chapter 12: The Pyramid — Strike force reaches pyramid sanctuary; Tor returns alive; Rahu revealed to be alive inside; soldiers prepare for battle
- Chapter 13: The Confrontation — Soldiers engage Rahu; Lynn merges with Lem; Rahu is stasis-paralyzed; Lynn dissolves into Lunar Capacitor; Iris realizes reset plan

**Next Planning:** Chapters 14+ (Great Fry sequence, transition to After Time)

**Key Story Elements Established:**
- Ships: **The Caucasian Eagle** (Lynn/Novak/Lem vessel; destroyed in Ch. 8) and **Hermes** (Tor's flagship; sacrificed in Ch. 11)
- Core Characters: Lem (Wood Vessel; merged with Lynn; carries her absence), Lynn (Water Vessel; dissolved into Lunar Capacitor to initiate reset), Tor (Earth Vessel; burned and helpless; witness to reset), Novak (Core operative; intelligent observer; calculates impossible truths), Rahu (Fire Vessel; defeated and paralyzed; present but irrelevant)
- Mission: Lunar strike team; false pretenses; actual purpose obscured by information warfare; transforms into pyramid confrontation; culminates in solar system reset
- Cataclysm Trigger: Lunar Capacitor discharge shatters the Moon; Tor sacrifices Hermes; pyramid emerges as sanctuary and battleground; Lynn activates system to initiate complete reset
- The Reset: Lynn merges with Lunar Capacitor; initiates "massive short circuit"; entire solar system will be unmade and reconstituted

## How to Contribute

1.  Check [world-building/facts.md](world-building/facts.md) to understand the rules of the universe.
2.  Browse [world-building/characters/](world-building/characters/) to meet the cast.
3.  Review [chapters/INDEX.md](chapters/INDEX.md) to understand the narrative structure and planning format.
4.  Read [.github/copilot-instructions.md](.github/copilot-instructions.md) for narrative standards and consistency framework.
5.  **For Phase V (Chapter Planning):** Edit chapter planning documents directly. Suggest structural changes, add critical questions, refine character arcs.
6.  **For Phase VI (Prose Generation):** Help draft prompts for AI agents or refine generated prose for narrative coherence and emotional impact.
7.  Propose changes via Pull Requests.

## Project Structure

```
ff-story/
├── README.md (this file)
├── synopsis.md (high-level narrative summary)
├── world-building/
│   ├── facts.md (canonical world facts; source of truth)
│   ├── timeline/timeline.md (chronological events)
│   ├── characters/ (individual character profiles)
│   ├── entities/ (mechanical beings, Synodics, etc.)
│   └── settings/ (locations: Earth, Moon, etc.)
├── chapters/ (chapter planning documents; Phase V output)
│   ├── INDEX.md (master chapter index)
│   ├── chapter_01_through_09.md (planning documents)
│   └── CHAPTER_PLANNING_PROMPT.md (system prompt for collaborative planning)
├── QUESTION_RESOLUTION_PROMPT.md (iterative system for hardening lore/plot)
└── .github/copilot-instructions.md (AI assistant directives; narrative standards)
```

## Documentation

- **[chapters/INDEX.md](chapters/INDEX.md)** — Master index of all chapter planning documents with section organization
- **[world-building/facts.md](world-building/facts.md)** — Canonical world facts; "source of truth" for all narrative decisions
- **[synopsis.md](synopsis.md)** — High-level narrative overview from prologue through Year 15 AT
- **[.github/copilot-instructions.md](.github/copilot-instructions.md)** — Complete narrative framework including Core Directives, Character Tracking, Known Contradictions, and Contradiction Resolution Protocol
