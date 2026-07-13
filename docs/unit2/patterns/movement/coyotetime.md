# Pattern 2.12.4 — Coyote Time

## Classification

**Type:** Movement Pattern

**Category:** Character Movement

**Difficulty:** Advanced

**Prerequisites:**

- CharacterBody3D
- Jump
- Floor Detection
- Timer Variables

---

# Problem

Imagine the player runs off the edge of a platform.

They press Jump...

...just a fraction of a second too late.

From the player's perspective:

> "I was still on the edge!"

From the computer's perspective:

> "You already left the floor."

The jump is rejected.

This often feels unfair.

Many platforming games solve this using **Coyote Time**.

The player is allowed to jump for a brief moment **after** leaving the ground.

---

# Starter Implementation

Add the following variables.

```gdscript
@export var coyote_time := 0.15

var coyote_timer := 0.0
```

Every frame:

```gdscript
if is_on_floor():

	coyote_timer = coyote_time

else:

	coyote_timer -= delta
```

Now replace the normal jump condition.

```gdscript
if Input.is_action_just_pressed("jump") and coyote_timer > 0:

	velocity.y = jump_velocity

	coyote_timer = 0
```

Run the scene.

Walk off the edge of a platform.

Press Jump just after leaving the edge.

Observe.

The jump still succeeds.

---

# How It Works

```text
Player Leaves Ground

↓

Coyote Timer Begins

↓

Player Presses Jump

↓

Timer Still Active?

↓

Jump Allowed
```

The player is no longer technically grounded.

The game simply delays removing the ability to jump.

---

# Anatomy

## coyote_time

How long jumping remains available after leaving the floor.

---

## coyote_timer

Counts down after the player leaves the ground.

---

## is_on_floor()

Resets the timer every time the player lands.

---

## Jump Condition

Uses the timer instead of requiring immediate floor contact.

---

# Design Principle

## Good games forgive small mistakes.

Players rarely perceive time as precisely as computers.

Coyote Time gives the player the jump they *intended* to perform.

Most players never consciously notice it.

They simply describe the controls as:

- responsive
- fair
- satisfying

---

# Experiment

Only change one thing.

---

### Experiment A

Increase:

```gdscript
coyote_time
```

to:

```gdscript
0.30
```

Observe.

Does the game become too forgiving?

---

### Experiment B

Reduce:

```gdscript
coyote_time
```

to:

```gdscript
0.03
```

Observe.

Can you still feel the effect?

---

### Experiment C

Comment out:

```gdscript
coyote_timer = coyote_time
```

Observe.

Does the mechanic still work?

---

### Experiment D

Print:

```gdscript
coyote_timer
```

Observe.

Watch the timer count down after leaving the platform.

---

### Experiment E

Try intentionally pressing Jump:

- immediately after leaving
- halfway through the timer
- long after falling

Observe when the jump is accepted.

---

# Practical Applications

Coyote Time appears throughout games.

Examples include:

- platformers
- adventure games
- precision movement
- wall jumping
- climbing
- parkour

Many responsive movement systems quietly include this mechanic.

---

# Common Misconceptions

### "The player is still on the floor."

No.

The player has already left the platform.

The game simply extends the jump window.

---

### "This makes the game easier."

Not necessarily.

It makes the controls feel more consistent with player expectations.

---

### "Longer is always better."

Too much Coyote Time feels unrealistic.

Choosing the duration is a design decision.

---

# Workbench Habit

Whenever players say:

> "I swear I pressed Jump!"

consider asking:

> **Should the game forgive slightly late input?**

Many polished platformers answer:

Yes.

---

# Challenge

Experiment with different values for:

```gdscript
coyote_time
```

Try:

- 0.02 seconds
- 0.10 seconds
- 0.20 seconds
- 0.50 seconds

Ask another student to try each version.

Can they tell which feels the most responsive?

Can they identify when the mechanic begins to feel unrealistic?

Notice that, just like Jump Buffer, the goal is not to change the physics.

The goal is to improve the player's experience.