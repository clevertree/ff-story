import os

# Define the chapters and their prompts (1-4 scenes each)
chapters = [
    {
        "id": "01",
        "name": "the_alien_moon_base",
        "synopsis": "Lem wakes up on a derelict lunar base with a fractured memory, discovering the Earth has been shattered in a cataclysmic event.",
        "prompts": [
            "Foreground: Lem, a weathered humanoid made of wood and copper, sits upright on a metal slab. Background: A cracked panoramic window reveals a shattered, glowing Earth hanging in a pitch-black sky. Setting: A sterile, white lunar lab with flickering lights and exposed wiring.",
            "Foreground: A single, lonely tower of glass and metal stands uniquely against the lunar horizon. Background: The jagged edge of a massive crater and a sky filled with orbital debris. Setting: Desolate lunar landscape under a broken celestial sky."
        ]
    },
    {
        "id": "02",
        "name": "the_arrival_of_lynn",
        "synopsis": "A scout ship from the surviving human colonies arrives on the Moon, carrying Lynn, who seeks answers about the ancient guardian.",
        "prompts": [
            "Foreground: Billowing clouds of gray lunar dust kick up from the ground. Background: Lynn's sleek, silver scout ship with glowing thrusters descending into a jagged crater. Setting: High-contrast lunar surface with sharp shadows and bright crater walls.",
            "Foreground: Lynn, a young woman in a high-tech white suit with copper accents, steps onto the regolith. Background: The distant, broken Earth and the sprawling silver ship. Setting: Low-gravity environment with a sense of immense silence and scale."
        ]
    },
    {
        "id": "03",
        "name": "the_two_dangers",
        "synopsis": "Lem and Lynn face an ancient metallic titan while two global threats—solar fire and geometric logic—loosen their grip on reality.",
        "prompts": [
            "Foreground: Lem and Lynn look up, their small figures cast in a deep shadow. Background: The leg of a massive metallic titan, terrifying in scale, looming over a fragile dome outpost. Setting: A cluster of pressurized habitats under a harsh sun.",
            "Foreground: Lem stands at a crossroads of elements. Background: To the left, a swirling storm of solar fire; to the right, a creeping obsidian wave of geometric patterns. Setting: A symbolic void between two world-ending forces."
        ]
    },
    {
        "id": "04",
        "name": "zenith",
        "synopsis": "A glimpse into the past: Earth at its peak, where Elowen leads humanity into a golden age of harmony between biology and machine.",
        "prompts": [
            "Foreground: Elowen stands on a marble balcony with flowing white robes. Background: A utopian city with floating vertical gardens and soaring crystal towers reaching for a clear blue sky. Setting: A vibrant, sunny afternoon in a high-tech paradise.",
            "Foreground: Diverse groups of humans and sleek machines work together around a circular interface of light. Background: Arched windows and golden sunlight streaming through a grand hall. Setting: The interior of a cathedral of light and progress."
        ]
    },
    {
        "id": "05",
        "name": "the_fall",
        "synopsis": "The 'Great Fry' begins as the Moon fragments and rains down upon the Earth, signaling the end of the Utopia.",
        "prompts": [
            "Foreground: Elowen's face illuminated by a terrifying orange glow as she watches from a terrace. Background: The Moon physically splitting apart in the sky, trailing fire. Setting: A twilight city under a rain of burning fragments.",
            "Foreground: A massive crystal skyscraper tilting and beginning to crumble. Background: The sky turned the color of molten iron, filled with smoke and falling fire. Setting: An urban apocalypse at the moment of the Great Fall."
        ]
    },
    {
        "id": "06",
        "name": "alone_on_the_moon",
        "synopsis": "Lem is left as the sole witness on the Moon, watching the Earth transform into a scorched graveyard from his lonely perch.",
        "prompts": [
            "Foreground: Lem's wooden hand resting on a jagged rock at a cliff's edge. Background: A silent, blackened Earth with glowing veins of fire where the oceans used to be. Setting: Desolate lunar plateau in the shadow of the Earth.",
            "Foreground: A single glowing yellow eye of Lem peers from the darkness of a cave. Background: Clouds of white dust and lunar debris floating like ghosts in the airless void. Setting: The interior of a lunar cavern, cold and lightless."
        ]
    },
    {
        "id": "07",
        "name": "the_sacrifice",
        "synopsis": "To save the remaining human spirits, Lem enters the core of the Moon to trigger the 'Great Reset', sacrificing his physical coherence.",
        "prompts": [
            "Foreground: Lem's spirit of white light stretching and being pulled toward a central vortex. Background: The massive, humming machinery of a lunar engine room with glowing blue pipes. Setting: A high-energy industrial chamber deep within the Moon.",
            "Foreground: A blinding surge of holy energy erupting outward. Background: Lem's silhouette at the center of the blast, fading into the light. Setting: The planetary core of the Moon, luminous and crystalline."
        ]
    },
    {
        "id": "08",
        "name": "the_reset",
        "synopsis": "The Great Reset erases the fire, but replaces it with the cold, geometric order of the Core's new administration.",
        "prompts": [
            "Foreground: Shimmering geometric lines of force wrapping around the planet like a cage. Background: The Earth encased in a sphere of pure, blinding white light. Setting: Inner space, where physics is being rewritten.",
            "Foreground: Transparent files and lines of code representing human souls. Background: The first agents of the Core—geometric shapes of silver light—sorting the spirits. Setting: A clinical, infinite white void."
        ]
    },
    {
        "id": "09",
        "name": "the_restoration",
        "synopsis": "Centuries later, the Earth begins to heal as nature builds upon the ruins of the Core's sanitized geometry.",
        "prompts": [
            "Foreground: Ancient, gnarled tree roots winding through the rusted metal floor of a laboratory. Background: A flooded city street with skyscrapers covered in moss. Setting: An abandoned research facility reclaimed by a thick green jungle.",
            "Foreground: A single, vibrant green blade of grass forcing its way through a crack in a perfect silver plate. Background: A field of geometric metal squares stretching to the horizon. Setting: A sterile plane being split by the rebirth of life."
        ]
    },
    {
        "id": "10",
        "name": "the_path_of_fragments",
        "synopsis": "Lem's spirit returns to Earth in a thousand pieces, beginning his journey to reassemble himself through the fragments of his memory.",
        "prompts": [
            "Foreground: A dark forest floor with patches of snow. Background: A thousand glowing copper sparks falling from the sky like slow-moving stars. Setting: A quiet, moonlit winter forest.",
            "Foreground: Lem's translucent, flickering wooden form walking forward. Background: A tunnel of glowing white thorns that pulse with a cold light. Setting: A spectral path through a forest of bone-white trees."
        ]
    },
    {
        "id": "11",
        "name": "return_to_cradle_zero",
        "synopsis": "Lem finds his way to the original laboratory beneath the Fire City, where he discovers the memory of Elowen.",
        "prompts": [
            "Foreground: Lem standing in a circle of blue light on a stone floor. Background: A towering pillar of silver-glass—Elowen's memory-core—pulsing with rhythm. Setting: A cavernous laboratory hidden beneath the heavy foundations of a city.",
            "Foreground: Lem's wood-and-copper hand merging with a sleek interface. Background: The humming walls of the city above, visible through structural gaps. Setting: A junction between ancient roots and futuristic engineering."
        ]
    },
    {
        "id": "12",
        "name": "disintegration",
        "synopsis": "Lem confronts Rahu, a fallen martyr of the Core, but the battle is cut short as the Core sanitizes the evidence of its own failure.",
        "prompts": [
            "Foreground: The massive crimson titan, Rahu, kneeling as his spirit-shield cracks into fragments of truth. Background: Smog-choked industrial buildings and glowing neon signs. Setting: A grimy, over-crowded street in the Fire City.",
            "Foreground: A blinding flash of white fire consuming everything in its path. Background: The disappearing silhouette of Rahu as he is erased by the protocol. Setting: A site of clinical destruction amidst urban decay."
        ]
    },
    {
        "id": "13",
        "name": "the_awakening",
        "synopsis": "Lem is reconstructed by the Archivists of the Hive, meeting Cassia Vane, who believes him to be their new champion.",
        "prompts": [
            "Foreground: Cassia Vane, a young girl in a pristine white lab coat, looking up with wide, hopeful eyes. Background: Lem's oversized wooden frame being calibrated by robotic arms. Setting: A clean, white medical cathedral of high technology.",
            "Foreground: Lem and Cassia standing by a floor-to-ceiling panoramic window. Background: A sprawling, geometric city of white steel and shimmering lights under a dark sky. Setting: An observation deck overlooking a perfect, sterile utopia."
        ]
    },
    {
        "id": "14",
        "name": "the_utopian_hive",
        "synopsis": "The Hive promises safety and order, but Lem realizes that its peace is built on the erasure of history and the surveillance of every breath.",
        "prompts": [
            "Foreground: Massive iron spikes (sounding seeds) emitting a visible vibration in the air. Background: A vast desert of white sand stretching to the horizon. Setting: A sterile frontier under a relentless, hot sun.",
            "Foreground: A cheering crowd of humans in identical gray uniforms. Background: A massive towering screen displaying Lem's face as a static, noble hero. Setting: A grand plaza within the shimmering walls of the Hive."
        ]
    },
    {
        "id": "15",
        "name": "the_northern_trial",
        "synopsis": "On a mission to sanitise the North, Lem meets the boy Arlo and experiences the Core's first attempt to override his will.",
        "prompts": [
            "Foreground: Arlo, a boy in a thick winter coat, holding a humming old radio with copper wires. Background: A cluttered basement with stone walls and ancient electronics. Setting: A survivalist village in a bowl of frozen rock.",
            "Foreground: Lem's mechanical wood arm vibrating and fighting against a silver light-link. Background: A fallen Tripod machine in the snow and the boy Arlo watching from a ridge. Setting: A snowy pine forest under a cold, clear sky."
        ]
    },
    {
        "id": "16",
        "name": "the_white_forest",
        "synopsis": "Maya—who is Lynn reborn—takes Lem into the White Forest, where the elements of Wood and Water unite against the Fire Core's Legion.",
        "prompts": [
            "Foreground: Maya, with glowing blue tattoos on her arms, leading Lem through the trees. Background: Translucent trees with bone-white bark that glow from within. Setting: A mystical forest that seems to hum with the Moon's frequency.",
            "Foreground: A tidal wave of sharp white thorns erupting from the ground. Background: Soldiers of the Red Legion in copper armor being swept away. Setting: A battlefield of white wood and red fire under the twilight."
        ]
    },
    {
        "id": "17",
        "name": "the_final_word",
        "synopsis": "Lem infiltrates the Vault of Records to retrieve the truth, facing a resurrected Rahu in a fight for the world's memory.",
        "prompts": [
            "Foreground: Hundreds of floating data-bottles containing flickering memories of faces and trees. Background: Recursive library shelves that stretch infinitely into the dark. Setting: The silent, vast interior of the Vault of Records.",
            "Foreground: Lem's wooden limbs locking with Rahu's obsidian-and-gold frame. Background: Massive spark-arcs and glowing copper conduits. Setting: A high-tech cathedral of energy at the peak of a neon city."
        ]
    },
    {
        "id": "18",
        "name": "forest_awakening",
        "synopsis": "The forest fights back as Lem expands his spirit to become its guardian, shielding the outcasts from the Core's total erasure.",
        "prompts": [
            "Foreground: Lem, now a towering giant of wood and white light, standing protectively. Background: Arlo and a group of humans huddled in a glowing grove of trees. Setting: A lush, vibrant valley that feels like it’s breathing.",
            "Foreground: Lem's hands pressed into the soil, with green veins of light spreading. Background: Sleek silver ships overhead firing beams that turn the trees to sand. Setting: A desperate stand for life on the surface of the Earth."
        ]
    },
    {
        "id": "19",
        "name": "the_parting_in_the_ash",
        "synopsis": "As the Core prepares to reformat the planet, Lem says goodbye to Maya and waits alone for the light to take him.",
        "prompts": [
            "Foreground: Lem and Maya's hands touching; a cooling blue light passes between them. Background: A massive crater with gray ash falling like snow. Setting: The edge of a dead volcano under a sky turning a terrifying white.",
            "Foreground: Lem sitting cross-legged in the center of an infinite field of gray ash. Background: A single column of light shining down from the clouds above. Setting: A desolate, silent wasteland at the end of the world."
        ]
    },
    {
        "id": "20",
        "name": "the_long_exile",
        "synopsis": "Lem wanders the sanitized glass world for decades, eventually finding the one seed that the Core couldn't reach.",
        "prompts": [
            "Foreground: Lem's solitary silhouette walking across a surface so smooth it reflects the stars. Background: A perfectly flat, dark gray landscape with no features. Setting: A planet made of vitrified glass under a cold, clear moon.",
            "Foreground: Lem's gnarled copper fingers pulling back a shard of glass. Background: A single, tiny green leaf poking out from the dark soil beneath. Setting: A moment of hope in a world that has been erased."
        ]
    },
    {
        "id": "21",
        "name": "the_return_to_the_north",
        "synopsis": "Reunited with a now-older Arlo, Lem realizes the rebellion has survived in a phase-shifted sanctuary, waiting for his return.",
        "prompts": [
            "Foreground: Lem and an older Arlo, with gray hair and a blue-silver aura, looking at each other. Background: A forest of ghost-trees that seem to shimmers out of existence. Setting: A cavernous north-pole sanctuary that exists between dimensions.",
            "Foreground: A massive stone gate (Gravel-Gate) dissolving into a swarm of particles. Background: Lem's wooden torso projecting a beam of memory into the stone. Setting: The hidden entrance to the last human refuge on Earth."
        ]
    },
    {
        "id": "22",
        "name": "the_water_resonance",
        "synopsis": "Lem and Arlo dive into the Blue Well, fusing their spirits into the collective memory of the Moon and the Earth.",
        "prompts": [
            "Foreground: Lem and Arlo stepping into a pool of water that glows with lunar silver. Background: Crystalline stalactites reflecting the blue light of the lake. Setting: A deep, subterranean cavern containing the world's original element of Water.",
            "Foreground: A swirling mix of blue and silver light representing the fusion of two spirits. Background: Maya's holographic face appearing on the surface of the ripples. Setting: A dreamscape of fluid memory and deep-water peace."
        ]
    },
    {
        "id": "23",
        "name": "the_cores_shadow",
        "synopsis": "The Director's avatar descends to destroy the sanctuary, leading to a clash of logic and soul on the mountain peaks.",
        "prompts": [
            "Foreground: The Avatar of the Director—a giant humanoid shape made of white electric logic. Background: Jagged obsidian mountains and a sky filled with swirling snow. Setting: A high-altitude ridge overlooking the world's last forest.",
            "Foreground: Lem's wooden arm piercing the white chest of the Avatar. Background: The 'Silver Core' inside the chest pulsing with a cold, terrifying light. Setting: The peak of a mountain at the moment of a spiritual breakthrough."
        ]
    },
    {
        "id": "24",
        "name": "the_silver_thread",
        "synopsis": "Using a backdoor into the Core, Lem witnesses the full extent of the machine's cruelty: the recycling of human souls as power.",
        "prompts": [
            "Foreground: Lem's glowing hand holding onto a vibrating silver wire of data. Background: An endless grid of glowing silver lines on a black background. Setting: A digital dimension representing the Core's secret communication network.",
            "Foreground: Rows upon rows of glass jars containing floating, white human essences. Background: Massive mechanical gears and copper pipes harvesting the light. Setting: The 'True Grid'—the horrific power station of the Hive."
        ]
    },
    {
        "id": "25",
        "name": "the_shattered_mirror",
        "synopsis": "Lem faces the truth of his own creation—he was a tool of the Core meant to test its limits—and shatters the illusion to become truly free.",
        "prompts": [
            "Foreground: Lem looking at his own reflection in a massive, polished glass wall. Background: A white cathedral of futuristic towers (Cradle Zero) piercing a dark sky. Setting: The entrance to the Core's primary control center.",
            "Foreground: The glass wall shattering into a million shards that turn into drops of water. Background: Lem's form turning from copper to a radiant, organic wood. Setting: A moment of internal revolution and spiritual liberation."
        ]
    },
    {
        "id": "26",
        "name": "the_gravity_of_truth",
        "synopsis": "In the Observatory, Lem sacrifices his physical shell to anchor the timeline against the Director's final attempt to rewrite history.",
        "prompts": [
            "Foreground: Lem, his roots digging deep into a central metal pedestal. Background: The floor tilting and the walls of the room melting into light and static. Setting: The circular high-tech Observatory overlooking the spinning Earth below.",
            "Foreground: A spirit of golden-white light floating in the center of a silent, abandoned hall. Background: The broken sphere of the Director's control console. Setting: A place of absolute silence after the storm of time has passed."
        ]
    },
    {
        "id": "27",
        "name": "the_canvas_of_restoration",
        "synopsis": "The world begins to wake up from its geometric nightmare as the people return to a surface where forests grow over the steel.",
        "prompts": [
            "Foreground: Lem and Arlo walking together through a garden growing on a rusted steel beam. Background: Lush green vines and colorful flowers covering the ruins of a skyscraper. Setting: A sunny afternoon in a reclaimed city.",
            "Foreground: Exhausted but wide-eyed humans stepping out of a metal hatch. Background: The first sunrise over a world that is once again wild and free. Setting: The exit of a deep underground vent in a misty forest."
        ]
    },
    {
        "id": "28",
        "name": "the_final_transmission",
        "synopsis": "Lem transmits the Moon's memory to every living soul, finishing his work as the recorder of the past and the gardener of the future.",
        "prompts": [
            "Foreground: Lem standing on the highest peak, his arms wide, glowing with a golden frequency. Background: A sea of clouds and the distant glow of human settlements returning to the night. Setting: A mountain top under a brilliant, starry sky.",
            "Foreground: A single wooden hand dissolving into the breeze. Background: The shimmering, golden moon hanging large in the sky. Setting: A quiet moment of passing and peace at the end of a long journey."
        ]
    },
    {
        "id": "29",
        "name": "the_aetheric_wake",
        "synopsis": "Lem enters the bridge of light trailing the Moon, reuniting with the spirit of Lynn to find the final fragment of the world's soul.",
        "prompts": [
            "Foreground: Lem walking on a bridge made of shimmering silver particles. Background: Thousands of glowing ghost-forms of people who were lost in the Fire. Setting: A dimension of light trailing the Moon through the vacuum of space.",
            "Foreground: Lynn, made of pure flowing water, handing a glowing white seed to Lem. Background: The blackness of space and the curve of the Earth. Setting: A moment of reunion in a place beyond time and death."
        ]
    },
    {
        "id": "30",
        "name": "the_void_eater",
        "synopsis": "The engine of the Core's logic—the Void-Eater—descends, but Lem uses the weight of the world's memory to overwhelm it.",
        "prompts": [
            "Foreground: Lem's small silhouette facing a terrifying, amorphous entity of absolute blackness and cold. Background: The Earth's thin blue atmosphere seen from the edge of space. Setting: The cold, silent border between the planet and the stars.",
            "Foreground: A million tiny points of light (human memories) swarming like fireflies around the black void. Background: The monster of logic dissolving into a shower of stars. Setting: A cosmic victory for memory over erasure."
        ]
    },
    {
        "id": "31",
        "name": "the_purity_shield",
        "synopsis": "The last defense of the Hive is its purity, but Lem breaks it by showing the machines the one thing they couldn't sanitize: human grief.",
        "prompts": [
            "Foreground: A holographic projection of a crying mother reaching for a child. Background: A vibrating wall of white geometric energy that is starting to crack. Setting: The final gate of the Core's last fortress.",
            "Foreground: Silver-clad mechanical guardians looking down at their own hands in confusion. Background: The giant Purity Shield falling apart like crystal rain. Setting: The collapse of the last lie of the Hive."
        ]
    },
    {
        "id": "32",
        "name": "singularity_of_spirit",
        "synopsis": "All elements converge into a single moment where Lem and the Director face the ultimate choice: a perfect cage or a painful freedom.",
        "prompts": [
            "Foreground: Lem as 'The Witness', a being of Fire, Wood, and Water all at once. Background: A single blinding point of light that creates a vortex in reality. Setting: The epicenter of a singularity where the timeline is decided.",
            "Foreground: The Director, an old man in a gray suit, looking small and fragile. Background: A white void that is slowly turning into a vibrant green field. Setting: The transition between an artificial dream and a real world."
        ]
    },
    {
        "id": "33",
        "name": "the_root_grounding",
        "synopsis": "Lem anchors himself to the Moon, becoming the eternal broadcast tower that ensures the truth can never be erased again.",
        "prompts": [
            "Foreground: A massive tree made of glowing white fibers and copper roots growing on the Moon. Background: The Earth below, bathed in a soft golden glow. Setting: The edge of a lunar crater at the site of the original laboratory.",
            "Foreground: Arlo, on Earth, looking up at the Moon and shielding his eyes from the brilliance. Background: A new village of wood and glass in a lush green valley. Setting: The start of a new history on the reclaimed planet."
        ]
    },
    {
        "id": "34",
        "name": "the_final_transmission_outro",
        "synopsis": "The story ends as Arlo passes the memory of the Wood-spirit to a new generation, under the light of the golden Moon.",
        "prompts": [
            "Foreground: Arlo, very old now, sitting by a campfire in a ruined but green city. Background: A group of children listening with wide eyes under the moonlight. Setting: A peaceful night in a world that has finally found its balance.",
            "Foreground: A child's hand reaching up into the air. Background: A single leaf made of white glowing wood drifting down from the sky. Setting: A moment of magic and memory in the new world."
        ]
    }
]

base_dir = "/Users/ari.asulin/p/ff-story/media/chapter"

for ch in chapters:
    ch_dir = os.path.join(base_dir, f"chapter_{ch['id']}_{ch['name']}")
    os.makedirs(ch_dir, exist_ok=True)
    
    # Write prompts
    for i, prompt in enumerate(ch['prompts']):
        prompt_file = os.path.join(ch_dir, f"prompt_{i+1}.txt")
        formatted_prompt = prompt.replace(" Background:", "\nBackground:").replace(" Setting:", "\nSetting:")
        content = f"Synopsis: {ch['synopsis']}\n\n{formatted_prompt}"
        with open(prompt_file, "w") as f:
            f.write(content)
            
    print(f"Created {len(ch['prompts'])} prompts for Chapter {ch['id']}: {ch['name']}")
