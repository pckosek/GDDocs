# 8.3.5 Inventory

## Classification

**Type:** Engineering Technique

**Category:** Interaction

**Difficulty:** Beginner

**Estimated Time:** 15–20 minutes

---

# Design Problem

Imagine the player finds a key.

Should the key disappear immediately?

Should the player use it right away?

Or should they carry it until they reach a locked door?

Sometimes the player needs to remember something for later.

Games call this an **Inventory**.

---

# Why This Matters

An inventory stores objects that the player has collected but not yet used.

Examples include:

- keys
- potions
- quest items
- resources
- tools

The inventory allows actions separated by time and place to become connected.

Finding something now may solve a problem much later.

---

# Mental Model

Think about carrying a backpack.

When you find something useful...

you place it inside.

Later...

when you need it...

you take it out.

Games work the same way.

```text
Collect

↓

Store

↓

Use

↓

Remove
```

The inventory connects those four actions.

---

# Starter Implementation

A very simple inventory might be:

```gdscript
var inventory = []
```

Collecting an item:

```gdscript
inventory.append("key")
```

Later:

```gdscript
if "key" in inventory:

    open_door()

    inventory.erase("key")
```

The inventory simply remembers what the player is carrying.

---

# Dissecting the System

Notice the workflow.

```text
World

↓

Collect

↓

Inventory

↓

Use

↓

World Changes
```

The item temporarily leaves the world.

Later...

it returns by changing the world in a new way.

---

# Design Principle

## Store information.

Not objects.

The inventory usually remembers:

- what the player has
- how many
- whether it has been used

Gameplay objects continue existing in the world independently.

The inventory stores information about the player's journey.

---

# Practical Observation

Many adventure games begin with remarkably small inventories.

For example:

- one key
- one bomb
- one potion

The interesting gameplay comes from deciding:

- when to collect
- when to use
- when to save

rather than from managing hundreds of items.

---

# Common Misconceptions

### "Inventories are only for RPGs."

Many adventure, puzzle, survival, and exploration games use simple inventories.

---

### "The inventory stores gameplay objects."

Usually not.

It stores information describing those objects.

The gameplay systems interpret that information later.

---

### "Every game needs a complicated inventory."

Not at all.

Many excellent games need only:

- collect
- use
- remove

Nothing more.

---

### "Inventory is separate from gameplay."

The inventory often becomes another gameplay system.

Players continually make decisions about:

- what to carry
- what to use
- what to save

---

# Reflection

Imagine your adventure game contains:

- a key
- a lantern
- a potion
- a bomb

Which items should disappear after use?

Which should remain?

What decisions do those choices create for the player?

---

# Looking Back

Earlier we explored:

- interaction
- dialogue
- keys and doors
- switches and events

Now we've added another important system.

The player can carry information from one part of the world to another.

The inventory becomes a bridge between past discoveries and future interactions.

---

# Looking Ahead

Items allow players to solve problems.

The final interaction system asks a larger question.

How do games organize longer-term goals?

How do players know what they are trying to accomplish?

We'll begin exploring:

> **Quests**