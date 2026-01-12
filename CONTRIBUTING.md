# Contributing to Forgotten Future

Thank you for your interest in contributing to## GitHub Issues (Reporting Problems)

Found a plot hole, inconsistency, or narrative issue? Open an issue.Forgotten Future**, an AI-driven open-source narrative experiment. This document outlines how you can help shape the story, whether through comments, lore suggestions, or direct contributions via GitHub.

## What is Forgotten Future?

Forgotten Future is a sci-fi narrative epic developed collaboratively. We use AI to maintain narrative consistency, explore complex world-building, and ensure causality is never sacrificed. The project is committed to remaining open-source and community-driven from conception to publication.

**Current Phase:** Phase VI — AI-Generated Prose Composition (ongoing refinement and lore hardening)

## Ways to Contribute

### 1. Web-Based Comments (Easiest)

No technical setup required. Simply visit our website and share your thoughts.

**What to contribute:**
- Story feedback and impressions
- Lore suggestions or world-building ideas
- Plot hole identification
- Character motivation discussions
- Creative theories and alternate ideas

**How:**
1. Visit [Forgotten Future website](https://ffga.me)
2. Use the Contact page or chapter discussion sections
3. Share your name (or handle) and comment
4. Your contribution is recorded and credited

### 2. GitHub Pull Requests (For Direct Changes)

For writers, developers, and technical contributors who want full control over changes.

**What to contribute:**
- **Prose & Writing:** Chapter drafts, dialogue refinement, narrative consistency improvements
- **World-Building:** Character profiles, lore documentation, timeline updates, setting details
- **Code & Tools:** Build scripts, utility tools, bug fixes, documentation improvements
- **Editorial:** Fact-checking, grammar/style improvements, consistency audits
- **POV Enforcement:** Ensuring the entire story remains strictly in Lem's POV (1st hand or discovered 2nd/3rd hand). No other POV characters are allowed.

**How to Get Started:**

#### Clone the Repository
```bash
git clone https://github.com/clevertree/ff-story.git
cd ff-story
```

#### Create a Feature Branch
```bash
git checkout -b feature/your-contribution-name
```

Use descriptive branch names:
- `feature/character-expansion-iris` — for character work
- `fix/timeline-inconsistency-chapter5` — for bug fixes
- `docs/expanded-lore-system` — for documentation

#### Make Your Changes
Before editing, familiarize yourself with:
- **[world-building/facts.md](world-building/facts.md)** — The canonical "facts" of the universe (source of truth)
- **[chapters/INDEX.md](chapters/INDEX.md)** — Story structure and formatting standards
- **[STYLE_GUIDE.md](manuscript/STYLE_GUIDE.md)** — Narrative voice and tone expectations
- **[.github/copilot-instructions.md](.github/copilot-instructions.md)** — AI narrative standards (if available)

#### Commit Your Changes
Use clear, imperative commit messages:
```bash
git commit -m "Add backstory for character Iris Novak"
git commit -m "Fix timeline inconsistency between Chapter 3 and Chapter 7"
git commit -m "Expand lore documentation for The Gorgons"
```

#### Push and Create a Pull Request
```bash
git push origin feature/your-contribution-name
```

Then open a Pull Request on GitHub with:
- **Title:** Clear description of changes
- **Description:** Why you made this change, any related context, or questions
- **References:** If related to any GitHub issues, mention them

### 3. GitHub Issues (Reporting Problems)

Found a plot hole, inconsistency, or narrative issue? Open an issue.

**How:**
1. Go to [Issues](https://github.com/clevertree/ff-story/issues)
2. Click "New Issue"
3. **Title:** Concise description of the problem
4. **Description:** 
   - What's the issue? (e.g., "Timeline contradiction between Chapter 4 and Chapter 9")
   - Where is it? (specific section/chapter)
   - What should happen instead?
   - Suggested fix (optional)

## Contribution Guidelines

### Consistency & Lore Integrity
- **Always check** [world-building/facts.md](world-building/facts.md) before making changes
- Ensure new lore doesn't contradict established canon
- If you're adding new facts, update the facts.md file
- Use the [QUESTION_RESOLUTION_PROMPT.md](QUESTION_RESOLUTION_PROMPT.md) to resolve ambiguities through iterative dialogue

### Narrative Voice & Tone
- Maintain the sci-fi atmosphere and tone established in existing chapters
- Preserve character voices and motivations as defined in [world-building/characters/](world-building/characters/)
- Use the manuscript [STYLE_GUIDE.md](manuscript/STYLE_GUIDE.md) for prose standards

### Documentation
- Update markdown files when adding or changing narrative elements
- Include clear explanations of changes in commit messages
- If modifying chapter structure, update [chapters/INDEX.md](chapters/INDEX.md)
- For character/world changes, update relevant docs in [world-building/](world-building/)

### Code Contributions
- Follow existing code style in Python scripts
- Include docstrings and comments for clarity
- Test scripts before submitting
- Update README documentation if adding new tools

## The Credits System

**Every contribution is credited permanently.**

### How It Works
1. All contributors are tracked by GitHub username or submitted name
2. Contributions are categorized: Narrative, Editorial, Code, Art & Design, etc.
3. Credits persist across all future editions and updates
4. As the project evolves toward publication, contributors may be eligible for revenue sharing (details TBD)

### Credit Categories
- **📖 Narrative:** Story, prose, dialogue, lore
- **🎨 Art & Design:** Visuals, UI, graphics, assets
- **⚙️ Development:** Code, tools, scripts, infrastructure
- **🔍 Editorial:** Feedback, fact-checking, QA, corrections

## Project Structure

```
ff-story/
├── README.md                          # Project overview
├── CONTRIBUTING.md                    # This file
├── synopsis.md                        # High-level narrative summary
├── world-building/
│   ├── facts.md                       # CANONICAL FACTS (source of truth)
│   ├── timeline/                      # Chronological events
│   ├── characters/                    # Character profiles
│   ├── entities/                      # Mechanical beings, Synodics, etc.
│   └── settings/                      # Locations
├── chapters/                          # Chapter planning documents
│   ├── INDEX.md                       # Master chapter index
│   ├── chapter_01_through_16.md       # Planning documents
│   └── CHAPTER_PLANNING_PROMPT.md     # System prompt for chapter planning
├── manuscript/
│   ├── FULL_MANUSCRIPT.md             # Assembled prose narrative
│   ├── STYLE_GUIDE.md                 # Narrative voice standards
│   └── text/                          # Individual chapter prose
└── scripts/                           # Build and utility scripts
```

## Questions or Discussions?

- **For general discussion:** Open a GitHub Discussion in the repository
- **For feedback:** Use the Contact page on the website
- **For specific issues:** Open a GitHub Issue with detailed information
- **To connect with other contributors:** Tag them in issues/PRs or start a Discussion

## Code of Conduct

We're building this narrative together. Be respectful, constructive, and open-minded:
- Assume good intent from other contributors
- Provide thoughtful feedback
- Acknowledge others' work and ideas
- Keep discussions focused on the project

## Recognition

- Contributors are publicly credited by name/handle in the repository and eventual publications
- Significant contributors may be listed in book credits
- As commercial opportunities develop, compensation discussions will include original contributors
- All commits are permanent history—your contribution is forever part of Forgotten Future

## Support

Have questions? 
- Check the [FAQ](https://ffga.me/faq)
- Visit the [Contribute page](https://ffga.me/contribute) for more details
- Email: ari@asu.edu
- GitHub: [@clevertree](https://github.com/clevertree)

---

**Thank you for helping us build Forgotten Future.** Whether it's a single comment or sustained collaboration, you're part of something unprecedented: a community-driven, AI-enhanced narrative experiment.

*The stars die. Let's write what comes next.* ✦
