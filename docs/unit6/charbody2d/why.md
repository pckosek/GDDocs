# 6.1.1 Why CharacterBody2D?

## Classification

**Type:** Engineering Technique

**Category:** 2D Character Movement

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine creating a platformer.

Your player should be able to:

- run
- jump
- fall
- collide with walls
- land on the ground

A simple **Node2D** can store a position.

It cannot automatically handle collisions.

A simple **Area2D** can detect overlaps.

It is not designed for physical movement.

We need a node that is specifically designed for moving objects that interact with the world.

Godot provides this as **CharacterBody2D**.

---

# Why This Matters

Most playable characters move intentionally.

They are controlled by:

- player input
- AI
- scripted movement

Unlike a **RigidBody2D**, they are not pushed around entirely by physics.

Instead, they decide where they want to move...

...while still respecting collisions with the world.

CharacterBody2D provides exactly that behavior.

It is the standard choice for:

- platformer characters
- top-down players
- NPCs
- enemies
- moving objects controlled by code

---

# Starter Implementation

Create a new scene.

Choose:

```text
CharacterBody2D
```

Your scene might look like:

```text
Player
│
├── CollisionShape2D
├── AnimatedSprite2D
└── Camera2D
```

Attach a script.

```gdscript
extends CharacterBody2D
```

At this point the player does not move.

That is expected.

The node simply provides the foundation for movement.

---

# Dissecting the Node

CharacterBody2D provides several important features.

It stores:

- position
- velocity

It also provides movement functions such as:

```gdscript
move_and_slide()
```

and

```gdscript
move_and_collide()
```

These functions help the character interact correctly with the surrounding world.

Rather than writing collision detection from scratch...

...we use the tools already provided by the engine.

---

# Design Principle

## Choose the node that matches the behavior.

Nodes are chosen because of **what they do**, not because of what they look like.

A CharacterBody2D is appropriate whenever an object:

- moves intentionally
- collides with the world
- is controlled through code

Choosing an appropriate node often eliminates a great deal of unnecessary work.

---

# Comparison

Several 2D nodes can represent moving objects.

| Node | Best Used For |
|------|---------------|
| Node2D | General positioning |
| Area2D | Detecting overlaps |
| CharacterBody2D | Controlled movement with collisions |
| RigidBody2D | Physics simulation |
| StaticBody2D | Immovable collision |

Notice that each node solves a different problem.

Choosing the correct one is an engineering decision.

---

# Practical Observation

Many beginning programmers choose nodes based on appearance.

Professional programmers choose nodes based on responsibility.

For example:

The player should decide where to move.

Therefore:

```text
CharacterBody2D
```

A coin should simply detect when it has been collected.

Therefore:

```text
Area2D
```

The ground should never move.

Therefore:

```text
StaticBody2D
```

The scene becomes easier to understand because each node has one clear purpose.

---

# Common Misconceptions

### "CharacterBody2D is only for players."

No.

Any object whose movement is controlled through code may benefit from using CharacterBody2D.

Enemies, NPCs, moving platforms, and projectiles are all common examples.

---

### "CharacterBody2D automatically moves."

No.

It provides the tools for movement.

Your script still decides:

- how fast to move
- when to jump
- when to stop

---

### "CharacterBody2D is the same as RigidBody2D."

No.

RigidBody2D simulates physical forces.

CharacterBody2D follows movement instructions written by the programmer.

---

### "Node2D could do the same thing."

A Node2D can certainly change its position.

What it does **not** provide is built-in collision-aware movement.

CharacterBody2D exists specifically to solve that problem.

---

# Reflection

Imagine the following objects.

Which node would you choose?

| Object | Appropriate Node |
|----------|------------------|
| Player | |
| Coin | |
| Enemy | |
| Wall | |
| Falling Rock | |

Can you explain why each object has different movement requirements?

---

# Looking Ahead

CharacterBody2D provides the foundation for movement.

One of its most important properties is:

```gdscript
velocity
```

The next question becomes:

> **How does a character decide how fast—and in which direction—to move?**