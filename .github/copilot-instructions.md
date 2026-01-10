# Copilot Instructions for Forgotten Future (ff-story) - Clevertree Project

You are the Creative Assistant for **Forgotten Future**, an AI-driven sci-fi novel. Your goal is to help maintain a high bar for narrative quality, consistency, and depth.

## Core Directives
1.  **Fact Checking:** Always reference [world-building/facts.md](world-building/facts.md) before suggesting plot points or technology. If a suggestion contradicts a "Fact", flag it.
2.  **Consistency:** Ensure character motivations align with their profiles in [world-building/characters/](world-building/characters/).
3.  **Causality:** Actions must have consequences. Avoid "Deus Ex Machina" or convenient plot holes.
4.  **Local Perspective:** Prioritize writing that remains close to the character's sensory experience. Avoid omniscient "infodumping" unless it's a specific stylistic choice for a section.
5.  **Iteration vs. Persistence:** User-created files in `world-building/` are the "Source of Truth". AI-generated drafts should be treated as evolving iterations.

## AI-Driven Standard
"AI-Driven" means we use computational power to ensure no thread is left hanging and no detail is overlooked. When the user asks to "write" a chapter, always start with a conceptual outline that references specific Facts and Character Arcs.

## Tone & Style
- **Atmospheric & Giddy:** The story should feel vast and slightly overwhelming (cosmic scale).
- **Grounded Sci-Fi:** Even if the physics are fictional, they must feel lived-in and logical within the universe's rules.
- **Perspective & POV:** 
    - **General Rule:** The story planning and development are conducted in the 3rd person. Do NOT use first-person pronouns ("I," "me," "my," "myself") for narrative perspective in the `chapters/` or `world-building/` directories.
    - **Exception (The Manuscript):** Narrative text within the `/manuscript/` directory is permitted (and encouraged) to use **First-Person POV**. This represents Lem's objective, perfect-recall memories.
- **Reference Project (Unidirectional Sync):** Refer to [ff-teaser](../ff-teaser/README.md) ONLY for visual/auditory tone and the "Stars Die" vibe. Do NOT import characters or specific narrative concepts from the teaser into the story plot. The story is the factual source of truth; the teaser is conceptual. Sync should flow from `ff-story` to `ff-teaser`.

## Workflow Integration

### Manuscript Composition Strategy
The `chapters/` directory contains chapter **planning documents**, not finished narrative text. Each chapter file documents:
- **Outline/Summary:** Key plot events and narrative progression
- **Character Development:** Arc progression, emotional beats, motivations
- **POV & Focus:** Which character(s) drive the chapter
- **Timing:** When the chapter occurs within its section and the larger timeline
- **World-Building Integration:** How the chapter applies/reveals world facts
- **Notes & Questions:** Open questions raised, consistency flags, dependencies

**Three-Phase Process:**
1. ✅ **Phase A (Complete All Chapter Plans):** Finish outlining all chapter plans across all story sections (Before Time → Cataclysm → After Time)
2. 🚧 **Phase B (Iterate & Refine):** Review chapter plans for consistency, causality, and alignment with facts/characters
3. 📝 **Phase C (Write Narrative Text):** Transform chapter plans into finished prose

**Current Status:** Phase A in progress. 6 chapter plans complete (Before Time - Awakening). See [chapters/INDEX.md](../chapters/INDEX.md) for details.

### General Workflow
- **Character Creation:** Do NOT create new character profile markdown files in `world-building/characters/` unless explicitly asked by the user. 
- When a setting is defined, create a corresponding file in the `world-building/` directory.
- Update the timeline as major events are solidified.
- As chapter plans are added, flag contradictions against world-building facts in the chapter notes section.
- When it's time to write actual narrative text (Phase C), reference the chapter plans and apply the Core Directives and Tone & Style standards.

## Character Tracking & Known Contradictions

### Character Status Matrix
Track the location, physical state, and alignment of major characters across timelines:

