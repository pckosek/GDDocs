---
tags: [technique, movement]
---

# Pattern 2.12.7 — Face Movement Direction

## Classification

**Type:** Movement Pattern

**Category:** NPC Movement

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- Movement
- Patrol Between Points

---

# Problem

An NPC moves correctly.

Unfortunately...

It continues looking in the same direction while moving.

The result feels unnatural.

Most moving objects should face the direction they are traveling.

Examples include:

- guards
- enemies
- animals
- vehicles
- projectiles

Movement and facing direction are usually separate systems.

---

# Starter Implementation

Starting with the previous patrol pattern, add the following code.

```gdscript
if velocity.length() > 0.01:

	look_at(global_position + velocity)
```

Run the scene.

Observe.

The NPC now rotates as it moves.

It always faces the direction of travel.

---

# How It Works

```text
Movement

↓

Velocity

↓

Direction

↓

Rotation
```

Notice that rotation is **derived** from movement.

The NPC doesn't decide which way to face.

Its velocity already contains that information.

---

# Anatomy

## velocity

Represents the current movement direction.

---

## look_at()

Rotates the object to face a target position.

---

## global_position + velocity

Creates a point directly in front of the NPC.

The object then rotates to face that point.

---

# Design Principle

## Behavior often generates orientation.

Many beginning developers manually rotate every object.

Instead, ask:

> Does another system already know which direction this object should face?

Often the answer is yes.

Movement naturally provides orientation.

---

# Experiment

Only change one thing.

---

### Experiment A

Comment out:

```gdscript
look_at(...)
```

Observe.

How different does the patrol feel?

---

### Experiment B

Increase the NPC's speed.

Observe.

Does the facing still work?

---

### Experiment C

Create a curved patrol route.

Observe.

How naturally does the NPC turn?

---

### Experiment D

Replace:

```gdscript
velocity
```

with:

```gdscript
-target.global_position
```

Observe.

What happens?

Why?

---

### Experiment E

Create several guards.

Observe.

Every NPC automatically faces its own movement direction without additional code.

---

# Practical Applications

This pattern appears throughout games.

Examples include:

- enemy AI
- wildlife
- racing games
- flying drones
- missiles
- companions

Many believable movement systems automatically align orientation with motion.

---

# Common Misconceptions

### "Movement automatically rotates the object."

Usually not.

Translation and rotation are separate properties.

---

### "The NPC should rotate every frame."

Only when it is actually moving.

Otherwise the object may jitter unnecessarily.

---

### "Facing direction should be hard-coded."

The current movement already contains this information.

Whenever possible, derive orientation from behavior.

---

# Workbench Habit

Whenever an object moves through the world, ask:

> **Should it also face that direction?**

If the answer is yes, the movement system often already provides everything you need.

Avoid storing the same information twice.

---

# Challenge

Create a simple museum with several patrolling guards.

Experiment with:

- slow guards
- fast guards
- long patrol routes
- short patrol routes

Observe.

Compare the scene:

- with automatic facing
- without automatic facing

Ask another student:

Which version feels more believable?

Notice that adding only one line of code dramatically improves the illusion of intelligence.