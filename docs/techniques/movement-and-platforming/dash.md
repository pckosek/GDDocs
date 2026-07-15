---
tags: [technique, movement]
---

# Pattern 2.12.10 — Dash

## Classification

**Type:** Movement Pattern

**Category:** Character Movement

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- Velocity
- Input Actions
- Timer Variables

---

# Problem

Many games allow the player to perform a quick burst of movement.

Examples include:

- combat dashes
- evasive rolls
- air dashes
- quick sprints
- teleport-like movement

Unlike walking, a dash is:

- fast
- temporary
- intentional

The player briefly moves much faster before returning to normal movement.

---

# Starter Implementation

Starting with the CharacterBody movement script, add:

```gdscript
@export var walk_speed := 5.0
@export var dash_speed := 18.0
@export var dash_duration := 0.20

var dash_timer := 0.0
```

Inside:

```gdscript
_physics_process(delta)
```

start the dash.

```gdscript
if Input.is_action_just_pressed("dash"):

	dash_timer = dash_duration
```

Then update the timer.

```gdscript
dash_timer -= delta
```

Determine the current speed.

```gdscript
var current_speed = walk_speed

if dash_timer > 0:

	current_speed = dash_speed
```

Finally:

```gdscript
velocity.x = direction.x * current_speed
velocity.z = direction.z * current_speed

move_and_slide()
```

Run the scene.

Press Dash while moving.

Observe.

The player briefly accelerates before returning to normal speed.

---

# How It Works

```text
Dash Button

↓

Dash Timer Starts

↓

Temporary Speed Increase

↓

Timer Ends

↓

Normal Movement Returns
```

Notice that the movement system never changes.

Only the movement speed changes.

---

# Anatomy

## dash_speed

The temporary movement speed.

---

## dash_duration

How long the dash lasts.

---

## dash_timer

Tracks how much dash time remains.

---

## current_speed

Determines whether the player walks or dashes.

---

# Design Principle

## Gameplay often changes temporarily.

Many mechanics are simply temporary modifications of existing systems.

Examples include:

- sprinting
- slowing
- freezing
- speed boosts
- power-ups

Rather than writing a completely new movement system, modify the one you already have.

---

# Experiment

Only change one thing.

---

### Experiment A

Increase:

```gdscript
dash_speed
```

Observe.

---

### Experiment B

Increase:

```gdscript
dash_duration
```

Observe.

How does the character feel?

---

### Experiment C

Reduce:

```gdscript
dash_duration
```

to:

```gdscript
0.05
```

Observe.

Does it still feel like a dash?

---

### Experiment D

Comment out:

```gdscript
dash_timer -= delta
```

Observe.

What happens?

---

### Experiment E

Try dashing:

- while standing still
- while walking
- while turning

Observe.

Which situations feel best?

---

# Practical Applications

Dash mechanics appear throughout games.

Examples include:

- action games
- platformers
- fighting games
- shooters
- roguelikes
- adventure games

Many movement systems include short bursts of speed to improve responsiveness and player expression.

---

# Common Misconceptions

### "A dash needs a different movement system."

Usually not.

Most dashes simply modify the player's existing movement.

---

### "The dash lasts until the button is released."

Not necessarily.

Many dashes are controlled entirely by a timer.

---

### "A dash is just moving faster."

Not quite.

A dash is usually:

- temporary
- intentional
- highly responsive

Those characteristics distinguish it from ordinary movement.

---

# Workbench Habit

Whenever gameplay asks:

> **How can this ability be temporary?**

consider using:

```text
State

↓

Timer

↓

Reset
```

Many movement mechanics follow exactly this pattern.

---

# Challenge

Experiment with different combinations of:

- walk_speed
- dash_speed
- dash_duration

Try to create a dash that feels:

- heavy
- snappy
- powerful
- evasive

Ask another student to try your implementation.

Can they describe the personality of your movement?

Notice that changing only three numbers dramatically changes the feel of the character without changing the underlying movement system.