---
tags: [technique, movement]
---

# Pattern 2.12.9 — Follow the Player

## Classification

**Type:** Movement Pattern

**Category:** NPC Movement

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- Patrol Between Points
- Face Movement Direction

---

# Problem

Many NPCs should react to the player's location.

Examples include:

- companions
- followers
- enemies
- pets
- security drones

Unlike a patrol, the destination is no longer fixed.

The destination moves continuously.

The NPC must constantly adjust its path.

---

# Starter Implementation

Create the following scene.

```text
World
├── Player (CharacterBody3D)
└── Companion (CharacterBody3D)
```

Attach the following script to the Companion.

```gdscript
extends CharacterBody3D

@export var player : CharacterBody3D
@export var speed := 3.0

func _physics_process(delta):

	var direction = (
		player.global_position - global_position
	).normalized()

	velocity = direction * speed

	move_and_slide()

	if velocity.length() > 0.01:

		look_at(global_position + velocity)
```

Run the scene.

Move the player.

Observe.

The companion continually follows.

---

# How It Works

```text
Find Player Position

↓

Compute Direction

↓

Move

↓

Repeat
```

Unlike a patrol route, the target is constantly changing.

The NPC continuously recomputes the direction every frame.

---

# Anatomy

## player

Stores a reference to the player.

---

## direction

Points toward the player's current location.

---

## velocity

Moves the NPC toward the player.

---

## look_at()

Faces the current direction of travel.

---

# Design Principle

## Dynamic goals require continuous observation.

Patrols move toward locations.

Followers move toward objects.

As the player moves...

the goal changes.

The NPC adapts automatically.

---

# Experiment

Only change one thing.

---

### Experiment A

Increase:

```gdscript
speed
```

Observe.

---

### Experiment B

Reduce:

```gdscript
speed
```

Observe.

How does the personality of the companion change?

---

### Experiment C

Comment out:

```gdscript
look_at(...)
```

Observe.

How much less believable does the movement become?

---

### Experiment D

Replace:

```gdscript
player
```

with another NPC.

Observe.

Can NPCs follow one another?

---

### Experiment E

Create several followers.

Observe.

Each one independently tracks the player.

---

# Practical Applications

Following appears throughout games.

Examples include:

- companions
- enemies
- pets
- drones
- zombies
- escort missions

Many AI systems begin with this exact movement pattern.

---

# Common Misconceptions

### "The NPC knows where the player will go."

No.

It only knows where the player is **right now**.

It continually updates its goal.

---

### "Following requires complicated AI."

Not necessarily.

Many convincing followers simply move toward the player's current position.

---

### "The player should move the NPC."

The player simply exists.

The NPC decides to follow.

---

# Workbench Habit

Whenever an object should pursue another object:

Think in two steps.

```text
Where is my target?

↓

How do I move toward it?
```

Keeping these questions separate makes more advanced AI much easier to build later.

---

# Challenge

Create a small level containing:

- one player
- three companions

Give each companion a different speed.

Observe.

Notice how different personalities emerge from changing only one variable.

Now ask yourself:

What happens if the companion catches the player?

Should it:

- stop?
- maintain a distance?
- circle the player?

Those questions lead naturally into more sophisticated movement behaviors.