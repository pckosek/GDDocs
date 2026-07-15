# 4.4.4 Change State

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Our object now remembers its current state.

```gdscript
var current_state = State.IDLE
```

But if that value never changes...

...the object will remain idle forever.

Objects change behavior because their **state changes**.

The question is no longer:

> **"What state am I in?"**

It becomes:

> **"When should I change to a different state?"**

---

# Why This Technique Matters

Gameplay is full of transitions.

A player:

- starts walking
- jumps
- lands
- stops moving

Each of these moments represents a change in behavior.

By updating one variable...

```gdscript
current_state
```

...the rest of the object's behavior can change naturally.

---

# Starter Implementation

Suppose our player begins in the Idle state.

```gdscript
var current_state = State.IDLE
```

When the player begins moving...

```gdscript
current_state = State.WALKING
```

When the player jumps...

```gdscript
current_state = State.JUMPING
```

After landing...

```gdscript
current_state = State.IDLE
```

The object's behavior changes simply by changing its current state.

---

# Dissecting the Code

Notice that we are always changing **one variable**.

```gdscript
current_state
```

The possible values never change.

```gdscript
enum State {
	IDLE,
	WALKING,
	JUMPING,
	FALLING
}
```

Only the object's current selection changes.

Think of it like a compass.

```text
Possible Directions

North

East

South

West
```

The compass always knows all four directions.

Its needle simply points to one of them at a time.

---

# Mental Model

Behavior often follows a sequence.

```text
Idle

↓

Walking

↓

Jumping

↓

Falling

↓

Idle
```

The player is not performing every behavior simultaneously.

Instead, gameplay moves the object from one state to another.

Each transition changes how the object behaves.

---

# Design Principle

## Behavior changes by changing state.

Instead of rewriting the object's logic every frame...

...we simply update its current state.

The rest of the program can respond accordingly.

One variable controls many possible behaviors.

---

# Experiment

Imagine the following events occur.

```text
Player Standing Still

↓

Player Presses Right

↓

Player Presses Jump

↓

Player Lands

↓

Player Stops Moving
```

After each event:

What should the value of:

```gdscript
current_state
```

be?

Can you describe the complete sequence?

---

# Practical Observation

Many beginning programmers try to control behavior with many separate variables.

For example:

```gdscript
is_walking
is_jumping
is_falling
is_climbing
is_attacking
```

Eventually several become true at the same time.

Now the program must decide which one is correct.

A single current state avoids much of that confusion.

Changing behavior becomes as simple as updating one variable.

---

# Common Misconceptions

### "Changing state changes the object's code."

No.

The code stays the same.

Changing the value of `current_state` changes which behavior the object should perform.

---

### "Every frame should change the state."

Not necessarily.

States usually change because something meaningful happened.

Examples include:

- a button was pressed
- the player landed
- an animation finished
- a timer expired

---

### "Changing state automatically performs the behavior."

Not yet.

The state tells the program **what** behavior should occur.

The program still needs logic that responds to that state.

---

### "Changing state creates a new object."

No.

The same object continues to exist.

Only its current behavior changes.

---

# Reflection

Think about the following objects.

What events might cause them to change state?

| Object | Possible Transition |
|----------|---------------------|
| Player | Idle → Walking |
| Door | Closed → Opening |
| Enemy | Patrol → Chase |
| Elevator | Moving → Stopped |
| Traffic Light | Green → Yellow |

Now ask yourself:

What event caused each transition?

---

# Looking Ahead

Changing state gives our objects new behaviors.

But should **every** transition be allowed?

Can a defeated enemy suddenly begin attacking again?

Can a closed door become "closing"?

The next challenge is deciding which transitions are actually valid.

> **How do we prevent impossible changes between states?**