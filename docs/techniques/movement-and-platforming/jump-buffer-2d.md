---
tags: [technique, movement, 2d]
---

# 6.2.4 Jump Buffering

## Classification

**Type:** Game Design Technique

**Category:** Platforming

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine the player is falling toward a platform.

They know exactly when they want to jump.

They press the Jump button...

...just before landing.

Technically...

the player is still in the air.

The jump fails.

A fraction of a second later...

the player lands.

The player immediately presses Jump again.

Although the timing error was tiny...

...the controls feel unresponsive.

Modern platform games often solve this using **Jump Buffering**.

---

# Why This Matters

Jump Buffering allows the game to briefly remember a jump request.

If the player lands shortly after pressing Jump...

...the jump happens automatically.

Instead of requiring frame-perfect timing...

...the game recognizes the player's intention.

The result feels:

- responsive
- forgiving
- natural

The controls appear faster than they actually are.

---

# Mental Model

Think of standing in line.

You raise your hand before your name is called.

When your turn arrives...

your request is already waiting.

Jump Buffering works the same way.

```text
Jump Button

↓

Remember Request

↓

Player Lands

↓

Perform Jump
```

The input is stored temporarily until it becomes valid.

---

# Starter Implementation

One common approach uses another timer.

```gdscript
const JUMP_BUFFER_TIME = 0.1

var jump_buffer = 0.0
```

Whenever the player presses Jump:

```gdscript
if Input.is_action_just_pressed("jump"):
    jump_buffer = JUMP_BUFFER_TIME
```

Each physics frame:

```gdscript
jump_buffer -= delta
```

Now the jump becomes:

```gdscript
if is_on_floor() \
    and jump_buffer > 0:

    velocity.y = JUMP_SPEED
    jump_buffer = 0
```

If the player lands while the buffered input is still active...

the jump happens immediately.

---

# Dissecting the Code

Notice what changed.

Previously we asked:

```text
Is Jump being pressed right now?
```

Now we ask:

```text
Has Jump been pressed recently?
```

The player no longer has to match the exact landing frame.

The input waits briefly.

---

# Design Principle

## Respect the player's intention.

Players think in actions.

Computers think in frames.

Jump Buffering helps bridge that gap.

Instead of demanding perfect timing...

...the game remembers what the player wanted to do.

---

# Practical Observation

Jump Buffering and Coyote Time solve opposite problems.

| Technique | Solves |
|-----------|--------|
| Coyote Time | Jump pressed slightly **too late** |
| Jump Buffering | Jump pressed slightly **too early** |

Together they dramatically improve the feel of platforming without changing the player's abilities.

Many players never notice these systems.

They simply describe the controls as "responsive."

---

# Common Misconceptions

### "Jump Buffering makes jumps automatic."

No.

The player must still press the Jump button.

The game simply remembers that input briefly.

---

### "Jump Buffering makes the game easier."

Not really.

The player still performs exactly the same actions.

The game simply becomes more forgiving of tiny timing errors.

---

### "The jump should stay buffered forever."

No.

The buffer is intentionally very short.

Usually only a fraction of a second.

If the player lands much later...

the request is forgotten.

---

### "Only platformers use input buffering."

Many games buffer inputs.

Examples include:

- fighting games
- rhythm games
- action games
- racing games

Buffering helps games respond to player intention rather than demanding frame-perfect timing.

---

# Reflection

Imagine removing Jump Buffering.

What situations might suddenly feel frustrating?

Now imagine changing the buffer duration.

| Buffer Length | Expected Result |
|---------------|-----------------|
| 0.02 seconds | |
| 0.10 seconds | |
| 0.30 seconds | |
| 1.00 second | |

At what point would buffering begin feeling unnatural?

---

# Looking Back

Earlier we introduced Coyote Time.

That technique remembered the player's **contact with the ground**.

Jump Buffering remembers something different.

It remembers the player's **input**.

Together they create one important design principle.

Games often feel better when they remember what the player recently intended to do.

---

# Looking Ahead

Our platformer now feels much more responsive.

The next challenge is handling another important part of movement.

What happens when the player walks onto:

- hills
- ramps
- uneven ground

We'll explore how platformers handle one of the most common environmental features:

> **Slopes.**