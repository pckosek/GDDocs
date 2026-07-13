# Technique 3.1 — Create a CanvasLayer

## Classification

**Type:** Engineering Technique

**Category:** Heads-Up Display (HUD)

**Difficulty:** Beginner

**Estimated Time:** 15–20 minutes

---

# Design Scenario

Your game now has information that the player needs to see.

Examples include:

- score
- health
- lives
- ammunition
- dialogue
- timers

Where should this information exist?

Should it be part of the game world?

Or should it remain attached to the screen?

This is the purpose of a **CanvasLayer**.

---

# Why This Technique Matters

Everything we have built so far exists **inside the game world**.

Examples include:

- players
- enemies
- platforms
- walls

These objects move as the camera moves.

A Heads-Up Display behaves differently.

The player should always be able to see:

- score
- health
- minimap
- dialogue

even while the camera moves through the world.

CanvasLayer creates a second coordinate system that remains attached to the screen.

---

# Mental Model

Imagine recording a soccer game.

The players move.

The camera follows.

The scoreboard does **not** move.

It remains fixed on the television screen.

Games work exactly the same way.

The world moves.

The HUD remains fixed.

---

# Starter Implementation

Create the following hierarchy.

```text
CanvasLayer
└── Control
```

Run the project.

Nothing appears to happen.

Now move the camera around the world.

Observe.

The CanvasLayer remains fixed to the screen.

Objects in the world move.

The HUD does not.

---

# Anatomy

## CanvasLayer

Responsible for:

> Drawing interface elements independently of the game camera.

---

## Control

Provides the foundation for user interface elements such as:

- Labels
- Buttons
- Panels
- Progress Bars
- TextureRects

Most HUD elements begin with a Control node.

---

# Design Principle

## The game world and the user interface are different spaces.

Think about these two questions.

Where is the player?

```text
3D World
```

Where is the score?

```text
Screen Space
```

These are fundamentally different coordinate systems.

Keeping them separate makes both systems easier to understand.

---

# Experiment

Only change one thing.

---

### Experiment A

Move the camera.

Observe.

Does the CanvasLayer move?

---

### Experiment B

Move the player.

Observe.

Does the CanvasLayer move?

---

### Experiment C

Add a Label beneath the Control node.

Observe.

The label remains attached to the screen.

---

### Experiment D

Delete the CanvasLayer.

Leave the Label.

Observe.

What changed?

---

### Experiment E

Create two CanvasLayers.

Experiment with placing different UI elements in each.

Observe.

---

# Practical Applications

CanvasLayers commonly contain:

- score displays
- health bars
- lives
- timers
- minimaps
- dialogue boxes
- pause menus
- inventory screens

Nearly every game contains at least one CanvasLayer.

---

# Common Misconceptions

### "The HUD belongs inside the 3D world."

Usually not.

HUD elements are generally attached to the screen.

---

### "CanvasLayer displays the interface."

CanvasLayer provides the drawing space.

The Control nodes actually create the interface.

---

### "The camera should move the HUD."

The HUD intentionally ignores camera movement.

That is one of its primary purposes.

---

# Reflection

Complete the sentence.

> The game world exists in...

Complete the sentence.

> The HUD exists in...

Now answer:

Why would it be frustrating if the player's health bar moved around the screen whenever the camera rotated?

---

# Self Check

Before moving on, ask yourself:

✓ I understand why CanvasLayer exists.

✓ I understand the difference between world space and screen space.

✓ I can create a CanvasLayer.

✓ I know that UI elements usually belong beneath a CanvasLayer.

---

# Looking Ahead

CanvasLayer provides the space for the interface.

The next question becomes:

> **How should we arrange the interface?**

We'll begin exploring **Control** nodes, anchors, and containers—the building blocks of every HUD.