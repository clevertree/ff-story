# Lost Detail Report: 71→32 Chapter Consolidation

This document catalogs content lost in the **71→32 chapter consolidation** (commit `0d7f8db`), which occurred **before** the v0.10.40 beat refactor. The consolidation reduced 71 chapter files to 32, with new filenames and merged/condensed content. Net change: **3,626 deletions, 1,593 insertions** across the chapters directory.

---

## 1. When and What Was Lost

- **Consolidation commit:** `0d7f8db` — "feat: assemble 32-chapter FULL_MANUSCRIPT and sync terminology"
- **Pre-consolidation baseline:** `0298cd9` (v0.10.2: Update INDEX.md, meta-data, and recompiled FULL_MANUSCRIPT)
- **Scope:** 71 chapter files (e.g. `chapter_01_invasion.md` … `chapter_71_the_wandering_wood.md`) were replaced by 32 new files with different names and structure (e.g. `chapter_01_the_arrival_of_lynn.md` … `chapter_32_the_final_transmission.md`).
- **Relationship to v0.10.40:** The v0.10.40 refactor (commit `b91f39c`) happened **after** this consolidation and operated on the resulting 34-chapter set (34 = 32 + added Ch 9 "The Reincarnation" and renumbering in later commits). So this report covers an **earlier** loss: the merge of 71 chapters into 32.

**How to recover pre-consolidation content:**  
`git show 0298cd9:chapters/<filename>` (e.g. `git show 0298cd9:chapters/chapter_12_the_pyramid.md`).

---

## 2. Summary of Changes

- **Deleted entirely (content not carried in new 32):** Many chapters were removed and their plot/outlines either merged into shorter beats in the new structure or dropped. The largest single-file losses (by lines removed) were:
  - **chapter_13_the_confrontation.md** (391 lines) — Pyramid interior: Rahu, Tor, Lynn reveal, merger, Lynn toward Lunar Capacitor, reset.
  - **chapter_12_the_pyramid.md** (294 lines) — Approach to pyramid, Tor’s return, "Rahu is still alive," Iris recalibrating.
  - **chapter_11_rahu.md** (254 lines) — Rahu confirmed, Tor’s decision, Hermes sacrifice, Tor’s ship crippled.
  - **chapter_09_waking_in_the_dream.md** (220 lines) — Post-crash Aether-Drive fugue, mechanical extraction, Novak’s message, Lynn’s link severed, Lem left with hovercraft.
  - **chapter_07_zenith.md** (120 lines) — Bridge/zenith content (partially reflected in new ch03/ch04).
  - **chapter_08_the_shattered_approach.md** (141 lines) — Lunar approach/shattered approach sequence.
- **Renamed / renumbered:** Some old chapters were renamed and shifted in order (e.g. old ch15 Path of Fragments → new ch08; old ch18 Disintegration → new ch10).
- **New names, different content:** The new 32-chapter set often had different titles and combined or split beats from the 71-chapter arc (e.g. new ch01 "The Arrival of Lynn" vs old ch01 "An Ordinary Distance" / "Invasion").

---

## 3. Per-Chapter Lost Detail (Old 71 → New 32)

For each **old** chapter (pre-consolidation), the table lists: filename, display title, approximate lines lost (from diff), brief content summary, and the **new** chapter number(s) that replaced or absorbed it (by filename/content). "Deleted, merged" means content was folded into other new chapters without a 1:1 new file.

