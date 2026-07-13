# 4.4.6 Build a Simple State Machine

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 30–40 minutes

---

# Design Problem

Throughout this chapter we've learned several individual techniques.

We can:

- define possible states
- create an enum
- remember the current state
- change states
- prevent invalid transitions

Now it's time to combine those ideas into a complete behavioral system.

This is called a **State Machine**.

---

# Why This Technique Matters

State machines help organize behavior.

Instead of asking dozens of unrelated questions...

```text
Is Jumping?

Is Walking?

Is Falling?

Is Climbing?

Is Attacking?
```

we ask one question.

```text
What state am I currently in?
```

The answer determines how the object should behave.

---

# Starter Implementation

Begin by defining the possible states.

```gdscript
extends CharacterBody3D

enum State {
	IDLE,
	WALKING,
	JUMPING,
	FALLING
}

var current_state = State.IDLE
```

Now use that state to guide behavior.

```gdscript
func _physics_process(delta):

	match current_state:

		State.IDLE:
			pass

		State.WALKING:
			pass

		State.JUMPING:
			pass

		State.FALLING:
			pass
```

Each section becomes responsible for one behavior.

---

Suppose the player presses the Jump button.

```gdscript
if current_state == State.IDLE:
	current_state = State.JUMPING
```

Only a valid transition changes the player's behavior.

---

# Dissecting the Code

Notice that the object contains three separate ideas.

First...

```gdscript
enum State
```

defines every possible behavior.

---

Second...

```gdscript
current_state
```

remembers which behavior is currently active.

---

Finally...

```gdscript
match current_state
```

decides what code should execute.

Together these pieces create a simple state machine.

---

# Mental Model

Think of the state machine as a traffic controller.

```text
Current State

↓

Choose Behavior

↓

Wait for Event

↓

Change State

↓

Repeat
```

The object is always cycling through this process.

It behaves according to its current state.

When something important happens...

...the state changes.

The cycle begins again.

---

# Design Principle

## Organize behavior around states.

Rather than scattering behavior throughout many independent conditions...

...group related behavior together.

Each state becomes responsible for one mode of operation.

This makes objects easier to understand, debug, and extend.

---

# Experiment

Imagine adding a new state.

```text
ATTACKING
```

What parts of your state machine would need to change?

- The enum?
- The current state variable?
- The behavior logic?
- The valid transitions?

Notice that the overall architecture remains the same.

Only the new behavior is added.

---

# Practical Observation

Simple state machines often begin with only three or four states.

As projects grow, additional states can be added without rewriting the entire object.

This makes state machines one of the most scalable ways to organize complex behavior.

Many professional games use state machines for:

- players
- enemies
- menus
- cutscenes
- animations
- AI
- user interfaces

The underlying idea remains the same.

---

# Common Misconceptions

### "State machines are complicated."

Not necessarily.

At their core, a simple state machine is just:

- an enum
- a variable
- some transitions
- behavior based on the current state

---

### "Every object needs a state machine."

No.

Some objects perform only one behavior.

State machines become useful when an object's behavior changes over time.

---

### "States replace all other programming techniques."

No.

State machines work alongside variables, signals, functions, and objects.

They are another tool for organizing software.

---

### "Once a state machine is built, it never changes."

As games evolve, new behaviors are often added.

A good state machine makes those additions easier instead of requiring the entire object to be redesigned.

---

# Reflection

Think about one of the games you've built.

Choose one object.

- What are its possible states?
- Which state does it begin in?
- What events cause it to change state?
- Which transitions should be prevented?

Can you sketch a simple state diagram before writing any code?

---

# Looking Back

This unit began with a simple question.

> **What information actually describes the current game?**

Along the way, we discovered that software needs more than variables.

Games need systems that:

- remember information
- own shared state
- communicate events
- organize changing behavior

Together, these ideas form the foundation of modern gameplay architecture.

Every game—from a simple platformer to a large open-world RPG—depends on these same principles.

The syntax will change from engine to engine.

The architectural ideas remain remarkably consistent.

---

# Looking Ahead

The next unit shifts our attention once again.

Our games now have memory, communication, and organized behavior.

The next challenge becomes teaching our games to **make decisions**.

How can objects choose *what* to do based on the world around them?