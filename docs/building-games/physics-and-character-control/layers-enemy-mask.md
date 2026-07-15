# Pattern 2.13.2 — Player and Enemy

## Classification

**Type:** Gameplay Pattern

**Category:** Collision Layers & Masks

**Difficulty:** Intermediate

**Prerequisites:**

- Collision Layers
- Collision Masks
- CharacterBody3D

---

# Problem

Many games contain both players and enemies.

Sometimes they should interact.

Examples include:

- colliding
- damaging one another
- blocking movement
- triggering combat

Other objects in the world should usually be ignored.

Collision Layers and Masks allow us to define exactly which objects can interact.

---

# Starter Implementation

Suppose your project uses the following layers.

| Layer | Purpose |
|--------|----------|
| 1 | World |
| 2 | Player |
| 3 | Enemy |
| 4 | Physics Objects |

Configure the Player.

```text
Player

Layer

✓ Player

Mask

✓ World
✓ Enemy
```

Configure the Enemy.

```text
Enemy

Layer

✓ Enemy

Mask

✓ World
✓ Player
```

Run the scene.

Observe.

Players collide with enemies.

Enemies collide with players.

Both continue interacting with the world.

---

# How It Works

```text
Player

↓

Player Layer

↓

Enemy Mask

↓

Interaction

↓

Enemy Layer

↓

Player Mask

↓

Interaction
```

Both objects have chosen to recognize one another.

---

# Anatomy

## Player Layer

Identifies the player.

---

## Enemy Layer

Identifies enemies.

---

## Player Mask

Determines what the player checks for.

---

## Enemy Mask

Determines what the enemy checks for.

---

# Design Principle

## Interaction should be intentional.

Not every object should interact with every other object.

Instead, decide:

Who should care about whom?

This makes gameplay easier to reason about.

---

# Experiment

Only change one thing.

---

### Experiment A

Disable:

```text
Enemy
```

inside the Player Mask.

Observe.

Can the player still collide with enemies?

---

### Experiment B

Disable:

```text
Player
```

inside the Enemy Mask.

Observe.

What changed?

---

### Experiment C

Create several enemies.

Observe.

Do they collide with one another?

Should they?

---

### Experiment D

Add a rolling crate.

Observe.

Should players interact with it?

Should enemies?

Adjust the Masks accordingly.

---

### Experiment E

Turn on:

```text
Visible Collision Shapes
```

Observe.

Nothing about the collision geometry changed.

Only the interaction rules changed.

---

# Practical Applications

Player ↔ Enemy interactions appear throughout games.

Examples include:

- melee combat
- pushing enemies
- stealth
- chasing
- touching hazards
- enemy detection

Many gameplay systems begin by deciding which objects should acknowledge one another.

---

# Common Misconceptions

### "Putting objects on different Layers prevents interaction."

Only if the Masks are configured appropriately.

Layers identify.

Masks decide.

---

### "The Player should detect everything."

Usually not.

Restricting interactions often makes gameplay simpler and easier to debug.

---

### "Every object needs every Layer enabled."

Most objects interact with only a small subset of the world.

---

# Workbench Habit

Whenever two objects behave unexpectedly, ask:

> **Should these objects interact at all?**

Often the answer lies in the Layer and Mask configuration rather than the script itself.

---

# Challenge

Create a small scene containing:

- one player
- three enemies
- one rolling crate

Experiment with different Layer and Mask configurations.

Can you create a world where:

- Players collide with enemies.
- Enemies ignore each other.
- Crates collide with everyone.

Notice that no gameplay code changed.

Only the interaction rules changed.