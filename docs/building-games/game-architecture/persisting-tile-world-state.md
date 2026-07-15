# 8.2.6 Persistence

## Classification

**Type:** Engineering Technique

**Category:** Tile-Based Worlds

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

Imagine the player reaches the middle of your adventure.

They have:

- defeated several enemies
- collected important items
- unlocked new abilities
- completed puzzles

Then they close the game.

What happens tomorrow?

Should everything disappear?

Most games answer:

No.

The player's progress is **saved**.

When the game starts again...

that progress is restored.

This process is called **Persistence**.

---

# Why This Matters

Persistence allows games to remember previous play sessions.

Instead of beginning from the start every time...

the game restores important information.

Examples include:

- player position
- inventory
- health
- completed quests
- unlocked abilities
- world progress

Persistence transforms individual play sessions into one continuous adventure.

---

# Mental Model

Think about writing in a notebook.

When you close the notebook...

the writing remains.

When you open it tomorrow...

everything is still there.

Games work similarly.

```text
Game State

↓

Save

↓

File

↓

Load

↓

Continue Playing
```

The file becomes a memory of the game.

---

# Starter Workflow

A typical save system follows this sequence.

```text
GameManager

↓

Collect Data

↓

Convert To JSON

↓

Write File
```

Later...

```text
Read File

↓

Parse JSON

↓

Restore Game State
```

The player continues exactly where they left off.

---

# Why JSON?

JSON stores information using a simple text format.

For example:

```json
{
  "health": 5,
  "coins": 27,
  "current_scene": "Dungeon01",
  "abilities": [
    "bow",
    "bomb"
  ]
}
```

This information can easily be:

- saved
- loaded
- inspected
- modified

JSON becomes one representation of the game's persistent state.

---

# Dissecting the System

Notice what is being saved.

Not the entire world.

Instead...

only the information needed to rebuild the world.

```text
Player State

+

World State

↓

Save File
```

When the game loads...

those values recreate the player's progress.

---

# Design Principle

## Save information.

Not objects.

Good save systems record the information needed to recreate the game.

Rather than saving every node in the scene...

save the data that describes those nodes.

Representations are often much smaller, simpler, and easier to maintain than entire gameplay objects.

---

# Practical Observation

Many beginning projects attempt to save entire scenes.

As projects become larger...

developers usually save only important information.

Examples include:

- numbers
- strings
- booleans
- arrays
- dictionaries

These simple values can later recreate much more complicated gameplay systems.

The save file becomes another representation of the world.

---

# Common Misconceptions

### "Saving means writing the whole game."

Usually not.

Most save systems store only the information necessary to rebuild the player's progress.

---

### "JSON saves gameplay objects."

JSON stores data.

The game later interprets that data to recreate gameplay objects.

---

### "Everything should be saved."

Not necessarily.

Some information is temporary.

Good save systems carefully choose what should persist between play sessions.

---

### "Persistence only matters for large games."

Even small games benefit from allowing players to continue where they left off.

Persistence improves accessibility and player experience.

---

# Reflection

Imagine saving your adventure game.

Which information should be stored?

| Information | Save? |
|-------------|-------|
| Player Health | |
| Inventory | |
| Current Scene | |
| Player Position | |
| Opened Doors | |
| Completed Quests | |
| Temporary Particle Effects | |

Now ask yourself:

Which information describes the player's journey...

...and which exists only for the current moment?

---

# Looking Back

Earlier we explored:

- procedural population
- spawn systems
- scene transitions

Now we've completed the world.

The game no longer exists only while it is running.

The player's progress can continue across many different play sessions.

Persistence allows adventures to extend beyond a single session by storing the information needed to recreate the world.

---

# Section Reflection

Throughout this section we explored how TileMaps become gameplay.

We learned that worlds can:

- describe interaction
- populate themselves procedurally
- spawn gameplay objects
- connect through scene transitions
- preserve player progress

The world is no longer simply a collection of graphics.

It has become a living system that players can explore, influence, and return to.

---

# Looking Ahead

The world now remembers the player.

The next challenge is making the player affect that world.

How do we create:

- dialogue
- switches
- keys
- inventories
- quests

that allow the world to respond intelligently?

We'll begin exploring:

> **Interaction Systems**