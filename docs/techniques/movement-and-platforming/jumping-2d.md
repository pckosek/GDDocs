---
tags: [technique, movement, 2d]
---

# 6.2.1 Jumping

## Classification

**Type:** Engineering Technique

**Category:** Platforming

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Walking is straightforward.

The player moves left or right across the ground.

Jumping is different.

The player should:

- leave the ground
- rise upward
- slow down
- begin falling
- land naturally

How can one simple action produce all of that behavior?

The answer is surprisingly simple.

Jumping gives the player an **initial upward velocity**.

Gravity does the rest.

---

# Why This Matters

Jumping is one of the defining mechanics of a platform game.

Almost everything else depends on it.

Examples include:

- collecting coins
- reaching platforms
- avoiding hazards
- defeating enemies
- exploring the level

A responsive jump often determines whether a platformer feels enjoyable to play.

---

# Starter Implementation

Suppose the player presses the Jump button.

```gdscript
const JUMP_SPEED = -400.0

func _physics_process(delta):

    if Input.is_action_just_pressed("jump") \
        and is_on_floor():

        velocity.y = JUMP_SPEED

    velocity.y += GRAVITY * delta

    move_and_slide()
```

When the player presses Jump...

the vertical velocity immediately becomes negative.

Gravity then gradually slows the upward movement until the player begins falling.

---

# Dissecting the Code

Notice the sequence.

```text
Jump Button

↓

Set Upward Velocity

↓

Gravity

↓

Slow Upward Movement

↓

Begin Falling

↓

Land
```

The jump itself lasts only one moment.

Everything afterwards happens because gravity continually changes the velocity.

---

# Mental Model

Think about throwing a ball.

You give it one initial push upward.

After that...

gravity takes over.

Platformer jumps work the same way.

```text
Initial Velocity

↓

Gravity

↓

Trajectory
```

The player is not continually moving upward.

The jump begins with one change in velocity.

---

# Design Principle

## Jumping changes velocity once.

Gravity changes velocity continuously.

Keeping these responsibilities separate produces movement that is simple, predictable, and easy to modify.

---

# Practical Observation

Notice the condition:

```gdscript
is_on_floor()
```

Without it...

the player could repeatedly jump while already in the air.

Most platform games only allow jumping when the character is standing on a surface.

Later in this unit we'll deliberately relax that rule using techniques such as:

- coyote time
- jump buffering

Those systems improve the feel of the game without changing the basic movement model.

---

# Common Misconceptions

### "Jumping moves the player upward."

Not directly.

Jumping changes the player's velocity.

Movement happens later when:

```gdscript
move_and_slide()
```

is called.

---

### "Gravity stops during the jump."

No.

Gravity begins affecting the player immediately.

Even while the player is moving upward...

gravity is already reducing that upward velocity.

---

### "The player should always be able to jump."

Usually not.

Most platformers require the player to be standing on the ground before another jump is allowed.

---

### "A bigger jump means moving farther upward."

Usually it means giving the player a larger initial upward velocity.

Gravity then determines the rest of the motion.

---

# Reflection

Imagine changing:

```gdscript
JUMP_SPEED
```

What would happen if the value became:

| Jump Speed | Expected Result |
|------------|-----------------|
| -200 | |
| -400 | |
| -800 | |
| 0 | |

Now ask yourself:

Would changing gravity produce a different feeling than changing jump speed?

Why?

---

# Looking Ahead

A basic jump works.

Experienced platform players, however, expect something more forgiving.

Sometimes they press Jump a fraction of a second too late.

Should the game ignore the input...

...or should it still allow the jump?

The next technique explores one of the most important ideas in modern platformer design:

> **Coyote Time.**