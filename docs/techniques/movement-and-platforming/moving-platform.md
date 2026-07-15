---
tags: [technique, movement]
---

# Pattern 2.12.13 — Ride a Moving Platform

## Classification

**Type:** Movement Pattern

**Category:** Environmental Movement

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- AnimatableBody3D
- Tweening
- Environmental Velocity (optional)

---

# Problem

Many games contain moving platforms.

Examples include:

- elevators
- moving bridges
- floating platforms
- lifts
- transport systems

The player should:

- stand on the platform
- move with it naturally
- retain full movement control
- step on and off freely

Unlike a conveyor belt, the platform itself moves through the world.

---

# Starter Implementation

Create the following scene.

```text
World
├── Player (CharacterBody3D)
└── Elevator (AnimatableBody3D)
```

Attach the following script to the Elevator.

```gdscript
extends AnimatableBody3D

@export var top := Vector3(0,5,0)
@export var bottom := Vector3.ZERO

func _ready():

	var tween = create_tween()

	tween.set_loops()

	tween.tween_property(
		self,
		"position",
		top,
		2.0
	)

	tween.tween_property(
		self,
		"position",
		bottom,
		2.0
	)
```

Run the scene.

Stand on the elevator.

Observe.

The player rides the platform while maintaining control.

---

# How It Works

```text
Platform Moves

↓

Collision Updates

↓

CharacterBody Responds

↓

Player Rides Platform
```

Notice that the player never becomes a child of the elevator.

Each object remains independent.

The physics engine coordinates the interaction.

---

# Anatomy

## AnimatableBody3D

Moves according to your script.

---

## CharacterBody3D

Maintains player control.

---

## CollisionShape3D

Allows the two systems to interact physically.

---

## Tween

Creates predictable platform motion.

---

# Design Principle

## Independent systems can cooperate.

The platform never controls the player.

The player never controls the platform.

Each system follows its own rules.

The interaction between those systems creates the gameplay.

This is one of the central ideas behind component-based game development.

---

# Experiment

Only change one thing.

---

### Experiment A

Increase the platform speed.

Observe.

Can the player still ride comfortably?

---

### Experiment B

Reduce the speed.

Observe.

How does the platform feel?

---

### Experiment C

Move horizontally instead of vertically.

Observe.

The same pattern creates a moving walkway.

---

### Experiment D

Create two elevators.

Ride between them.

Observe.

Each platform behaves independently.

---

### Experiment E

Replace the Tween with your own movement code.

Observe.

The interaction remains the same.

Only the movement implementation changes.

---

# Practical Applications

This pattern appears throughout games.

Examples include:

- elevators
- floating platforms
- moving bridges
- cable cars
- trains
- boats
- floating islands

Many environmental systems rely on this exact interaction.

---

# Common Misconceptions

### "The player should become a child of the elevator."

Usually not.

The CharacterBody and AnimatableBody remain separate systems.

---

### "The elevator moves the player."

The elevator moves itself.

The CharacterBody naturally responds to the changing environment.

---

### "Moving platforms require complicated code."

Often the movement itself is simple.

The interesting behavior emerges from the interaction between two existing systems.

---

# Workbench Habit

Whenever gameplay involves two moving systems interacting, ask:

> **Can each object remain responsible for its own behavior?**

Keeping systems independent usually makes them much easier to reuse.

---

# Challenge

Build a small level containing:

- two elevators
- one horizontal platform
- one player

Experiment with:

- different speeds
- different paths
- different platform sizes

Can you create a navigable level using nothing more than moving platforms?

Notice that each platform uses exactly the same movement pattern.

Only the destinations change.