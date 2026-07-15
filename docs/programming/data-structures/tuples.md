# 5.1.3 Fixed Collections (Tuples)

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Representation

**Difficulty:** Beginner

---

# Design Problem

Suppose we want to represent the position of a player.

A position consists of two values:

- an x-coordinate
- a y-coordinate

These two values belong together.

```text
(12, 8)
```

Should the program accidentally remove one?

Should another value suddenly appear?

Usually not.

Some collections represent information that should remain together and unchanged.

These are called **Tuples**.

---

# Why This Matters

Many ideas in computing naturally consist of a fixed number of values.

Examples include:

- a position `(x, y)`
- a color `(r, g, b)`
- a size `(width, height)`
- a velocity `(vx, vy)`
- a point in 3D `(x, y, z)`

These values describe one complete idea.

A tuple groups them together while indicating that the overall structure should remain fixed.

---

# Mental Model

Think of a tuple as a label on a package.

```text
Player Position

↓

(12, 8)
```

The position may change later.

```text
(15, 9)
```

But each position is still exactly two values.

We don't suddenly add a third coordinate.

Likewise, a color is always:

```text
(R, G, B)
```

Not

```text
(R, G)
```

Not

```text
(R, G, B, Purple)
```

The structure remains fixed.

---

# Starter Implementation

Creating a tuple is straightforward.

```python
position = (12, 8)
```

Another example.

```python
color = (255, 128, 64)
```

Or

```python
size = (640, 480)
```

Tuples can contain many kinds of values.

```python
player = ("Alex", 12, True)
```

The important characteristic is that the tuple represents one complete concept.

---

# Dissecting the Structure

Like lists, tuples preserve order.

```python
(12, 8)
```

is different from

```python
(8, 12)
```

However, tuples differ in one important way.

The number of values is expected to remain fixed.

A position always contains two coordinates.

An RGB color always contains three color channels.

The representation itself communicates that expectation.

---

# Design Principle

## Use a tuple when several values describe one idea.

If multiple values naturally belong together...

...and the structure itself should remain fixed...

...a tuple is often an appropriate representation.

Tuples represent relationships rather than growing collections.

---

# Experiment

Consider each example.

Would a tuple be an appropriate representation?

| Information | Tuple? |
|-------------|--------|
| Player Position | |
| RGB Color | |
| Image Width and Height | |
| Player Inventory | |
| Velocity | |
| Deck of Cards | |

Can you explain why?

---

# Practical Observation

Notice that many game development libraries naturally use tuples.

Examples include:

```python
(x, y)
```

```python
(width, height)
```

```python
(r, g, b)
```

These values almost always travel together.

Representing them as a tuple makes their relationship immediately clear.

---

# Common Misconceptions

### "Tuples are just slower lists."

No.

Tuples communicate a different design intention.

They represent fixed groups of related values.

---

### "Tuples are only useful because Python has them."

No.

Many programming languages include similar ways of representing small fixed collections.

The exact syntax varies.

The underlying idea is common throughout software engineering.

---

### "Tuples replace lists."

No.

Lists and tuples solve different problems.

Lists represent collections that may grow or shrink.

Tuples represent one concept composed of several related values.

---

### "A tuple means the values can never change."

Not exactly.

The *tuple* itself represents a fixed structure.

A program can always create a new tuple representing a new state.

For example:

```python
position = (12, 8)

↓

position = (15, 9)
```

The position changes.

Each position is still represented by a pair of coordinates.

---

# Reflection

Consider the following ideas.

Would you represent each one using a list or a tuple?

| Representation | List or Tuple? |
|----------------|----------------|
| Player Position | |
| Inventory | |
| RGB Color | |
| Animation Frames | |
| Velocity | |
| Sound Samples | |

Now ask yourself:

Which of these represents **one complete idea**, and which represents **many independent items**?

---

# Looking Ahead

Lists preserve order.

Tuples preserve structure.

Sometimes, however, order doesn't matter at all.

Instead, the important question becomes:

> **How can we ensure that every value appears only once?**