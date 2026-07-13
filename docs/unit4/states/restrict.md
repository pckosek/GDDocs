# 4.4.5 Restrict Invalid Transitions

## Classification

**Type:** Design / Engineering Guide

**Category:** Game Architecture

**Difficulty:** Intermediate

---

# Design Problem

Changing state is easy.

```gdscript
current_state = State.JUMPING
```

But should this always be allowed?

Imagine the following situations.

Can a player:

- jump while already falling?
- attack while defeated?
- climb while swimming?
- open a door that is already open?

Technically, the code might allow these changes.

That doesn't mean they make sense.

As games become more complex, we need a way to prevent impossible or illogical behavior.

---

# Why This Matters

A state machine is more than a collection of states.

It also defines **which transitions are allowed.**

For example:

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

This sequence feels natural.

Now imagine:

```text
Defeated

↓

Running
```

That probably shouldn't happen.

Good state machines prevent objects from entering states that don't make sense.

---

# Mental Model

Think of states as rooms connected by doors.

```text
Idle

↓

Walking

↓

Jumping

↓

Falling
```

Some doors exist.

Others do not.

You can only move through the doors that have been built.

Trying to walk through a wall doesn't change your location.

State transitions work the same way.

---

# Starter Implementation

Suppose the player is currently jumping.

```gdscript
current_state = State.JUMPING
```

Before changing state, ask whether the transition is allowed.

```gdscript
if current_state == State.IDLE:
	current_state = State.JUMPING
```

Here, the player may only begin jumping from the Idle state.

If the player is already falling...

...nothing changes.

---

Another example.

```gdscript
if current_state == State.FALLING:
	current_state = State.IDLE
```

Landing only makes sense after falling.

---

# Dissecting the Code

Notice that we no longer ask only:

```text
What state should I become?
```

We also ask:

```text
What state am I in now?
```

Both questions matter.

A transition depends on:

- the current state
- the desired state

Without both pieces of information, we cannot decide whether the transition makes sense.

---

# Design Principle

## Not every state should be able to reach every other state.

Good state machines describe both:

- the possible states
- the valid paths between them

Restricting transitions prevents impossible behaviors and keeps objects behaving predictably.

---

# Experiment

Consider the following player states.

```text
Idle

Walking

Jumping

Falling

Defeated
```

For each transition below, decide whether it should usually be allowed.

| Transition | Allowed? |
|------------|----------|
| Idle → Walking | |
| Walking → Jumping | |
| Falling → Idle | |
| Defeated → Walking | |
| Jumping → Falling | |
| Idle → Defeated | |

Can you explain your reasoning?

---

# Practical Observation

Many gameplay bugs are not caused by incorrect code.

They're caused by incorrect transitions.

Examples include:

- jumping again while already in the air
- attacking after the character has died
- opening a door that is already open
- starting the same animation multiple times

Often, the solution is not adding more behavior.

It's preventing behavior that should never occur.

---

# Common Misconceptions

### "Every state should connect to every other state."

No.

Many transitions simply don't make sense.

Restricting them makes behavior more predictable.

---

### "The player should never be prevented from changing state."

Sometimes preventing a transition is exactly the correct behavior.

For example, a defeated character usually cannot begin running.

---

### "Checking the current state is unnecessary."

Without checking the current state, objects may enter impossible combinations of behavior.

Knowing where an object is now is essential before deciding where it may go next.

---

### "Invalid transitions are programming mistakes."

Not necessarily.

Sometimes they are intentional player inputs that occur at the wrong time.

The job of the state machine is to decide whether those requests should be accepted or ignored.

---

# Reflection

Think about one of your favorite games.

List three actions that **should not** be possible.

Examples might include:

- jumping after dying
- firing while reloading
- opening a locked chest

Now ask yourself:

How might a state machine prevent those actions?

---

# Looking Ahead

Our objects can now:

- define possible states
- remember their current state
- change between states
- reject impossible transitions

The final step is bringing these ideas together.

> **How can we build a complete state machine that manages an object's behavior?**