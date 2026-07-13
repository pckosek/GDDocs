# Technique 3.8 — Bind Interface Elements to Game Data

## Classification

**Type:** Engineering Technique

**Category:** Heads-Up Display (HUD)

**Difficulty:** Intermediate

**Estimated Time:** 25–30 minutes

---

# Design Scenario

Your game now has:

- a score
- player health
- remaining lives
- ammunition

Your HUD displays all of these values.

At first, everything works.

Then you add a second way to gain points.

Later you add a bonus multiplier.

Soon you discover that some parts of the interface update correctly...

...while others still display old information.

The problem is not that the HUD is broken.

The problem is that the game now has **multiple copies of the same information**.

Instead, the interface should always display the game's current state.

This relationship is called **binding**.

---

# Why This Technique Matters

A HUD should never *own* gameplay information.

Its job is simply to display it.

The game determines:

- score
- health
- inventory
- objectives

The interface observes those values and presents them to the player.

Keeping these responsibilities separate makes games easier to maintain and much less prone to errors.

---

# Mental Model

Imagine the departure board at an airport.

The board does not decide when a plane leaves.

It simply displays information supplied by another system.

If a flight changes gates, the board updates.

If the flight is cancelled, the board reflects that change.

The display never becomes the source of truth.

It is simply a window into the underlying information.

A game HUD should behave the same way.

---

# Starter Implementation

Suppose your player stores their score.

```gdscript
var score := 0
```

Your HUD contains a Label.

```text
CanvasLayer
└── Control
    └── Label
```

Whenever the score changes:

```gdscript
score += 100
score_label.text = str(score)
```

Notice what happened.

The game owns the score.

The Label simply reflects its current value.

---

# Anatomy

## Game State

The information that represents the current condition of the game.

Examples include:

- score
- health
- ammunition
- remaining lives
- collected items

---

## Interface

Displays information to the player.

It should avoid storing independent copies of gameplay data.

---

## Binding

A relationship between game data and an interface element.

When the data changes, the displayed information changes as well.

---

## Source of Truth

The single location responsible for maintaining a piece of information.

Whenever possible:

- the gameplay system owns the data
- the interface displays the data

Not the other way around.

---

# Design Principle

## Display information instead of duplicating it.

Consider a classroom whiteboard.

The attendance sheet records who is present.

The whiteboard displays today's attendance.

If the attendance changes, the whiteboard should be updated.

Creating a second attendance list would only introduce opportunities for mistakes.

Good software follows the same principle.

One source.

Many displays.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Create a variable called:

```gdscript
score
```

Display it in a Label.

Increase the score.

Observe.

Does the Label update?

---

### Experiment B

Create a second Label displaying the same score.

Update both Labels.

Observe.

Can multiple interface elements display the same information?

---

### Experiment C

Intentionally stop updating one Label.

Observe.

What happens?

Which Label now represents the correct game state?

---

### Experiment D

Create a health variable.

Bind a Label to display the current health.

Reduce the health.

Observe how the interface changes.

---

### Experiment E

Imagine storing one score inside the Player...

...and another inside the HUD.

What problems might occur?

---

# Practical Observation

Many interface elements display bound information, including:

- score counters
- health bars
- stamina meters
- ammunition counters
- inventory quantities
- timers
- objective text

Although the visual appearance differs, the underlying principle is always the same.

The interface reflects the current game state.

---

# Common Misconceptions

### "The HUD should store the score."

Usually not.

The gameplay system owns the score.

The HUD simply displays it.

---

### "Updating the Label changes the game."

No.

Changing displayed text does not change the underlying game data.

The interface is a presentation layer.

---

### "Every object should have its own copy of important information."

This often leads to inconsistent behaviour.

Maintaining a single source of truth makes programs easier to understand and debug.

---

# Reflection

Complete the sentence.

> The game owns...

Complete the sentence.

> The HUD displays...

Now answer:

Why is it safer to maintain one copy of the score than several independent copies?

---

# Self Check

Before moving on, ask yourself:

✓ I understand what binding means.

✓ I can explain the difference between game state and interface state.

✓ I know why the HUD should not own gameplay information.

✓ I understand the idea of a single source of truth.

---

# Looking Ahead

Our HUD is now complete.

It can:

- exist independently of the game world
- organize itself automatically
- adapt to different screen sizes
- communicate using signals
- display live game information

With the interface in place, we're ready to explore the broader challenge of **managing game state**, where multiple gameplay systems must work together to control the flow of an entire game.