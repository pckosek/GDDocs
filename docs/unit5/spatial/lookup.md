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

Or even:

```python
neighbors = {
    5: [1,4,6,9]
}
```

The important idea is not the dictionary itself.

The important idea is that the answers have already been computed.

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

---

With a lookup table:

```text
Question

↓

Lookup

↓

Answer
```

The work has already been done.

The computer simply retrieves the result.

---

# Design Principle

## Compute once.

Reuse many times.

Whenever the same computation will be performed repeatedly...

...consider whether precomputing the answers would simplify the program.

Good representations often eliminate unnecessary work.

---

# Experiment

Suppose your program repeatedly asks:

- Which tile is north?
- Which pixel is at (10, 4)?
- Which cells surround this location?

Would you rather:

- calculate the answer every time?

or

- calculate it once and store it?

Why?

---

# Practical Observation

Many professional software systems trade memory for speed.

Lookup tables are one example.

The program stores additional information...

...so that later computations become much faster.

As projects become larger, this simple idea often produces significant performance improvements.

More importantly...

...it often makes algorithms easier to read.

Instead of describing *how* to compute something...

...the code simply retrieves the answer.

---

# Common Misconceptions

### "Lookup tables store new information."

Not really.

They usually store information that could have been computed.

The lookup table simply remembers the result.

---

### "Lookup tables are only useful for optimization."

No.

They also improve readability.

Many algorithms become much simpler when relationships have already been represented.

---

### "Every problem needs a lookup table."

Not necessarily.

If a computation happens only once...

...precomputing it may provide little benefit.

Lookup tables become valuable when the same questions are asked repeatedly.

---

### "Lookup tables are unique to gridworlds."

No.

Lookup tables appear throughout computing.

Examples include:

- color palettes
- Unicode tables
- trigonometric tables
- routing tables
- caches
- dictionaries

The underlying idea remains the same.

---

# Reflection

Imagine writing one of the following.

- Cellular Automata
- Prim's Algorithm
- Pathfinding
- Image Processing

What questions might your program ask thousands of times?

Would those questions benefit from lookup tables?

Now ask yourself:

Would your algorithm become simpler if those answers were already available?

---

# Looking Back

We began this section by asking:

> **How can computers represent space?**

Along the way we discovered that a useful spatial representation includes more than just cells.

It often includes:

- a representation of the world
- translations between coordinates and indexes
- relationships between neighboring locations
- lookup tables that make those relationships easy to access

Together, these representations provide the foundation for many computational algorithms.

---

# Looking Ahead

Our world is now represented.

Our relationships are represented.

Our common questions have already been answered.

The next challenge is putting all of these ideas together to build computational systems that create new worlds.