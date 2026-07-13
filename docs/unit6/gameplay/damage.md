# 6.5.4 Damage Systems

## Classification

**Type:** Engineering Technique

**Category:** Gameplay Objects

**Difficulty:** Intermediate

**Estimated Time:** 30–40 minutes

---

# Design Problem

Suppose the player swings a sword.

An enemy is standing nearby.

Several questions immediately appear.

- Did the attack actually hit?
- How much damage should it cause?
- Should the enemy be pushed backward?
- Should the enemy die?
- Should the player receive feedback?

Damage is rarely one event.

Instead...

...it is a collection of interacting gameplay systems.

Organizing those systems carefully makes combat much easier to build and extend.

---

# Why This Matters

Most action games separate combat into several responsibilities.

Examples include:

- attack detection
- damage calculation
- health management
- knockback
- visual feedback
- state changes

Keeping these systems separate allows new weapons, enemies, and attacks to be added without rewriting existing code.

---

# Mental Model

Think of combat as a conversation.

```text
Attack

↓

Did Something Get Hit?

↓

Apply Damage

↓

React

↓

Continue Playing
```

Each step has one responsibility.

No single object performs every part of the interaction.

---

# Starter Structure

A typical enemy might contain:

```text
Enemy (CharacterBody2D)

├── CollisionShape2D
├── AnimatedSprite2D
├── Hurtbox (Area2D)
└── Detection Area (Area2D)
```

The player's weapon might contain:

```text
Sword

└── Hitbox (Area2D)
```

Rather than asking:

> Did the player touch the enemy?

the game asks:

> Did the player's **Hitbox** overlap the enemy's **Hurtbox**?

---

# Dissecting the System

A typical combat interaction follows this sequence.

```text
Hitbox

↓

Hurtbox

↓

Damage

↓

Health

↓

Knockback

↓

State Change
```

Notice that every step has one responsibility.

The Hitbox detects.

The Hurtbox receives.

The Health system stores health.

The State Machine decides what happens next.

Each system remains simple.

---

# Design Principle

## Separate detection from consequences.

Detecting a hit is not the same as applying damage.

Applying damage is not the same as dying.

Breaking combat into smaller systems makes gameplay easier to extend and debug.

---

# Practical Observation

Many beginner projects place all combat logic inside one script.

As projects become larger...

combat naturally separates into systems.

For example:

- Hitboxes detect attacks.
- Hurtboxes receive attacks.
- Health stores hit points.
- Knockback modifies movement.
- State Machines decide how the object reacts.

Each system becomes easier to understand because it has one clear responsibility.

---

# Common Misconceptions

### "Collision means damage."

Not necessarily.

Many collisions do not cause damage.

Damage usually requires a specific gameplay interaction such as a Hitbox overlapping a Hurtbox.

---

### "Health belongs inside the weapon."

No.

Weapons produce attacks.

Health belongs to the object that can receive damage.

---

### "Knockback is part of movement."

Knockback affects movement.

It is usually triggered by the damage system rather than the movement system itself.

Keeping those systems separate makes them easier to modify.

---

### "Death should happen immediately."

Not always.

Many games allow an object to:

- play a hit animation
- experience knockback
- play a sound
- enter a DEAD state

before finally being removed.

Death is often another stage in the object's lifecycle.

---

# Reflection

Imagine a sword striking an enemy.

Which system should be responsible for each task?

| Task | System |
|------|--------|
| Detect Attack | |
| Reduce Health | |
| Apply Knockback | |
| Play Hit Animation | |
| Play Sound | |
| Remove Enemy | |

Now ask yourself:

Could these systems be reused by a completely different enemy?

Why?

---

# Looking Back

Earlier we learned that enemies change behavior using State Machines.

Now we've discovered another important idea.

Combat is not one system.

It is several small systems working together.

Detection.

Health.

Movement.

Animation.

State.

Each contributes one part of the interaction.

---

# Looking Ahead

Damage changes gameplay.

Eventually...

an object's health reaches zero.

What should happen next?

Should the object disappear immediately?

Should it play an animation?

Should it finish a sound?

The next lesson explores one of the most overlooked parts of gameplay programming:

> **Death and Destruction**