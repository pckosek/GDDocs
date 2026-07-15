---
tags: [technique, trigger]
---

# Pattern 2.11.1 — Enter an Area

## Classification

**Type:** Gameplay Pattern

**Category:** Area Detection

**Difficulty:** Beginner

**Prerequisites:**

- Area3D
- Signals

---

# Problem

Many gameplay systems need to know:

> **When did something enter this Area?**

Examples include:

- checkpoints
- finish lines
- pickup items
- trigger zones
- enemy detection
- damage zones

Rather than continuously checking for nearby objects, Area3D automatically emits a signal whenever something enters its collision volume.

---

# Starter Implementation

Create an **Area3D** with a **CollisionShape3D**.

Connect:

```text
body_entered(body)
```

Attach the following script.

```gdscript
extends Area3D

func _on_body_entered(body):

	print(body)
```

Run the scene.

Walk the player into the Area.

Observe.

The object that entered the Area is printed.

---

# How It Works

Area3D continuously monitors its collision volume.

Whenever another physics body enters:

```text
Body Enters

↓

Area Detects

↓

body_entered Signal

↓

Your Code Executes
```

Notice that your script never asks:

> "Is something inside me?"

The Area tells you automatically.

---

# Anatomy

## Area3D

Observes overlap.

---

## body_entered(body)

Executes once whenever a body enters the Area.

---

## body

Represents the object that entered.

Examples include:

- CharacterBody3D
- RigidBody3D
- AnimatableBody3D

---

# Experiment

Only change one thing.

---

### Experiment A

Print:

```gdscript
body.name
```

instead.

Observe.

---

### Experiment B

Resize the Area.

Observe.

How does changing the detection volume affect gameplay?

---

### Experiment C

Walk into the Area multiple times.

Observe.

How many signals are emitted?

---

### Experiment D

Roll a RigidBody into the Area.

Observe.

Does the same signal fire?

---

### Experiment E

Create two Areas.

Observe.

Does each Area detect independently?

---

# Common Uses

This pattern appears throughout games.

Examples include:

- checkpoints
- finish lines
- pickups
- hazards
- music regions
- dialogue triggers
- save points

Many gameplay systems begin with:

> Something entered an Area.

---

# Common Misconceptions

### "The Area blocks movement."

No.

Areas detect.

They usually do not obstruct.

---

### "The signal runs continuously."

No.

It runs once when an object enters.

---

### "Only players can trigger Areas."

Any compatible physics body can enter an Area.

---

# Workbench Habit

Whenever your gameplay begins with:

> **"When something enters..."**

start with:

```gdscript
body_entered(body)
```

Many gameplay systems begin with this exact signal.

---

# Challenge

Build a simple room containing:

- one player
- one rolling ball
- one checkpoint

Print the name of every object that enters the Area.

Observe.

Notice that the Area doesn't care **what** entered.

It simply reports the event.

Your code decides what to do next.