| Old # | Old filename | Old title | Lines lost | Brief content (pre-consolidation) | New chapter(s) |
|-------|----------------|-----------|------------|------------------------------------|----------------|
| 1 | chapter_01_invasion.md | An Ordinary Distance | 77 | Suburban routine, Monoliths/Tripods, military convoy | Replaced by ch01_the_arrival_of_lynn (different start) |
| 2 | chapter_02_lynn.md | Lynn | 83 | Lynn’s arrival, recruitment | ch02_the_two_dangers |
| 3 | chapter_03_doorway.md | The Doorway | 83 | Boarding/ship | ch03_zenith |
| 4 | chapter_04_drafted.md | Drafted | 86 | Drafted into mission | ch04_the_fall |
| 5 | chapter_05_the_briefing_he_never_had.md | The Briefing He Never Had | 84 | Marshal, briefing code, mission context | Deleted, merged |
| 6 | chapter_06_the_near_moon.md | The Near Moon | 87 | Lunar approach | Deleted, merged into 5–7 |
| 7 | chapter_07_zenith.md | Zenith | 120 | Bridge, Moon proximity, crew/jettison | ch03_zenith / ch04_the_fall |
| 8 | chapter_08_the_shattered_approach.md | The Shattered Approach | 141 | Shattered approach to base | Deleted, merged |
| 9 | chapter_09_waking_in_the_dream.md | Waking in the Dream and the Rescue | 220 | Post-crash fugue, claw extraction, Novak, Lynn’s link severed, Lem with hovercraft | Deleted, merged into new 8 (path of fragments) / extraction beat |
| 10 | chapter_10_alone_on_the_moon.md | Alone on the Moon | 73 | Lem alone on moon | ch05_alone_on_the_moon |
| 11 | chapter_11_rahu.md | Rahu | 254 | Rahu confirmed, Tor from Hermes, sacrifice decision, Hermes vs Rahu, ship crippled | ch06_the_sacrifice |
| 12 | chapter_12_the_pyramid.md | The Pyramid | 294 | Fleet to pyramid, ground unstable, evacuation into pyramid, door slammed, Tor returns, "Rahu is still alive," Iris recalibrates | Deleted, merged into ch07_the_reset |
| 13 | chapter_13_the_confrontation.md | The Confrontation | 391 | Chamber, Rahu, Tor vs Rahu, soldiers fire, Lynn reveal, Technocracy argument, stasis failure, Lem-Lynn merger, Lynn to center, reset | Deleted, merged into ch07_the_reset |
| 14 | chapter_14_the_shifting_moon.md | The Shifting Moon | 52 | Moon shifting | Deleted, merged |
| 15 | chapter_15_the_path_of_fragments.md | The Path of Fragments | (renamed) | Fragments / aftermath | ch08_the_path_of_fragments |
| 16 | chapter_16_the_return.md | The Return | 47 | Return to Cradle | Deleted, merged |
| 17 | chapter_17_the_spirit_port.md | The Spirit Port | 37 | Spirit port | Deleted, merged |
| 18 | chapter_18_disintegration.md | Disintegration | (renamed) | Rahu/Lem data, purge | ch10_disintegration |
| 19 | chapter_19_the_new_lab.md | The New Lab | 41 | Archivist lab, Cassia | Deleted, merged into ch11_the_awakening |
| 20 | chapter_20_the_awakening.md | The Awakening | 45 | Awakening in lab | ch11_the_awakening |
| 21 | chapter_21_aggressive_expansion.md | Aggressive Expansion | 10 | Stub/beat | Deleted |
| 22 | chapter_22_the_beacon_strike.md | The Beacon Strike | 47 | Beacon strike | Deleted, merged |
| 23 | chapter_23_the_utopian_hive.md | The Utopian Hive | 10 | Stub | Deleted |
| 24 | chapter_24_northern_shield.md | Northern Shield | 10 | Stub | Deleted |
| 25 | chapter_25_the_village_encounter.md | The Village Encounter | 51 | Village, Arlo | Deleted, merged into ch20/22 |
| 26 | chapter_26_the_tripod_anomaly.md | The Tripod Anomaly | 63 | Tripod anomaly | Deleted, merged |
| 27 | chapter_27_the_white_forest_mission.md | The White Forest Mission | 10 | Stub | Deleted |
| 28 | chapter_28_myrr.md | Myrr | 31 | Myrr | Deleted, merged into ch20/21 |
| 29 | chapter_29_the_analog_interface.md | The Analog Interface | 40 | Analog interface | Deleted, merged |
| 30 | chapter_30_the_final_word.md | The Final Word | (renamed) | Anton, stasis | ch15_the_final_word |
| 31 | chapter_31_stasis_and_awakening.md | Stasis and Awakening | 10 | Stub | Deleted |
| 32 | chapter_32_analog_lem.md | Analog Lem | 40 | Analog Lem | Deleted, merged |
| 33 | chapter_33_the_parting_in_the_ash.md | The Parting in the Ash | (renamed) | Myrr, forest | ch17_the_parting_in_the_ash |
| 34 | chapter_34_the_long_exile.md | The Long Exile | 10 | Stub | Deleted |
| 35 | chapter_35_the_return_to_the_north.md | The Return to the North | 10 | Stub | Deleted |
| 36 | chapter_36_the_whistle_in_the_woods.md | The Whistle in the Woods | 56 | Myrr’s whistle, forest, "Witch Maya" legend, analog sanctuary | Deleted, merged into ch20/21 |
| 37 | chapter_37_the_village_leader.md | The Village Leader | 48 | Village gate, Mission 3 ruins, Arlo, Water Key, "Maya" reveal | Deleted, merged into ch20/21 |
| 38 | chapter_38_the_witch_maya.md | The Witch Maya | 49 | Arlo/Maya, identity, HID | Deleted, merged into ch20/21 |
| 39 | chapter_39_the_shore_of_shadows.md | The Shore of Shadows | 10 | Stub | Deleted |
| 40 | chapter_40_the_great_refusal.md | The Great Refusal | 10 | Stub | Deleted |
| 41 | chapter_41_the_arsenal_of_the_ash.md | The Arsenal of the Ash | 40 | White Forest seeds, hybrid blueprints, Nodes, test strike | Deleted, merged into ch21/22 |
| 42 | chapter_42_the_battle_of_trees.md | The Battle of Trees | 44 | Battle of trees | Deleted, merged |
| 43 | chapter_43_the_siege_of_cradle_zero.md | The Siege of Cradle Zero | 38 | Siege | ch22_the_siege_of_cradle_zero |
| 44 | chapter_44_the_ghost_in_the_dust.md | The Ghost in the Dust | 10 | Stub | Deleted |
| 45 | chapter_45_the_invisible_front.md | The Invisible Front | 10 | Stub | Deleted |
| 46 | chapter_46_the_great_stalemate.md | The Great Stalemate | 26 | Stalemate | Deleted, merged |
| 47 | chapter_47_the_core_debate.md | The Core Debate | 30 | Core debate | Deleted, merged |
| 48 | chapter_48_the_failing_cities.md | The Failing Cities | 25 | Failing cities | Deleted, merged |
| 49 | chapter_49_the_peaceful_emissary.md | The Peaceful Emissary | 10 | Stub | Deleted |
| 50 | chapter_50_the_stoic_refusal.md | The Stoic Refusal | 24 | Arlo’s refusal | ch24_the_stoic_refusal |
| 51 | chapter_51_the_infiltration_gambit.md | The Infiltration Gambit | 37 | Infiltration | Deleted, merged |
| 52 | chapter_52_the_pillar_of_fire.md | The Pillar of Fire | 28 | Pillar | Deleted, merged into ch25/26 |
| 53 | chapter_53_the_greeting.md | The Greeting | 31 | Greeting | Deleted, merged |
| 54 | chapter_54_the_false_stalemate.md | The False Stalemate | 29 | False stalemate | Deleted, merged |
| 55 | chapter_55_the_gathering_of_strands.md | The Gathering of Strands | 13 | Strands | ch26_the_gathering_of_strands |
| 56 | chapter_56_the_narrative_trap.md | The Narrative Trap | 14 | Narrative trap | Deleted, merged |
| 57 | chapter_57_the_siege_of_pods.md | The Siege of Pods | 11 | Siege of pods | Deleted, merged |
| 58 | chapter_58_the_final_lesson.md | The Final Lesson | 13 | Final lesson | Deleted, merged |
| 59 | chapter_59_the_aetheric_wake.md | The Aetheric Wake | 12 | Aetheric wake | ch27_the_aetheric_wake |
| 60 | chapter_60_the_witchs_return.md | The Witch’s Return | 10 | Stub | Deleted |
| 61 | chapter_61_the_resonance_of_the_fall.md | The Resonance of the Fall | 38 | Lab lockdown, Drexler, plasma purge, spirit migration, analog path, rebirth at White Forest | Deleted, merged into ch28 |
| 62 | chapter_62_the_hooting_call.md | The Hooting Call | 37 | Hooting Call, Gorgons drop tools, migration, Tor’s reconfigured war | Deleted, merged into ch28/30 |
| 63 | chapter_63_the_ancient_shield.md | The Ancient Shield | 37 | Beacons toppled, Ancient Arsenal ballistic weapons, slaughter, False Victory | Deleted, merged into ch29/31 |
| 64 | chapter_64_the_liquid_ghost.md | The Liquid Ghost | 38 | Maya in lab, liquid form | ch28_the_liquid_ghost |
| 65 | chapter_65_the_fall_of_the_general.md | The Fall of the General | 42 | Tor’s fall, Maya vs Tor | ch29_the_fall_of_the_general |
| 66 | chapter_66_the_vision_and_the_answer.md | The Vision and the Answer | 10 | Stub | Deleted |
| 67 | chapter_67_the_mission_five_lunar_assault.md | Mission 5: The Lunar Assault | 37 | Lunar assault | ch30_the_lunar_assault |
| 68 | chapter_68_the_creator_in_the_pyramid.md | The Creator in the Pyramid | 10 | Stub | ch31_the_creator_in_the_pyramid |
| 69 | chapter_69_the_grounding_of_the_fire.md | The Grounding of the Fire | 42 | Grounding of fire | Deleted, merged into ch31/32 |
| 70 | chapter_70_the_final_transmission.md | The Final Transmission | 40 | Final transmission | ch32_the_final_transmission |
| 71 | chapter_71_the_wandering_wood.md | The Wandering Wood | 10 | Stub | Deleted |

