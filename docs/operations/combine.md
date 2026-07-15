# 5.2.4 Combine

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Operations

**Difficulty:** Beginner

---

# Design Problem

Sometimes one collection is not enough.

Imagine a game with:

- two inventories
- two sound effects
- two images
- two lists of enemy locations

How can we create a single representation that contains information from both?

The operation of bringing two or more representations together is called **combining**.

---

# Why This Matters

Combining information is one of the most common operations in computing.

Games constantly combine data.

Examples include:

- joining two inventories
- appending one animation after another
- layering two sound waveforms
- merging game settings
- combining paths during maze generation
- assembling multiple procedural components into one world

Large computational artifacts are often built by repeatedly combining smaller ones.

---

# Mental Model

Think of building with LEGO® bricks.

One brick is useful.

Two bricks connected together become something larger.

Representations work the same way.

```text
Representation A

+

Representation B

↓

Larger Representation
```

The resulting structure contains information from both.

---

# Starter Implementation

Lists naturally combine by placing one sequence after another.

```python
inventory_1 = [
    "Sword",
    "Shield"
]

inventory_2 = [
    "Potion",
    "Key"
]

inventory = inventory_1 + inventory_2
```

Result:

```text
Sword

Shield

Potion

Key
```

---

Tuples also combine.

```python
position = (12, 8)

velocity = (2, -1)

data = position + velocity
```

Result:

```text
(12, 8, 2, -1)
```

---

Sets combine through **union**.

```python
visited_1 = {
    "Town",
    "Forest"
}

visited_2 = {
    "Forest",
    "Castle"
}

visited = visited_1 | visited_2
```

Result:

```text
Town

Forest

Castle
```

Duplicate values are automatically removed.

---

Dictionaries combine by merging keys and values.

```python
player = {
    "health": 100,
    "coins": 25
}

settings = {
    "volume": 0.75,
    "difficulty": "Normal"
}

combined = player | settings
```

The resulting dictionary contains information from both collections.

---

# Dissecting the Operation

Notice that every representation combines differently.

| Representation | Combination |
|----------------|-------------|
| List | Append sequences |
| Tuple | Join fixed groups |
| Set | Union of unique values |
| Dictionary | Merge key-value pairs |

The underlying idea remains the same.

We create a larger representation from smaller ones.

---

# Design Principle

## Larger systems are often built by combining smaller representations.

Instead of generating one enormous structure all at once...

...many algorithms create small pieces and assemble them together.

Combination is one of the fundamental ways complexity emerges from simple parts.

---

# Experiment

Imagine building the following.

How might separate representations be combined?

| Artifact | Smaller Pieces |
|-----------|----------------|
| Inventory | |
| Tile Map | |
| Sound Effect | |
| Animation | |
| Procedural Dungeon | |
| Boss Database | |

Can you identify what operation combines the pieces?

---

# Practical Observation

Different representations combine for different reasons.

Lists combine to preserve order.

Tuples combine to extend related information.

Sets combine to expand unique collections.

Dictionaries combine to merge named information.

Understanding *why* a representation combines the way it does is often more important than remembering the exact syntax.

---

# Common Misconceptions

### "Every representation combines the same way."

No.

Each representation has its own rules for combination.

The result depends on what the representation is designed to preserve.

---

### "Combining always produces duplicates."

Not necessarily.

Lists preserve duplicates.

Sets remove them.

Different representations produce different results.

---

### "Combining changes the original collections."

Sometimes.

Sometimes a new representation is produced instead.

Understanding whether an operation modifies an existing representation or creates a new one is an important part of software design.

---

### "Combining only works on collections of the same kind."

Usually collections of the same representation combine most naturally.

However, many programs build larger systems by combining different representations into more complex structures.

For example, a dictionary might contain lists, tuples, and sets.

---

# Reflection

Suppose you are creating a procedurally generated game.

Which representations might you combine?

| Representation A | Representation B | Result |
|------------------|------------------|--------|
| Inventory | Loot Found | |
| Visited Rooms | Newly Visited Rooms | |
| Player Data | Game Settings | |
| Two Sound Effects | | |
| Two Tile Maps | | |

Now ask yourself:

When combining information, what characteristics should remain unchanged?

- Order?
- Uniqueness?
- Named values?
- Fixed structure?

---

# Looking Ahead

Sometimes we don't want **all** of the information.

Instead, we want only the parts that satisfy some condition.

The next question becomes:

> **How can we keep only the information that matters?**