---
tags: [technique, movement]
---

# Pattern 2.12.12 — Conveyor Belt

## Classification

**Type:** Movement Pattern

**Category:** Environmental Movement

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- Area3D
- Velocity
- Signals

---

# Problem

Many games contain moving surfaces.

Examples include:

- conveyor belts
- flowing rivers
- moving walkways
- escalators
- wind tunnels
- ice currents

These objects should influence the player's movement without taking control away from them.

The player can still walk.

The environment simply contributes additional motion.

---

# Starter Implementation

Create the following scene.

```text
Conveyor (Area3D)
├── CollisionShape3D
└── MeshInstance3D
```

Attach the following script.

```gdscript
extends Area3D

@export var conveyor_velocity := Vector3.RIGHT * 3.0

func _on_body_entered(body):

	if body is CharacterBody3D:

		body.environment_velocity = conveyor_velocity

func _on_body_exited(body):

	if body is CharacterBody3D:

		body.environment_velocity = Vector3.ZERO
```

Now add this variable to the player's movement script.

```gdscript
var environment_velocity := Vector3.ZERO
```

Modify the player's movement.

```gdscript
velocity.x =
	player_input.x * walk_speed
	+ environment_velocity.x

velocity.z =
	player_input.z * walk_speed
	+ environment_velocity.z
```

Run the scene.

Walk onto the conveyor.

Observe.

The player is gently carried while still retaining full control.

---

# How It Works

```text
Player Enters Area

↓

Area Applies Environmental Velocity

↓

Player Adds Velocity

↓

Player Moves

↓

Player Leaves Area

↓

Environmental Velocity Removed
```

Notice that the conveyor never moves the player directly.

Instead, it contributes to the player's existing movement.

---

# Anatomy

## Area3D

Determines when the player is on the conveyor.

---

## environment_velocity

Stores the velocity contributed by the environment.

---

## Player Movement

Combines:

- player input
- environmental movement

into one final velocity.

---

# Design Principle

## Movement often comes from multiple sources.

The player's final movement is no longer determined by one system.

Instead:

```text
Player Input

+

Environment

↓

Final Movement
```

Many sophisticated movement systems combine several influences this way.

---

# Experiment

Only change one thing.

---

### Experiment A

Increase:

```gdscript
conveyor_velocity
```

Observe.

---

### Experiment B

Reverse:

```gdscript
Vector3.RIGHT
```

Observe.

---

### Experiment C

Create two conveyors moving in opposite directions.

Walk between them.

Observe.

---

### Experiment D

Walk against the conveyor.

Observe.

Can the player overcome it?

---

### Experiment E

Stand still.

Observe.

The conveyor continues carrying the player.

---

# Practical Applications

This pattern appears throughout games.

Examples include:

- conveyor belts
- flowing rivers
- airport walkways
- moving sidewalks
- wind currents
- magical force fields
- underwater currents

Many environmental systems simply contribute additional movement.

---

# Common Misconceptions

### "The conveyor should move the player."

Not directly.

The conveyor contributes movement.

The player still controls their own CharacterBody.

---

### "The player loses control."

Usually not.

Player movement and conveyor movement combine.

---

### "The conveyor needs physics."

Not necessarily.

Many conveyors are simply Areas modifying player movement.

---

# Workbench Habit

Whenever the environment should influence movement, ask:

> **Can I add another source of velocity?**

Rather than replacing movement, many systems simply contribute to it.

This approach produces flexible movement systems that are easy to expand.

---

# Challenge

Build a small factory.

Create:

- one conveyor
- one player

Experiment with:

- fast conveyors
- slow conveyors
- opposing conveyors

Can you build a puzzle where the player must work with—or against—the environment?

Notice that the player's movement code barely changes.

The complexity emerges from combining two simple systems.