# 5.2.5 Filter

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Operations

**Difficulty:** Beginner

---

# Design Problem

Imagine a game with one hundred enemies.

Only twelve are currently visible.

Should the game update all one hundred?

Probably not.

Or imagine a collection of player scores.

Perhaps we only want scores greater than 1000.

Or a maze algorithm.

Perhaps we only want cells that are still frontiers.

Many computational problems begin with a simple question.

> **Which information should we keep?**

The operation of selecting only the information we need is called **filtering**.

---

# Why This Matters

Computers often store far more information than they use at any particular moment.

Filtering allows programs to focus only on the information that satisfies some condition.

Examples include:

- enemies within range
- walkable tiles
- active particles
- unlocked achievements
- frontier cells
- visible objects

Filtering simplifies later operations by reducing the amount of information we must process.

---

# Mental Model

Think about panning for gold.

A miner begins with a pan full of dirt.

Most of it is discarded.

Only the valuable pieces remain.

```text
Many Values

↓

Apply Rule

↓

Selected Values
```

Filtering works exactly the same way.

The representation already exists.

We simply decide which parts to keep.

---

# Starter Implementation

Suppose we have a list of scores.

```python
scores = [
    120,
    980,
    1400,
    210,
    1800
]
```

We want only scores greater than 1000.

```python
high_scores = [
    score
    for score in scores
    if score > 1000
]
```

Result:

```text
1400

1800
```

The original list still exists.

Filtering creates a new representation containing only the values that satisfy the rule.

---

Filtering works for many representations.

Suppose we have a set.

```python
visited = {
    "Town",
    "Forest",
    "Castle"
}
```

We might choose only locations beginning with the letter **C**.

The operation changes.

The idea remains the same.

---

Suppose we have a dictionary.

```python
player = {
    "health": 100,
    "coins": 12,
    "score": 900
}
```

We might filter entries according to their values or keys.

Again...

The representation changes.

The computational operation remains filtering.

---

# Dissecting the Operation

Filtering always asks two questions.

```text
Look at Value

↓

Does it satisfy the rule?

↓

Yes

↓

Keep It

---------------

No

↓

Discard It
```

The rule may be simple.

```text
Greater than 10
```

Or much more complicated.

The process remains the same.

---

# Design Principle

## Keep only the information you need.

Programs become simpler when unnecessary information is removed before further computation.

Filtering reduces complexity by focusing attention on the values that matter.

---

# Experiment

Imagine the following collections.

What rule might you use to filter each one?

| Collection | Possible Filter |
|------------|-----------------|
| Enemy List | |
| Inventory | |
| Pixels | |
| Sound Samples | |
| Frontier Cells | |
| High Scores | |

Can you describe the rule without writing code?

---

# Practical Observation

Many algorithms repeatedly perform filtering.

For example:

- remove invalid moves
- keep nearby objects
- select walkable tiles
- identify frontier cells
- locate neighboring pixels
- reject impossible candidates

Filtering often appears before another operation such as transformation or combination.

It prepares the data for the next step.

---

# Common Misconceptions

### "Filtering changes the original representation."

Not necessarily.

Many filtering operations create a new representation while leaving the original unchanged.

---

### "Filtering removes random values."

No.

Filtering always follows a rule.

The rule determines which values remain.

---

### "Filtering only works with lists."

No.

Lists, tuples, sets, and dictionaries can all be filtered.

The exact implementation changes.

The computational idea remains the same.

---

### "Filtering makes information disappear."

Usually not.

The original representation often still exists.

Filtering simply creates another representation containing the selected values.

---

# Reflection

Suppose you are writing a Zelda-style game.

What information might you filter?

| Representation | Possible Filter |
|----------------|-----------------|
| Enemies | |
| Items | |
| Rooms | |
| Player Inventory | |
| Tile Map | |
| Sound Samples | |

Now ask yourself:

Why is it often easier to process a filtered representation than the original one?

---

# Looking Ahead

Filtering decides **which** information remains.

Sometimes, however, we want to change **every** value in a representation.

The next question becomes:

> **How can we transform an entire representation into something new?**