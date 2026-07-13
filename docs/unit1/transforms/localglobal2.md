# Technique 3.2 — Local and Global Coordinates

## Classification

**Type:** Transform Systems Technique

**Category:** Transform Systems

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

One of the first confusing moments in Godot occurs when you look at an object's position in the Inspector and think:

> "That can't be right."

The object appears to be somewhere in the world...

...yet the Inspector reports something completely different.

This happens because every object can be described using **two different coordinate systems**:

* **Local Coordinates**
* **Global Coordinates**

Both describe the same object.

Both are correct.

They simply answer different questions.

---

# Why This Technique Matters

Most beginner projects contain only a few independent objects.

As projects become more sophisticated, objects begin belonging to other objects.

Examples include:

* A camera attached to a player
* A moon orbiting a planet
* A wheel attached to a vehicle
* A weapon attached to a character
* A light attached to a moving platform

Once objects begin living inside other objects, understanding coordinate systems becomes essential.

---

# Mental Model

Imagine giving directions to a friend.

You could say:

> "Meet me at **123 Main Street**."

That is a **global** location.

Or you could say:

> "I'm sitting in the **third chair** inside the classroom."

That is a **local** location.

Both descriptions locate you.

One is measured relative to the world.

The other is measured relative to something nearby.

Godot works exactly the same way.

---

# Core Idea

## Local Coordinates

Local coordinates answer:

> **"Where am I relative to my parent?"**

---

## Global Coordinates

Global coordinates answer:

> **"Where am I in the world?"**

These are different questions.

Neither is more correct.

---

# Experiment

Create the following hierarchy:

```text id="aq81fv"
World
└── Parent
    └── Child
```

Set:

```text id="l9jlwm"
Parent Position = (5, 0, 0)

Child Position = (2, 0, 0)
```

Do **not** run the scene yet.

Before testing, answer:

> Where do you think the Child exists in the world?

Write down your prediction.

---

Now run the scene.

Observe:

* the Parent's local position
* the Child's local position
* the Child's global position

Move the Parent.

Observe what changes.

Move only the Child.

Observe again.

---

# Investigation

Try the following.

### Experiment A

Move only the Parent.

Questions:

* Does the Child move?
* Does the Child's local position change?
* Does the Child's global position change?

---

### Experiment B

Move only the Child.

Questions:

* What changes?
* What remains the same?

---

### Experiment C

Move both.

How do the two coordinate systems respond?

---

# Design Principle

## Every parent creates a new coordinate system.

This is one of the fundamental ideas behind scene hierarchies.

When you create:

```text id="jlwm7i"
Vehicle
└── Wheel
```

the wheel no longer measures itself relative to the world.

It measures itself relative to the vehicle.

This makes complex systems much easier to build.

---

# Practical Applications

Understanding local coordinates simplifies many common systems.

Examples:

### Cameras

A camera remains behind the player because it stores its position relative to the player.

---

### Solar Systems

A moon orbits a planet because its position is measured relative to the planet.

---

### Vehicles

Wheels stay attached because they inherit the vehicle's coordinate system.

---

### User Interfaces

Buttons remain inside windows because they use local positioning.

---

# Common Misconceptions

### "Local coordinates are wrong."

No.

They simply describe position relative to a different origin.

---

### "Global coordinates are always better."

Not at all.

Many gameplay systems are much easier to build using local coordinates.

---

### "Moving the parent changes the child's Position."

It changes the child's **global** position.

The child's **local** position may not change at all.

This surprises almost every new Godot developer the first time they see it.

---

# Challenge

Without testing first, predict the answers.

Suppose:

```text id="jlwm93"
Parent Position = (10, 0, 0)

Child Position = (3, 0, 0)
```

Questions:

* What is the Child's local position?
* What is the Child's global position?

Now verify your prediction inside Godot.

If your prediction was incorrect, explain **why**.

---

# Reflection

Complete the following sentences.

> Local coordinates describe an object relative to _____________________.

> Global coordinates describe an object relative to _____________________.

Now answer:

> Which coordinate system would you use for a camera attached to a player?

Why?

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain the difference between local and global coordinates?

✓ Can I predict what happens when a parent moves?

✓ Can I explain why the Inspector sometimes shows values that seem "wrong"?

✓ Can I decide when local coordinates are more useful than global coordinates?

---

# Looking Ahead

Local and global coordinates are the beginning of a much larger idea.

Soon you will discover that every object also has its own:

* forward direction
* right direction
* up direction

Those directions are stored inside the object's **Transform Basis**.

Understanding local coordinates first makes those later concepts much easier to understand.
