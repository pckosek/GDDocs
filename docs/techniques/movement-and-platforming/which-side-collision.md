---
tags: [technique, movement]
---

# Pattern 2.10.3 — Identify Which Side I Collided With

## Classification

**Type:** Gameplay Pattern

**Category:** Collision Detection

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- move_and_slide()
- Identifying Collision Objects

---

# Problem

Knowing **what** you collided with is often not enough.

Sometimes you also need to know:

> **Which side did I hit?**

Examples include:

- Did I land on the floor?
- Did I hit a wall?
- Did I hit the ceiling?
- Which way should I bounce?
- Which direction should an enemy patrol?

The collision **normal** answers these questions.

---

# Starter Implementation

```gdscript
extends CharacterBody3D

func _physics_process(delta):

	# Movement code goes here...

	move_and_slide()

	for i in get_slide_collision_count():

		var collision = get_slide_collision(i)

		print(collision.get_normal())
```

Run the scene.

Walk into:

- a wall
- the floor
- a ramp

Observe the Output panel.

Notice that the reported direction changes depending on the surface that was struck.

---

# Dissecting the Code

Every collision stores a **normal vector**.

```gdscript
collision.get_normal()
```

The normal points **away from the surface** that was hit.

Think of it as the surface saying:

> "This is the direction I'm facing."

---

# Mental Model

Imagine placing an arrow perpendicular to every surface.

For example:

Floor

```text
↑
────────────
```

The arrow points upward.

---

Left Wall

```text
│
│ →
│
```

The arrow points away from the wall.

---

Ceiling

```text
────────────
↓
```

Again, the arrow always points away from the surface.

This arrow is the **collision normal**.

---

# Pattern Variations

Print the normal.

```gdscript
print(collision.get_normal())
```

---

Determine if the player hit the floor.

```gdscript
if collision.get_normal().y > 0.9:
	print("Floor")
```

---

Determine if the player hit the ceiling.

```gdscript
if collision.get_normal().y < -0.9:
	print("Ceiling")
```

---

Determine if the player hit a wall.

```gdscript
if abs(collision.get_normal().x) > 0.9:
	print("Wall")
```

---

These are only examples.

The exact thresholds depend on your game.

---

# Experiment

Only change one thing.

---

### Experiment A

Walk into a vertical wall.

Observe.

What does the normal look like?

---

### Experiment B

Jump onto the floor.

Observe.

How does the normal differ?

---

### Experiment C

Walk onto a ramp.

Observe.

Notice that the normal is no longer perfectly vertical.

Why?

---

### Experiment D

Print both:

```gdscript
collision.get_collider().name

collision.get_normal()
```

Observe.

Can two different walls have different normals?

---

# Practical Applications

Collision normals appear throughout game development.

Examples include:

- bouncing projectiles
- ricochets
- wall sliding
- wall jumping
- enemy patrols
- slope detection
- footstep effects
- impact particles

Many advanced systems begin by asking:

> **Which direction is this surface facing?**

---

# Common Misconceptions

### "The normal points where I was moving."

No.

It points away from the surface.

---

### "Walls always have the same normal."

Different walls face different directions.

The normal depends on the surface that was struck.

---

### "Only physics objects have normals."

Any collision that produces contact also produces a collision normal.

---

### "I need complicated math."

Not yet.

For many gameplay systems, simply observing the normal is enough.

The mathematics can come later.

---

# Workbench Habit

Whenever your gameplay depends on **how** an object collided rather than simply **what** it collided with, inspect the collision normal first.

It often contains exactly the information you need.

---

# Challenge

Create a simple maze.

When the player collides with:

- the floor
- a wall
- a ramp

print a different message.

Do not identify the objects by name.

Instead, determine the type of surface using the collision normal.

Observe how the same pattern works even when new walls are added to the level.