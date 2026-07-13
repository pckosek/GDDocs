# Technique 3.5 — Use Safe Margins

## Classification

**Type:** Engineering Technique

**Category:** Heads-Up Display (HUD)

**Difficulty:** Beginner

**Estimated Time:** 15–20 minutes

---

# Design Scenario

Your interface looks perfect on your computer.

Then someone plays your game.

Part of the score is hidden behind the edge of the screen.

A pause button is difficult to reach.

Dialogue appears too close to the bezel.

Nothing is technically outside the window.

Yet the interface feels cramped.

Professional interfaces rarely place important information directly against the edge of the screen.

Instead, they leave **safe margins**.

---

# Why This Technique Matters

The edges of a screen are visually busy.

Players naturally focus toward the center of their display.

Leaving a small amount of empty space around important interface elements makes them:

- easier to read
- easier to click
- easier to notice
- more visually comfortable

Safe margins are not simply empty space.

They improve usability.

---

# Mental Model

Imagine hanging a picture in a frame.

You would not place the artwork so that it touches the edges of the frame.

Instead, a border surrounds the image.

That empty border helps the artwork stand out.

User interfaces work the same way.

Empty space is an intentional part of the design.

---

# Starter Implementation

Create the following hierarchy.

```text
CanvasLayer
└── Control
    └── Label
```

Anchor the Label to the upper-right corner.

Now adjust its offsets.

Instead of placing the Label exactly on the edge of the screen, leave approximately:

- 16–32 pixels from the top
- 16–32 pixels from the right

Run the project.

Observe.

The interface feels more balanced, even though the Label contains exactly the same information.

---

# Anatomy

## Anchors

Determine **which edge of the screen an interface element follows.**

---

## Offsets

Determine **how far the element remains from those edges.**

Safe margins are created primarily by adjusting offsets.

---

## Empty Space

Although it contains no information, empty space contributes to:

- readability
- organization
- visual hierarchy
- accessibility

Good interface design considers empty space to be an active design element.

---

# Design Principle

## Empty space communicates.

Beginners often try to fill every available part of the screen.

Professional interfaces often do the opposite.

Space separates ideas.

It helps players recognize:

- groups
- priorities
- relationships

Sometimes adding nothing makes an interface easier to understand.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Place a Label directly against the upper-left corner.

Observe.

How comfortable is it to read?

---

### Experiment B

Move the same Label inward by 24 pixels.

Observe.

How does the interface feel different?

---

### Experiment C

Create four Labels.

Anchor one to each corner.

Give each Label a consistent margin.

Observe the overall balance of the interface.

---

### Experiment D

Reduce all margins to zero.

Observe.

What changed?

Did the interface become harder to read?

---

### Experiment E

Increase the margins significantly.

Observe.

At what point does too much empty space become a problem?

---

# Practical Observation

Many games maintain consistent margins for:

- score displays
- health bars
- minimaps
- objective text
- dialogue boxes
- pause buttons
- inventory panels

Using consistent spacing creates interfaces that feel organized, even when players cannot explain why.

---

# Common Misconceptions

### "Empty space is wasted space."

Usually not.

Thoughtful spacing often improves readability more than adding additional graphics.

---

### "Safe margins are only for large screens."

No.

Margins become even more important on smaller displays, where clutter quickly reduces readability.

---

### "Anchors automatically create good layouts."

Anchors determine where interface elements stay.

Safe margins determine how comfortably those elements fit within the screen.

Both are necessary.

---

# Reflection

Complete the sentence.

> Anchors determine...

Complete the sentence.

> Safe margins provide...

Now answer:

Why might an interface become more difficult to use if every element touched the edge of the screen?

---

# Self Check

Before moving on, ask yourself:

✓ I understand why safe margins exist.

✓ I can use offsets to create consistent spacing.

✓ I know that empty space is part of good interface design.

✓ I can explain why interfaces should avoid placing important information directly against the edge of the screen.

---

# Looking Ahead

Our interface now has structure, organization, and comfortable spacing.

The next question becomes:

> **How do we display information to the player?**

We'll begin with one of the most fundamental interface elements:

**Labels**, which display changing text such as scores, health values, timers, and player messages.