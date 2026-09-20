# Wilds of Ossë

Homebrew content for **Wilds of Ossë**, a homebrew D&D 5e campaign, packaged as a [5e.tools](https://5e.tools) homebrew file.

Everything lives in a single file: [`wilds-of-osse.json`](wilds-of-osse.json).

---

## Loading it into 5e.tools

**From this repository (recommended).** Open the Bestiary, click **Manage Homebrew**, choose **Load from URL**, and paste:

```
https://raw.githubusercontent.com/AlcubierreWarp/Wilds-of-Osse/main/wilds-of-osse.json
```

It has to be the `raw.githubusercontent.com` link. The normal repository page URL with `/blob/` in it will not work.

**From a download.** Grab the file and use **Upload File** in the same dialog.

Either way, 5e.tools keeps a copy in browser storage. That copy does not update on its own, so after a change here, remove the old brew and load it again.

---

## What is in the file

Source name **Wilds of Ossë**, abbreviation **WoO**. Everything is filterable under that source and stays separate from official content.

### Creatures (32)

**The Drover's Rest** — the Pyreborn safehouse cast.

| Creature | CR |
|---|---|
| Nessa Ruhl | 3 |
| Pyreborn Bravo | 1/2 |
| Alma Marrow | 0 |
| Denn Marrow | 0 |
| Yard Dog | 1/8 |

**Pyreborn** — arson-and-extortion gang in Althon's Gate.

| Creature | CR |
|---|---|
| Pyreborn Initiate | 1/8 |
| Pyreborn Thug | 1 |
| Pyreborn Enforcer | 2 |
| Pyreborn Lieutenant | 4 |
| Bram Kell | 5 |

**The Unbowed** — revolutionary cells working the poor quarters.

| Creature | CR |
|---|---|
| Unbowed Agitator | 1/2 |
| Unbowed Organizer | 2 |
| Unbowed Supervisor | 4 |
| Ilna Vesk | 6 |

**Arcane Marshals** — rune-trained law enforcement.

| Creature | CR |
|---|---|
| Marshal Constable-Adept | 1 |
| Marshal Sergeant-Adept | 3 |
| Marshal Lieutenant | 5 |
| Marshal-Captain Elowen Rhys | 9 |

**Oss'kai** — the K'Tinga and their spellcraft and healing lineages.

| Creature | CR |
|---|---|
| Oss'kai Scout | 1/2 |
| Oss'kai Hunter | 2 |
| Oss'kai Mage (Apprentice) | 1 |
| Oss'kai Mage (Journeyman) | 4 |
| Oss'kai Mage (Master) | 8 |
| Oss'kai Mage-Adept | 13 |
| Oss'kai Healer (Apprentice) | 1 |
| Oss'kai Healer (Journeyman) | 4 |
| Oss'kai Healer (Master) | 8 |
| Oss'kai Healer-Adept | 13 |

**Nobility and tournament competitors.**

| Creature | CR |
|---|---|
| Marquis Corvane Aerrowyn | 7 |
| Lord Cassian Aerrowyn | 5 |
| Baroness Eclair Exquisite | 5 |

**Other.**

| Creature | CR |
|---|---|
| Poor-Quarter Rioter | 1/8 |

### Hazards (1)

- **Sabotaged Shield Rune** — a defensive rune altered to invert on discharge.

### Items (6)

- Sun and Moon Signet Ring
- Split Ring, Sun Half
- Split Ring, Moon Half
- Father Barichello's Rosary
- Father Barichello's Bible
- Blank Rune Tablet

---

## Conventions

- **One file for now.** As the collection grows it will likely split by type or by faction, at which point the raw URL above changes.
- **Version.** Bumped in `_meta.sources[0].version` on every meaningful change. Reload in 5e.tools to pick it up.
- **Adepts are not encounters.** The two CR 13 Oss'kai Adepts are deliberately out of reach for a mid-level party. They are people you negotiate with.
- **Non-combatants** are included at CR 0 because their hit points and traits matter at the table. They will look strange in an encounter calculator, which is expected.
- **Roll20.** This format does not import into Roll20. Copy a rendered block into a character sheet, or export the entry as Markdown into a handout.

## Spoiler warning

This file is written from the DM side. Creature fluff includes motives, weaknesses, secrets, and trigger conditions that players are not meant to know. Read at your own risk.
