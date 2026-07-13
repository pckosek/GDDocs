# 5.4.1 What is a Neighbor?

## Classification

**Type:** Design / Engineering Guide

**Category:** Spatial Relationships

**Difficulty:** Beginner

---

# Design Problem

Knowing where something is...

...is only part of understanding a world.

Imagine standing in a maze.

Knowing your current location is useful.

But eventually you will ask questions like:

- Where can I move?
- Which walls surround me?
- Which enemies are nearby?
- Which trees are adjacent?
- Which pixels influence this pixel?

These questions are not about locations.

They are about **relationships between locations**.

Those nearby locations are called **neighbors**.

---

# Why This Matters

Many computational systems reason locally.

Instead of examining an entire world...

...they examine one location and the locations immediately around it.

Examples include:

- maze generation
- pathfinding
- cellular automata
- image filters
- terrain smoothing
- flood fill

Nearly every spatial algorithm begins with the same question.

> **Who are my neighbors?**

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

The neighborhood describes the local environment.

It tells the computer:

> **These are the locations immediately related to this one.**

---

Another way to think about it is:

```text
Location

↓

Neighborhood

↓

Local Decisions
```

The computer rarely needs to examine the entire world.

Most algorithms make decisions using only nearby information.

---

# Design Principle

## Complex behavior often emerges from local relationships.

Many computational systems never examine the entire world.

Instead...

...each location repeatedly interacts only with its neighbors.

Remarkably complex structures often emerge from these simple local interactions.

---

# Examples

Neighbors appear throughout computational media.

| Medium | Neighbor Relationship |
|----------|----------------------|
| Maze | Adjacent Cells |
| Image | Surrounding Pixels |
| Cellular Automata | Nearby Cells |
| Height Map | Adjacent Heights |
| Tile Map | Adjacent Tiles |
| Graph | Connected Nodes |

Although these systems appear very different...

...they all rely on the same underlying idea.

---

# Practical Observation

Beginning programmers often think globally.

They ask:

> What does the whole world look like?

Professional programmers often think locally.

They ask:

> What information surrounds this location?

That small shift in perspective makes many algorithms dramatically simpler.

---

# Common Misconceptions

### "Neighbors only exist in gridworlds."

No.

Neighborhoods appear throughout computing.

Graphs, networks, images, simulations, robotics, and many other systems all rely on local relationships.

---

### "Every neighbor is equally important."

Not necessarily.

Different algorithms use different neighborhood definitions.

Some consider only adjacent cells.

Others include diagonals or even much larger regions.

The definition depends on the problem being solved.

---

### "The neighborhood is part of the world."

Not exactly.

The world stores locations.

The neighborhood describes relationships between those locations.

These are different representations.

---

### "Algorithms need the whole world."

Often they do not.

Many surprisingly sophisticated algorithms make decisions using only local information.

---

# Reflection

Think about one of the following.

- a maze
- an image
- a chess board
- a cave

Choose one location.

Who are its neighbors?

Now ask yourself:

If that location could only see its neighbors...

...what kinds of decisions could it still make?

---

# Looking Ahead

Now that we understand what neighbors are...

...the next question becomes:

> **Which locations should count as neighbors?**

Should we consider only the four cardinal directions?

Or should diagonal locations also be included?