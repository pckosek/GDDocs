# 4.4.2 Create an Enum

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

We now know that objects can exist in different behavioral states.

For example, a player might be:

- Idle
- Walking
- Jumping
- Falling

But how should we represent those states in code?

We could write:

```gdscript
state = 0
```

But what does **0** mean?

Idle?

Walking?

Jumping?

The computer may understand numbers.

Humans do not.

Instead, we can give those values meaningful names.

Godot provides **Enums** for exactly this purpose.

---

# Why This Technique Matters

An **Enum** (short for *enumeration*) creates a named collection of related values.

Instead of remembering that:

```text
0 = Idle

1 = Walking

2 = Jumping

3 = Falling
```

our code can simply use:

```text
State.IDLE

State.WALKING

State.JUMPING

State.FALLING
```

The program behaves the same.

The code becomes much easier to read.

---

# Starter Implementation

Create an enumeration near the top of your script.

```gdscript
extends CharacterBody3D

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

The player now begins in the **Idle** state.

---

Later, changing state becomes much clearer.

```gdscript
current_state = State.JUMPING
```

Instead of assigning an unexplained number, the code now clearly communicates its intention.

---

# Dissecting the Code

This line:

```gdscript
enum State {
	IDLE,
	WALKING,
	JUMPING,
	FALLING
}
```

creates a list of named values.

Behind the scenes, Godot still assigns numbers.

```text
IDLE      → 0
WALKING   → 1
JUMPING   → 2
FALLING   → 3
```

Most of the time, however, we don't care about the numbers.

We care about the names.

The names make the code easier for people to read.

---

# Design Principle

## Name ideas, not numbers.

Programs are read far more often than they are written.

Meaningful names help other programmers—and your future self—understand what the code is doing.

Enums replace mysterious numbers with descriptive language.

---

# Experiment

Imagine reading these two lines.

```gdscript
current_state = 2
```

Now compare it with:

```gdscript
current_state = State.JUMPING
```

Which one is easier to understand?

Which one would you rather debug six months from now?

---

# Practical Observation

Enums work best when the possible values are limited and well-defined.

Good examples include:

- player movement states
- enemy AI states
- game difficulty
- weapon types
- menu screens
- traffic light colors

If you can list all the possible choices ahead of time, an enum is often a good solution.

---

# Common Misconceptions

### "Enums create new variables."

No.

An enum defines a collection of named values.

Variables store one of those values.

---

### "Enums replace strings."

Not exactly.

You could write:

```gdscript
current_state = "Jumping"
```

But enums reduce spelling mistakes and make code easier to maintain.

---

### "Enums are only for state machines."

No.

Enums can represent any small collection of related options.

Behavioral states are simply one common use.

---

### "The numbers inside an enum are important."

Usually not.

The names are what make enums valuable.

The numbers exist primarily for the computer.

---

# Reflection

Imagine creating an enum for each object below.

What values might it contain?

| Object | Possible Enum Values |
|----------|----------------------|
| Player | |
| Door | |
| Enemy | |
| Elevator | |
| Traffic Light | |

Now ask yourself:

Would numbers or descriptive names make those states easier to understand?

---

# Looking Ahead

Our states now have meaningful names.

The next challenge is remembering which one is currently active.

> **How can we keep track of an object's current state?**