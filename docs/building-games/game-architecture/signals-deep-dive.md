# 4.3.1 Review Built-in Signals

## Classification

**Type:** Design / Engineering Guide

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–25 minutes

---

# Design Problem

Imagine a player presses a button.

Should every object in the game constantly ask:

```text
Has the button been pressed yet?

Has it been pressed now?

What about now?
```

Probably not.

Instead, it would be much simpler if the button could simply announce:

> **"I was pressed."**

This kind of announcement is called an **event**.

In Godot, many events are communicated using **Signals**.

---

# Why This Matters

In the previous section, we learned that important information belongs to a single owner.

But ownership alone is not enough.

When something changes...

...other systems often need to know.

For example:

- A player loses health.
- A button is pressed.
- An animation finishes.
- A timer reaches zero.
- An Area detects another object.

These events happen once.

Other objects may want to respond.

Signals provide a way for objects to announce those events without needing to know who is listening.

---

# Built-in Signals

Many Godot nodes already include useful signals.

For example:

| Node | Example Signal |
|------|----------------|
| Button | `pressed()` |
| Timer | `timeout()` |
| Area2D / Area3D | `body_entered()` |
| AnimationPlayer | `animation_finished()` |
| Tree | `tree_entered()` |
| Node | `ready()` |

These signals are built into the engine.

You do not need to create them yourself.

---

# Mental Model

Think of a signal like making an announcement.

```text
Button

↓

"I'm pressed!"
```

Who hears the announcement?

Potentially many different systems.

```text
Button Pressed

↓

HUD

Sound Effect

Door

Dialogue System

Achievement System
```

The button does not know who is listening.

It simply announces that something happened.

---

# Design Principle

## Signals announce events.

Signals are not variables.

Signals are not game state.

Signals communicate that **something has just happened.**

State remembers.

Signals announce.

---

# Experiment

Consider each example.

Is it describing **state** or an **event**?

| Example | State or Event? |
|----------|-----------------|
| Player Health = 50 | |
| Button Pressed | |
| Door Open | |
| Animation Finished | |
| Current Score | |
| Timer Timeout | |
| Enemy Defeated | |
| Game Paused | |

Can you explain why?

---

# Practical Observation

One of the strengths of Godot is that many common interactions already have built-in signals.

Instead of writing code to repeatedly check whether something has happened...

...you can simply respond when the event occurs.

This often produces code that is simpler, easier to read, and more efficient.

---

# Common Misconceptions

### "Signals store information."

No.

Signals communicate that an event occurred.

If information needs to persist, it should usually be stored as game state.

---

### "Signals happen continuously."

No.

Signals occur at specific moments.

Once the event has happened, the signal is finished.

---

### "Signals require another object to exist."

Not necessarily.

A node can emit a signal whether or not anything is currently listening.

If nobody is listening...

...nothing happens.

---

### "Signals replace variables."

No.

Variables describe the current game.

Signals announce changes within the game.

Most games use both together.

---

# Reflection

Think about a simple game.

List five things that happen only briefly.

Examples might include:

- a button is pressed
- a coin is collected
- a timer expires

Now list five pieces of information the game must continue remembering.

How are those two lists different?

---

# Looking Ahead

Godot provides many useful signals automatically.

Eventually, however, your own objects will need to announce events as well.

The next question becomes:

> **How can we create our own custom signals?**