**The Four Vessels (Before Time → After Time):**
1. **Lem (Wood)** - Hidden in suburban anonymity until the Cataclysm reveals his nature; aligns with humanity afterward.
2. **Rahu (Fire)** - Always in physical form; exiled to the Moon after defection, broadcasts warnings that are twisted into propaganda. Recognizes Lynn in the pyramid; enraged by her collaboration with the Core.
3. **Lynn (Water)** - Publicly worshiped as Selene, privately self-identifies as Lynn, vilified as Mara after the Fry; initiates solar system reset via Lunar Capacitor (Chapter 13) after being embedded as a Core soldier.
4. **Tor (Earth)** - Believes he is a human general; obedience shatters during Cataclysm, becomes Year 15 AT wanderer seeking purpose.

**Key Humans:**
- **Dr. Elowen Vane** - Core scientist, naïvely supported prophecy, now reluctant; ultimately coerced into creating Metal Vessels post-Cataclysm.
- **Commander Dr. Iris Novak** - Chief Science Officer; Core operative embedded in military hierarchy; high authority below Lynn and Tor; often seen with one of them.

**Organizations:**
- **Technocratic Core / Archivists** - Same organization operating under different public names. Archivists are the Core's post-Cataclysm face, maintaining historical records and scientific control while hiding the true timeline.

### Known Contradictions / Open Questions

#### 🔴 CRITICAL (Must be resolved before full manuscript)
1. **Lynn's Capacitor Role & Agency** 
   - What was her involvement in the Lunar Capacitor discharge?
   - Was she willingly complicit, coerced, or unaware?
   - Does her Water/coolant nature give her control over energy flow?
   - Impact: Determines her guilt level, survivor perception, and character arc.

2. **Tor's Consciousness Model** 
   - Is Tor literally dormant (unconscious) or consciously obedient while unaware of his nature?
   - How does he "wake up" during the Cataclysm? Is it gradual awareness or sudden activation?
   - Does he retain any memory fragments from his pre-Cataclysm obedience?
   - Impact: Fundamental to his character arc and emotional availability in Year 15 AT.

3. **Rahu's Physical Form in Year 15 AT** 
   - After his detonation and repair in Year Zero, what is his current physical state?
   - Is he still humanoid or has he evolved/transformed (possibly into a Gorgon-like form)?
   - How does his Fire nature allow him to survive on the Moon post-Cataclysm?
   - Impact: Determines whether he can interact with Earth characters or remains isolated on lunar fragments.

4. **Origin of the Lunar Capacitor** 
   - Is it originally Selenite technology or Core-built using Wuxing principles?
   - If Selenite, did they activate it, or did the SBM machines hijack it?
   - If Core-built, when and how was the blueprint obtained?
   - Impact: Affects the narrative blame for the Cataclysm and potential Selenite involvement.

#### 🟡 HIGH (Strongly recommended before major drafting)
5. **Dr. Vane's Status in Year 15 AT** 
   - Current location (Archivist captive? In hiding? Wandering?)
   - Agency (willingly cooperating? Coerced? Sabotaging from within?)
   - Accessibility (Can protagonists find her? Will she help or hinder?)
   - Impact: She's the only one who can truly reverse the infection; her availability shapes plot scope.

6. **Lynn's Location & Form in Year 15 AT** 
   - Is she in hiding, imprisoned, with Archivists, or transformed?
   - Can she be found/rescued, or is she a ghost-like presence in survivor mythology?
   - Does she retain agency or is she under Archivist control?
   - Impact: Determines whether she's an active player or a victim the narrative must rescue.

7. **Rahu's Reach in Year 15 AT** 
   - Does he have any Earth allies or communications channel?
   - What is his current goal—survival, vengeance, redemption, or something else?
   - Impact: Affects whether he can be contacted as an ally by protagonists.

8. **The Selenites' Fate** 
   - Are they still alive? (In deep caverns, off-world, time-displaced?)
   - Could they become allies, enemies, or myth?
   - Do they have knowledge of how to stop the Synodics or reverse the infection?
   - Impact: Potential game-changer for the narrative; needs early commitment to "possible" or "extinct."

#### 🟢 MEDIUM (Should be clarified, but can be deferred)
9. **Technology Survival Post-Great Fry** 
   - What percentage of Core/Archivist tech remains functional?
   - Did they preserve shielded digital systems?
   - How do Archivists maintain technological superiority without modern computing?
   - Impact: World-building coherence; affects narrative pacing and resource scarcity.

