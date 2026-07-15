---
tags: [technique, movement]
---

# 6.2.5 Slopes

## Classification

**Type:** Engineering Technique

**Category:** Platforming

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Until now, our player has walked across flat ground.

But many platform games include:

- hills
- ramps
- uneven terrain
- natural landscapes

Should the player stop every time they reach an angled surface?

Probably not.

Good platform controllers allow the player to move smoothly across slopes while still feeling predictable.

---

# Why This Matters

Slopes change more than the appearance of a level.

They influence:

- movement
- jumping
- falling
- collisions
- game feel

Even small changes in how a character interacts with slopes can dramatically change how a platformer feels to play.

---

# Mental Model

Think about walking up a hill.

You are still moving forward.

The ground beneath you changes gradually.

```text
Flat Ground

──────────────

↓

Slope

────────╱────
```

The player should continue moving naturally.

The shape of the ground changes.

The intention of the movement does not.

---

# Starter Implementation

One advantage of using:

```gdscript
CharacterBody2D
```

together with:

```gdscript
move_and_slide()
```

is that many common slope interactions are handled automatically.

```gdscript
func _physics_process(delta):

    velocity.y += GRAVITY * delta

    move_and_slide()
```

As long as the collision shapes are built correctly...

the player will usually move smoothly across gentle slopes without additional code.

---

# Dissecting the Movement

Notice that the player is still trying to move horizontally.

```text
Input

↓

Velocity

↓

move_and_slide()

↓

Adjusted Movement
```

The engine resolves the collision against the slope.

Instead of walking through the ground...

the player follows its surface.

The movement function adapts the final motion to match the environment.

---

# Design Principle

## Players think about intention, not geometry.

When a player presses Right...

they intend to move right.

They do not intend to calculate surface normals or collision angles.

Good movement systems preserve the player's intention while adapting to the world.

The engine performs the geometric work.

The player experiences smooth movement.

---

# Practical Observation

Although `move_and_slide()` handles many slopes automatically...

slopes often expose subtle gameplay issues.

Examples include:

- characters leaving the ground unexpectedly
- inconsistent jump timing
- sliding down steep hills
- movement that feels "sticky"
- difficulty climbing steep terrain

These behaviors are often influenced by:

- collision shape design
- slope angles
- movement speed
- gravity

Designing enjoyable terrain is just as important as writing correct movement code.

---

# Common Misconceptions

### "Slopes require completely different movement code."

Usually not.

Most platformers continue using exactly the same movement system.

The collision geometry changes.

The movement logic often remains the same.

---

### "Every slope should be climbable."

Not necessarily.

Very steep slopes may intentionally block movement.

The appropriate behavior depends on the game being designed.

---

### "Flat ground and slopes are different mechanics."

Not really.

They are different environments.

A well-designed movement system behaves naturally in both.

---

### "If slopes feel wrong, the movement code must be broken."

Not always.

Sometimes the level geometry or collision shapes are responsible.

Good platforming depends on both programming and level design.

---

# Reflection

Imagine creating the following terrain.

| Terrain | Desired Player Experience |
|----------|---------------------------|
| Gentle Hill | |
| Steep Cliff | |
| Rolling Landscape | |
| Small Ramp | |
| Mountain | |

Should every surface behave the same?

Why?

Now ask yourself:

How much should the terrain influence the player's movement?

---

# Looking Back

Earlier we focused on movement itself.

Now we've discovered that movement also depends on the environment.

The player's controls remain the same.

The world changes beneath them.

Good platformers create movement systems that adapt naturally to different kinds of terrain while preserving the player's intention.

---

# Looking Ahead

Our movement now feels responsive on a variety of terrain.

The next challenge is handling a special kind of platform.

Sometimes the player should be able to:

- stand on a platform
- jump upward through it
- land on it again

How can we create platforms that behave differently depending on the direction of movement?

> **One-Way Platforms**