# Pattern 2.12.1 — Jump

## Classification

**Type:** Movement Pattern

**Category:** Character Movement

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- Velocity
- move_and_slide()
- Floor Detection
- Input Actions

---

# Problem

Most games allow the player to jump.

A jump should:

- begin only while standing on the ground
- launch the player upward
- allow gravity to bring the player back down
- prevent repeated jumping while airborne

This is one of the most common movement patterns in game development.

---

# Starter Implementation

Starting with the basic CharacterBody3D movement script, add:

```gdscript
@export var jump_velocity := 7.0
@export var gravity := 18.0
```

Inside:

```gdscript
func _physics_process(delta):
```

apply gravity.

```gdscript
if not is_on_floor():

	velocity.y -= gravity * delta
```

Then add the jump.

```gdscript
if Input.is_action_just_pressed("jump") and is_on_floor():

	velocity.y = jump_velocity
```

Finally:

```gdscript
move_and_slide()
```

Run the scene.

Press Jump.

Observe.

The player launches upward, then naturally falls back to the ground.

---

# How It Works

A jump is actually very simple.

```text
Player Presses Jump

↓

Initial Upward Velocity

↓

Gravity Slows Upward Motion

↓

Velocity Becomes Zero

↓

Gravity Pulls Downward

↓

Player Lands
```

Notice that the jump only supplies the **initial push**.

Gravity performs the rest of the motion.

---

# Anatomy

## jump_velocity

Determines how strongly the player leaves the ground.

---

## gravity

Continuously accelerates the player downward.

---

## is_on_floor()

Prevents jumping while airborne.

---

## move_and_slide()

Applies the velocity while resolving collisions.

---

# Design Principle

## A jump is an initial condition.

Many beginning programmers think a jump means:

> Move upward.

Actually, a jump means:

> Begin with an upward velocity.

Everything that follows is simply physics.

This distinction becomes important later when adding:

- double jumps
- wall jumps
- moving platforms
- knockback

---

# Experiment

Only change one thing.

---

### Experiment A

Increase:

```gdscript
jump_velocity
```

Observe.

---

### Experiment B

Decrease:

```gdscript
jump_velocity
```

Observe.

---

### Experiment C

Increase:

```gdscript
gravity
```

Observe.

How does the jump feel?

---

### Experiment D

Reduce:

```gdscript
gravity
```

Observe.

How does the jump change?

---

### Experiment E

Comment out:

```gdscript
is_on_floor()
```

Observe.

What new behavior appears?

Why?

---

# Practical Applications

This pattern forms the basis of many movement systems.

Examples include:

- platformers
- first-person games
- third-person games
- puzzle games
- adventure games

Many advanced movement systems simply build upon this one.

---

# Common Misconceptions

### "Jumping means moving upward."

Not exactly.

Jumping means assigning an initial upward velocity.

---

### "Gravity makes the player jump."

Gravity actually ends the jump.

The jump begins because of the initial velocity.

---

### "The player should always be allowed to jump."

Most games require the player to be grounded first.

The floor check prevents repeated jumping while airborne.

---

### "Gravity should only apply while falling."

Gravity applies continuously.

Even while the player is moving upward.

That continuous downward acceleration creates the familiar arc of a jump.

---

# Workbench Habit

Think of every jump as two separate systems.

```text
Jump

↓

Initial Velocity

↓

Gravity

↓

Landing
```

Keeping these ideas separate makes advanced movement mechanics much easier to build later.

---

# Challenge

Experiment with different combinations of:

- jump_velocity
- gravity

Try to create jumps that feel:

- heavy
- floaty
- realistic
- arcade-like

Notice that changing only two numbers dramatically changes the personality of the character.

The code never changes.

Only the tuning does.