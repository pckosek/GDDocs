# Technique 3.1 — Understand Local and Global Coordinates

## Classification

**Type:** Transform Systems Technique

**Category:** Transform Systems

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

As scenes become more complex, objects begin existing inside other objects.

A camera belongs to a player.

A moon belongs to a planet.

A wheel belongs to a vehicle.

A sword belongs to a character.

At some point, a simple question becomes surprisingly difficult:

> **"Where is this object?"**

The answer depends on **which coordinate system you are using.**

Understanding the difference between **local** and **global** coordinates is one of the most important conceptual steps in learning Godot.

---

# Why This Technique Matters

Many confusing bugs can be traced back to one misunderstanding:

> Students think there is only one coordinate system.

There isn't.

Every parent object creates its own coordinate system.

This means an object can simultaneously have:

* one local position
* one global position

Both are correct.

They are simply describing the object from different points of view.

---

# Mental Model

Imagine a passenger sitting in a moving car.

Relative to the car:

```text
Seat Position = (0, 0, 0)
```

The passenger isn't moving.

Relative to the Earth:

The passenger is traveling down the road.

Both descriptions are true.

Neither is incorrect.

Godot works the same way.

---

# Experiment

Create the following hierarchy:

```text
World
└── Parent Cube
    └── Child Cube
```

Position the Parent Cube somewhere away from the world origin.

Leave the Child Cube at:

```text
Position = (0,0,0)
```

Observe:

Where is the child?

Where is the parent?

Now move only the parent.

Observe again.

Finally, move only the child.

What changed?

What stayed the same?

---

# Investigation

Open the Inspector.

Observe the Child Cube.

Notice that its Position still reads:

```text
(0,0,0)
```

even though it has clearly moved through the world.

Ask yourself:

> Why?

Discuss your explanation before moving on.

---

# Design Principle

## Every object lives inside someone else's coordinate system.

A child's transform is measured relative to its parent.

This makes hierarchies powerful.

Instead of describing:

> "The moon is 384,000 km from world origin."

we describe:

> "The moon is 384,000 km from Earth."

That relationship remains meaningful even when the Earth moves.

---

# Common Applications

Understanding local coordinates makes many systems easier to build.

Examples include:

* Solar Systems
* Vehicles
* Cameras
* Character Equipment
* Doors
* Turrets
* Orbiting Objects

Nearly every hierarchical system relies on local coordinates.

---

# Common Misconceptions

### "Local coordinates are fake."

They are simply measured from a different origin.

---

### "Global coordinates are always better."

Neither system is better.

Each answers a different question.

---

### "Moving the parent changes the child's local coordinates."

Not necessarily.

Moving the parent changes the child's **global** position while its **local** position may remain unchanged.

---

# Challenge

Without running the scene, predict the answer.

Suppose:

```text
Parent Position = (10,0,0)

Child Position = (2,0,0)
```

Questions:

Where is the child:

* locally?

* globally?

Now test your prediction inside Godot.

---

# Reflection

Complete the following sentence:

> Local coordinates describe an object relative to...

> Global coordinates describe an object relative to...

Now consider:

When would you intentionally choose one over the other?

---

# Looking Ahead

Local and global coordinates prepare you for one of the most important ideas in Godot:

Objects don't simply have positions.

They have **transformations**.

In the next techniques you'll explore how those transformations define:

* forward
* right
* up
* orientation
* movement

Understanding coordinate systems is the first step toward understanding how objects think about the space around them.
