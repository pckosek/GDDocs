# 5.4.4 Boundary Conditions

## Classification

**Type:** Design / Engineering Guide

**Category:** Spatial Relationships

**Difficulty:** Beginner

---

# Design Problem

Suppose we are standing in the upper-left corner of a grid.

```text
X □ □

□ □ □

□ □ □
```

Now ask:

> What is the neighbor to the left?

Or:

> What is the neighbor above?

Those locations do not exist.

The world has ended.

How should the computer represent something that isn't there?

Questions like these are called **boundary conditions**.

---

# Why This Matters

Every finite world has edges.

Eventually an algorithm reaches:

- the first row
- the last row
- the left edge
- the right edge

At those locations, some neighboring cells simply do not exist.

Every spatial algorithm must decide how those situations should be handled.

Without clear boundary rules...

...many algorithms produce incorrect results or crash entirely.

---

# Mental Model

Think of a map.

```text
□□□□□□□□

□□□□□□□□

□□□□□□□□
```

Most locations have four neighbors.

An edge cell has fewer.

A corner has fewer still.

The neighborhood changes because the world has limits.

Those limits are called **boundaries**.

---

# Example

Consider this grid.

```text
0  1  2

3  4  5

6  7  8
```

Cell **4** has four neighbors.

```text
1

3   4   5

7
```

Cell **0** does not.

```text
X

X   0   1

3
```

Some neighboring locations simply do not exist.

The representation must account for that.

---

# Dissecting the Problem

Notice that the representation has not failed.

The question itself is invalid.

The world contains no location:

```text
(-1, 0)
```

The algorithm must recognize that some requests have no answer.

This is not an error.

It is a property of the representation.

---

# Design Principle

## Every representation has limits.

Good software explicitly describes what happens at those limits.

Ignoring boundary conditions often produces incorrect behavior.

Handling them intentionally makes algorithms predictable and reliable.

---

# Experiment

Suppose each location uses cardinal neighbors.

How many neighbors should each location have?

| Location | Number of Neighbors |
|----------|---------------------|
| Center Cell | |
| Edge Cell | |
| Corner Cell | |

Now ask yourself:

Why are these numbers different?

---

# Practical Observation

Different algorithms choose different boundary rules.

Some possibilities include:

- Ignore neighbors outside the world.
- Represent missing neighbors as `None`.
- Wrap around to the opposite side.
- Treat everything outside the world as walls.
- Treat everything outside the world as empty space.

None of these choices is universally correct.

The best choice depends on the problem being solved.

For example, a maze generator may treat the edge of the world as solid walls, while an image-processing algorithm may simply ignore pixels that lie outside the image.

---

# Common Misconceptions

### "Every location has the same number of neighbors."

No.

Boundary locations naturally have fewer neighbors unless the representation defines another rule.

---

### "Boundary conditions are programming mistakes."

No.

Boundaries are an unavoidable property of finite worlds.

Every spatial algorithm must decide how to handle them.

---

### "There is one correct boundary rule."

No.

Different algorithms make different choices depending on the desired behavior.

---

### "Boundary conditions only matter at the edges."

Although they occur only at the edges...

...every algorithm that explores a world must eventually encounter them.

Planning for boundaries early often prevents many later bugs.

---

# Reflection

Imagine writing one of the following.

- a maze generator
- a cellular automata simulation
- an image filter
- a tile-based game

How should your program behave when it reaches the edge of the world?

Should it:

- stop?
- wrap?
- ignore missing neighbors?
- invent new neighbors?

Explain your reasoning.

---

# Looking Ahead

We now understand:

- locations
- neighborhoods
- lookup tables
- boundaries

Together, these ideas form the foundation of many spatial algorithms.

The next challenge is combining them into reusable neighborhood structures that many different algorithms can share.