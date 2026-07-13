# 5.4.3 Neighbor Lookup Tables

## Classification

**Type:** Design / Engineering Guide

**Category:** Spatial Relationships

**Difficulty:** Beginner

---

# Design Problem

Suppose we are exploring a maze.

For every location we visit, we repeatedly ask:

- Who are my neighbors?
- Can I move north?
- Can I move east?
- Which neighboring cells exist?

If we calculate these relationships every time...

...we perform the same work over and over again.

Instead, we can compute every neighborhood once.

Then simply remember the answers.

This representation is called a **Neighbor Lookup Table**.

---

# Why This Matters

Many grid-based algorithms repeatedly examine neighboring cells.

Examples include:

- maze generation
- cellular automata
- flood fill
- pathfinding
- image processing
- terrain generation

Rather than calculating neighbors every time...

...we build one representation that stores every neighborhood in advance.

Later algorithms simply retrieve the information.

---

# Mental Model

Imagine every cell carrying a small note.

```text
Cell 5

↓

Neighbors:

1

4

6

9
```

Whenever an algorithm reaches Cell 5...

...it no longer asks:

> "Who are my neighbors?"

It already knows.

The answer has been represented.

---

# Starter Representation

Suppose our world looks like this.

```text
0  1  2  3

4  5  6  7

8  9 10 11
```

A neighbor lookup table might look like:

```python
neighbors = {
    0: [4, 1],
    1: [5, 0, 2],
    2: [6, 1, 3],
    3: [7, 2],
    ...
}
```

Each key represents one location.

Each value stores the neighboring locations.

The table represents relationships throughout the entire world.

---

# Dissecting the Representation

Notice something important.

The lookup table does **not** create new neighbors.

Those relationships already existed.

The lookup table simply stores them.

Instead of repeatedly asking:

```text
Who are my neighbors?
```

the algorithm asks:

```text
What does the lookup table say?
```

The relationship has become data.

---

# Design Principle

## Store relationships once.

Reuse them often.

Many algorithms repeatedly ask the same questions.

Representing those answers directly often produces code that is simpler, faster, and easier to understand.

---

# Experiment

Imagine creating neighbor lookup tables for:

| Representation | Neighbor Relationship |
|----------------|----------------------|
| Maze | |
| Tile Map | |
| Height Map | |
| Image | |
| Cellular Automata | |

Now ask yourself:

Which algorithms would benefit from retrieving neighbors instead of recalculating them?

---

# Practical Observation

Notice how many later algorithms become remarkably similar.

Instead of writing:

```text
Calculate Neighbors

↓

Process Neighbors
```

they become:

```text
Lookup Neighbors

↓

Process Neighbors
```

The representation handles the geometry.

The algorithm focuses on solving its actual problem.

Separating these responsibilities makes programs much easier to maintain.

---

# Common Misconceptions

### "Neighbor lookup tables change the world."

No.

They describe the world.

The relationships already exist.

The lookup table simply remembers them.

---

### "Every algorithm must build its own neighborhood."

Usually not.

Many different algorithms can share the same neighbor lookup table.

The representation becomes reusable.

---

### "Lookup tables are only for speed."

No.

They also simplify algorithms.

Instead of mixing geometry with logic...

...the geometry is represented separately.

---

### "Neighbor lookup tables are unique to gridworlds."

No.

Many computational systems represent relationships explicitly.

Graphs, social networks, road maps, and communication networks all use similar ideas.

---

# Reflection

Suppose your game contains:

- a maze
- a cave
- an image
- a tile map

Would you rather:

- calculate neighbors every time?

or

- build one neighbor lookup table?

Explain your reasoning.

Now ask yourself:

If five different algorithms all need neighbors...

...how many neighbor lookup tables should your program create?

---

# Looking Ahead

Our world now knows:

- where every location is
- how locations are connected

The next challenge is making those relationships even more flexible.

> **How can different definitions of neighborhoods produce different computational behavior?**