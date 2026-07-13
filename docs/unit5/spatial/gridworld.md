# 5.3.1 What is a Gridworld?

## Classification

**Type:** Design / Engineering Guide

**Category:** Spatial Representation

**Difficulty:** Beginner

---

# Design Problem

Many games take place in space.

A player moves.

Enemies patrol.

Walls block movement.

Trees grow.

Rivers flow.

Before a computer can simulate any of these things...

...it must answer a simple question.

> **How should space itself be represented?**

One of the most common answers is a **Gridworld**.

A gridworld divides space into many small cells.

Each cell stores information about one location in the world.

---

# Why This Matters

Gridworlds appear throughout game development.

Examples include:

- tile maps
- dungeon layouts
- strategy games
- puzzle games
- cellular automata
- image processing
- terrain generation

Even digital images can be thought of as gridworlds.

Each pixel occupies one location in a two-dimensional grid.

Once we understand gridworlds...

...many seemingly different computational problems become remarkably similar.

---

# Mental Model

Imagine placing graph paper over a game world.

```text
□□□□□□□□

□□□□□□□□

□□□□□□□□

□□□□□□□□
```

Each square becomes one location.

That location might contain:

- a wall
- a floor
- water
- a tree
- an enemy
- a treasure chest

The world becomes a collection of individual cells.

Together...

those cells describe the larger world.

---

Another way to think about it is:

```text
World

↓

Cells

↓

Information
```

The computer rarely reasons about "the whole world."

Instead, it reasons about one cell at a time.

---

# Design Principle

## Complex spaces are often represented as many simple locations.

Rather than treating the world as one enormous object...

...we divide it into many smaller pieces.

Each piece stores only the information needed for that location.

This makes computation much simpler.

---

# Examples

Gridworlds appear in many different media.

| Medium | Cell Represents |
|----------|-----------------|
| Tile Map | One Tile |
| Maze | One Location |
| Image | One Pixel |
| Cellular Automata | One Cell |
| Height Map | One Height Value |
| Game Board | One Space |

Although these systems look different...

...their underlying representation is remarkably similar.

---

# Practical Observation

Beginning programmers often think about worlds visually.

Professional programmers often think about worlds structurally.

Instead of asking:

> What does the player see?

they begin asking:

> What information does each location need to store?

This shift in perspective makes many procedural algorithms much easier to understand.

---

# Common Misconceptions

### "A gridworld is only for games."

No.

Gridworlds also appear in:

- image processing
- robotics
- geographic information systems
- pathfinding
- scientific simulation
- artificial intelligence

They are one of the most common ways of representing two-dimensional space.

---

### "Gridworlds only store walls."

No.

Each cell may represent almost any kind of information.

Examples include:

- color
- terrain
- temperature
- occupancy
- distance
- movement cost

The representation depends on the problem being solved.

---

### "The player sees the grid."

Not necessarily.

Many games hide the underlying grid completely.

The player experiences a continuous world.

The computer often continues thinking in terms of cells.

---

### "Gridworlds are always square."

Usually.

But the underlying idea extends to hexagonal grids, triangular grids, voxel worlds, and many other spatial representations.

The important idea is dividing space into manageable pieces.

---

# Reflection

Think about one of your favorite games.

If the game were represented as a gridworld...

What might each cell contain?

Would it store:

- terrain?
- walls?
- colors?
- enemies?
- movement cost?
- something else?

Now ask yourself:

What information does the computer need that the player never sees?

---

# Looking Ahead

A gridworld divides space into cells.

The next question becomes:

> **How can we efficiently store thousands—or millions—of those cells inside a computer?**