---

## 4. Mapping: Old 71 → New 32 (Post-Consolidation)

The new 32-chapter set (commit `0d7f8db`) had these filenames. Later commits added Ch 9 "The Reincarnation" and renumbered to 34, then the repo expanded to 57 chapters (see [LOST_DETAIL_V0.10.40.md](LOST_DETAIL_V0.10.40.md) for 34→57 mapping).

| New # (32) | New filename (post-consolidation) | Primary content |
|------------|-----------------------------------|------------------|
| 1 | chapter_01_the_arrival_of_lynn.md | Lynn’s arrival |
| 2 | chapter_02_the_two_dangers.md | Ship, two dangers |
| 3 | chapter_03_zenith.md | Zenith |
| 4 | chapter_04_the_fall.md | The fall |
| 5 | chapter_05_alone_on_the_moon.md | Alone on moon |
| 6 | chapter_06_the_sacrifice.md | Hermes / sacrifice |
| 7 | chapter_07_the_reset.md | Pyramid, Tor, Lynn, reset |
| 8 | chapter_08_the_path_of_fragments.md | Path of fragments |
| 9 | chapter_09_return_to_cradle_zero.md | Return to Cradle Zero |
| 10 | chapter_10_disintegration.md | Disintegration |
| 11 | chapter_11_the_awakening.md | Awakening |
| 12 | chapter_12_the_utopian_hive.md | Utopian Hive |
| 13 | chapter_13_the_northern_trial.md | Northern trial |
| 14 | chapter_14_the_white_forest.md | White Forest |
| 15 | chapter_15_the_final_word.md | Anton, final word |
| 16 | chapter_16_forest_awakening.md | Forest awakening |
| 17 | chapter_17_the_parting_in_the_ash.md | Parting in the ash |
| 18 | chapter_18_the_long_exile.md | Long exile |
| 19 | chapter_19_the_return_to_the_north.md | Return to north |
| 20 | chapter_20_the_water_resonance.md | Water resonance |
| 21 | chapter_21_the_great_refusal.md | Great refusal |
| 22 | chapter_22_the_siege_of_cradle_zero.md | Siege of Cradle Zero |
| 23 | chapter_23_the_invisible_front.md | Invisible front |
| 24 | chapter_24_the_stoic_refusal.md | Stoic refusal |
| 25 | chapter_25_the_fire_spire.md | Fire spire |
| 26 | chapter_26_the_gathering_of_strands.md | Gathering of strands |
| 27 | chapter_27_the_aetheric_wake.md | Aetheric wake |
| 28 | chapter_28_the_liquid_ghost.md | Liquid ghost |
| 29 | chapter_29_the_fall_of_the_general.md | Fall of the general |
| 30 | chapter_30_the_lunar_assault.md | Lunar assault |
| 31 | chapter_31_the_creator_in_the_pyramid.md | Creator in pyramid |
| 32 | chapter_32_the_final_transmission.md | Final transmission |

