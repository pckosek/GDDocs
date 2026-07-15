---
tags: [technique, trigger]
---

# Pattern 2.11.4 — Trigger a Checkpoint

## Classification

**Type:** Gameplay Pattern

**Category:** Area Detection

**Difficulty:** Intermediate

**Prerequisites:**

- Area3D
- body_entered()
- CharacterBody3D

---

# Problem

Many games allow the player to save their progress as they explore.

Examples include:

- checkpoints
- save points
- respawn locations
- level transitions

When the player reaches the checkpoint, the game should remember:

> **"If something goes wrong later, restart me here."**

Unlike a collectible, the checkpoint usually remains in the world after it has been activated.

---

# Starter Implementation

Create the following hierarchy.

```text
Checkpoint (Area3D)
├── CollisionShape3D
└── MeshInstance3D
```

Attach the following script.

```gdscript
extends Area3D

var activated := false

func _on_body_entered(body):

	if body is CharacterBody3D and not activated:

		activated = true

		print("Checkpoint Activated!")
```

Run the scene.

Walk into the checkpoint.

Observe.

The message appears only once.

Walking through the checkpoint again has no effect.

---

# How It Works

```text
Player Enters

↓

Area Detects

↓

Checkpoint Activates

↓

Game Remembers
```

Unlike a coin, the checkpoint is not removed.

Instead, it changes its internal state.

---

# Anatomy

## Area3D

Detects when the player enters.

---

## activated

Remembers whether this checkpoint has already been triggered.

---

## body_entered()

Executes only when the player first enters the checkpoint.

---

# Design Principle

## Some interactions should only happen once.

Not every event is repeatable.

A checkpoint usually remembers that it has already been activated.

This idea appears throughout games.

Examples include:

- opened doors
- completed objectives
- solved puzzles
- unlocked shortcuts

Remembering state is often just as important as detecting events.

---

# Experiment

Only change one thing.

---

### Experiment A

Remove:

```gdscript
not activated
```

Observe.

Can the checkpoint activate repeatedly?

---

### Experiment B

Replace:

```gdscript
print("Checkpoint Activated!")
```

with:

```gdscript
$MeshInstance3D.modulate = Color.GREEN
```

(or change the material)

Observe.

How can visual feedback help the player understand that the checkpoint is active?

---

### Experiment C

Duplicate the checkpoint.

Walk through both.

Observe.

Each checkpoint remembers its own state independently.

---

### Experiment D

Restart the scene.

Observe.

Why did the checkpoint become inactive again?

Where should this information eventually be stored?

---

# Practical Applications

Checkpoint systems commonly remember:

- respawn positions
- level progress
- puzzle completion
- player progress
- save locations

This pattern introduces one of the first examples of persistent gameplay state.

---

# Common Misconceptions

### "The checkpoint should disappear."

Usually not.

Players often expect checkpoints to remain visible.

---

### "The checkpoint should activate every time."

Most checkpoints activate only once.

---

### "The checkpoint respawns the player."

Not yet.

The checkpoint simply records information.

Another system will eventually use that information.

---

# Workbench Habit

Many gameplay systems follow this pattern.

```text
Detect

↓

Remember

↓

React Later
```

Notice that the response does not need to happen immediately.

Sometimes the most important thing an event can do is simply remember that it happened.

---

# Challenge

Build three checkpoints.

Each one should activate only once.

When activated:

- print its name
- change its appearance
- remember that it has already been visited

Then ask yourself:

If the player falls off the level...

Which checkpoint should they return to?

You now have enough information to answer that question.

The actual respawn system comes later.