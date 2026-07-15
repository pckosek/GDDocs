---
tags: [technique, movement]
---

# Pattern 2.12.2 — Double Jump

## Classification

**Type:** Movement Pattern

**Category:** Character Movement

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- Jump
- Floor Detection

---

# Problem

Many platforming games allow the player to jump again while airborne.

Examples include:

- double jumps
- air jumps
- magical jumps
- jet-assisted jumps

Unlike a normal jump, the player is allowed one additional jump before returning to the ground.

---

# Starter Implementation

Starting with the Jump pattern, add:

```gdscript
@export var max_jumps := 2

var jumps_remaining := max_jumps
```

Reset the jump count whenever the player lands.

```gdscript
if is_on_floor():

	jumps_remaining = max_jumps
```

Replace the jump code with:

```gdscript
if Input.is_action_just_pressed("jump") and jumps_remaining > 0:

	velocity.y = jump_velocity

	jumps_remaining -= 1
```

Run the scene.

Observe.

The player can now jump:

- once from the ground
- once again while airborne

Landing restores both jumps.

---

# How It Works

```text
Player Lands

↓

Reset Jump Counter

↓

Jump

↓

Remaining = 1

↓

Jump Again

↓

Remaining = 0

↓

Must Land Again
```

Rather than asking:

> Am I on the floor?

we now ask:

> How many jumps remain?

---

# Anatomy

## max_jumps

The maximum number of jumps before landing.

---

## jumps_remaining

Tracks how many jumps are currently available.

---

## is_on_floor()

Resets the jump count.

---

## jump_velocity

Launches the player upward.

---

# Design Principle

## State changes the rules.

The movement code barely changed.

What changed was the **state**.

The player now carries information:

```text
Remaining Jumps
```

Gameplay often emerges from small pieces of remembered state.

---

# Experiment

Only change one thing.

---

### Experiment A

Set:

```gdscript
max_jumps = 3
```

Observe.

---

### Experiment B

Set:

```gdscript
max_jumps = 1
```

Observe.

You've recreated the original jump.

---

### Experiment C

Print:

```gdscript
jumps_remaining
```

after every jump.

Observe.

How does the value change?

---

### Experiment D

Comment out:

```gdscript
jumps_remaining = max_jumps
```

Observe.

Why can the player eventually stop jumping altogether?

---

### Experiment E

Try different:

```gdscript
jump_velocity
```

for:

- first jump
- second jump

How does that affect the feel?

---

# Practical Applications

This same pattern appears throughout games.

Examples include:

- double jumps
- triple jumps
- dash charges
- ammunition
- stamina
- spell charges

Many mechanics are simply counters that reset under specific conditions.

---

# Common Misconceptions

### "Double jumping means writing another jump."

No.

It usually means allowing the existing jump to occur more than once.

---

### "The player needs two movement systems."

The movement remains identical.

Only the rule changes.

---

### "Landing creates the jump."

Landing simply restores the available jumps.

---

# Workbench Habit

Whenever gameplay asks:

> **How many times may the player do this?**

consider using:

```gdscript
remaining

↓

use

↓

reset
```

Many gameplay mechanics follow this exact pattern.

---

# Challenge

Experiment with:

- one jump
- two jumps
- three jumps

Then try giving the second jump a different height.

Ask yourself:

Which version feels:

- realistic?
- fun?
- empowering?
- difficult?

Notice that the underlying movement system never changed.

Only the gameplay rule changed.