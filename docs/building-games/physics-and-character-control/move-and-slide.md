# 6.1.4 `move_and_slide()`

## Classification

**Type:** Engineering Technique

**Category:** 2D Character Movement

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Suppose we write:

```gdscript
velocity.x = 200
```

Should the player move?

Surprisingly...

...nothing happens.

The player now **has** a velocity.

But the engine has not yet used that velocity to move the character.

CharacterBody2D separates these two responsibilities.

First...

you describe how the character wants to move.

Then...

you ask the engine to perform that movement.

This is the purpose of:

```gdscript
move_and_slide()
```

---

# Why This Matters

`move_and_slide()` is one of the most important functions used by `CharacterBody2D`.

It takes the current velocity...

...moves the character...

...checks for collisions...

...and adjusts the final motion accordingly.

Most platformers call this function once during every physics frame.

Without it...

velocity is simply information.

---

# Starter Implementation

A typical movement loop looks like this.

```gdscript
func _physics_process(delta):

    velocity.x = 200

    velocity.y += GRAVITY * delta

    move_and_slide()
```

Notice that:

```gdscript
move_and_slide()
```

is usually the **last** step.

First we decide how the character should move.

Then the engine performs the movement.

---

# Dissecting the Code

Think about the sequence.

```text
Read Input

↓

Update Velocity

↓

Apply Gravity

↓

move_and_slide()

↓

New Position
```

Notice that we never write:

```gdscript
position += ...
```

CharacterBody2D manages the position automatically.

Our job is simply to update the velocity.

---

# Mental Model

Imagine driving a car.

Pressing the accelerator does not instantly teleport the car.

Instead, you request movement.

The engine moves the vehicle.

`move_and_slide()` works similarly.

```text
Velocity

↓

Movement Request

↓

Engine Resolves Movement

↓

Updated Position
```

The engine handles the details.

We describe the intention.

---

# Design Principle

## Separate intention from execution.

Your script decides:

- how fast to move
- which direction to move

The engine decides:

- how collisions are resolved
- where the character finally ends up

Separating these responsibilities keeps movement code much simpler.

---

# Practical Observation

Most CharacterBody2D scripts follow the same overall pattern.

```gdscript
func _physics_process(delta):

    # Read input

    # Update velocity

    # Apply gravity

    # Jump

    move_and_slide()
```

As your character becomes more sophisticated...

the code before:

```gdscript
move_and_slide()
```

grows larger.

The call to:

```gdscript
move_and_slide()
```

usually stays exactly the same.

---

# Common Misconceptions

### "Setting velocity moves the player."

No.

Velocity only describes the desired movement.

`move_and_slide()` performs the movement.

---

### "move_and_slide() calculates my movement."

Not exactly.

Your script calculates the velocity.

`move_and_slide()` applies that velocity while handling collisions.

---

### "I should call move_and_slide() many times."

Usually not.

Most character controllers call it **once** during each physics frame.

---

### "move_and_slide() replaces velocity."

No.

The two work together.

Velocity describes motion.

`move_and_slide()` executes it.

---

# Reflection

Imagine removing:

```gdscript
move_and_slide()
```

from your player.

What would happen?

Now imagine calling it **before** updating the velocity.

Would the character behave differently?

Why?

---

# Looking Ahead

`move_and_slide()` makes movement feel natural because it automatically responds to collisions.

The next challenge is understanding how those collisions affect gameplay.

How does the player know:

- whether they're standing on the ground?
- whether they hit a wall?
- whether they bumped their head?

Those questions become the foundation for jumping, wall collisions, and many other platforming mechanics.