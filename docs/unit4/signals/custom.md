# 4.3.2 Create Custom Signals

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Godot provides many useful built-in signals.

A button can announce that it was pressed.

A timer can announce that time has expired.

An Area can announce that a body has entered.

But what if your own object needs to communicate?

Imagine a checkpoint.

When the player activates it, other systems may need to know.

- The HUD might display "Checkpoint Reached!"
- The Game Manager might save the checkpoint.
- A sound effect might play.
- A particle effect might begin.

None of these are built into Godot.

Your object needs a way to announce its own events.

---

# Why This Technique Matters

Custom signals allow your own scripts to communicate with the rest of the game.

Instead of directly telling every other object what to do...

...your script simply announces that something happened.

Other objects decide whether they care.

This keeps systems independent and easier to maintain.

---

# Starter Implementation

Suppose we are creating a checkpoint.

At the top of the script, define a signal.

```gdscript
extends Area3D

signal checkpoint_activated
```

This tells Godot:

> "This object can announce when a checkpoint is activated."

Later, when the player reaches the checkpoint, emit the signal.

```gdscript
func activate():
	print("Checkpoint Activated")

	checkpoint_activated.emit()
```

Whenever `activate()` is called, the object announces its event.

---

# Dissecting the Code

Creating the signal:

```gdscript
signal checkpoint_activated
```

does not make anything happen.

It simply defines a new kind of announcement.

---

Calling:

```gdscript
checkpoint_activated.emit()
```

actually broadcasts the event.

Think of it as speaking.

```text
Checkpoint

↓

"Checkpoint Activated!"
```

Whether anyone responds depends on who is listening.

---

# Design Principle

## Objects should announce what they know.

A checkpoint knows when it has been activated.

A door knows when it opens.

A player knows when they take damage.

Each object should communicate events that naturally belong to it.

---

# Experiment

Imagine the following game objects.

What custom signal might each one create?

| Object | Possible Signal |
|----------|-----------------|
| Door | `door_opened` |
| Enemy | `enemy_defeated` |
| Treasure Chest | `chest_opened` |
| Player | `player_died` |
| Elevator | `arrived_at_floor` |

Notice that every signal describes **something that happened.**

---

# Practical Observation

Signals often read like sentences.

For example:

```gdscript
signal player_died
signal level_completed
signal puzzle_solved
signal coin_collected
```

These names describe events.

When reading the code later, the purpose of each signal is immediately clear.

Choosing descriptive names makes large projects much easier to understand.

---

# Common Misconceptions

### "Creating a signal automatically runs code."

No.

Defining a signal simply creates a new type of event.

Nothing happens until the signal is emitted.

---

### "Signals store information."

No.

Signals announce that an event occurred.

If information needs to be remembered, it belongs in game state.

---

### "Every object should use custom signals."

Not necessarily.

Many objects can use Godot's built-in signals.

Create custom signals when your own gameplay objects need to communicate events that the engine does not already provide.

---

### "Signals tell other objects what to do."

Not exactly.

Signals announce what happened.

Other objects decide how—or whether—to respond.

---

# Reflection

Think about a game you've built.

Can you identify three objects that might benefit from creating their own signals?

For each one, answer:

- What event should it announce?
- Which other systems might want to know about it?

---

# Looking Ahead

Creating a signal allows an object to announce that something happened.

Sometimes, however, the announcement needs more than just the event itself.

The next question becomes:

> **How can a signal send additional information along with the event?**