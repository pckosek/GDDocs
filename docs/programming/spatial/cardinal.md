# 5.4.2 Cardinal Neighbors

## Classification

**Type:** Design / Engineering Guide

**Category:** Spatial Relationships

**Difficulty:** Beginner

---

# Design Problem

We now know that every location may have neighbors.

But that raises another question.

> **Which nearby locations count as neighbors?**

Imagine standing in the middle of a maze.

Should you be allowed to move diagonally through walls?

Usually not.

Many grid-based systems define neighbors using only the four primary compass directions.

These are called the **cardinal neighbors**.

---

# Why This Matters

Cardinal neighborhoods appear throughout game development.

Examples include:

- tile-based movement
- maze generation
- flood fill
- pathfinding
- many puzzle games

Restricting movement to the four cardinal directions often produces simpler and more predictable behavior.

Many important algorithms begin with this neighborhood definition.

---

# Mental Model

Imagine standing on one cell.

```text
□ □ □

□ X □

□ □ □
```

Only four neighboring locations are considered connected.

```text
    N

W   X   E

    S
```

The corner cells exist...

...but they are **not** considered neighbors.

The neighborhood describes movement, not simply distance.

---

# Starter Representation

One common way to describe the four directions is:

```python
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
```

Together they form the four cardinal directions.

```python
cardinal = [
    UP,
    DOWN,
    LEFT,
    RIGHT
]
```

Rather than writing separate code for every direction...

...many algorithms simply iterate through this collection.

---

# Dissecting the Representation

Notice that each direction is simply an **offset**.

For example:

```text
Current Position

↓

(5, 8)
```

Moving right means

```text
(+1, 0)
```

producing

```text
(6, 8)
```

Likewise,

moving up means

```text
(0, -1)
```

producing

```text
(5, 7)
```

Each direction represents a small change in position.

---

# Design Principle

## Represent movement as relationships.

Rather than writing separate code for every possible direction...

...represent the directions themselves.

Algorithms become simpler when movement is represented as data rather than duplicated code.

---

# Experiment

Suppose you are standing at:

```text
(8, 3)
```

Where would each cardinal direction take you?

| Direction | New Position |
|-----------|--------------|
| North | |
| South | |
| East | |
| West | |

Now ask yourself:

Would these rules still work anywhere else in the world?

---

# Practical Observation

Many grid-based algorithms never explicitly ask:

> "Can I move north?"

Instead, they simply iterate through the cardinal directions.

For each direction:

- compute the neighboring location
- determine whether it exists
- decide whether it should be visited

The same logic works everywhere in the world.

Representing directions as data makes algorithms much easier to reuse.

---

# Common Misconceptions

### "Cardinal neighbors are the only kind of neighborhood."

No.

They are simply one common definition.

Other algorithms use diagonal neighbors or even much larger neighborhoods.

---

### "Neighbors represent distance."

Not exactly.

Neighbors represent **relationships**.

Two nearby locations may or may not be considered neighbors depending on the rules of the algorithm.

---

### "Movement must always be represented with four directions."

No.

Some games allow:

- diagonal movement
- hexagonal movement
- continuous movement

The neighborhood should match the problem being solved.

---

### "The four directions are hard-coded into the algorithm."

They don't have to be.

Representing directions as data makes algorithms more flexible and easier to extend.

---

# Reflection

Think about the following games.

Would they naturally use cardinal neighbors?

| Game | Cardinal Neighborhood? |
|------|-------------------------|
| Chess | |
| Zelda | |
| Tetris | |
| Pac-Man | |
| Minesweeper | |
| Sokoban | |

Can you explain why?

---

# Looking Ahead

Cardinal neighborhoods define one common relationship between locations.

Sometimes, however, diagonal relationships matter as well.

The next question becomes:

> **How can we represent larger neighborhoods that include more than just the four cardinal directions?**