# Pattern 2.13.1 — Player Only

## Classification

**Type:** Gameplay Pattern

**Category:** Collision Layers & Masks

**Difficulty:** Intermediate

**Prerequisites:**

- Area3D
- Collision Layers
- Collision Masks

---

# Problem

Many gameplay systems should only interact with the player.

Examples include:

- checkpoints
- tutorial prompts
- dialogue triggers
- save points
- finish lines

If another object enters the Area:

- a crate
- a ball
- an enemy

nothing should happen.

Collision Layers and Masks allow us to choose **who is allowed to interact**.

---

# Starter Implementation

Open the **Area3D**.

In the Inspector, locate:

```text
Collision

├── Layer
└── Mask
```

Suppose your project uses:

| Layer | Purpose |
|--------|----------|
| 1 | World |
| 2 | Player |
| 3 | Enemy |
| 4 | Physics Objects |

Configure the Area.

```text
Layer

Checkpoint
↓

Layer 5
```

Configure the Mask.

```text
Mask

✓ Player

☐ Enemy

☐ Physics Objects
```

Run the scene.

Walk the player into the Area.

Observe.

Now roll a physics object through the same Area.

Observe.

Only the player triggers the interaction.

---

# How It Works

```text
Player

↓

Layer 2

↓

Area Mask

↓

Allowed

↓

Signal Fires
```

Objects on other layers are simply ignored.

---

# Anatomy

## Collision Layer

Defines:

> **What this object is.**

---

## Collision Mask

Defines:

> **What this object cares about.**

---

## Interaction

Both objects must agree before interaction occurs.

Layers describe identity.

Masks describe interest.

---

# Design Principle

## Most objects should ignore most other objects.

Imagine a game containing:

- players
- enemies
- bullets
- pickups
- decorations
- triggers

Should every object interact with every other object?

Usually not.

Collision filtering allows the engine to ignore unnecessary interactions.

This makes gameplay easier to design and often improves performance.

---

# Experiment

Only change one thing.

---

### Experiment A

Enable:

```text
Enemy
```

inside the Mask.

Observe.

Enemies now trigger the Area.

---

### Experiment B

Enable:

```text
Physics Objects
```

Observe.

Can rolling crates activate the checkpoint?

---

### Experiment C

Disable:

```text
Player
```

Observe.

Can the player still activate it?

---

### Experiment D

Create two Areas.

Configure different Masks.

Observe.

Each Area now reacts to different objects.

---

### Experiment E

Turn on:

```text
Debug > Visible Collision Shapes
```

Observe.

The collision volumes remain identical.

Only the interaction rules changed.

---

# Practical Applications

Player-only Areas appear throughout games.

Examples include:

- checkpoints
- finish lines
- tutorials
- save stations
- dialogue regions
- quest triggers

Many gameplay systems should ignore everything except the player.

---

# Common Misconceptions

### "Layers determine who collides."

Not entirely.

Layers describe what an object **is**.

Masks describe what an object **checks for**.

Both participate in the decision.

---

### "Every object should interact with everything."

Usually not.

Filtering interactions often simplifies gameplay dramatically.

---

### "Changing the Mask changes the object's appearance."

Layers and Masks affect only interaction.

They do not affect rendering.

---

# Workbench Habit

Whenever something interacts unexpectedly, ask yourself:

> **Should these two objects even know about one another?**

Often the solution is not changing the code.

It's changing the Layer or the Mask.

---

# Challenge

Create a simple level containing:

- one player
- one enemy
- one rolling crate
- one checkpoint

Configure the checkpoint so that **only the player** can activate it.

Experiment by changing the collision masks.

Notice that the Area script never changes.

Only the interaction rules do.