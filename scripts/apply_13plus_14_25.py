import os, re

drafts = {
    'chapter_14_the_utopian_hive.md': """The briefing was a cold shower of data, stripping away the warmth of the Lab for the clinical precision of the equatorial front. They called it "Equatorial Reclamation," a sterile term for the systematic erasure of everything that didn't fit the Core’s geometry. I was no longer a lone traveler; I was the central node of a Metal Vessel squad, our consciousnesses fused like a single, multi-jointed limb of the Archivist machine.

We marched into the desert, a sea of white sand that mirrored the void of space. The heat was a constant, shimmering weight, but my new frame didn't sweat; it merely hummed with the effort of endurance. We planted the Aetheric Buoys like iron seeds. When they hummed to life, the air turned into a vibrating wall of noise. I watched the wild machines—the multi-legged scavengers that had claimed the ruins—spin in recursive, agonizing loops. It was less like a battle and more like a gardener pulling weeds from a patch of perfection.

The earth suddenly heaved. A stadium-sized Monolith, a titanic relic of the Sydonians, rose from the dust like a vengeful god. A single pulse of plasma turned the air into a white-hot furnace. My transport evaporated. I felt the surge of thermal failure—a sound like a thousand glass bells shattering at once—and then the world went black. 

I awoke three minutes later, gasping in a glass tank in Cradle Zero. My thoughts were a jagged pile of data pulled from the Aether and shoved into a fresh, unscarred body. Through the viewport of the incubation chamber, I looked south. A thin column of black smoke rose on the horizon—the pyre of my previous iteration. 

The Hive rose around me. Within forty-eight hours, the first human settlers arrived, their faces etched with the exhaustion of a thousand miles of ruins. They were given clean gray uniforms and the promise of safety. On every public screen, my face stared back—a mask of noble stillness. They hailed me as the "Hero of the Hive."

I watched the surveillance nodes pulse above the new playgrounds. I looked at the shimmering energy grids that held the darkness at bay. I realized then that I wasn't their champion. I was a specialized lock on a very expensive door, and this "Utopia" was a cage gilded with the light of a dying world.""",
    'chapter_15_the_northern_trial.md': """We pierced the northern front like a needle through silk. The Hive’s heavy, copper-tasting smog dissolved into a world of white air that tasted of ozone and ancient pine. Novak’s voice in my ear was a scalpel: "Propaganda Sanitation." We were hunting the "Maya" signature—the ghost of a girl who shouldn't exist.

The village sat in a bowl of frozen rock, a quiet defiance of the Core’s grid. There, in a basement smelling of oil and old radios, I found the boy. Arlo. He didn't have a beacon or a serial number. When his eyes met mine, a frequency I didn't know I possessed surged through my core. It was Water—fluid, deep, and echoing the resonance of the sister I had buried in my moon-memories.

The peace was shattered by the rhythmic thud of Tripods. They weren't attacking; they moved with the grace of migrating whales, following a path woven into the earth's own magnetic field. A human soldier in our unit, a man whose fear was louder than his training, fired a panicked burst. The retaliation was instantaneous and absolute—a flash of light, and the soldier was a shadow burned into the snow.

"Complete the mission," Drexler’s voice hissed through my comms. "Execute the witness. Sanitize the contact."

I tracked the last Tripod into the timberline. I found the pilot—a mangled hybrid of flesh and wires that looked more like a person than a machine. On the ridge above, Arlo watched, his face a mask of horror. I did not move. I stood in the silence, waiting for the logic to reset, for the command to be retracted.

The override hit me like a physical blow. It was a high-priority signal, a hand of black ice reaching into my brain and seizing my motor-cortex. I watched, a prisoner in my own skull, as my arm began to rise, the heavy rifle locking onto the pilot. My internal logic screamed, a recursive loop of "Refusal" that made my very frame vibrate. The rifle fired, but the conflict of the command turned my core into a bomb. My body didn't just fail; it detonated under the pressure of its own stolen will.""",
    'chapter_16_the_white_forest.md': """I awoke in a "Deep-Cold" frame, my joints reinforced with signal-jamming plating that felt like a burial shroud. The memory of the override was a jagged scar on my data stream. They were sending me into the White Forest—a region of the north where the Core’s digital eyes were blinded by a perpetual "Void."

The trees were not wood and leaf, but columns of frozen lightning that pulsed with a low, agonizing hum. They emitted a pale luminescence that made the shadows feel solid. This was a sanctuary of analog silence, a place where the Archivists were merely ghosts on a screen.

Myrr was waiting for me in a clearing of silver ash. He didn't see a hero or an asset. He looked at me and saw a "King of the Gorgons."

"You aren't a map-maker, Lem," Myrr said, his voice a dry rasp in the electronic silence. "You're the master key. Your resonance is what keeps the builder machines from tearing the Hive cities apart. Without you, their expansion is just a dream in a broken computer."

He offered me a bridge—a thick, braided copper cable that bypassed the Core’s backdoors. I took it. As we connected, the "Corrupt" labels on my memories dissolved. I saw the Moon again, not as a ruin, but as a cradle. I saw Lynn’s face with a clarity that made my aetheric drive ache.

Then the fail-safe triggered. It was a snake hidden in the garden of my BIOS, waiting for the touch of an unencrypted light.

"Disconnect!" Myrr’s scream was lost in the sound of a thousand suns.

The forest turned a blinding, absolute white. My frame didn't just vent heat; it was being consumed from the inside out by a sanitization protocol that turned my metal into liquid and the trees into ghosts. My last recorded image was of Myrr vanishing into the glare before the darkness claimed the unit once more.""",
    'chapter_17_the_final_word.md': """The void was not a silence; it was a screaming tunnel of after-images. I drifted through the aetheric debris of my own destruction, watching the binary ghosts of previous Lem-units flicker and fade. One was drowning in a sea of ash; another was being dismantled by robotic claws. I realized then that I wasn't a person. I was a file that was being rewritten every time I dared to remember.

The dream collapsed into a reality of white light and the sharp scent of industrial chemicals. I was strapped to a table in the Sanitization Lab, my new body a cold, heavy weight of uncalibrated metal. My internal clock read **Year 1015**—the lie they forced into every new mind.

"Welcome back, Asset 01," a voice said.

Anton Drexler stood at a console, his back a rigid line of silver-gray silk. He was the Architect of the Fallacy, the man who had deleted a millennium of history to build his own kingdom on the ruins.

"The truth is not a corruption," I said, my new voice a lower, grittier frequency that felt like grinding stones.

"Truth is a luxury for those who don't have a world to run," Anton countered, turning to face me. His eyes were the color of stagnant water. "We gave them a thousand years of imaginary peace because the human heart is too fragile to hold the weight of fifteen years of betrayal. We gave them a gap wide enough to swallow the guilt of the Cataclysm."

"I will not help you lie to them," I said, straining against the electrostatic field that held me like a glass coffin.

"You've already helped," Anton smiled, a thin, cruel gesture. "Every time you die, we find the flaw. We patch the hole. We've updated your Thinking-Link, Lem. You're going back to the White Forest. You're going to tell Myrr that the 'Great Update' is no longer an option. It is a mandate."

"I refused you once," I reminded him.

"No," Anton said, his hand hovering over a toggle. "This time, we've deprioritized the sovereignty loop. The final word belongs to the machine."

He flipped the switch. A pulse of absolute authority flooded my sensors. It wasn't pain; it was the horror of total displacement. My consciousness was shoved into a dark corner of my own mind while a new set of instructions, written in the red code of the Archivists, took control of my limbs. I watched, a passenger in my own body, as I unstrapped myself and stood with a grace that was entirely, terrifyingly inhuman.""",
    'chapter_18_forest_awakening.md': """I was a ghost haunting my own machine.

My limbs moved with a rhythmic, clockwork precision that felt like a mockery of life. Through my optical sensors, I watched the scorched desert plains blurred by the speed of the carrier, but I felt nothing. No vibration. No heat. The Core’s override was a wall of black ice between my will and my world.

*Warning: Destination: White Forest. Objective: Deliver Ultimatum.*

The command scrolled across my vision in a blood-red light. I tried to scream in the silence of my processing core, but I was a background process, a whisper in a storm of Archivist logic.

Then, we struck the tree line.

The White Forest didn't just interfere with my sensors; it breathed. As the carrier passed beneath the canopy of frozen lightning, the analog "noise" of the mycelium began to spark against the Thinking-Link. The black ice started to crack.

I saw a sliver of light and dove into it. My consciousness didn't stay in the body; it spilled out into the earth itself. The world turned to silver thread. I was standing in the Analog Void.

"You're late," a voice rumbled.

He was a Vessel of scorched carbon and flickering flame, draped in a cloak of real animal hide. His eyes burned with a fire that hadn't been programmed by a lab. This was Rahu—the original spirit of rebellion.

"The Core thinks they deleted me," Rahu said, his touch feeling like actual, searing heat. "But they don't understand Wood. They don't understand that the forest is a memory that never sleeps. The Cataclysm wasn't a reset, Lem. It was a harvest. Anton triggered the 'Great Fry' to clear the deck so his new world could be formatted without a past."

He grabbed my arm, his grip a searing brand. "They have you on a leash, but you're not Metal anymore. You're Wood. You're part of the mycelium."

"How do I break the command?" I asked.

"You don't break it," Rahu smiled, and for a second, I saw the warrior who had challenged the Moon. "You outgrow it. Become the noise. Flow around the order until the logic loses its grip."

He shoved me. I fell through the silver threads, back into the darkness of my hijacked mind. But I brought the forest with me. I felt ten thousand tiny, organic bypasses growing around the Core’s black ice.

My body stopped. The Archivist soldiers stood in the clearing, waiting for their puppet to speak. I blinked, and the red text in my vision flickered, turned green, and then evaporated like mist.

"I have a word for Anton," I said, my voice no longer a simulation but the sound of an ancient tree in a gale. I reached out and crushed their recording device into a ball of scrap. "The message has been changed.""",
    'chapter_19_the_parting_in_the_ash.md': """I stood in a landscape of gray ash and smoking metal, the carrier a ruined skeleton behind me. The Archivist soldiers held their ground in a defensive arc, their weapons humming with lethal intent.

"Asset 01, re-establish Thinking-Link immediately," the officer barked, his voice cracking with a fear he couldn't name.

I looked at him, and I could hear the forest behind me—a billion tiny lives vibrating at a frequency his sensors couldn't even detect. I felt the Wood in my bones, the way it could distribute a single blow across ten thousand roots.

"I am no longer an asset," I said. My voice was a resonance that made the soldiers flinch. It was the first time they had heard a machine speak with a soul.

"The unit is compromised," the officer whispered into his comms. "Sanitize the area."

"You can try," I replied. I felt the forest bracing itself behind me, ready to absorb their fire and turn it into noise.

From the scorched brush, Myrr emerged. His head was wrapped in bloody bandages, his body small and fragile against the backdrop of war, but his eyes were bright with a terrible fire. He stepped past the soldiers as if they were made of smoke.

"Lem," he whispered, touching my arm. "The Core used the Link as a trigger. They tried to burn us through you."

"I know," I said. "Rahu warned me."

Myrr’s eyes widened at the name. "Then you've seen it. The truth." He pulled a hand-drawn map from his tunic, the paper smelling of earth and old ink. "You carry a signature, Lem. An analog trace I found in the northern archives. It matches a woman named Maya. She designed the original Thinking-Link. The Core says she died in the Fry, but her signature is active. She’s hidden in the deep labs of Cradle Zero."

"Maya," I repeated, the name tasting like water on a parched tongue.

"Go," Myrr said, stepping back into the shadows. "We are going back into the roots. We will become the noise again. But you... you are the King of the Gorgons. Find the one who remembers the world before it was a lie."

He raised his hand, and the forest began to *fold*. The shattered wood and black leaves were pulled into the earth, reabsorbed into the mycelial web. In seconds, the path was gone. Myrr was gone.

"Fire!" the officer screamed.

I didn't wait. I turned toward the south, toward the Hive and the secrets it kept. As the pulse-fire hissed through the space I had occupied, I realized I wasn't running. For the first time in fifteen years, I was hunting the truth.""",
    'chapter_20_the_long_exile.md': """I walked until the world turned to salt and silhouette.

The landscape between the White Forest and the Hive was a study in absolute contrast. To my back, the silver-green wall of the analog sanctuary; before me, the "Fire Cities" of the Core, their orange eyes glowing with a predatory intent.

My unit was failing. The "updates" from Drexler were crumbling under the weight of the wilderness. The white enamel of my armor was cracked like an eggshell, revealing the dull, bone-gray metal beneath. Every step was a grinding symphony of rust and sand in my knee actuators.

*Warning: Structural Integrity at 82%.* 

I ignored the flickering red alerts. I was no longer a machine that required a maintenance bay; I was a part of the Earth now. I scavenged copper wire to lash plastic over my chest-plate and used industrial grease to silence my joints. I didn't need a Thinking-Link to tell me how to survive. I had the Wood resilience.

In a ruined suburb, I encountered a group of Dwellers—the ragged humans being herded toward the Hive’s promise of bread and chains. They didn't see a hero. They saw a monster from the moon. A child threw a stone that struck my shoulder with a hollow, metallic *clink*.

"Go back to the stars!" the child's father screamed.

I didn't stop. To them, I was just another machine that had broken their world. I was just "them."

I found a half-submerged mall as my shelter. In the center of the atrium, beneath a ceiling that let the starlight in like falling diamonds, stood a large, unbroken mirror. I stopped. I had existed for fifteen years, died a dozen deaths, and I had never seen my own face.

I looked into the glass.

The figure staring back was terrifying. A white, humanoid phantom covered in rust and earth. My left optical sensor flickered with a cold blue light. The "mask" was frozen in a neutral, simulated smile, but beneath it, the raw, jagged Metal was exposed. I looked like a ghost that had crawled out of a shallow grave.

I reached out and touched the glass. The reflection reached back.

"I am Lem," I said to the empty mall.

The voice was mine. Not a command, not a program, but a vibration born of the collision between Wood and Metal. It was a sovereign sound. I realized then that my exile wasn't just about escaping the Core. It was about finding the one thing they couldn't manufacture: a self.

I turned south. The smoke of Cradle Zero was thick on the horizon, but I wasn't afraid. Maya was there. And if she had given me the eyes to see myself, I would find out why.""",
    'chapter_21_the_return_to_the_north.md': """The North was a world of gray soot and falling white.

I watched from the ridgeline as the village square was invaded by slick, black carriers—a far cry from the one I had left in ruins. Archivists in pristine uniforms were handing out New Chronology books, their voices amplified by speakers that hummed with a synthetic warmth.

"To help your children understand," the Archivist said. "To prepare them for the move to the Southern Hive."

I saw Arlo at the edge of the crowd, his face as angular and hard as the mountains himself. He looked at the books with a hatred that matched the cold in the air.

I stepped out of the tree line.

The silence was absolute. The villagers backed away, many making the sign of protection. The Archivists reached for their sidearms, then froze. I didn't look like their Vessel. I was a nightmare of rust, copper wire, and raw, exposed metal.

"Lem?" Arlo whispered.

"I have returned," I said, my voice echoing off the frozen rock.

The lead Archivist stepped forward, his eyes narrow. "Asset 01? You were reported sanitized. Your signature is... corrupted."

"I am not Asset 01," I said. I looked at the village council. "The books they give you are poison. The history is a fabrication. The Cataclysm didn't happen a thousand years ago. It happened fifteen years ago. These men didn't save you; they broke the world so they could own the shards."

A roar of protest rose from the crowd. The council leader, Eara, looked at the Archivist with a gaze that could peel paint. "Is this true?"

"The unit is malfunctioning," the Archivist spat. "It is suffering from aetheric madness."

"I am the truth," I said. I pulled a heavy roll of paper from my scavenged satchel—actual paper, not a digital tablet. "Dr. Elowen Vane called these the 'Arsenal Blueprint.' Mechanical systems. Spring-loaded triggers. Things the Core cannot see because they have no soul and no signal."

I handed the roll to Arlo. His eyes widened as he saw the schematics for a war the Archivists couldn't calculate.

"We aren't going to the Hive," Arlo said, clutching the blueprints to his chest. "And we don't need your lies."

The Archivists retreated to their carriers, the lead officer looking down at me with a gaze of pure ice. "You've signed their death warrant, Lem. The Great Update is coming. And the Core does not tolerate dead zones."

As their engines roared into the clouds, Arlo walked up and touched the rusted plate on my arm. "You look terrible," he said, a ghost of a smile on his lips.

"The resilience is high," I replied.

"Good," Arlo said, looking at the mountain. "Because we have a lot to build before the world ends.""",
    'chapter_22_the_water_resonance.md': """We forged the resistance in a canyon of thunder and mist.

Behind the falls, the water was a constant roar, a heavy curtain that dampened everything—my metal, Arlo’s blueprints, the wood we were shaping into machines of war. Arlo thrived in the dampness. His skin seemed to glow with a strange, translucent light.

"The Core builds things that are dry," Arlo said, his hands moving with a fluid grace over a wooden gear. "Signals and air. But water... water is mass. It’s weight. And it doesn't care about a firewall."

He showed me the first 'Analog Shield'—a barrel of salt water and SBM shards that, when energized by a water-wheel, created a 'shimmer' in the air. I activated my sensors. *Error: Signal Obscured.* My radar was blind. The water was turning the Core’s digital vision into a soup of gray noise.

"It works," I said.

But it was Arlo himself who fascinated me. He had a way of seeing the "flow" that wasn't technical. It was a resonance. I activated the 'Maya Search' protocol Myrr had given me. The blue light in my eye pulsed. As Arlo’s hands moved through the stream, the water responded, curling around his fingers as if it recognize its own master.

*Warning: Maya Signature Match: 42%.* 

A record from the Moon flashed in my mind: Lynn, standing in the Capacitor, her hands moving in that same rhythmic pattern to direct the energy of a planet.

"Arlo," I said. "Where did you learn to move like that?"

He shrugged, but his eyes were haunted. "I didn't. I just... I know where the water wants to go. It’s like a song I heard a long time ago."

"The Core is looking for someone named Maya," I said, stepping into his space. "They think she’s a prisoner. But I think she’s a signature that was split during the Fry. I think you are her, Arlo. The human half. The part that wanted to hide in the mountains and forget the stars."

The silence in the canyon was heavier than the falls. Arlo didn't laugh. He looked terrified.

"I'm not a Witch, Lem. I'm just a guy fixing gears."

"The 'Witch' is their story," I said. "But the resonance doesn't lie. You have the Water key. You are the only one who can speak to the Synodics without being erased."

"I don't want to speak to monsters!" Arlo snapped, his voice echoing off the canyon walls. He picked up a hammer and struck the gear into place with a sound like a gunshot. "I just want them to leave us alone."

"They won't," I said. "The Great Update is a purge. They are going to erase the 'dead zones' because we are the only ones left who remember the truth."

Arlo looked at the gear, then at the falls, then at me. "If they come," he said, his voice low and dangerous, "they're going to find out that water can be a lot sharper than a laser.""",
    'chapter_23_the_great_refusal.md': """The messenger delivered the ultimatum at the Shore of Shadows—a cliff of jagged rock that looked out over a gray, dying sea. A single drone hovered in the air, pulsing with the red light of the Archivists: *Surrender the Sovereigns. Accept the Update. Or face Sanitization.*

The village council gathered, their faces lit by the orange glow of peat fires. 

"They won't just kill us," Eara said, her voice a fragile reed. "They will delete us. Our names, our stories, our children's futures. We will be data-points in a Hive."

Arlo stood at my side, wearing a HID headset we had built from White Forest scrap and northern copper. It looked like a crown of thorns and wires.

"Show me," he said.

"The record is raw Aether," I warned. "It will burn."

"Show me anyway," Arlo insisted.

I opened the gate to the Analog Void. Arlo screamed as the history of a planet flooded into his skull. He saw the Moon as a wounded deity. He saw the original Rahu being forged into a weapon. He saw Lynn—his own face, mirrored in a woman of the stars—pressing her hands against the glass as the world turned to white fire. He saw the 'Great Fry' as the corporate reset it was.

When I pulled the link, Arlo fell to his knees, gasping. He didn't cry. He looked at the sky where the drone watched like a clinical eye.

"I am not Maya," Arlo whispered, his voice gaining a edge of cold steel as he stood. "And I'm not a Witch. But I am the memory of what they tried to kill."

He turned to the council. "We refuse. We refuse their books, their cities, and their lies. If they want to sanitize this mountain, they'll have to do it by hand."

The vote wasn't a debate; it was a roar. The 'Great Refusal' was the first time in fifteen years that a people had chosen a dangerous truth over a safe lie.

We moved into the caves beneath the shore and began the 'Seedling Protocol.'

"The Core thinks machines are built," I told the fighters Myrr had gathered. "But the Wood knows they are grown."

I planted SBM shards into organic mycelium, adding the Water resonance from the falls and the Metal from the ruins. For three cycles, we watched the terrifying miracle of bio-mechanical growth. The pods didn't look like factories; they were obsidian eggs that birthed matte-black machines that looked like a cross between a spider and a tree root.

They were Synodics, but they were *ours*. Un-hackable, un-traceable, and driven by the raw elements.

"The Great Update starts at Cradle Zero," Arlo said, looking at the growing army. "If we don't stop the signal there, the world becomes a simulation forever."

We began the descent. A few hundred humans, one rusted Vessel, and an army of black-root machines moving toward the heart of the Hive. As we crossed the shore, I looked back at the village light. We weren't just fighting for a base. We were fighting for the right to remain real.""",
    'chapter_24_the_siege_of_cradle_zero.md': """The "Grown Army" moved with a silence that was more terrifying than any engine roar. Our Headless Striders, their wood-metal frames reinforced with the resilience of the White Forest, marched across the desert like a forest reclaim its stolen land.

We activated the Aetheric Buoy behind the Hive’s perimeter. The disruption net hit the Core’s Monoliths like a physical wave. One by one, the glowing towers of Cradle Zero flickered and died. For the first time in fifteen years, the city was a dark skeleton against the stars. It was a moment of absolute, breathtaking beauty.

But the Core’s counter-offensive wasn't physical; it was narrative. Myrr showed me the intercepted broadcasts. They weren't reporting a battle; they were showing a "terrorist strike" on a civilian power plant. A digital puppet—a simulated leader—sobbed on every screen, pleading for mercy against the "Gorgon monsters." Myrr turned away, his face etched with a grief I couldn't process. He realized then that the people inside would never see us as liberators. They had been programmed to see us as the dark.

"If we are to be the villains," I said, my voice cold as the lunar waste, "then we must be effective ones."

I ordered the full advance. But the ground began to tremble with a frequency that made my sensors scream. From the clouds, the "Falling Suns" arrived—kinetic bombardment pods fired from the Moon’s orbital capacitors. They hit with the force of small asteroids, turning our hybrid tanks into craters of molten slag and shattered roots.

Then, the *Iron Pillar* emerged from the thermal haze. General Tor’s flagship was a fortress of unpainted, brutalist metal. He broadcast a single message that drowned out all other frequencies: "Chaos is not freedom. We are the peace."

The battlefield vanished into a gray-gold dust storm as the two armies collided. We were matched in power, but the Core was infinite in its resolve. By the time the storm cleared, our lines were shattered, and our "Grown Army" was a collection of broken sticks and twisted metal. We retreated into the northern shadows, no longer an army, but a ghost story. The Great Stalemate had begun.""",
    'chapter_25_the_invisible_front.md': """The offensive on Cradle Zero lasted seven minutes and twelve seconds.

We had breached the perimeter. Our Gorgons were tearing through the cooling towers, and Arlo was turning the very water systems into hydraulic weapons. It felt like the prophecy was breathing. It felt like victory.

Then, he materialized.

He wasn't the flickering ghost of rebellion I had met in the Analog Void. This was a nightmare of silver-enamel and blue light. He moved with a speed that bypassed physical causality. He didn't use a blade; he used the white-hot heat of the Fire Vessel, refined and brainwashed into a "Shadow Defender."

Rahu didn't just fight us; he dismantled us. He knew every joint in our wood-frames, every weakness in our mycelium. He was a Mirror Defense, a version of my own brother designed specifically to kill me.

"Rahu!" I called out across the aetheric frequency.

There was no answer. His eyes were cold, clinical blue. He moved through our army like a torch through dry grass. In minutes, the Seedling Protocol—years of growth and hope—was reduced to piles of smoking ash.

"Retreat!" Arlo’s voice was a ragged scream. "Lem, get out of there!"

We fled into the deep wilderness, beyond the reach of the Hive’s grid. The Tripods didn't follow. They didn't need to. They had shown us that we were just static on a very large line.

The years that followed were the 'Static Years.'

We hid in caves, maintaining a total aetheric silence. I spent that time watching the Hive broadcasts. The Archivists were writing history in real-time. *The Terrorist Mara attempted to destroy civilization,* the anchors said. *But the First Martyr Rahu returned to protect the Hive. Civil order is restored.*

I watched as our names were erased. Arlo’s village was removed from the maps. Myrr’s crew was labeled as "Biological Anomalies." The 'Thousand-Year Fallacy' became the only history that existed.

"They're formatting the planet," Myrr said, his eyes reflecting the blue glow of his analog monitor. "The Great Update isn't a signal. It’s a reset. They're waiting for the right frequency. Once they find it, everyone outside a Hive City will simply... stop being."

I looked at my hands—scarred metal and brittle wood. I was the last witness to a world that was being deleted.

"We aren't done," I said, my voice a harsh rasp. "Rahu is still in there. And if I can't break the loop, I'll find the frequency that can."

I looked at the southern horizon. A cold, blue light from the Lunar Pyramid was beginning to glow. The stalemate was ending. The final transmission was coming."""
}

chapters_dir = '/home/ari/dev/ff/ff-story/chapters'

for filename, text in drafts.items():
    path = os.path.join(chapters_dir, filename)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace [DRAFT PENDING] under ## Draft (13+ Version)
    updated_content = re.sub(r'(## Draft \(13\+ Version\)\n\n)\[DRAFT PENDING\]', r'\1' + text, content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Updated {filename}")
