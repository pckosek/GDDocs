# 4.3.5 One Event, Many Listeners

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine the player defeats the final enemy in a level.

Many different systems may need to react.

- The score increases.
- A sound effect plays.
- A particle effect appears.
- The exit door unlocks.
- An achievement is checked.
- The HUD displays a message.

Should the enemy directly tell each of these systems what to do?

That quickly becomes difficult to maintain.

Instead, the enemy can simply announce:

> **"Enemy Defeated."**

Every interested system can respond independently.

---

# Why This Technique Matters

One of the greatest strengths of signals is that they support **one-to-many communication**.

A single event can notify many listeners.

The object emitting the signal never needs to know:

- who is listening
- how many listeners exist
- what each listener will do

It simply announces the event.

---

# Starter Implementation

Suppose an enemy defines the following signal.

```gdscript
signal enemy_defeated(points)
```

When the enemy is defeated:

```gdscript
enemy_defeated.emit(100)
```

Several different systems have connected to this signal.

```text
Enemy Defeated

↓

HUD
Update Score Display

↓

Game Manager
Increase Score

↓

Sound Manager
Play Victory Sound

↓

Achievement Manager
Check Progress

↓

Door
Unlock Exit
```

Each system responds independently.

---

# Dissecting the Technique

Notice something important.

The enemy only emits **one** signal.

```gdscript
enemy_defeated.emit(100)
```

It does **not** call:

```text
HUD.update()

Achievement.check()

Door.unlock()

Sound.play()
```

Instead, every listener receives the same event.

Each decides how to respond.

The emitter remains simple.

---

# Mental Model

Think of a public announcement.

```text
"The library will close in 10 minutes."
```

Different people respond differently.

```text
Student

↓

Finish Homework

-------------------

Teacher

↓

Lock Classroom

-------------------

Custodian

↓

Begin Cleaning

-------------------

Security

↓

Prepare Building
```

The announcement is the same.

The responses are different.

Signals work the same way.

---

# Design Principle

## One event can have many consequences.

The object announcing an event should not be responsible for every consequence.

Instead, each interested system should respond according to its own responsibility.

This keeps software modular and easier to extend.

---

# Experiment

Imagine your game emits:

```text
Level Completed
```

List every system that might respond.

Examples include:

- Save Progress
- Display Victory Screen
- Unlock Next Level
- Play Music
- Award Achievement
- Record Statistics

Would the Level object need to know about every one of those systems?

Or is it enough to simply announce the event?

---

# Practical Observation

One of the biggest advantages of signals appears as projects grow.

Suppose six months later you decide to add:

```text
Analytics System
```

It wants to record every completed level.

Without signals, you might need to modify several existing scripts.

With signals, the new system simply connects to:

```text
level_completed
```

No existing gameplay code needs to change.

Adding new features becomes much easier.

---

# Common Misconceptions

### "A signal can only have one listener."

No.

Any number of objects can connect to the same signal.

Each listener receives the event independently.

---

### "The emitter controls what every listener does."

No.

The emitter simply announces the event.

Each listener decides how to respond.

---

### "Adding more listeners changes the signal."

No.

The signal remains exactly the same.

Only the number of responding systems changes.

---

### "Signals are only useful for large projects."

Even small projects benefit from keeping systems independent.

Learning this pattern early makes larger projects much easier to build later.

---

# Reflection

Imagine your Player emits:

```text
player_died
```

List at least five different systems that could respond.

For each one, describe its responsibility.

Now ask yourself:

Did the Player need to know about any of those systems?

Or was announcing the event enough?

---

# Looking Ahead

Signals make communication flexible because objects don't need to know about one another directly.

This leads to one of the most important ideas in software architecture.

> **How can independent systems work together without becoming tightly connected?**