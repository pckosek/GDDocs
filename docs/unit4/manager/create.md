# 4.2.1 Create a Game Manager

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

In the previous section, we discovered that some information belongs to the entire game.

Examples include:

- current score
- player lives
- game difficulty
- current level
- game paused

Many different objects need access to this information.

If every object keeps its own copy, the game eventually becomes inconsistent.

We need one object whose job is to own the game's shared information.

This object is commonly called the **Game Manager**.

---

# Why This Technique Matters

A Game Manager gives the game a single place to manage information that belongs to everyone.

Instead of asking:

> Which object should remember this?

we begin asking:

> Does this belong to the entire game?

If the answer is yes, the Game Manager is often the right place for it.

The Game Manager becomes the **owner** of the game's global state.

---

# Starter Implementation

Create a new scene.

Choose:

```text
Node
```

Rename the root node:

```text
GameManager
```

Create a new script for the node.

Your scene should look like this.

```text
GameManager
└── GameManager.gd
```

At the moment, the script doesn't need to do anything.

```gdscript
extends Node
```

You have created an object whose responsibility is managing information rather than representing something visible in the game world.

---

# Dissecting the Scene

Notice that the Game Manager is different from most objects we've created so far.

It has:

- no mesh
- no collider
- no sprite
- no camera

Players will never see it.

Instead, it exists to organize information and coordinate systems.

This is an example of a **manager object**.

Manager objects exist to organize behavior rather than represent physical things.

---

# Design Principle

## Objects should have clear responsibilities.

An enemy should manage enemy behavior.

A door should manage door behavior.

The player should manage player behavior.

The Game Manager should manage information that belongs to the entire game.

Giving each object a clear responsibility makes software easier to understand and maintain.

---

# Experiment

Imagine the following pieces of information.

Would you store them in the Game Manager?

### Player Score

```text
✓ Probably
```

---

### Current Difficulty

```text
✓ Probably
```

---

### Enemy Health

```text
✗ Probably not
```

Each enemy should own its own health.

---

### Door Open

```text
✗ Probably not
```

Each door should remember its own state.

---

### Current Level

```text
✓ Probably
```

The entire game shares this information.

---

# Practical Observation

The Game Manager is not a replacement for every script.

It should not become a place where every variable and every function is stored.

Instead, it should manage information that naturally belongs to the game as a whole.

As your projects become larger, keeping responsibilities separated becomes increasingly important.

---

# Common Misconceptions

### "The Game Manager should manage everything."

No.

It manages **global** information.

Individual objects should continue managing their own local state.

---

### "Every project must have a Game Manager."

Not necessarily.

Very small projects may not need one.

As projects grow, however, having a central place for global state often simplifies the design.

---

### "The Game Manager replaces the Player."

No.

The Player still owns player-specific behavior.

The Game Manager owns information that belongs to the game itself.

---

### "The Game Manager must be visible."

No.

Like many software systems, it performs an important role without ever appearing on the screen.

---

# Reflection

Consider the following pieces of information.

Would you store them in the Game Manager, or somewhere else?

| Information | Game Manager? |
|--------------|---------------|
| Current Score | |
| Player Health | |
| Volume Setting | |
| Enemy Health | |
| Current Level | |
| Inventory | |
| Pause State | |

Can you explain **why** each piece of information belongs where it does?

---

# Looking Ahead

Creating a Game Manager is only the first step.

Right now, it behaves like any other object in a scene.

The next question becomes:

> **How can we make the Game Manager available to the entire game?**