---

## 5. Summary: What Can Be Re-Added (High Value)

The following **pre-consolidation** content was removed or heavily condensed and may be worth re-adding or re-referencing in the **current** 57-chapter structure (using [LOST_DETAIL_V0.10.40.md](LOST_DETAIL_V0.10.40.md) to map new 32 → current 57).

### Lunar / Cataclysm arc (old ch9–13)

- **ch09 Waking in the Dream and the Rescue (220 lines):** Aether-Drive fugue post-crash, mechanical claw extraction, Novak’s message that Lynn’s link is severed, Lem "mission-ready" with hovercraft. Re-add as beats or reference in current Extraction / approach chapters (e.g. ch8, ch9).
- **ch11 Rahu (254 lines):** Rahu confirmed, Tor on Hermes, "traitor Prometheus" confusion, Tor’s sacrifice decision, Hermes vs Rahu, ship crippled. Enrich current Sacrifice (ch10) with Tor’s POV and Rahu’s broadcast.
- **ch12 The Pyramid (294 lines):** Biker fleet to pyramid, ground unstable, evacuation into pyramid, door pounding, Tor’s return, "Rahu is still alive," Iris recalibrates. Re-add to current Cradle Alpha / pyramid approach (ch11, ch12).
- **ch13 The Confrontation (391 lines):** Full chamber sequence: Rahu, Tor’s accusations, Rahu’s defense, soldiers fire, Lynn reveal, Technocracy argument, stasis failure, **Lem-Lynn merger**, Lynn to center, Tor tries to stop her, barrier accepts Lynn, "massive short circuit," reset. Re-add or summarize in current pyramid/reset chapters (ch12 Maya, ch13 Reset, ch14 Abortion).

