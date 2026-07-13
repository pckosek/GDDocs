# Pattern 2.12.3 — Jump Buffer

## Classification

**Type:** Movement Pattern

**Category:** Character Movement

**Difficulty:** Advanced

**Prerequisites:**

- CharacterBody3D
- Jump
- Timer Variables

---

# Problem

Imagine the player presses Jump...

...just a fraction of a second **before** landing.

From the player's perspective:

> "I pressed Jump."

From the computer's perspective:

> "You weren't on the floor yet."

Nothing happens.

This feels frustrating.

Many games solve this problem using **Jump Buffering**.

Instead of requiring perfect timing, the game briefly remembers that the player wanted to jump.

---

# Starter Implementation

Add the following variables.

```gdscript
@export var jump_buffer_time := 0.15

var jump_buffer := 0.0
```

Every frame, decrease the timer.

```gdscript
jump_buffer -= delta
```

Whenever the player presses Jump:

```gdscript
if Input.is_action_just_pressed("jump"):

	jump_buffer = jump_buffer_time
```

Now replace the normal jump condition.

```gdscript
if is_on_floor() and jump_buffer > 0:

	velocity.y = jump_velocity

	jump_buffer = 0
```

Run the scene.

Try pressing Jump just before landing.

Observe.

The jump still occurs.

---

# How It Works

```text
Player Presses Jump

↓

Remember Input

↓

Player Lands

↓

Buffered Jump Executes

↓

Buffer Cleared
```

The game briefly remembers the player's intention.

---

# Anatomy

## jump_buffer_time

How long the game remembers the Jump input.

---

## jump_buffer

Counts down toward zero.

---

## Input

Stores the player's intention.

---

## Landing

Checks whether a buffered jump should occur.

---

# Design Principle

## Good games remember intentions.

Computers measure time perfectly.

People do not.

Jump buffering allows the game to respond to **what the player meant to do**, rather than demanding frame-perfect timing.

Many players never consciously notice jump buffering.

They simply feel that the controls are responsive.

---

# Experiment

Only change one thing.

---

### Experiment A

Increase:

```gdscript
jump_buffer_time
```

to:

```gdscript
0.30
```

Observe.

Does the game begin feeling too forgiving?

---

### Experiment B

Reduce:

```gdscript
jump_buffer_time
```

to:

```gdscript
0.02
```

Observe.

Can you still notice the effect?

---

### Experiment C

Comment out:

```gdscript
jump_buffer = 0
```

Observe.

What unexpected behavior appears?

---

### Experiment D

Print:

```gdscript
jump_buffer
```

Observe.

Watch the timer count down.

---

### Experiment E

Try intentionally pressing Jump:

- much too early
- slightly early
- exactly on landing

Which inputs are accepted?

---

# Practical Applications

Buffered input appears throughout games.

Examples include:

- jumping
- attacking
- dashing
- reloading
- interacting
- combo systems

Many responsive games remember player input for a short period rather than requiring perfect timing.

---

# Common Misconceptions

### "The game is ignoring my mistake."

Not exactly.

The game is remembering your intention.

---

### "Jump buffering changes the jump."

No.

It changes **when the jump is allowed to occur.**

---

### "Longer is always better."

Too much buffering can make controls feel unpredictable.

Finding the right value is a design decision.

---

# Workbench Habit

Whenever players say:

> "I pressed the button!"

consider asking:

> **Should the game briefly remember that input?**

Many polished games do exactly that.

---

# Challenge

Experiment with different buffer times.

Try:

- 0.02 seconds
- 0.10 seconds
- 0.20 seconds
- 0.50 seconds

Ask another student to play your character.

Can they feel the difference?

Which value feels the most responsive?

Which begins to feel unrealistic?

Remember:

This pattern is not about correctness.

It is about creating an experience that feels satisfying to play.