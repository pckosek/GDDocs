# 6.1.3 Gravity

## Classification

**Type:** Engineering Technique

**Category:** 2D Character Movement

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Suppose the player jumps.

Eventually...

...the player should come back down.

Nothing in CharacterBody2D automatically causes this to happen.

Without additional code...

the player would simply continue moving upward forever.

The world needs a force that continually pulls the character downward.

That force is **gravity**.

---

# Why This Matters

Gravity is one of the defining characteristics of a platformer.

It influences:

- jumping
- falling
- landing
- movement timing
- game feel

Rather than moving the player downward directly...

...we gradually increase the player's downward velocity.

The engine then performs the actual movement.

---

# Starter Implementation

A common approach is:

```gdscript
const GRAVITY = 980.0

func _physics_process(delta):

    velocity.y += GRAVITY * delta

    move_and_slide()
```

Every physics frame...

the player's vertical velocity increases.

The character gradually accelerates downward.

---

Jumping works by changing that velocity.

```gdscript
velocity.y = -400
```

The player begins moving upward.

Gravity then slowly reduces that upward movement...

...until the player begins falling again.

---

# Dissecting the Code

Notice the sequence.

```text
Jump

↓

Negative Y Velocity

↓

Gravity

↓

Velocity Increases

↓

Fall
```

Gravity does **not** move the player directly.

Instead...

it continuously changes the player's velocity.

The movement function uses that updated velocity to move the character.

---

# Design Principle

## Gravity changes velocity.

Velocity changes position.

Keeping these responsibilities separate makes movement much easier to understand.

Rather than manually moving the player downward...

...we allow gravity to influence the player's motion naturally.

---

# Practical Observation

Students are often surprised by one detail.

In Godot's 2D coordinate system:

```text
Y Increases

↓

Downward
```

That means:

```gdscript
velocity.y += GRAVITY
```

moves the player downward.

Jumping therefore requires:

```gdscript
velocity.y = -JUMP_SPEED
```

A negative vertical velocity moves the player upward.

Although this may feel unusual at first...

...it quickly becomes natural.

---

# Common Misconceptions

### "Gravity moves the player."

Not directly.

Gravity changes the player's velocity.

The movement function updates the player's position.

---

### "Gravity only matters while falling."

No.

Gravity acts continuously.

Even while the player is moving upward after a jump...

gravity is already slowing that upward movement.

---

### "Jumping means adding upward movement."

Not exactly.

Jumping gives the player an initial upward velocity.

Gravity immediately begins reducing that velocity.

---

### "The gravity value must match the real world."

Not at all.

Game gravity is a design decision.

Many platformers intentionally exaggerate gravity to make movement feel more responsive.

---

# Reflection

Imagine changing the gravity value.

What would happen if gravity became:

| Gravity | Expected Result |
|----------|-----------------|
| Very Small | |
| Very Large | |
| Zero | |
| Negative | |

Now ask yourself:

Which version would feel most enjoyable to play?

Would realism always produce the best gameplay?

---

# Looking Ahead

Our character can now:

- move horizontally
- accelerate downward
- jump

The final piece is allowing the engine to resolve movement against the world.

The next question becomes:

> **How does `move_and_slide()` turn velocity into smooth, collision-aware movement?**