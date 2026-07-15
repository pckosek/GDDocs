---
tags: [technique, movement]
---

# Pattern 2.10.5 — NPC Stops at a Wall

## Classification

**Type:** Gameplay Pattern

**Category:** Collision Detection

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- move_and_slide()
- Detect Every Collision
- Collision Normals

---

# Problem

Many NPCs move continuously through the world.

Eventually they encounter a wall.

How can they recognize the collision and respond?

This is one of the simplest forms of autonomous behavior.

---

# Starter Implementation

Create the following scene.

```text
World
├── NPC (CharacterBody3D)
└── Wall (StaticBody3D)
```

Attach the following script to the NPC.

```gdscript
extends CharacterBody3D

@export var speed := 3.0

func _physics_process(delta):

	velocity = Vector3.LEFT * speed

	move_and_slide()

	for i in get_slide_collision_count():

		var collision = get_slide_collision(i)

		if collision.get_collider() is StaticBody3D:

			print("Wall Detected!")
```

Run the scene.

The NPC walks toward the wall.

When it reaches the wall, the message appears.

---

# How It Works

Every frame:

```text
Move

↓

Collide

↓

Inspect Collision

↓

Identify Wall

↓

Respond
```

This pattern separates movement from decision-making.

The NPC moves first.

Then evaluates the result.

---

# Anatomy

## CharacterBody3D

Responsible for movement.

---

## move_and_slide()

Responsible for collision resolution.

---

## Collision Detection

Responsible for identifying what was hit.

---

## Decision

Responsible for determining what to do next.

Each responsibility remains independent.

---

# Design Principle

## Observe before reacting.

Many beginning programmers try to predict collisions.

Instead:

Move first.

Observe the result.

Then decide what to do.

This pattern appears repeatedly throughout gameplay programming.

---

# Experiment

Only modify one thing.

---

### Experiment A

Increase:

```gdscript
speed
```

Observe.

Does the NPC still detect the wall correctly?

---

### Experiment B

Replace:

```gdscript
print("Wall Detected!")
```

with:

```gdscript
velocity = Vector3.ZERO
```

Observe.

The NPC now stops moving.

---

### Experiment C

Create multiple walls.

Observe.

Can the NPC detect all of them?

---

### Experiment D

Replace the wall with a RigidBody3D.

Observe.

Does the detection still work?

Why?

---

### Experiment E

Print:

```gdscript
collision.get_collider().name
```

Observe.

Can the NPC identify which wall it reached?

---

# Practical Applications

This pattern appears throughout games.

Examples include:

- guards
- robots
- moving hazards
- enemies
- patrols
- simple wildlife

Many autonomous systems begin with this exact interaction.

---

# Common Misconceptions

### "The wall stops the NPC."

The wall provides the collision.

The NPC decides how to respond.

---

### "Colliding automatically changes behavior."

Collisions only provide information.

Your script determines the gameplay.

---

### "NPC behavior must be complicated."

Many convincing behaviors begin with very simple rules.

---

# Workbench Habit

Separate every autonomous system into two steps.

1. Observe.

2. Decide.

Avoid mixing movement and decision-making into one block of code whenever possible.

---

# Challenge

Create a hallway.

Place an NPC inside.

Modify the script so that when the NPC reaches the wall it:

- stops
- waits briefly (optional)
- prints a message

Do not worry about turning around yet.

The goal is simply to recognize that the NPC can perceive its environment and respond appropriately.