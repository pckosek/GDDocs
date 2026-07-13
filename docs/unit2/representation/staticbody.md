# Technique 2.2 — Create a StaticBody3D

## Classification

**Type:** Engineering Technique

**Category:** Physical Interaction

**Difficulty:** Beginner

**Estimated Time:** 15–20 minutes

---

# Design Scenario

You are building a **wall**.

The wall should:

- be visible
- block movement
- never move

Consulting the **Physical Representation Guide**, we choose:

```text
StaticBody3D
```

because the wall is an immovable object.

---

# Why This Technique Matters

A wall is one of the simplest physical objects in a game.

It introduces an important idea:

An interactive object is usually built from **multiple cooperating nodes**, each with a different responsibility.

Instead of one node doing everything, Godot encourages us to separate:

- physical behavior
- collision geometry
- visual appearance

Understanding this pattern makes every future body type easier to understand.

---

# Starter Implementation

Create the following hierarchy.

```text
Wall (StaticBody3D)
├── CollisionShape3D
└── MeshInstance3D
```

Assign:

**MeshInstance3D**

- BoxMesh

**CollisionShape3D**

- BoxShape3D

Run the scene.

Visually, the wall appears exactly as it did before.

The important difference is invisible.

The wall now participates in the physical world.

---

# Anatomy

This object is built from three cooperating parts.

## StaticBody3D

Responsible for:

> **How the object behaves in the physics simulation.**

A StaticBody3D never moves because of physics.

It simply occupies space.

---

## CollisionShape3D

Responsible for:

> **Where the object occupies physical space.**

Without a CollisionShape3D, the StaticBody3D has no physical volume.

The object exists...

...but nothing can collide with it.

---

## MeshInstance3D

Responsible for:

> **What the player sees.**

It has no effect on collisions.

Removing the mesh makes the wall invisible.

It does not remove the wall from the physics simulation.

---

# Design Principle

## Physical objects have multiple responsibilities.

Notice that no single node performs every job.

Instead, the wall is assembled from specialized components.

```text
Behavior
↓
StaticBody3D

Physical Shape
↓
CollisionShape3D

Appearance
↓
MeshInstance3D
```

Good game development frequently separates responsibilities in this way.

---

# Experiment

Build three versions of the wall.

---

### Version A

Delete:

```text
MeshInstance3D
```

Run the scene.

Observe.

Can the wall still participate in physics?

---

### Version B

Delete:

```text
CollisionShape3D
```

Run the scene.

The wall is still visible.

Does it still behave like a wall?

---

### Version C

Replace:

```text
StaticBody3D
```

with:

```text
Node3D
```

Run the scene.

Observe.

What changed?

What stayed the same?

---

# Practical Observation

Many important systems in games are invisible.

Examples include:

- collision shapes
- trigger areas
- navigation meshes
- checkpoints
- spawn locations

Players rarely see these systems directly.

Yet they define how the world behaves.

---

# Common Uses

StaticBody3Ds commonly represent:

- walls
- floors
- buildings
- terrain
- cliffs
- immovable obstacles

Whenever an object should remain fixed while interacting physically with other objects, StaticBody3D is usually an appropriate choice.

---

# Common Misconceptions

### "The Mesh collides."

No.

The mesh is visual.

The CollisionShape3D is physical.

---

### "The StaticBody3D makes the object visible."

No.

Visibility comes from the MeshInstance3D.

---

### "Every visible object needs a collider."

Not necessarily.

Background scenery often exists only for visual effect.

Only gameplay objects require physical representation.

---

### "The CollisionShape should perfectly match the mesh."

Usually not.

Simple collision geometry is often:

- faster
- easier to debug
- easier to maintain

Believable interaction is usually more important than geometric perfection.

---

# Reflection

Complete the following sentences.

> A MeshInstance3D is responsible for...

> A CollisionShape3D is responsible for...

> A StaticBody3D is responsible for...

Now answer:

Why do you think Godot separates these responsibilities instead of combining them into one node?

---

# Self Check

Before moving on, ask yourself:

✓ I can build a StaticBody3D.

✓ I understand why it requires a CollisionShape3D.

✓ I understand why it usually also has a MeshInstance3D.

✓ I can explain why a wall is represented by a StaticBody3D.

---

# Looking Ahead

StaticBody3Ds never move.

Many game objects, however, do.

The next technique asks a different question:

> **What if I want the object to move because *my script* tells it to?**

We'll explore **AnimatableBody3D**, which is designed specifically for scripted movement while remaining part of the physical world.