---
tags: [technique, movement]
---

# Technique 2.9 — Crossing a Finish Line

## Classification

**Type:** Engineering Technique

**Category:** Physical Interaction

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Scenario

You are building a race.

The player should:

- freely walk across the finish line
- not collide with the finish line
- trigger an event when crossing it
- notify the game that the level has been completed

This is one of the simplest examples of an **Area3D** interacting with a **CharacterBody3D**.

---

# Why This Technique Matters

Not every interaction should stop movement.

Sometimes the world simply needs to observe.

Examples include:

- finish lines
- checkpoints
- save points
- trigger zones
- dialogue regions

Area3D allows the game to react to the player's presence without interrupting movement.

---

# Starter Implementation

Create the following scene.

```text
World
├── Player (CharacterBody3D)
└── Finish Line (Area3D)
    ├── CollisionShape3D
    └── MeshInstance3D
```

Connect the:

```text
body_entered()
```

signal.

Attach the following script.

```gdscript
extends Area3D

func _on_body_entered(body):

	if body is CharacterBody3D:

		print("Level Complete!")
```

Run the scene.

Walk through the finish line.

Observe.

The player continues moving.

The signal fires.

---

# Anatomy of the Interaction

Two independent systems cooperate.

```text
CharacterBody3D

↓

Area3D

↓

Signal

↓

Game Event
```

Neither object directly controls the other.

The Area simply detects the interaction.

---

# Design Principle

## Detection is often more important than collision.

Walls stop the player.

Finish lines observe the player.

These are fundamentally different gameplay mechanics.

Understanding that distinction is one of the most important reasons Area3D exists.

---

# Experiment

Only modify one thing at a time.

---

### Experiment A

Resize the Area.

Observe.

How does changing the detection volume affect gameplay?

---

### Experiment B

Move the finish line.

Observe.

Does the player still trigger it?

---

### Experiment C

Remove the MeshInstance3D.

Run the scene.

Can the player still complete the level?

---

### Experiment D

Replace:

```gdscript
print("Level Complete!")
```

with:

```gdscript
print(body.name)
```

Observe.

What object actually entered the Area?

---

### Experiment E

Create two finish lines.

Observe.

Does each Area work independently?

---

# Practical Observation

Many gameplay systems share this exact structure.

Examples include:

- checkpoints
- save stations
- dialogue triggers
- music regions
- tutorial prompts
- level exits

The gameplay changes.

The interaction pattern remains the same.

---

# Common Uses

CharacterBody3D interacting with Area3D commonly represents:

- finish lines
- checkpoints
- save points
- trigger zones
- cutscene triggers
- interaction regions

Whenever the player should trigger an event without being physically blocked, this interaction is often the correct solution.

---

# Common Misconceptions

### "The finish line should stop the player."

Usually not.

The purpose of the Area is to detect, not obstruct.

---

### "The Area knows what to do."

The Area only detects the interaction.

Your script decides what happens next.

---

### "The player activates the finish line."

More accurately:

The Area detects the player.

Then emits a signal.

Then your code responds.

---

### "The finish line must be visible."

Not necessarily.

Many trigger volumes are completely invisible during gameplay.

---

# Reflection

Complete the sentence.

> Crossing a finish line is different from walking into a wall because...

Now answer:

Why is Area3D a better choice than StaticBody3D for this problem?

Can you think of three other gameplay events that could use the same interaction?

---

# Self Check

Before moving on, ask yourself:

✓ I understand the difference between collision and detection.

✓ I can detect when the player enters an Area3D.

✓ I understand why Area3D usually does not block movement.

✓ I can explain why the finish line is an event rather than a physical obstacle.

---

# Looking Ahead

The player isn't the only object that can trigger an Area.

What if the object entering the goal isn't a player...

...but a ball?

In the next technique, we'll build a simple scoring system by allowing a **RigidBody3D** to interact with an **Area3D**.

The interaction pattern stays the same.

Only the participating objects change.