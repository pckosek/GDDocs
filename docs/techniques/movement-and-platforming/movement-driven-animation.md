---
tags: [technique, movement]
---

# Pattern 2.12.8 — Change Animations Based on Movement

## Classification

**Type:** Movement Pattern

**Category:** Character Animation

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- AnimationPlayer
- Jump
- Floor Detection

---

# Problem

A player can:

- stand
- walk
- jump

But visually...

They always look the same.

Most games change animations automatically as the player's movement changes.

The important idea is:

> **Gameplay determines animation.**

Not the other way around.

---

# Starter Implementation

Add an **AnimationPlayer** to the Character.

Create two animations:

- Idle
- Walk

Attach the following script.

```gdscript
@onready var animation := $AnimationPlayer

func update_animation():

	if not is_on_floor():

		animation.play("Jump")

	elif velocity.length() > 0.1:

		animation.play("Walk")

	else:

		animation.play("Idle")
```

Call:

```gdscript
update_animation()
```

at the end of:

```gdscript
_physics_process()
```

Run the scene.

Observe.

Standing still:

Idle.

Walking:

Walk.

Jumping:

Jump.

---

# How It Works

```text
Gameplay

↓

Movement State

↓

Animation Decision

↓

AnimationPlayer
```

Notice that the animations never decide gameplay.

Gameplay decides the animations.

---

# Anatomy

## velocity

Determines whether the player is moving.

---

## is_on_floor()

Determines whether the player is airborne.

---

## AnimationPlayer

Displays the appropriate animation.

---

# Design Principle

## Animation reflects gameplay.

Players care about what the character is doing.

Animations should communicate that behavior.

The animation system should observe gameplay rather than attempting to control it.

---

# Experiment

Only change one thing.

---

### Experiment A

Walk.

Observe.

---

### Experiment B

Stand still.

Observe.

---

### Experiment C

Jump.

Observe.

---

### Experiment D

Comment out:

```gdscript
animation.play("Jump")
```

Observe.

How much information is lost?

---

### Experiment E

Increase movement speed.

Observe.

Does the animation still feel appropriate?

---

# Practical Applications

This pattern appears throughout games.

Examples include:

- Idle
- Walk
- Run
- Jump
- Fall
- Swim
- Climb
- Die
- Attack

Many animation systems simply observe gameplay state.

---

# Common Misconceptions

### "Animations control gameplay."

Usually not.

Gameplay drives animation.

---

### "The animation should decide whether the player is walking."

The movement code already knows that.

Reuse the information you already have.

---

### "Every movement needs a new script."

Often the gameplay code remains identical.

Only the animation selection changes.

---

# Workbench Habit

Whenever you create a new movement mechanic, ask yourself:

> **How should the player know this state changed?**

The answer is often:

Animation.

Good animation communicates gameplay without requiring words.

---

# Challenge

Create four animations:

- Idle
- Walk
- Jump
- Fall

Use only gameplay information to decide which animation should play.

Notice that adding animations does not require changing the movement system itself.

The movement and animation systems remain independent while cooperating to create a much more believable character.