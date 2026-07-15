# 5.3.5 Lookup Tables

## Classification

**Type:** Design / Engineering Guide

**Category:** Spatial Representation

**Difficulty:** Beginner

---

# Design Problem

Imagine a maze containing ten thousand cells.

Suppose we repeatedly ask questions like:

- What are this cell's neighbors?
- Which coordinates belong to this index?
- Which index belongs to these coordinates?
- Can I move north? Can I move east?

If we calculate those answers every time...

...we perform the same work again and again.

Wouldn't it be simpler to calculate the answers once...

...and remember them?

This idea is called a **lookup table**.

---

# Why This Matters

Many computational problems repeatedly answer the same questions.

Examples include:

- coordinate conversions
- neighboring cells
- movement directions
- image locations
- tile positions
- maze generation
- cellular automata
- flood fill
- pathfinding
- terrain generation

Rather than solving these problems every time they occur...

...we solve them once.

Later, we simply look up the answer.

---

# Mental Model

Think of a multiplication table.

Suppose someone asks:

```text
8 × 7
```

You could calculate it every time.

Or...

...you could simply remember:

```text
8 × 7

↓

56
```

A lookup table works exactly the same way.

Instead of repeatedly solving the problem...

...we remember the answer.

Now imagine every cell in a grid carrying a small note:

```text
Cell 5

↓

Neighbors:

1

4

6

9
```

Whenever an algorithm reaches Cell 5, it no longer asks "who are my neighbors?" — it already knows. The answer has been represented, not recalculated.

---

# Starter Representation

Suppose our grid contains:

```text
0  1  2  3

4  5  6  7

8  9 10 11
```

We might build a lookup table such as:

```python
xy_lookup = {
    (0,0): 0,
    (1,0): 1,
    (2,0): 2,
    ...
}
```

Or perhaps:

```python
index_lookup = {
    0: (0,0),
    1: (1,0),
    2: (2,0),
    ...
}
```

Or, when the question is specifically about neighbors:

```python
neighbors = {
    0: [4, 1],
    1: [5, 0, 2],
    2: [6, 1, 3],
    3: [7, 2],
    ...
}
```

Each key represents one location. Each value stores the neighboring locations. The table represents relationships throughout the entire world.

The important idea is not the dictionary itself. The important idea is that the answers have already been computed.

---

# Dissecting the Representation

Notice the workflow.

Without a lookup table:

```text
Question

↓

Compute

↓

Answer
```

Every time.

With a lookup table:

```text
Question

↓

Lookup

↓

Answer
```

The work has already been done. The computer simply retrieves the result.

This applies just as much to a neighbor relationship as it does to a coordinate conversion. The lookup table does **not** create new neighbors or new coordinates — those relationships already existed. The lookup table simply stores them, so the algorithm asks "what does the lookup table say?" instead of "how do I compute this?" The relationship has become data.

---

# Design Principle

## Compute once. Reuse many times.

Whenever the same computation — or the same relationship, like a neighborhood — will be asked about repeatedly, consider whether precomputing the answers would simplify the program.

Good representations often eliminate unnecessary work, and often make algorithms easier to read: instead of describing *how* to compute something, the code simply retrieves the answer.

---

# Experiment

Suppose your program repeatedly asks:

- Which tile is north?
- Which pixel is at (10, 4)?
- Which cells surround this location?

Would you rather calculate the answer every time, or calculate it once and store it? Why?

Now consider building a neighbor lookup table for each of the following representations:

| Representation | Neighbor Relationship |
|----------------|----------------------|
| Maze | |
| Tile Map | |
| Height Map | |
| Image | |
| Cellular Automata | |

Which of these would benefit most from retrieving neighbors instead of recalculating them?

---

# Practical Observation

Many professional software systems trade memory for speed. Lookup tables are one example — the program stores additional information so that later computations become much faster.

More importantly, this simple idea often makes algorithms easier to read and maintain. Instead of writing:

```text
Calculate Neighbors

↓

Process Neighbors
```

algorithms become:

```text
Lookup Neighbors

↓

Process Neighbors
```

The representation handles the geometry. The algorithm focuses on solving its actual problem. Separating these responsibilities makes programs much easier to maintain as projects grow larger.

---

# Common Misconceptions

### "Lookup tables store new information."

Not really. They usually store information that could have been computed — coordinates, neighbors, relationships that already existed. The lookup table simply remembers the result.

### "Lookup tables are only useful for optimization."

No. They also improve readability, and separate geometry from logic. Many algorithms become much simpler when relationships have already been represented, independent of any speed benefit.

### "Every problem needs a lookup table."

Not necessarily. If a computation happens only once, precomputing it may provide little benefit. Lookup tables become valuable when the same questions are asked repeatedly.

### "Every algorithm must build its own neighborhood."

Usually not. Many different algorithms can share the same neighbor lookup table — the representation becomes reusable across a whole project, not just within one function.

### "Lookup tables are unique to gridworlds."

No. Lookup tables appear throughout computing — color palettes, Unicode tables, trigonometric tables, routing tables, caches, dictionaries, graphs, social networks, road maps. The underlying idea remains the same regardless of domain.

---

# Reflection

Imagine writing one of the following:

- Cellular Automata
- Prim's Algorithm
- Pathfinding
- Image Processing

What questions might your program ask thousands of times? Would those questions benefit from lookup tables? Would your algorithm become simpler if those answers were already available?

Now suppose your game contains a maze, a cave, an image, and a tile map, and five different algorithms all need neighbor information. Would you rather calculate neighbors every time, or build one shared neighbor lookup table? How many neighbor lookup tables should your program actually create?

---

# Looking Back

We began this section by asking:

> **How can computers represent space?**

Along the way we discovered that a useful spatial representation includes more than just cells. It often includes:

- a representation of the world
- translations between coordinates and indexes
- relationships between neighboring locations
- lookup tables that make those relationships easy to access

Together, these representations provide the foundation for many computational algorithms.

---

# Looking Ahead

Our world is now represented. Our relationships are represented. Our common questions have already been answered.

The next challenge is putting all of these ideas together to build computational systems that create new worlds — and asking how different definitions of neighborhoods might produce different computational behavior.
