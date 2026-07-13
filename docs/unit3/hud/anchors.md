# Technique 3.3 — Use Anchors

## Classification

**Type:** Engineering Technique

**Category:** Heads-Up Display (HUD)

**Difficulty:** Beginner

**Estimated Time:** 20–25 minutes

---

# Design Scenario

Your interface looks perfect.

Until you run the game on a different monitor.

Suddenly:

- the score has shifted
- the health bar is no longer in the corner
- buttons overlap one another
- dialogue boxes appear in unexpected places

Nothing is actually wrong with your interface.

The screen simply changed size.

To build interfaces that work across different resolutions, Godot uses **Anchors**.

---

# Why This Technique Matters

Game worlds are measured in meters.

Interfaces are measured relative to the player's screen.

A player might run your game:

- in a small window
- fullscreen
- on an ultrawide monitor
- on a laptop
- on a handheld device

Your interface should adapt automatically.

Anchors describe **which part of the screen a Control node should stay attached to**.

---

# Mental Model

Imagine hanging a picture frame.

If you nail it to the left wall, it remains attached to that wall even if the room becomes wider.

If you center it between two walls, it remains centered as the room changes size.

Anchors work the same way.

They define **what part of the screen your interface should remain attached to**.

The screen may grow or shrink.

The relationship stays the same.

---

# Starter Implementation

Begin with the following hierarchy.

```text
CanvasLayer
└── Control
    └── Label
```

Select the **Label**.

Experiment with the built-in Anchor Presets.

Try placing the Label:

- Top Left
- Top Right
- Bottom Left
- Bottom Right
- Center

Run the project.

Resize the game window.

Observe what happens.

---

# Anatomy

## Control

Provides the region where interface elements exist.

---

## Anchors

Determine **which edges of the screen a Control node follows**.

Rather than storing a fixed screen position, anchors describe a relationship to the screen itself.

---

## Offsets

Once anchors establish the general location, offsets determine the exact spacing from those anchored edges.

For example:

```text
Top Right Anchor
        +
16 pixel offset
```

keeps an element near the upper-right corner while maintaining a consistent margin.

---

# Design Principle

## Position is relative.

Earlier we positioned objects using world coordinates.

Now we position interface elements using relationships.

Instead of asking:

> "Where is this object?"

we ask:

> "What should this object stay attached to?"

Those are fundamentally different questions.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Anchor a Label to the top-left corner.

Resize the game window.

Observe.

---

### Experiment B

Move the same Label to the bottom-right anchor.

Resize the window again.

Observe.

---

### Experiment C

Anchor the Label to the center.

Resize the window.

Observe.

Why does the Label remain centered?

---

### Experiment D

Adjust only the offsets.

Observe how spacing changes while the overall attachment remains the same.

---

### Experiment E

Create several Labels.

Anchor one to each corner.

Resize the window repeatedly.

Observe how each Label behaves.

---

# Practical Observation

Many familiar interface elements rely on anchors:

- score displays
- health bars
- minimaps
- inventory panels
- pause buttons
- dialogue boxes

Players rarely notice good anchoring.

They immediately notice poor anchoring.

---

# Common Misconceptions

### "Anchors move the object."

Not exactly.

Anchors define **what part of the screen the object follows**.

Offsets determine the final position.

---

### "I can just drag everything into place."

That may work for one screen size.

It often breaks on another.

Anchors allow layouts to adapt automatically.

---

### "Anchors are only useful for menus."

No.

Nearly every interface benefits from appropriate anchoring.

Even a simple score display should remain attached to the same corner throughout the game.

---

# Reflection

Complete the sentence.

> World objects are positioned relative to...

Complete the sentence.

> Interface elements are anchored relative to...

Now answer:

Why might a fixed pixel position create problems on different screen sizes?

---

# Self Check

Before moving on, ask yourself:

✓ I understand what anchors do.

✓ I can explain the difference between anchors and offsets.

✓ I can place interface elements in different parts of the screen.

✓ I understand why interfaces should adapt to different resolutions.

---

# Looking Ahead

Anchors determine **where** interface elements belong.

The next question becomes:

> **How should multiple interface elements be arranged together?**

We'll begin exploring **Containers**, which automatically organize groups of interface elements into flexible layouts.