# Technique 2.8 — Rotating Platform

## Classification

**Type:** Engineering Technique

**Category:** Physical Interaction

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Scenario

You have built:

- a **CharacterBody3D**
- an **AnimatableBody3D**

Individually, both systems work correctly.

Now combine them.

The goal is simple.

The player should:

- stand on the moving platform
- ride as the platform moves
- remain standing on the platform
- not be "frictionless"

This is the first time we ask:

> **What happens when two moving physical systems interact?**

---

# Why This Technique Matters

Moving platforms appear in countless games.

Examples include:

- elevators
- lifts
- moving bridges
- floating platforms
- conveyor belts

Although these objects appear simple, they introduce one of the first situations where multiple systems must cooperate correctly.

---

# Starter Implementation

Create the following scene.

```text
World
├── Player (CharacterBody3D)
└── Platform (AnimatableBody3D)
```

Use the CharacterBody3D from the previous technique.

Use the AnimatableBody3D from the previous technique.

Place the player on top of the movingplatform.

Run the scene.

Observe.

Does the player remain on the platform?

Does the player move with it?

---

# Anatomy of the Interaction

Two independent systems are cooperating.

```text
CharacterBody3D

↓

Collision

↓

AnimatableBody3D

↓

Scripted Motion
```

The player does not know the elevator is an elevator.

The elevator does not know the player is standing on it.

The physics engine resolves the interaction.

---

# Design Principle

## Interesting gameplay often emerges from interacting systems.

Neither the CharacterBody3D nor the AnimatableBody3D was designed specifically for elevators.

The elevator emerges because two independent systems cooperate.

Many game mechanics are created this way.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Increase the elevator speed.

Observe.

Does the player continue riding successfully?

---

### Experiment B

Slow the elevator dramatically.

Observe.

Does the interaction feel different?

---

### Experiment C

Replace the vertical motion with horizontal motion.

Observe.

How does carrying the player change?

---

### Experiment D

Step onto the platform while it is already moving.

Observe.

What happens?

---

### Experiment E

Jump onto the platform.

Observe.

Can the player successfully land while the elevator is moving?

---

# Practical Observation

Moving platforms introduce many subtle design problems.

Examples include:

- carrying the player
- stepping on
- stepping off
- changing direction
- multiple passengers

Fortunately, CharacterBody3D and AnimatableBody3D were designed to cooperate in these situations.

---

# Common Uses

This interaction appears in many games.

Examples include:

- elevators
- moving platforms
- floating islands
- conveyor belts
- moving trains
- rotating platforms

The underlying relationship remains the same.

A scripted object carries a player through the world.

---

# Common Misconceptions

### "The elevator moves the player."

Not directly.

The player and the elevator each follow their own movement rules.

The physics engine resolves their interaction.

---

### "The player is parented to the elevator."

Usually not.

The player remains an independent object.

---

### "Any moving object should be a RigidBody3D."

Not necessarily.

Objects that follow predetermined paths are often better represented as AnimatableBody3Ds.

---

### "This is just another wall."

Not quite.

The wall remained stationary.

The elevator changes position continuously while still participating in collisions.

That makes the interaction fundamentally different.

---

# Reflection

Complete the sentence.

> Riding an elevator is different from walking into a wall because...

Now answer:

Why is an elevator a better candidate for AnimatableBody3D than StaticBody3D?

Can you think of three other game objects that should carry the player in a similar way?

---

# Self Check

Before moving on, ask yourself:

✓ I understand how CharacterBody3D and AnimatableBody3D interact.

✓ I can explain why moving platforms are different from walls.

✓ I can build a simple elevator.

✓ I recognize that interesting gameplay often emerges from multiple systems working together.

---

# Looking Ahead

So far, our interactions have involved physical contact.

Walls stop movement.

Platforms carry the player.

Next we'll explore a different kind of interaction.

Some objects do not block movement at all.

Instead...

they simply notice that something has happened.

We'll build a finish line using **Area3D**, where interaction is detected rather than obstructed.