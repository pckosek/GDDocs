# Pattern 2.12.11 — Knockback

## Classification

**Type:** Movement Pattern

**Category:** Character Movement

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- Velocity
- CharacterBody Movement
- Collision Detection

---

# Problem

Many games need to push the player away from danger.

Examples include:

- enemy attacks
- explosions
- spikes
- projectiles
- traps

Unlike ordinary movement, knockback is not controlled by the player.

It is caused by another object interacting with the player.

---

# Starter Implementation

Starting with the CharacterBody movement script, add:

```gdscript
@export var knockback_strength := 10.0
```

Create a function to receive knockback.

```gdscript
func apply_knockback(direction : Vector3):

	velocity += direction.normalized() * knockback_strength
```

Whenever an enemy damages the player:

```gdscript
var direction = player.global_position - enemy.global_position

player.apply_knockback(direction)
```

Run the scene.

Observe.

The player is pushed away from the enemy.

The movement then naturally slows as the player's normal movement takes over again.

---

# How It Works

```text
Enemy Hits Player

↓

Direction Calculated

↓

Velocity Modified

↓

CharacterBody Moves

↓

Player Recovers
```

Notice that knockback does not create a new movement system.

It temporarily modifies the existing one.

---

# Anatomy

## knockback_strength

Determines how strongly the player is pushed.

---

## direction

Points away from the source of the attack.

---

## velocity

Stores both player movement and knockback.

The two naturally combine.

---

# Design Principle

## Gameplay systems often cooperate.

The enemy does not move the player.

The enemy provides information:

> Push the player this direction.

The player then modifies its own movement.

Each object remains responsible for itself.

---

# Experiment

Only change one thing.

---

### Experiment A

Increase:

```gdscript
knockback_strength
```

Observe.

---

### Experiment B

Reduce:

```gdscript
knockback_strength
```

Observe.

---

### Experiment C

Reverse:

```gdscript
direction
```

Observe.

What happens?

---

### Experiment D

Apply knockback several times in quick succession.

Observe.

How does velocity accumulate?

---

### Experiment E

Apply knockback from:

- the front
- the side
- behind

Observe.

The same code automatically produces different movement.

---

# Practical Applications

Knockback appears throughout games.

Examples include:

- enemy attacks
- explosions
- recoil
- bumping hazards
- melee combat
- magical spells

Many combat systems use knockback to communicate impact.

---

# Common Misconceptions

### "The enemy moves the player."

Not directly.

The enemy provides the direction.

The player updates its own velocity.

---

### "Knockback needs a new movement system."

Usually not.

It simply modifies the existing velocity.

---

### "The player should teleport."

Knockback is movement.

Not repositioning.

The player still interacts with the world while being pushed.

---

# Workbench Habit

Whenever another object should influence movement, ask:

> **Can I modify the existing velocity instead of replacing it?**

This often produces smoother, more natural gameplay.

---

# Challenge

Create a simple arena.

Add:

- one player
- one enemy

Every time the player touches the enemy:

- apply knockback
- experiment with different strengths

Then ask another student to play.

Does the impact feel:

- weak?
- heavy?
- satisfying?
- unfair?

Remember:

The mechanics remain identical.

Only the tuning changes.