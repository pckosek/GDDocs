# 5.3.3 Convert Between Coordinates

## Classification

**Type:** Design / Engineering Guide

**Category:** Spatial Representation

**Difficulty:** Beginner

---

# Design Problem

Players think about locations like this.

```text
(x, y)

↓

(3, 2)
```

The computer stores the same world like this.

```text
□□□□□□□□□□□□
```

A player might say:

> "Move to column 3, row 2."

The computer asks:

> "Which element in the list is that?"

Likewise...

Suppose the computer knows:

```text
Index 17
```

How can we determine where that location appears in the world?

To work with gridworlds, we must be able to move between these two representations.

---

# Why This Matters

Almost every grid-based algorithm repeatedly asks questions such as:

- Which cell is north?
- Which pixel is at (10, 25)?
- Which tile occupies this location?
- Which list element stores this position?

Computers constantly translate between:

```text
Coordinates

↓

List Index
```

and

```text
List Index

↓

Coordinates
```

Without these conversions, navigating a gridworld becomes extremely difficult.

---

# Mental Model

Think of a city.

People navigate using addresses.

```text
125 Main Street
```

The postal service might instead use an internal sorting code.

Both describe the same location.

They are simply different representations.

Gridworlds work the same way.

```text
Visual Location

↓

(x, y)

---------------------

Internal Location

↓

Index
```

Neither representation is more correct.

Each is useful for different tasks.

---

# Starter Implementation

Suppose we have a world.

```python
width = 4
height = 3
```

Visually, it looks like this.

```text
  (0,0) (1,0) (2,0) (3,0)

  (0,1) (1,1) (2,1) (3,1)

  (0,2) (1,2) (2,2) (3,2)
```

Internally, the same world becomes

```text
0  1  2  3

4  5  6  7

8  9 10 11
```

The computer continually moves between these two views.

For example:

```text
(2,1)

↓

6
```

Or

```text
9

↓

(1,2)
```

These conversions describe exactly the same location.

---

# Dissecting the Representation

Notice something important.

Coordinates describe:

```text
Where?
```

Indexes describe:

```text
Which element?
```

The information is identical.

Only the representation changes.

Many algorithms switch between these representations hundreds or thousands of times every second.

---

# Design Principle

## Choose the representation that best suits the current task.

Humans naturally think in coordinates.

Computers often work more efficiently with indexes.

Good software moves easily between the two.

Rather than committing to one representation...

...it translates when necessary.

---

# Experiment

Consider the following tasks.

Which representation seems more natural?

| Task | Coordinates or Index? |
|------|------------------------|
| Draw a pixel | |
| Store a grid | |
| Find the player's location | |
| Print a map | |
| Iterate through every cell | |
| Display a tile to the player | |

Can you explain why?

---

# Practical Observation

Many beginner programmers try to work exclusively with coordinates.

Others try to work exclusively with indexes.

Professional programmers often use both.

Coordinates are excellent for reasoning about space.

Indexes are excellent for storing and processing information.

Translation between the two becomes a routine part of computational thinking.

---

# Common Misconceptions

### "Coordinates and indexes represent different locations."

No.

They are simply two ways of describing the same cell.

---

### "The player needs indexes."

Usually not.

Indexes exist primarily for the computer and the programmer.

Players naturally think in terms of positions.

---

### "Coordinates are always easier."

Not necessarily.

Many algorithms become much simpler once the world is stored as one collection.

Indexes often make iteration and storage easier.

---

### "The conversion is the difficult part."

Usually not.

Once the relationship is understood, converting between representations becomes a routine operation that appears throughout grid-based programming.

---

# Reflection

Imagine building a tile-based adventure game.

When would you naturally think in:

- coordinates?

When would you naturally think in:

- indexes?

Now ask yourself:

Why might a professional game engine support both representations simultaneously?

---

# Looking Ahead

Once we can move between coordinates and indexes...

...we can finally begin exploring the structure of the world itself.

The next question becomes:

> **How can we discover which locations surround a particular cell?**