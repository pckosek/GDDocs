---
tags: [technique, movement]
---

# 6.2.2 Variable Jump Height

## Classification

**Type:** Engineering Technique

**Category:** Platforming

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Suppose the player presses Jump.

Should every jump be exactly the same height?

Imagine trying to:

- hop onto a small platform
- clear a large gap
- avoid spikes overhead

If every jump reaches the same height...

...the player loses an important way of controlling movement.

Most platform games allow the player to influence the jump.

A short button press produces a small jump.

Holding the button produces a higher jump.

This technique is called **Variable Jump Height**.

---

# Why This Matters

Variable jump height makes movement feel much more expressive.

Instead of simply deciding:

> Jump

the player decides:

> **How much should I jump?**

This gives the player finer control while making the character feel more responsive.

Many successful platformers use some form of variable jumping.

---

# Starter Implementation

One common approach is to monitor the Jump button while the player is still moving upward.

```gdscript
if Input.is_action_just_released("jump") \
    and velocity.y < 0:

    velocity.y *= 0.5
```

When the player releases the button...

the upward velocity is reduced.

Gravity quickly takes over.

The character begins falling sooner.

Holding the button allows the player to continue rising.

---

# Dissecting the Code

Notice what is changing.

We are **not** changing gravity.

We are **not** changing the movement function.

We are changing only:

```gdscript
velocity.y
```

The sequence becomes:

```text
Jump

↓

Initial Upward Velocity

↓

Release Button?

↓

Reduce Upward Velocity

↓

Gravity

↓

Fall
```

The earlier the button is released...

...the sooner the jump ends.

---

# Mental Model

Think about throwing a paper airplane.

A gentle throw produces a short flight.

A stronger throw carries it farther.

Variable jumping works similarly.

The player influences the **energy** of the jump.

Gravity always behaves the same.

Only the upward motion changes.

---

# Design Principle

## Give the player continuous control.

Interesting movement often comes from allowing the player to influence an action after it has begun.

Rather than treating jumping as:

```text
On

Off
```

Variable jumping creates a spectrum of possible outcomes.

The player feels more connected to the movement.

---

# Practical Observation

Many beginning programmers assume realistic physics creates enjoyable movement.

In practice...

platform games often sacrifice realism in favor of responsiveness.

Variable jump height is one example.

The player gains more control...

...even though the resulting motion is less physically realistic.

Game feel often matters more than physical accuracy.

---

# Common Misconceptions

### "Variable jumping changes gravity."

No.

Gravity usually remains exactly the same.

The jump changes because the upward velocity changes.

---

### "The player jumps again when holding the button."

No.

The jump still begins only once.

Holding the button simply allows the upward movement to continue longer.

---

### "Every platformer uses the same jump."

Not at all.

Different games tune:

- jump speed
- gravity
- release timing
- velocity reduction

to create very different movement styles.

---

### "Realistic jumps feel best."

Not necessarily.

Platform games are usually designed for responsiveness rather than realism.

The best jump is often the one that feels easiest for the player to control.

---

# Reflection

Imagine changing:

```gdscript
velocity.y *= 0.5
```

What might happen if the multiplier became:

| Multiplier | Expected Result |
|------------|-----------------|
| 0.9 | |
| 0.5 | |
| 0.2 | |
| 0.0 | |

Now ask yourself:

Which version would produce the most satisfying platforming?

Why?

---

# Looking Ahead

Variable jumping gives the player more control **during** the jump.

The next technique addresses a different problem.

Sometimes the player presses Jump...

...just a fraction of a second **too late**.

Should the game refuse the jump?

Or should it help the player?

The next lesson explores one of the most famous platforming techniques:

> **Coyote Time.**