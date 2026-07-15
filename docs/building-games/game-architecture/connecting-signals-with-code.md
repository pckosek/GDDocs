# 4.3.4 Connect Signals in Code

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Creating a signal allows an object to announce an event.

Emitting the signal broadcasts that announcement.

But there is still one missing piece.

Who is listening?

Until another object connects to the signal, every announcement simply disappears.

To make signals useful, we must connect them to code that should respond.

---

# Why This Technique Matters

Signals allow objects to remain independent.

The object that emits the signal does not need to know:

- who is listening
- how many listeners exist
- what those listeners will do

Instead, listeners choose which events they care about.

Connecting a signal establishes that relationship.

---

# Starter Implementation

Suppose we have a player with a custom signal.

```gdscript
signal health_changed(new_health)
```

Another object wants to respond whenever that signal is emitted.

Inside its script, connect the signal.

```gdscript
func _ready():
	Player.health_changed.connect(_on_health_changed)
```

Now define the function that will respond.

```gdscript
func _on_health_changed(new_health):
	print("Health:", new_health)
```

Whenever the player emits:

```gdscript
health_changed.emit(75)
```

Godot automatically calls:

```gdscript
_on_health_changed(75)
```

---

# Dissecting the Code

This line:

```gdscript
Player.health_changed.connect(_on_health_changed)
```

creates the connection.

Think of it as saying:

> "Whenever this signal happens..."

"...run this function."

---

The signal

```gdscript
health_changed
```

does not know anything about:

```gdscript
_on_health_changed()
```

Likewise,

```gdscript
_on_health_changed()
```

does not need to know when the signal will occur.

The connection joins the two.

---

# Mental Model

Think of a signal as a radio broadcast.

```text
Player

↓

Broadcast

↓

Health Changed (75)
```

Objects that have connected receive the message.

```text
HUD

↓

Update Health Bar

-------------------

Sound System

↓

Play Damage Sound

-------------------

Achievement System

↓

Check Milestone
```

The Player broadcasts.

The listeners decide how to react.

---

# Design Principle

## Emitters announce.

## Listeners respond.

The object producing the event should not control what happens afterwards.

Each listener is responsible for its own behavior.

This keeps systems flexible and independent.

---

# Experiment

Suppose a door emits:

```text
door_opened
```

Which systems might connect to that signal?

- Play a sound
- Display a message
- Unlock the next room
- Save progress
- Trigger an achievement

Would the door need to know about any of those systems?

Or can they simply listen?

---

# Practical Observation

Signals often connect during:

```gdscript
_ready()
```

This ensures that the connection exists before gameplay begins.

Once connected, the relationship remains active until it is disconnected or one of the objects is removed.

---

# Common Misconceptions

### "Connecting a signal runs the function."

No.

Connecting simply establishes the relationship.

The function runs later, when the signal is emitted.

---

### "The signal chooses which function to call."

Not exactly.

The listener chooses to connect.

The emitter simply broadcasts the event.

---

### "Only one function can connect."

No.

Many different functions—even on different objects—can connect to the same signal.

Each will be called when the event occurs.

---

### "Objects need to know about each other."

Usually not.

Signals allow objects to communicate without tightly coupling their behavior.

Each object focuses on its own responsibility.

---

# Reflection

Imagine your Player emits:

```text
player_died
```

List three different objects that might connect to this signal.

For each one, describe what it would do after receiving the event.

Now ask yourself:

Did the Player need to know about any of those systems?

---

# Looking Ahead

A single signal is not limited to a single listener.

One announcement can notify many different systems simultaneously.

The next question becomes:

> **How can one event coordinate many independent parts of the game?**