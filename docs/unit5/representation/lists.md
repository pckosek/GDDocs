# 5.1.2 Ordered Collections (Lists)

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Representation

**Difficulty:** Beginner

---

# Design Problem

Imagine storing the player's inventory.

```
Sword
Shield
Potion
Key
```

Now imagine storing the pixels in an image.

Or the samples in a sound.

Or the cells in a game world.

Does the order matter?

In every one of these examples, the answer is **yes**.

Changing the order changes the meaning of the data.

Whenever order matters, one of the simplest and most useful representations is a **List**.

---

# Why This Matters

Lists are one of the most commonly used collections in programming.

They appear everywhere.

For example:

- player inventories
- game worlds
- animation frames
- image pixels
- audio samples
- paths through a maze
- enemy spawn locations

A list allows us to store many related values while preserving the order in which they appear.

---

# Mental Model

Think of a list as a numbered sequence.

```text
Inventory

0  Sword

1  Shield

2  Potion

3  Key
```

Every value has a position.

That position is called its **index**.

Because every value has an index, we can quickly retrieve any element in the collection.

---

Another example.

```text
Image

0  255

1  240

2  180

3  90

...
```

Changing the order of those pixels changes the image.

Order is part of the representation.

---

# Starter Implementation

Creating a list is straightforward.

```python
inventory = [
    "Sword",
    "Shield",
    "Potion",
    "Key"
]
```

Lists can also store numbers.

```python
scores = [
    100,
    250,
    410,
    900
]
```

Or even other collections.

```python
points = [
    (2, 3),
    (5, 7),
    (9, 1)
]
```

A list simply stores an ordered collection of values.

---

# Dissecting the Structure

Notice two important characteristics.

A list:

- preserves order
- allows duplicate values

For example:

```python
inventory = [
    "Potion",
    "Potion",
    "Potion"
]
```

This is perfectly valid.

The list remembers all three potions in order.

---

# Design Principle

## Use a list when order matters.

If the first element is different from the second...

...and the second is different from the third...

...a list is often an appropriate representation.

Order is one of the defining features of a list.

---

# Experiment

Consider the following situations.

Does the order matter?

| Collection | Does Order Matter? |
|------------|--------------------|
| High Scores (sorted) | |
| Pixels in an Image | |
| Audio Samples | |
| Cards in a Deck | |
| Player Inventory | |
| Enemy Spawn Order | |

Can you explain why?

---

# Practical Observation

Lists are especially powerful because they grow naturally.

You can begin with an empty list.

```python
inventory = []
```

As the game runs...

items can be added.

Later...

items can be removed.

The representation changes while the overall structure remains the same.

This flexibility makes lists useful for many gameplay systems.

---

# Common Misconceptions

### "A list stores only numbers."

No.

Lists can store almost any kind of value.

Examples include:

- integers
- strings
- tuples
- dictionaries
- objects
- even other lists

---

### "Every value in a list must be unique."

No.

Lists allow repeated values.

If a player has three identical potions, a list can represent all three.

---

### "Lists automatically sort themselves."

No.

A list preserves the order in which values are stored.

If you want a different order, your program must change it.

---

### "Changing the order doesn't matter."

Sometimes it matters enormously.

Reordering the pixels in an image or the samples in a sound completely changes the resulting artifact.

---

# Reflection

Suppose you are creating each of the following.

Would a list be an appropriate representation?

| Problem | List? |
|----------|-------|
| Player Inventory | |
| Pixels in an Image | |
| Sound Samples | |
| Game Board | |
| Maze Path | |
| Set of Unlocked Achievements | |

Now ask yourself:

What would happen if the order of those values changed?

---

# Looking Ahead

Lists preserve order.

Sometimes, however, we want a collection whose values should never change after they are created.

The next question becomes:

> **How can we represent a fixed collection of values?**