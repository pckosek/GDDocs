# 8.2.5 Scene Transitions

## Classification

**Type:** Engineering Technique

**Category:** Tile-Based Worlds

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

Imagine leaving a dungeon.

The player walks through a doorway.

The screen fades to black.

A new area appears.

Several questions immediately arise.

- Where does the player appear?
- Does the score remain?
- Does the inventory disappear?
- Do defeated enemies return?
- What happens to the GameManager?

Changing scenes is more than loading another level.

It is continuing the player's journey.

---

# Why This Matters

Many games are built from multiple scenes.

Examples include:

- overworlds
- dungeons
- houses
- shops
- caves

Moving between these scenes should feel seamless.

The player experiences one continuous world...

...even though the game loads many separate scenes.

---

# Mental Model

Think about walking from one room to another in a house.

The room changes.

The person does not.

Games work the same way.

```text
Current Scene

↓

Transition

↓

New Scene
```

The world changes.

The player continues.

---

# Example

A common scene transition might follow this sequence.

```text
Player Reaches Door

↓

Fade Screen

↓

Load New Scene

↓

Position Player

↓

Fade In
```

The transition itself becomes part of the player's experience.

A smooth transition helps the world feel connected rather than fragmented.

---

# Persisting Game State

Notice that not everything should disappear.

When changing scenes...

the game often preserves:

- score
- inventory
- player health
- completed objectives
- unlocked abilities

These systems usually belong somewhere outside the individual level.

For many projects...

this responsibility belongs to the:

```text
GameManager
```

The GameManager survives while scenes change.

It carries the player's progress throughout the game.

---

# Dissecting the System

Notice the separation.

```text
Scene

↓

Temporary World
```

```text
GameManager

↓

Persistent Game State
```

Scenes come and go.

The GameManager continues.

This separation allows the player's adventure to remain continuous across many different locations.

---

# Design Principle

## Separate worlds from progress.

Levels are temporary.

Player progress is not.

Keeping persistent information outside individual scenes creates worlds that can change while preserving the player's journey.

---

# Practical Observation

Many beginning projects accidentally store important information inside the level.

When the scene changes...

everything disappears.

As projects become larger...

persistent information naturally moves into systems such as:

- GameManager
- save files
- global data

The scene represents **where** the player is.

The GameManager represents **who** the player has become.

---

# Common Misconceptions

### "Changing scenes restarts the game."

Not necessarily.

Only the current scene changes.

Persistent systems continue existing.

---

### "The GameManager belongs inside every scene."

Usually not.

The GameManager typically exists independently so it can survive scene transitions.

---

### "Transitions are only visual."

Visual transitions help players understand that the world is changing.

They also provide time for loading and positioning the next scene.

Presentation and functionality work together.

---

### "Every room should be one enormous scene."

Not always.

Many games divide worlds into smaller scenes because they are easier to:

- edit
- organize
- load
- maintain

Scene transitions allow those pieces to feel like one continuous world.

---

# Reflection

Imagine creating an adventure game.

When the player enters a dungeon...

which information should remain?

| Information | Persist? |
|-------------|----------|
| Score | |
| Inventory | |
| Health | |
| Enemy Positions | |
| Current Room | |
| Unlocked Abilities | |

Now ask yourself:

Which information belongs to the world...

...and which belongs to the player?

---

# Looking Back

Earlier we learned that TileMaps describe individual worlds.

Now we've discovered that games often contain many worlds.

Scene transitions connect those worlds into one continuous adventure.

The player experiences one journey...

even though many different scenes appear behind the scenes.

Persistent systems preserve that continuity.

---

# Looking Ahead

Moving between scenes preserves the player's progress.

The final challenge is preserving that progress even after the game closes.

How do we save and restore:

- inventory
- health
- completed quests
- world state

We'll begin exploring:

> **Persistence**