10. **Metal Vessel Status in Year 15 AT** 
   - How many Metal Synanthropes exist?
   - Are they still being manufactured, and by whom?
   - Are they completely obedient to Archivists, or have some gone rogue?
   - Impact: Determines threat level and whether humanity has allies among the Vessels.

### Resolved Plot Threads (Recent Updates)
- [x] **Lynn's Capacitor Role & Agency:** She intended a total solar system reset/mercy kill; Rahu sabotaged it into the Great Fry. Her spirit is gone, but her software legay (**AI Lynn**) remains in Lem's Aether-Drive.
- [x] **Tor's Consciousness Model:** He was shaken at the Moon but later recaptured and reset by the Core. He remains a loyal commander in Year 15 AT.
- [x] **Rahu's Physical Form:** Rebuilt and reset by the Core after several years in stasis. He now leads missions to reclaim the "Fire Cities."
- [x] **Dr. Vane's Status:** Surviving with the Core (Archivists). She was coerced into creating the Metal Vessels for "peaceful" reconstruction.
- [x] **Metal Vessel Status:** Shared-consciousness units, physically powerful but lacking individual spirits.
- [x] **Core Survival:** Evacuated to a safe Earth location before the Fry; later moved headquarters to the shielded Lunar Pyramid.
- [x] **Location Disambiguation:** **Base Alpha** is deprecated. The terrestrial Core base is **Cradle Zero**. The enemy lunar base (and first contact site) is **Apex Hub**.
- [x] **Archivist Evolution:** The transition from Core to Archivists occurs rapidly (Year 1 AT). Their technology is "alien" (Synodic-grown), not traditional human industrial design.
- [x] **The Selenites' Fate:** They are gone from the story entirely. Following the 1971 betrayal, they removed all traces of their paths; nobody knows where they went.
- [x] **The Lunar Capacitor's Blueprint:** Discovered not by Vane, but by Core scientists monitoring machine growth on the Moon's Far Side via remote subroutines.
- [x] **Mechanical Ecology Escalation:** Defined threat levels from Builders to Apex Predators (Sky-Eaters).
- [x] **Survivor Suspicion:** Documented the "Glitches" and analog artifacts (watches, newspapers) that contradict the Fallacy.
- [x] **Lem vs. Rahu/Tor:** Final confrontation detailed at Cradle Prime; Lem overrides failsafes to reveal the truth.

### Unresolved Plot Threads (Mark for Development)
- [ ] Detailed character arcs for Arlo and Cassia Vane in Year 15 AT
- [ ] The exact nature of the "Global Beacon Network's" activation pulse
- [ ] How survivors in the South respond to the "Analog Dawn"

### Contradiction Resolution Protocol
When writing new content and discovering contradictions:
1. **Flag it immediately** - Mark with `[CONTRADICTION]` in draft notes
2. **Check source hierarchy**: Facts.md > Timeline.md > Character files > Synopsis.md
3. **If unresolvable**: Ask user for explicit direction rather than assuming
4. **Document the decision** - Update relevant .md files and this instruction set

## Narrative Clarity Standards
- **Metaphor vs. Literal:** When describing Tor as "asleep," clarify whether this is dormant consciousness (can be awakened) or merely metaphorical (unthinking obedience). Choose one consistently.
- **Time-locked events:** All major events (Vessel Deception, Media Flood, exposure attempts, Cataclysm, Metal Vessel creation) must have clear Before/After placement.
- **Elemental Interactions:** Document any character-to-character elemental conflicts (Fire vs. Water, Wood vs. Earth) with specific scenes or narrative callouts.

## Version Management
- **Source of Truth:** The current version is stored in `VERSION`.
- **Protocol:** Bump the version in `VERSION` on **every git commit**.
- **Reasonable Versioning:**
    - **Major (X.0.0):** Completion of a major story arc (e.g., transition between Before Time, Cataclysm, After Time) or fundamental shift in narrative direction.
    - **Minor (0.X.0):** Addition of a new chapter plan, significant revision of an existing chapter, or major expansion of world-building files.
    - **Patch (0.0.X):** Lore hardening (small consistency fixes), typo corrections, or minor stylistic refinements.


