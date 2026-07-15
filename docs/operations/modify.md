# 5.2.3 Modify

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Operations

**Difficulty:** Beginner

---

# Design Problem

Representations rarely stay the same.

Imagine a player collecting a coin.

The inventory changes.

The score changes.

The number of remaining enemies changes.

As a game runs, information is constantly updated.

Representations are not static.

They evolve over time.

The operation of changing an existing representation is called **modification**.

---

# Why This Matters

Games are built around change.

Players:

- gain health
- lose health
- collect items
- open doors
- unlock achievements
- discover locations

Every one of these events modifies an existing representation.

Without modification, games would never progress beyond their initial state.

---

# Mental Model

Think of a whiteboard.

At the beginning of class, it is empty.

As the lesson continues:

- new ideas are written
- mistakes are erased
- diagrams are updated

The whiteboard remains the same object.

Only its contents change.

Modification works the same way.

The representation remains.

Its information changes.

---

# Starter Implementation

Suppose we have an inventory.

```python
inventory = [
    "Sword",
    "Shield",
    "Potion"
]
```

Later, the player finds a key.

```python
inventory.append("Key")
```

The inventory has been modified.

---

Or perhaps a player dictionary.

```python
player = {
    "health": 100,
    "coins": 12
}
```

After collecting a coin:

```python
player["coins"] += 1
```

The representation still describes the same player.

Only one value has changed.

---

# Dissecting the Operation

Notice that modification changes existing information.

For example:

```text
Health

100

↓

82
```

Or

```text
Inventory

Sword

Shield

Potion

↓

Sword

Shield

Potion

Key
```

The representation grows and evolves.

It is still the same collection.

---

# Design Principle

## Modify only what has changed.

Good software avoids rebuilding an entire representation when only a small part has changed.

If one value changes...

...modify that value.

This keeps programs efficient and easier to understand.

---

# Experiment

Suppose the following events occur.

| Event | What Changes? |
|--------|---------------|
| Player takes damage | |
| Player picks up a key | |
| Enemy defeated | |
| Volume increased | |
| Door unlocked | |

For each example, identify which representation is being modified.

---

# Practical Observation

Many different kinds of modifications exist.

Examples include:

- changing one value
- adding a new value
- removing a value
- replacing an existing value

Although these operations look different...

...they all modify an existing representation.

The representation survives.

Its contents change.

---

# Common Misconceptions

### "Modification creates a new representation."

Usually not.

Modification updates an existing representation.

The overall structure remains.

---

### "Every modification changes the whole collection."

No.

Often only one value changes.

The rest of the representation remains exactly the same.

---

### "Modification is only adding information."

No.

Modification may involve:

- adding
- removing
- replacing
- updating

All are forms of changing an existing representation.

---

### "Changing one value changes what the representation is."

Usually not.

A player is still a player.

An inventory is still an inventory.

Only the information stored inside has changed.

---

# Reflection

Imagine a simple adventure game.

During gameplay, which of the following representations will probably be modified?

| Representation | Modified? |
|----------------|-----------|
| Player Statistics | |
| Inventory | |
| Tile Map | |
| Current Position | |
| RGB Color | |
| Image Width | |

Now ask yourself:

Which representations change frequently?

Which rarely change?

Why?

---

# Looking Ahead

Modification changes one representation.

Sometimes, however, we need to bring **two** representations together.

The next question becomes:

> **How can we combine information to create something new?**