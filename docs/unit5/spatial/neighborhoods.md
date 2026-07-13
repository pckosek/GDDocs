# 5.3.4 Represent Neighborhoods

## Classification

**Type:** Design / Engineering Guide

**Category:** Spatial Representation

**Difficulty:** Beginner

---

# Design Problem

Representing individual locations is only the beginning.

Imagine standing in the middle of a maze.

Knowing your current location is useful.

But many questions require something more.

For example:

- Where can I move next?
- Which walls surround me?
- Which neighboring cells are empty?
- Which nearby pixels should I examine?
- Which adjacent tiles should change?

These questions are no longer about individual locations.

They are about **relationships between locations**.

Those relationships are called **neighborhoods**.

---

# Why This Matters

Many computational algorithms reason locally.

Rather than examining an entire world...

...they examine one location and its nearby neighbors.

Examples include:

- maze generation
- cellular automata
- pathfinding
- image processing
- flood fill
- terrain generation

Neighborhoods provide the computer with a way of understanding local structure.

---

# Mental Model

Imagine standing in one square of a grid.

```text
□ □ □

□ X □

□ □ □
```

The center cell represents your current location.

The surrounding cells form its neighborhood.

Sometimes we care only about the four cardinal neighbors.

```text
    ↑

←   X   →

    ↓
```

Sometimes we care about all eight surrounding cells.

The appropriate neighborhood depends on the problem being solved.

---

# Representing Relationships

Notice that neighborhoods describe **connections**.

A location by itself tells us:

```text
Where am I?
```

A neighborhood tells us:

```text
Where can I go?
```

or

```text
Who surrounds me?
```

The neighborhood represents the relationship between one location and the locations nearby.

---

# Starter Representation

Suppose this world:

```text
0  1  2  3

4  5  6  7

8  9 10 11
```

Cell **5** has the following neighbors.

```text
1

4   5   6

9
```

One useful representation might be:

```python
neighbors = {
    5: [1, 4, 6, 9]
}
```

The computer no longer has to calculate these relationships every time.

Instead...

...it simply looks them up.

---

# Dissecting the Representation

Notice that the neighborhood is itself another representation.

It stores information about relationships.

```text
Location

↓

Neighbor List
```

Each location is associated with the cells surrounding it.

The world has become more than a collection of cells.

It has become a network of connected locations.

---

# Design Principle

## Relationships deserve representations too.

Representing locations is important.

Representing how those locations connect is equally important.

Many algorithms become dramatically simpler once relationships have been represented explicitly.

---

# Experiment

Suppose each of the following has neighborhoods.

What would a neighborhood represent?

| Representation | Neighborhood |
|----------------|--------------|
| Tile Map | |
| Maze | |
| Image | |
| Cellular Automata | |
| Height Map | |
| Chess Board | |

Can you explain what "neighbor" means in each case?

---

# Practical Observation

Beginning programmers often calculate neighboring locations every time they need them.

As programs become larger...

...those same calculations may happen thousands or even millions of times.

Representing neighborhoods once allows later algorithms to focus on solving their actual problem instead of repeatedly performing the same calculations.

---

# Common Misconceptions

### "Neighbors only exist in games."

No.

Neighborhoods appear throughout computing.

Images, simulations, robotics, graphs, and scientific models all reason about nearby locations.

---

### "Every neighborhood has four neighbors."

Not necessarily.

Different algorithms define neighborhoods differently.

Some use four.

Some use eight.

Others use completely different relationships.

---

### "Neighborhoods are part of the world."

Not exactly.

The world stores locations.

The neighborhood stores relationships between locations.

These are different representations.

---

### "Neighborhoods must always be calculated."

Not at all.

Many programs build neighborhood representations once and reuse them throughout the computation.

---

# Reflection

Think about one computational artifact.

- an image
- a maze
- a cave
- a tile map

Choose one location.

Who are its neighbors?

Now ask yourself:

Would solving the problem become easier if every location already knew its neighbors?

---

# Looking Ahead

Once relationships have been represented...

...we can begin making computation much more efficient.

The next question becomes:

> **How can we build lookup tables that allow the computer to answer common questions instantly?**