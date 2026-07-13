# 4.1.4 Mutable and Immutable State

## Classification

**Type:** Design / Engineering Guide

**Category:** Game Architecture

**Difficulty:** Intermediate

---

# Design Problem

Not all game information changes.

Some information is expected to change throughout the game.

Other information should remain the same once it has been established.

As programmers, we should understand which kind of information we are working with.

---

# Why This Matters

Imagine keeping track of a player's score.

Every time the player earns points, the score increases.

Changing the score is expected.

Now imagine the game suddenly changes the number of players from one to seventeen halfway through a level.

That probably isn't supposed to happen.

Some information is meant to change.

Some information should stay fixed.

Recognizing the difference helps us design more reliable software.

---

# Mutable State

**Mutable** means **able to change**.

Most gameplay state is mutable because games are constantly changing.

Examples include:

- player health
- score
- ammunition
- enemy health
- inventory contents
- remaining time
- current level

These values change as the player interacts with the game.

```text
Health = 100

↓

Health = 82

↓

Health = 17
```

The information describes the current state of the game.

As the game changes, so does the value.

---

# Immutable State

**Immutable** means **does not change**.

Immutable information usually describes the rules or configuration of the game rather than the current gameplay.

Examples include:

- maximum number of players
- gravity (usually)
- map dimensions
- tile size
- the name of the current project
- the value of π

These values are established once and are rarely modified during gameplay.

```text
Tile Size = 32 pixels
```

That value is used throughout the game.

It doesn't need to change every frame.

---

# Comparing the Two

| Mutable State | Immutable State |
|----------------|-----------------|
| Changes during gameplay | Usually stays the same |
| Describes the current game | Describes the game's rules or configuration |
| Examples: Health, Score, Inventory | Examples: Tile Size, Maximum Players, Gravity |

---

# Design Principle

## Change only what needs to change.

Every time information changes, the game becomes more complicated.

If a value never needs to change, keeping it fixed makes the program easier to understand.

---

# Practical Observation

Many beginner programmers store everything in ordinary variables.

Professional programmers often ask a different question.

> **Should this ever change?**

If the answer is "no," then treating it as fixed makes accidental bugs much less likely.

Thinking carefully about what should—and shouldn't—change is an important part of software design.

---

# Common Misconceptions

### "Everything in a game is mutable."

No.

Many values describe the game itself rather than the current play session.

These often remain constant.

---

### "Immutable means permanent forever."

Not necessarily.

It simply means that, once established, the value is not expected to change during normal gameplay.

A new level or a new project might use different values.

---

### "Changing a value is always bad."

Not at all.

Games depend on changing information.

The goal is simply to change the information that represents gameplay, while keeping configuration information stable whenever possible.

---

# Reflection

For each piece of information below, decide whether it is usually mutable or immutable.

| Information | Mutable or Immutable? |
|--------------|-----------------------|
| Player Health | |
| Current Score | |
| Gravity Setting | |
| Window Title | |
| Inventory Contents | |
| Tile Size | |
| Remaining Lives | |
| Maximum Players | |

Now ask yourself:

Which values describe **the current game**, and which describe **the game itself?**

---

# Looking Ahead

As we identify more and more pieces of game state, another challenge appears.

Sometimes the same information is accidentally stored in more than one place.

When that happens, different parts of the game can disagree about what is true.

How do we prevent that from happening?