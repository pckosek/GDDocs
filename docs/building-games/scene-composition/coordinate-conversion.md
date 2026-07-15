# Technique 3.6 — Coordinate Space Conversion

## Classification

**Type:** Transform Systems Technique

**Category:** Transform Systems

**Difficulty:** Advanced

**Estimated Time:** 30–45 minutes

---

# Design Problem

Imagine a player clicks on an object.

The mouse reports:

```text
World Position
```

But the object you want to move exists inside:

```text
Player
└── Weapon
```

The weapon doesn't think in world coordinates.

It thinks relative to its parent.

How do we translate between those two perspectives?

This is the problem of **Coordinate Space Conversion**.

---

# Why This Technique Matters

As projects become more sophisticated, different systems begin describing the world differently.

Examples include:

* Mouse positions
* Cameras
* Players
* Enemies
* User Interfaces
* Physics systems

Each may operate in its own coordinate space.

To make those systems work together, we often need to convert information between coordinate systems.

---

# Mental Model

Imagine two people giving directions.

One says:

> "The library is three blocks east."

Another says:

> "The library is next to the coffee shop."

Neither description is wrong.

They simply describe the same location from different frames of reference.

Coordinate conversion performs the same translation inside the engine.

---

# Core Idea

Objects often need to answer questions like:

> Where is this point...

...relative to me?

or

...relative to the world?

Converting coordinate spaces allows those questions to be answered consistently.

Common conversions include:

```text
Local
        ↓
Global

Global
        ↓
Local
```

---

# Experiment

Create the following hierarchy:

```text
World

├── Parent

│   └── Child
```

Position the Parent somewhere away from the world origin.

Now position the Child relative to the Parent.

Observe:

The Child now has:

* a local position
* a global position

Both describe the same object.

---

# Investigation

Move the Parent.

Observe:

The Child's:

* local coordinates
* global coordinates

Which values changed?

Which remained constant?

Why?

---

# Practical Investigation

Suppose a player clicks somewhere in the world.

Ask yourself:

Should an attached weapon think about that position:

* globally?

or

* relative to itself?

Now experiment using:

```gdscript
to_global()

to_local()
```

Observe what changes.

Rather than memorizing these functions, try to understand **why** they exist.

---

# Design Principle

## Every coordinate system tells the truth.

The important question is not:

> Which coordinate system is correct?

The important question is:

> Which coordinate system is most useful for solving this problem?

Good developers learn to switch between perspectives as needed.

---

# Practical Applications

Coordinate conversion appears throughout game development.

Examples include:

### Mouse Picking

Convert screen positions into world positions.

---

### Cameras

Convert between camera space and world space.

---

### User Interfaces

Convert mouse positions into interface coordinates.

---

### Weapons

Aim relative to the player.

---

### Procedural Generation

Place objects relative to other objects.

---

Many advanced systems depend on coordinate conversion.

---

# Common Misconceptions

### "There is only one position."

Objects often have several useful descriptions.

---

### "Global coordinates are always easier."

Not when building hierarchical systems.

---

### "Coordinate conversion changes the object."

No.

It changes how we describe the object.

---

### "These functions are magic."

They simply translate between coordinate systems.

Nothing more.

---

# Challenge

Create two Parent objects.

Place a Child beneath each.

Move the Parents to different locations.

Now predict:

If both Children have:

```text
Local Position

(2,0,0)
```

Will they occupy the same place in the world?

Test your prediction.

Then explain why.

---

# Reflection

Complete the sentence:

> Coordinate conversion allows different systems to...

Now answer:

When would it be easier to think locally?

When would it be easier to think globally?

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain why local and global coordinates describe the same object differently?

✓ Can I predict what happens when a parent moves?

✓ Can I explain why coordinate conversion is necessary?

✓ Can I decide which coordinate system best fits a particular problem?

---

# Looking Ahead

Coordinate space conversion is one of the final pieces needed before building more advanced systems.

Once you understand:

* local coordinates
* global coordinates
* transform inheritance
* transform basis
* coordinate conversion

you have developed one of the most important mental models in Godot.

Many future topics—including procedural animation, AI movement, camera systems, and procedural generation—are simply increasingly sophisticated applications of these same ideas.
