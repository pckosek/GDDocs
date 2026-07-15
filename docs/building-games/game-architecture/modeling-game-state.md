# 4.1.1 What is Game State?

## Classification

**Type:** Design / Engineering Guide

**Category:** Game Architecture

**Difficulty:** Intermediate

---

# Design Problem

So far, our games have reacted to what is happening **right now**.

A player enters an Area.

A platform begins moving.

An enemy takes damage.

A sound plays.

These are all **events**.

Events happen...

...and then they are over.

But many games need to remember what has already happened.

Consider these questions:

- Has the player collected the key?
- Which checkpoint was activated?
- Is the door already open?
- How many coins have been collected?
- What is the player's current health?
- Which level is currently loaded?

None of these describe something that is *happening.*

They describe something that **is true.**

That information is called **game state.**

---

# Why This Matters

Without memory, games become impossible.

Imagine a checkpoint that forgets it was activated.

Or a door that closes every frame because it forgets it was opened.

Or an inventory that loses every item whenever the player moves.

The game world must remember the consequences of what has already happened.

Game state is that memory.

---

# Mental Model

Think of a game as two different systems.

```text
Things Happen
```

These are **events.**

Events are temporary.

Examples include:

- button pressed
- player entered an area
- collision occurred
- enemy defeated

---

The game also stores information.

```text
Things Are True
```

This is **state.**

State persists until something changes it.

Examples include:

- score = 350
- door_open = true
- coins = 17
- current_level = 2
- player_health = 85

---

Another way to think about it is:

```text
Event
    ↓
Changes
    ↓
State
    ↓
Influences
    ↓
Future Gameplay
```

Events happen once.

State remains.

---

# Design Principle

## Events change state.

## State changes gameplay.

This relationship appears throughout game development.

For example:

```text
Player collects key
        ↓
has_key = true
        ↓
Door can now open
```

Or

```text
Enemy defeated
        ↓
enemies_remaining -= 1
        ↓
Exit unlocks
```

The event is temporary.

The state persists.

---

# State Vocabulary

Throughout this unit we will encounter several different kinds of state.

| Type | Example |
|--------|---------|
| Boolean | Door Open? |
| Counter | Coins Collected |
| Number | Player Health |
| Reference | Current Checkpoint |
| Enumeration | Idle / Walking / Jumping |
| Collection | Inventory Items |

Each represents a different way of describing the current game.

---

# Practical Observation

When students first begin programming games, they often think that every action needs to happen continuously.

Instead, many actions happen only once.

The important part is remembering that they happened.

Often the simplest solution is not to repeat an event.

It is to store its result.

---

# Common Misconceptions

### "Game state only matters when saving a game."

No.

Almost every gameplay mechanic depends on state.

Saving a game simply stores that state permanently.

---

### "Everything that happens is state."

No.

Many things happen briefly and disappear.

State is the information that remains afterwards.

---

### "Variables are only temporary."

Some variables exist only while a function runs.

Others represent the ongoing state of the game.

Learning where information belongs is one of the central ideas of software engineering.

---

### "Every object should remember everything."

Usually not.

Good systems give each object responsibility only for the information it actually owns.

Later in this unit we'll learn how different objects communicate instead of duplicating information.

---

# Reflection

Complete the sentence.

> An event is...

Complete the sentence.

> Game state is...

Now answer:

Think about your favorite game.

Can you identify five pieces of information that the game must remember while you play?

---

# Looking Ahead

Understanding that games need memory is only the first step.

The next question becomes:

> **Which object should own that information?**