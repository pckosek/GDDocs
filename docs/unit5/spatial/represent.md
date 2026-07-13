# 5.3.2 Represent a Grid

## Classification

**Type:** Design / Engineering Guide

**Category:** Spatial Representation

**Difficulty:** Beginner

---

# Design Problem

Imagine creating a game world that is:

```text
8 tiles wide

×

8 tiles tall
```

Visually, it looks like this.

```text
□□□□□□□□

□□□□□□□□

□□□□□□□□

□□□□□□□□

□□□□□□□□

□□□□□□□□

□□□□□□□□

□□□□□□□□
```

The player naturally thinks about rows and columns.

The computer, however, has another question.

> **How should all of these cells be stored in memory?**

One surprisingly elegant answer is:

Store them as one long collection.

---

# Why This Matters

Although we often draw worlds as two-dimensional grids...

...computers naturally organize information as sequences.

Instead of storing:

```text
□□□□□□□□

□□□□□□□□

□□□□□□□□

□□□□□□□□
```

we can store:

```text
□□□□□□□□□□□□□□□□
```

The world still contains the same information.

Only the representation has changed.

This representation turns out to be remarkably useful for many computational algorithms.

---

# Mental Model

Think about reading a book.

Although words appear on many lines...

...the author wrote one continuous sequence of characters.

Gridworlds work similarly.

We can imagine reading the world:

Left to right.

Then top to bottom.

```text
0  1  2  3

4  5  6  7

8  9 10 11
```

becomes

```text
0 1 2 3 4 5 6 7 8 9 10 11
```

The information is identical.

The representation is different.

---

# Starter Representation

Suppose we wish to create a blank world.

```python
width = 4
height = 3

grid = [
    0
    for _ in range(width * height)
]
```

The representation becomes:

```text
[0, 0, 0, 0,
 0, 0, 0, 0,
 0, 0, 0, 0]
```

Although this is one list...

...we still think of it as a two-dimensional world.

---

# Dissecting the Representation

Notice that the representation stores only the values.

The concepts of:

- rows
- columns
- neighbors

are not stored directly.

Instead...

...they are computed from the representation.

This separation is important.

The representation stores information.

Algorithms interpret that information.

---

# Design Principle

## Representations should make later operations easier.

Many algorithms repeatedly perform operations such as:

- visiting neighbors
- updating cells
- filtering locations
- generating new worlds

A simple representation often makes those later operations much easier to implement.

Choosing the representation is part of designing the algorithm.

---

# Experiment

Imagine each of the following worlds.

Would representing them as one collection still make sense?

| World | One Collection? |
|--------|-----------------|
| Chess Board | |
| Image | |
| Tile Map | |
| Height Map | |
| Maze | |
| Cellular Automata | |

Can you explain why?

---

# Practical Observation

Many beginning programmers expect the computer to store the world exactly as they draw it.

Professional programmers often separate:

```text
Representation

↓

Visualization
```

The internal representation is chosen because it makes computation easier.

The visualization is chosen because it makes understanding easier.

The two do not have to be identical.

---

# Common Misconceptions

### "A one-dimensional representation means the world is one-dimensional."

No.

The representation is one-dimensional.

The world remains two-dimensional.

---

### "The computer loses information."

No.

Every cell still exists.

The representation simply stores the cells in a different order.

---

### "The player experiences the representation."

No.

The representation exists for the programmer and the computer.

The player experiences the rendered world.

---

### "There is only one correct representation."

Not at all.

Many different representations are possible.

This particular representation is useful because it makes many later algorithms simple and efficient.

---

# Reflection

Suppose you are creating:

- a maze
- a tile map
- an image
- a cave

Would you rather store:

- one variable for every cell?

or

- one collection containing every cell?

Why?

Now ask yourself:

What operations might become easier if every location lived inside one collection?

---

# Looking Ahead

Representing a world as one collection is only the beginning.

The next challenge is navigating that world.

The computer must constantly answer questions like:

> **Which location does this cell represent?**

and

> **How do I move between positions in the world?**