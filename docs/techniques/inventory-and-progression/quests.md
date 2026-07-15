---
tags: [technique, inventory]
---

# 8.3.6 Quests

## Classification

**Type:** Engineering Technique

**Category:** Interaction

**Difficulty:** Beginner

**Estimated Time:** 15–20 minutes

---

# Design Problem

Imagine speaking to a villager.

They ask:

> "Please find my lost key."

The conversation ends.

Nothing happens immediately.

Much later...

the player finds the key.

Returns.

Receives a reward.

How did the game remember what the player was trying to do?

This is called a **Quest**.

---

# Why This Matters

Quests organize longer-term player goals.

Rather than completing an interaction immediately...

the player continues exploring the world before returning later.

Quests help connect:

- exploration
- interaction
- progression

into one larger experience.

---

# Mental Model

Think about writing a reminder.

You do not complete the task immediately.

Instead...

you remember it until the appropriate time.

Games work similarly.

```text
Goal

↓

Explore

↓

Complete

↓

Reward
```

The game remembers the objective while the player continues playing.

---

# Starter Workflow

A simple quest often follows this sequence.

```text
NPC

↓

Goal Given

↓

Player Explores

↓

Objective Completed

↓

Reward
```

Each stage changes the quest's state.

The player gradually moves toward completion.

---

# Dissecting the System

Notice that quests are another example of state.

```text
Not Started

↓

Active

↓

Complete
```

The player's interactions gradually change the quest's state.

Different NPCs and gameplay systems respond differently depending on that state.

---

# Design Principle

## Goals create direction.

Players enjoy exploring.

Quests provide purpose for that exploration.

Rather than telling players exactly how to play...

quests suggest meaningful objectives while allowing players freedom in how they achieve them.

---

# Practical Observation

Many beginning projects only need very simple quests.

Examples include:

- collect one item
- reach one location
- defeat one enemy
- activate one switch

Complex quest systems can always be added later.

The important idea is that the game remembers what the player is trying to accomplish.

---

# Common Misconceptions

### "Quests require dialogue."

Not necessarily.

A quest may begin through:

- exploration
- discovering an object
- entering an area
- interacting with an NPC

---

### "Every game needs a quest log."

Not at all.

Many games communicate goals naturally through the world itself.

---

### "Quests are only for RPGs."

Adventure games.

Puzzle games.

Exploration games.

Many genres organize player goals using simple quest systems.

---

### "Quests are separate from game state."

Quests are another form of state.

The player's actions gradually change their progress toward completion.

---

# Reflection

Imagine designing a simple adventure.

What quests might the player complete?

- find a key
- rescue a character
- activate three switches
- deliver an item

How would the game know when each quest is complete?

What information would it need to remember?

---

# Looking Back

Throughout this section we explored interaction.

We learned how players:

- interact with objects
- talk to NPCs
- unlock doors
- activate switches
- carry items

Quests combine those ideas into longer-term goals.

The player's actions gradually transform the world while the game remembers their progress.

Interaction now extends across the entire adventure.

---

# Section Reflection

Adventure games are built from interactions.

Players do more than move.

They:

- explore
- communicate
- collect
- unlock
- activate
- complete goals

Each interaction changes the state of the world.

The world gradually becomes a record of the player's journey.

---

# Looking Ahead

The world can now respond intelligently to the player.

The final challenge is making the world respond intelligently on its own.

How do enemies:

- patrol
- investigate
- chase
- attack

while sharing the same interactive world?

We'll begin exploring:

> **Enemy Behaviour**