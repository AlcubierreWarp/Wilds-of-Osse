# Wilds of Ossë

Homebrew content for **Wilds of Ossë**, a homebrew D&D 5e campaign, packaged for [5e.tools](https://5e.tools).

The loadable file is [`wilds-of-osse.json`](wilds-of-osse.json) at the root. It is **generated**, not hand-edited. The sources live in [`src/`](src) and a GitHub Action reassembles the combined file whenever a fragment changes.

---

## Loading it into 5e.tools

Open the Bestiary, click **Manage Homebrew**, choose **Load from URL**, and paste:

```
https://raw.githubusercontent.com/AlcubierreWarp/Wilds-of-Osse/main/wilds-of-osse.json
```

It has to be the `raw.githubusercontent.com` link. The repository page URL with `/blob/` in it will not work. To load from a download instead, grab the file and use **Upload File** in the same dialog.

Either way, 5e.tools keeps its own copy in browser storage, and that copy does not update on its own. After a change here, remove the old brew and load it again.

---

## How the repository works

```
wilds-of-osse.json          generated, do not edit
src/
  _meta.json                source block, version, timestamps
  pyreborn.json             Pyreborn gang and the Drover's Rest cast
  unbowed.json              The Unbowed
  arcane-marshals.json      Arcane Marshals
  oss-kai.json              Oss'kai mage and healer lineages
  misc.json                 ungrouped creatures
  items.json                items
  hazards.json              traps and hazards
tools/
  build.py                  merges src/ into wilds-of-osse.json
  split.py                  one-time split, already run
.github/workflows/
  build-homebrew.yml        rebuilds on any change under src/
  split-brew.yml            the one-time split, can be deleted
```

**To change content**, edit the relevant file in `src/`. On push to `main`, the build workflow merges the fragments, validates the result, and commits the rebuilt `wilds-of-osse.json` only if it actually differs. The raw URL above never changes.

**Fragments are just buckets.** The build concatenates whatever it finds, in alphabetical order of filename. Entries can be moved between files freely, and new fragment files can be added without touching anything else. A fragment is a JSON object whose keys are 5eTools content arrays (`monster`, `item`, `trap`), with no `_meta` block of its own.

**The build fails loudly** on malformed JSON, on a duplicate entry name within a type, on a fragment containing a stray `_meta`, and on a missing `src/_meta.json`. It stamps `dateLastModified` on every run. `version` in `src/_meta.json` is bumped by hand for meaningful content changes.

Running the build workflow with no `src/` directory is treated as a skip rather than a failure, so an empty state cannot overwrite the combined file.

The split has already been run and will refuse to run again. `split-brew.yml` is safe to delete.

---

## What is in it

Source name **Wilds of Ossë**, abbreviation **WoO**. Everything is filterable under that source and stays separate from official content.

### Creatures (32)

**Pyreborn** (`src/pyreborn.json`) — arson-and-extortion gang in Althon's Gate, plus the Drover's Rest safehouse cast.

| Creature | CR |
|---|---|
| Pyreborn Initiate | 1/8 |
| Yard Dog | 1/8 |
| Pyreborn Bravo | 1/2 |
| Pyreborn Thug | 1 |
| Pyreborn Enforcer | 2 |
| Nessa Ruhl | 3 |
| Pyreborn Lieutenant | 4 |
| Bram Kell | 5 |

**The Unbowed** (`src/unbowed.json`) — revolutionary cells working the poor quarters.

| Creature | CR |
|---|---|
| Unbowed Agitator | 1/2 |
| Unbowed Organizer | 2 |
| Unbowed Supervisor | 4 |
| Ilna Vesk | 6 |

**Arcane Marshals** (`src/arcane-marshals.json`) — rune-trained law enforcement.

| Creature | CR |
|---|---|
| Marshal Constable-Adept | 1 |
| Marshal Sergeant-Adept | 3 |
| Marshal Lieutenant | 5 |
| Marshal-Captain Elowen Rhys | 9 |

**Oss'kai** (`src/oss-kai.json`) — the K'Tinga and their spellcraft and healing lineages.

| Creature | CR |
|---|---|
| Oss'kai Scout | 1/2 |
| Oss'kai Mage (Apprentice) | 1 |
| Oss'kai Healer (Apprentice) | 1 |
| Oss'kai Hunter | 2 |
| Oss'kai Mage (Journeyman) | 4 |
| Oss'kai Healer (Journeyman) | 4 |
| Oss'kai Mage (Master) | 8 |
| Oss'kai Healer (Master) | 8 |
| Oss'kai Mage-Adept | 13 |
| Oss'kai Healer-Adept | 13 |

**Ungrouped** (`src/misc.json`) — nobility, tournament competitors, civilians.

| Creature | CR |
|---|---|
| Alma Marrow | 0 |
| Denn Marrow | 0 |
| Poor-Quarter Rioter | 1/8 |
| Lord Cassian Aerrowyn | 5 |
| Baroness Eclair Exquisite | 5 |
| Marquis Corvane Aerrowyn | 7 |

### Hazards (1) — `src/hazards.json`

- **Sabotaged Shield Rune** — a defensive rune altered to invert on discharge.

### Items (6) — `src/items.json`

- Sun and Moon Signet Ring
- Split Ring, Sun Half
- Split Ring, Moon Half
- Father Barichello's Rosary
- Father Barichello's Bible
- Blank Rune Tablet

---

## Conventions

- **Adepts are not encounters.** The two CR 13 Oss'kai Adepts are deliberately out of reach for a mid-level party. They are people you negotiate with.
- **Non-combatants** are included at CR 0 because their hit points and traits matter at the table. They will look wrong in an encounter calculator, which is expected.
- **Creature grouping** comes from the `group` field, which is what the original split keyed on and what a future split would key on again. An entry with no group lands in `misc.json`.
- **Roll20.** This format does not import into Roll20. Copy a rendered block into a character sheet, or export the entry as Markdown into a handout.
- **Workflow permissions** must be set to read and write under Settings, Actions, General. The build commits back to the repository.

## Spoiler warning

This is written from the DM side. Creature fluff includes motives, weaknesses, secrets, and trigger conditions that players are not meant to know. Read at your own risk.
