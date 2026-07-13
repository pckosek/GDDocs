# 6.2.3 Coyote Time

## Classification

**Type:** Game Design Technique

**Category:** Platforming

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine the player runs toward the edge of a platform.

They press the Jump button...

...just a fraction of a second too late.

Technically...

the player is already in the air.

According to the rules...

the jump should fail.

Unfortunately...

this often feels unfair.

The player *intended* to jump from the platform.

Modern platform games frequently solve this problem using a technique called **Coyote Time**.

---

# Why This Matters

Coyote Time makes platformers feel more responsive.

Instead of requiring perfect timing...

...the game briefly remembers that the player was standing on the ground.

For a very short period after leaving the platform...

jumping is still allowed.

The player experiences:

- fewer frustrating missed jumps
- more forgiving controls
- smoother movement

The rules become slightly more generous.

The game feels better.

---

# Mental Model

Think about a cartoon character.

The character runs off the edge of a cliff.

For a brief moment...

they continue moving through the air.

Only then do they begin falling.

```text
Ground

↓

Leave Edge

↓

Short Grace Period

↓

Jump Still Allowed

↓

Fall
```

Platform games borrow this idea.

The player receives a small window of forgiveness after leaving the ground.

---

# Starter Implementation

One common approach uses a timer.

```gdscript
const COYOTE_TIME = 0.1

var coyote_timer = 0.0
```

Whenever the player is standing on the ground:

```gdscript
if is_on_floor():
    coyote_timer = COYOTE_TIME
```

Otherwise:

```gdscript
coyote_timer -= delta
```

Now jumping becomes:

```gdscript
if Input.is_action_just_pressed("jump") \
    and coyote_timer > 0:

    velocity.y = JUMP_SPEED
```

The player may jump during the short grace period.

---

# Dissecting the Code

Notice what changed.

Previously we asked:

```text
Is the player on the floor?
```

Now we ask:

```text
Has the player been on the floor recently?
```

That tiny change dramatically improves the feel of the game.

The player's intention becomes more important than frame-perfect timing.

---

# Design Principle

## Design for people, not perfect timing.

Players are not perfectly precise.

Good game design often includes small amounts of forgiveness that make interactions feel natural rather than frustrating.

The goal is not to make the game easier.

The goal is to make the controls feel fair.

---

# Practical Observation

Most players never notice Coyote Time.

Instead...

they simply describe the controls as:

- responsive
- smooth
- satisfying

Ironically...

the best implementation is often invisible.

Players should feel that the game understood what they meant to do.

---

# Common Misconceptions

### "Coyote Time makes the game easier."

Not necessarily.

The player is not gaining new abilities.

The game is simply allowing intended actions to succeed more consistently.

---

### "Coyote Time is unrealistic."

Absolutely.

It intentionally ignores physical realism.

The goal is improving game feel rather than simulating physics.

---

### "The player can jump forever."

No.

The grace period is extremely short.

Typically only a fraction of a second.

---

### "Only platform games use forgiveness."

Many games include similar ideas.

Examples include:

- input buffering
- aim assist
- generous interaction ranges
- forgiving collision timing

These techniques all help align the game's behavior with the player's intention.

---

# Reflection

Imagine removing Coyote Time from your platformer.

What situations might suddenly feel frustrating?

Now imagine making the grace period:

| Duration | Expected Result |
|----------|-----------------|
| 0.02 seconds | |
| 0.10 seconds | |
| 0.50 seconds | |
| 2.00 seconds | |

At what point does forgiveness begin feeling unrealistic?

---

# Looking Back

Earlier we built a physically correct jump.

Coyote Time deliberately changes that behavior.

Not because the physics were wrong...

...but because the player's experience matters more than perfect simulation.

This is one of the first examples where game feel becomes more important than realism.

---

# Looking Ahead

Coyote Time helps when the player presses Jump **too late**.

Another common problem happens in the opposite direction.

Sometimes the player presses Jump...

...just before landing.

Should that jump also be lost?

The next technique answers:

> **How can we remember the player's input until the game is ready to respond?**