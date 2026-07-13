# 4.4.3 Track Current State

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

We have created an enum that defines all of our possible states.

```gdscript
enum State {
	IDLE,
	WALKING,
	JUMPING,
	FALLING
}
```

But defining possible states is not enough.

The object must also remember:

> **Which state am I in right now?**

Without that information, the object has no way to decide how it should behave.

---

# Why This Technique Matters

A state machine works because the object always knows its current state.

For example:

```text
Current State

↓

IDLE
```

Later...

```text
Current State

↓

WALKING
```

Then...

```text
Current State

↓

JUMPING
```

At any given moment, the object has one active state.

Everything else follows from that.

---

# Starter Implementation

Begin with your enum.

```gdscript
enum State {
	IDLE,
	WALKING,
	JUMPING,
	FALLING
}
```

Now create a variable.

```gdscript
var current_state = State.IDLE
```

When the game begins, the player starts in the **Idle** state.

Whenever behavior changes, update the variable.

```gdscript
current_state = State.WALKING
```

Later...

```gdscript
current_state = State.JUMPING
```

The variable always describes the object's current behavior.

---

# Dissecting the Code

Notice that the enum never changes.

```gdscript
enum State {
	IDLE,
	WALKING,
	JUMPING,
	FALLING
}
```

These are simply the possible choices.

The variable is what changes.

```gdscript
current_state
```

Think of it this way.

```text
Enum

↓

Possible States

-------------------

Variable

↓

Current State
```

The enum defines the menu.

The variable records today's selection.

---

# Design Principle

## An object should always know what it is currently doing.

Behavior becomes much easier to organize when there is one clearly defined current state.

Instead of asking many independent questions...

```text
Am I walking?

Am I jumping?

Am I falling?
```

we can simply ask:

```gdscript
current_state
```

One variable answers the question.

---

# Experiment

Suppose the following events occur.

```text
Player starts game.

↓

Player begins walking.

↓

Player jumps.

↓

Player lands.

↓

Player stands still.
```

What should the value of:

```gdscript
current_state
```

be after each event?

Can you trace the sequence?

---

# Practical Observation

Notice something interesting.

Earlier in this unit we discussed **Game State**.

Now we've created:

```gdscript
current_state
```

This is actually another piece of state.

The object must remember its current behavior.

Behavioral state is still information.

It simply describes **what the object is doing** rather than facts like score or health.

---

# Common Misconceptions

### "The enum remembers the current state."

No.

The enum only defines the available choices.

The variable remembers which choice is currently active.

---

### "Multiple current states should be active."

Usually not.

Most state machines assume one active behavioral state at a time.

Changing behavior means changing the current state.

---

### "Changing the state changes the object's code."

No.

Changing the state changes the value of a variable.

Your code will later use that value to decide what behavior should occur.

---

### "Tracking the current state automatically changes behavior."

Not yet.

Right now, the variable only stores information.

In the next lesson, we'll begin using that information to control behavior.

---

# Reflection

Imagine the following objects.

What variable might each one use to track its current state?

| Object | Current State Variable |
|----------|------------------------|
| Player | |
| Enemy | |
| Door | |
| Elevator | |
| Traffic Light | |

Now ask yourself:

How does each object know when it should change from one state to another?

---

# Looking Ahead

Our objects now know their current state.

The next challenge is deciding when that state should change.

> **How do we move from one state to another during gameplay?**