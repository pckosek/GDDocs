---
tags: [technique, enemy]
---

# 8.4.4 Combat

## Classification

**Type:** Engineering Technique

**Category:** Enemy Behaviour

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine the player presses:

```text
Attack
```

Should every nearby enemy take damage?

Probably not.

The player is facing east.

The enemy is standing west.

Direction matters.

Combat begins by answering one simple question.

> **Did the attack actually hit?**

---

# Why This Matters

Combat combines many ideas we've already explored.

Examples include:

- facing direction
- interaction
- Area2D
- state
- feedback

Rather than introducing completely new systems...

combat applies familiar systems to create meaningful encounters.

---

# Mental Model

Think about swinging a flashlight.

The light shines in one direction.

Objects behind you remain unaffected.

Combat works similarly.

```text
Player

↓

Attack Direction

↓

Hit Detection

↓

Response
```

Direction determines what the attack can affect.

---

# Melee Combat

A simple sword attack might follow this sequence.

```text
Attack Button

↓

Create Hitbox

↓

Area2D Detects

↓

Enemy Hurtbox

↓

Damage
```

The Area2D exists only briefly.

It detects which enemies are inside the attack.

The enemy decides how to respond.

---

# Projectile Combat

Projectiles follow a similar pattern.

```text
Create Projectile

↓

Move Forward

↓

Area2D Collision

↓

Damage

↓

Disappear
```

The projectile carries the interaction through the world.

The underlying idea remains exactly the same.

---

# Dissecting the System

Notice the architecture.

```text
Attack

↓

Hitbox

↓

Area2D

↓

Enemy Hurtbox

↓

State Change
```

The attack detects.

The enemy responds.

Each object performs one responsibility.

---

# Design Principle

## Detection and response should remain separate.

The attack determines **whether** something was hit.

The enemy determines **what happens next**.

This separation allows many different enemies to respond differently to the same attack.

Combat becomes flexible rather than hardcoded.

---

# Practical Observation

Many beginning projects place combat logic entirely inside the player.

As projects become larger...

combat naturally separates into systems.

The player creates attacks.

The attack detects collisions.

The enemy interprets the result.

Each part remains small and reusable.

---

# Common Misconceptions

### "The sword damages the enemy."

Not directly.

The sword creates a hitbox.

The enemy decides how it responds when that hitbox reaches its hurtbox.

---

### "Projectiles require a different combat system."

Usually not.

Both melee attacks and projectiles follow the same interaction pattern.

Only the delivery changes.

---

### "Combat is only about reducing health."

Combat also communicates:

- danger
- timing
- positioning
- player skill

Health is only one consequence.

---

### "Area2D belongs only to collectibles."

Area2D appears throughout gameplay.

Combat is another example of interaction through detection rather than physical collision.

---

# Reflection

Imagine creating two weapons.

- a sword
- a bow

How are they different?

How are they similar?

Which parts of the combat system could both weapons share?

What changes?

---

# Looking Back

Earlier we explored:

- interaction
- facing direction
- damage systems

Now we've brought those ideas together.

Combat is not one system.

It is several small systems cooperating.

Direction.

Detection.

Response.

Feedback.

The gameplay emerges from their interaction.

---

# Looking Ahead

Enemies can now:

- patrol
- chase
- investigate
- fight

One final challenge remains.

How should they move through complicated worlds?

How can enemies navigate around:

- walls
- obstacles
- rooms

to reach the player?

We'll begin exploring:

> **Navigation**