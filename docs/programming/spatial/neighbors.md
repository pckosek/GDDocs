# 5.4.1 What is a Neighbor?

## Classification

**Type:** Design / Engineering Guide

**Category:** Spatial Relationships

**Difficulty:** Beginner

---

# Design Problem

Knowing where something is...

...is only part of understanding a world.

Imagine standing in the middle of a maze.

Knowing your current location is useful. But eventually you will ask questions like:

- Where can I move next?
- Which walls surround me?
- Which enemies are nearby, or which neighboring cells are empty?
- Which adjacent tiles or trees are nearby?
- Which pixels influence this pixel?

These questions are no longer about individual locations.

They are about **relationships between locations**.

Those nearby, related locations are called **neighbors**, and the full set of them around a location is its **neighborhood**.

---

# Why This Matters

Many computational systems and algorithms reason locally. Instead of examining an entire world, they examine one location and the locations immediately around it.

Examples include:

- maze generation
- pathfinding
- cellular automata
- image filters and image processing
- terrain smoothing and terrain generation
- flood fill

Nearly every spatial algorithm begins with the same question:

> **Who are my neighbors?**

Neighborhoods give the computer a way of understanding local structure without needing to examine the entire world at once.

---

# Mental Model

Imagine standing in one square of a grid.

```text
□ □ □

□ X □

□ □ □
```

The center cell represents your current location. The surrounding cells form its neighborhood.

Sometimes we care only about the four cardinal neighbors:

```text
    ↑

←   X   →

    ↓
```

Sometimes we care about all eight surrounding cells. The appropriate neighborhood depends on the problem being solved.

Another way to think about it:

```text
Location

↓

Neighborhood

↓

Local Decisions
```

The computer rarely needs to examine the entire world. Most algorithms make decisions using only nearby information.

---

# Representing Relationships

Notice that a neighborhood describes **connections**, not just a location.

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

Cell **5** has the following neighbors:

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

The computer no longer has to calculate these relationships every time — it simply looks them up.

---

# Dissecting the Representation

Notice that the neighborhood is itself another representation. It stores information about relationships:

```text
Location

↓

Neighbor List
```

Each location is associated with the cells surrounding it. The world has become more than a collection of cells — it has become a network of connected locations.

---

# Design Principles

## Relationships deserve representations too.

Representing locations is important. Representing how those locations connect is equally important. Many algorithms become dramatically simpler once relationships have been represented explicitly.

## Complex behavior often emerges from local relationships.

Many computational systems never examine the entire world. Instead, each location repeatedly interacts only with its neighbors. Remarkably complex structures often emerge from these simple local interactions.

---

# Examples & Experiment

Neighbors appear throughout computational media, though the exact meaning of "neighbor" changes with the representation:

| Medium / Representation | Neighbor Relationship |
|----------|----------------------|
| Maze | Adjacent Cells |
| Image | Surrounding Pixels |
| Cellular Automata | Nearby Cells |
| Height Map | Adjacent Heights |
| Tile Map | Adjacent Tiles |
| Graph | Connected Nodes |
| Chess Board | (what would "neighbor" mean here?) |

Although these systems appear very different, they all rely on the same underlying idea. Can you explain what "neighbor" means in each case — and what a neighborhood representation for it would need to store?

---

# Practical Observation

Beginning programmers often think globally. They ask:

> What does the whole world look like?

Professional programmers often think locally. They ask:

> What information surrounds this location?

That small shift in perspective makes many algorithms dramatically simpler — and it compounds: as programs grow larger, calculations that happen "every time we need a neighbor" may end up running thousands or millions of times. Representing neighborhoods once, rather than recalculating them, lets later algorithms focus on solving their actual problem.

---

# Common Misconceptions

### "Neighbors only exist in games or gridworlds."

No. Neighborhoods appear throughout computing — graphs, networks, images, simulations, robotics, and scientific models all reason about nearby locations.

### "Every neighborhood has exactly four neighbors, and every neighbor matters equally."

Not necessarily. Different algorithms define neighborhoods differently. Some use four cardinal neighbors, some use eight, and others use completely different relationships or weight some neighbors more than others. The definition depends on the problem being solved.

### "The neighborhood is part of the world."

Not exactly. The world stores locations. The neighborhood stores relationships between those locations. These are different representations, even though they describe the same space.

### "Neighborhoods must always be calculated on demand."

Not at all. Many programs build neighborhood representations once and reuse them throughout the computation, rather than recalculating them every time they're needed.

### "Algorithms need the whole world to make good decisions."

Often they do not. Many surprisingly sophisticated algorithms make decisions using only local, neighbor-level information.

---

# Reflection

Think about one computational artifact — an image, a maze, a cave, a tile map, or a chess board.

Choose one location. Who are its neighbors?

Now ask yourself: would solving the problem become easier if every location already knew its neighbors? And if that location could only see its neighbors, what kinds of decisions could it still make?

---

# Looking Ahead

Now that we understand what neighbors are and how to represent them, two questions remain open:

> **Which locations should count as neighbors?** Should we consider only the four cardinal directions, or should diagonal locations also be included?

> **How can we build lookup tables that let the computer answer these questions instantly**, rather than recalculating a neighborhood every time it's needed?
