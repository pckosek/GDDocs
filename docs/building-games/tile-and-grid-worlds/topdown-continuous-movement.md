# 8.1.1 Continuous vs Grid Movement

## Classification

**Type:** Design / Engineering Guide

**Category:** Overworld

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine moving through a platformer.

The player:

- runs
- jumps
- falls
- slides

Movement is smooth and continuous.

Now imagine exploring an overworld.

The player moves:

- one tile north
- one tile east
- one tile south

The movement feels completely different.

The player is no longer navigating gravity.

They are navigating space.

Although both games involve movement...

...they create very different player experiences.

---

# Why This Matters

Movement influences almost every other part of a game.

Continuous movement emphasizes:

- timing
- precision
- momentum

Grid movement emphasizes:

- planning
- positioning
- decision making

Changing the movement system changes the way players think about the world.

---

# Mental Model

Imagine drawing with a pencil.

You can move it smoothly across the page.

```text
──────────────
```

Now imagine drawing on graph paper by colouring one square at a time.

```text
□ □ □ □ □
```

Both create pictures.

The movement feels completely different.

Games work the same way.

---

# Continuous Movement

Platformers usually use continuous movement.

```text
Player

↓

Move Anywhere

↓

Physics

↓

Momentum
```

The player continuously adjusts:

- position
- speed
- timing

Movement becomes an ongoing physical skill.

---

# Grid Movement

Many overworld games use discrete movement.

```text
Player

↓

Choose Direction

↓

Move One Cell

↓

Stop
```

Each movement becomes a decision.

The player thinks about:

- position
- path
- interaction

rather than momentum.

---

# Dissecting the Difference

Notice what changes.

Platformer:

```text
Movement

↓

Control
```

Overworld:

```text
Movement

↓

Choice
```

The player performs fewer physical adjustments...

...and more spatial decisions.

The mechanics have changed.

So has the player's mindset.

---

# Design Principle

## Movement shapes thinking.

Players naturally adapt their behaviour to the movement system.

Continuous movement encourages:

- reaction
- precision
- flow

Grid movement encourages:

- planning
- observation
- strategy

Neither is better.

Each creates a different experience.

---

# Practical Observation

Many games combine both approaches.

Examples include:

- free exploration
- tile-based puzzles
- tactical combat
- smooth overworld movement
- grid-based enemy behaviour

The important design question is not:

> Which movement system is correct?

Instead ask:

> Which movement system best supports the experience I want players to have?

---

# Common Misconceptions

### "Grid movement is simpler."

Technically it often is.

Design-wise...

it creates entirely different gameplay.

Planning becomes much more important than physical precision.

---

### "Continuous movement feels more modern."

Many modern games intentionally choose grid movement because it creates thoughtful, strategic play.

The appropriate choice depends on the design goals.

---

### "Changing movement only changes controls."

Movement influences:

- puzzles
- enemies
- exploration
- level design
- pacing

Changing movement changes the entire game.

---

### "Overworld games cannot use physics."

Many do.

The important distinction is not the engine.

It is the player's experience.

Games exist along a spectrum between continuous and discrete movement.

---

# Reflection

Imagine building the same dungeon twice.

Version One uses:

- continuous movement

Version Two uses:

- grid movement

How would the player's experience change?

Would puzzles feel different?

Would combat change?

Would exploration become more thoughtful or more reactive?

Why?

---

# Looking Back

Earlier we built platformers.

Movement emphasized:

- gravity
- jumping
- momentum
- timing

Now we enter a different genre.

Movement becomes less about physics...

...and more about navigating the world.

Changing the movement system changes the player's way of thinking.

The world asks different questions.

The player develops different skills.

---

# Looking Ahead

Now that we've changed how movement works...

...we need to decide how the player should actually move.

Should movement be:

- completely free?
- locked to four directions?
- based on tiles?

We'll begin by exploring the most common movement system used in overworld games:

> **Four-Way Movement**