### Northern / village arc (old ch36–38, 41)

- **ch36 The Whistle in the Woods (56 lines):** Myrr’s melodic whistle, "Witch Maya" legend, analog sanctuary as fortress, shared Archive from White Forest contact. Re-add to current Myrr / White Forest (ch31, ch30).
- **ch37 The Village Leader (48 lines):** Mission 3 ruins, Tripod skeletons, village gate, Arlo, Water Key reveal, "Maya" identity bomb, HID offer. Re-add to current Myrr / Arlo beats (ch31).
- **ch38 The Witch Maya (49 lines):** Arlo/Maya identity, conditions for "experiment." Re-add to current Myrr (ch31).
- **ch41 The Arsenal of the Ash (40 lines):** White Forest seeds, hybrid blueprints, biological fabricators, Nodes, "test" strike decision. Re-add to current Forge / siege planning (ch24, ch40).

### Uprising / climax (old ch61–63)

- **ch61 The Resonance of the Fall (38 lines):** Lab lockdown, Drexler, plasma purge, "analog path" vs dark corridor, rebirth at White Forest. Re-add to current Breach / Colonization (ch48, ch50).
- **ch62 The Hooting Call (37 lines):** Non-digital signal, Gorgons drop tools, migration, Tor’s "evacuation vehicles reconfigured for war." Re-add to current Colonization (ch50).
- **ch63 The Ancient Shield (37 lines):** Beacons toppled, **Ancient Arsenal** (21st-century ballistic missiles), slaughter of Synodics, False Victory. Re-add to current Duel / Blackout (ch45, ch51).

### Caveats

- **Canon:** Re-add only where consistent with current world-building (Cradle Zero vs Base Alpha, resolved threads in .cursorrules / OUTSTANDING_QUESTIONS).
- **Duplicate content:** Some beats were later restored or rephrased in the 34-chapter set and again in the 57-chapter set; check current chapters before re-adding to avoid duplication.
- **Recovery:** Full text for any old chapter: `git show 0298cd9:chapters/<filename>`.

---

*Report generated from diff `0298cd9` (71 chapters) vs `0d7f8db` (32 chapters).*
