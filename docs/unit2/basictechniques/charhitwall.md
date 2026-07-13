# Technique 2.7 — Walking Into a Wall

## Classification

**Type:** Engineering Technique

**Category:** Physical Interaction

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Scenario

You have built:

- a player using **CharacterBody3D**
- a wall using **StaticBody3D**

Individually, both objects work correctly.

The next question is simple:

> **What happens when they meet?**

This is the first interaction between two physical representations.

---

# Why This Technique Matters

Collisions are not interesting because objects stop.

They are interesting because they define the rules of the world.

A wall tells the player:

> You cannot go here.

Without collisions:

- walls have no purpose
- rooms have no boundaries
- platforms cannot be stood upon

Physical interaction transforms geometry into gameplay.

---

# Starter Implementation

Create a simple room.

```text
Floor (StaticBody3D)

Wall (StaticBody3D)

Player (CharacterBody3D)
```

Use the CharacterBody3D movement script from the previous technique.

Run the scene.

Walk toward the wall.

Observe.

The player stops.

Notice:

Your movement script never says:

> "Stop at the wall."

Instead:

```gdscript
move_and_slide()
```

detects the collision and resolves it automatically.

---

# Anatomy of the Interaction

Two independent systems are now cooperating.

```text
Player

↓

CharacterBody3D

↓

move_and_slide()

↓

Collision

↓

StaticBody3D

↓

Wall
```

Neither object knows anything about the other.

The physics engine resolves the interaction.

---

# Design Principle

## Gameplay emerges from interaction.

Neither the wall nor the player is interesting alone.

The interesting behavior appears when they begin interacting.

Many game mechanics emerge from simple interactions between well-designed systems.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Increase the player's speed.

Observe.

Does collision still work?

---

### Experiment B

Create a narrow hallway.

Walk through it.

Observe.

---

### Experiment C

Create a corner.

Walk diagonally into it.

Observe.

What does `move_and_slide()` do?

---

### Experiment D

Remove the CollisionShape3D from the wall.

Run the scene.

Observe.

What changed?

---

### Experiment E

Replace the StaticBody3D with a Node3D.

Keep everything else the same.

Observe.

Can the player still collide?

---

# Practical Observation

Games rarely contain one wall.

Instead they contain hundreds.

Fortunately, every StaticBody3D follows the same rules.

Once one wall works...

every wall works.

The interaction scales naturally.

---

# Common Uses

CharacterBody3D interacting with StaticBody3D creates:

- walls
- rooms
- hallways
- platforms
- stairs
- obstacles
- buildings

Nearly every navigable level depends on this relationship.

---

# Common Misconceptions

### "The wall stops the player."

Not exactly.

The wall simply occupies physical space.

The CharacterBody3D decides how to respond to that collision.

---

### "move_and_slide() only moves."

It also performs collision resolution.

Without it, the player would pass through walls.

---

### "Collisions happen because of the mesh."

The CollisionShape3D defines the physical interaction.

The mesh is only visual.

---

### "The player should stop before touching the wall."

The CollisionShape—not necessarily the visible mesh—determines where contact occurs.

---

# Reflection

Complete the sentence.

> The wall does not know about the player because...

Now answer:

Why is it useful that the player and wall remain independent systems?

Could you build an entire level using the same interaction?

---

# Self Check

Before moving on, ask yourself:

✓ I understand why CharacterBody3D requires move_and_slide().

✓ I understand why StaticBody3D requires a CollisionShape3D.

✓ I can explain why the player cannot pass through the wall.

✓ I understand that interaction emerges from two independent systems working together.

---

# Looking Ahead

Walls are only the beginning.

Some objects move.

The next interaction asks a different question.

> **What happens when the floor itself begins moving?**

We'll explore how a CharacterBody3D interacts with an **AnimatableBody3D** by building an elevator that carries the player through the world.