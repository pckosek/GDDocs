# Pattern 2.11.9 — Require Multiple Objects Inside an Area

## Classification

**Type:** Gameplay Pattern

**Category:** Area Detection

**Difficulty:** Intermediate

**Prerequisites:**

- Count Objects Inside an Area
- body_entered()
- body_exited()

---

# Problem

Sometimes one object is not enough.

Examples include:

- two players standing on pressure plates
- several crates activating a switch
- multiple enemies entering a capture zone
- cooperative puzzles
- weighted platforms

Instead of asking:

> **Did something enter?**

we ask:

> **Are enough objects inside?**

---

# Starter Implementation

Create an **Area3D**.

Attach the following script.

```gdscript
extends Area3D

@export var required_objects := 2

var occupants := 0

func _on_body_entered(body):

	occupants += 1

	check_area()

func _on_body_exited(body):

	occupants -= 1

	check_area()

func check_area():

	if occupants >= required_objects:

		print("Activated!")

	else:

		print("Waiting...")
```

Run the scene.

Move objects into and out of the Area.

Observe.

The Area becomes active only when enough objects are present.

---

# How It Works

```text
Object Enters

↓

Occupants Increase

↓

Current Count Updated

↓

Requirement Checked

↓

Gameplay Decision
```

Notice that entering the Area does **not** immediately activate the system.

The current state determines the result.

---

# Anatomy

## body_entered()

Updates the current count.

---

## body_exited()

Keeps the count accurate.

---

## occupants

Stores the current number of objects inside.

---

## required_objects

Defines how many objects are needed.

---

## check_area()

Determines whether the gameplay condition has been satisfied.

---

# Design Principle

## Events update state.

State drives gameplay.

Rather than reacting to a single event, many systems continuously evaluate the current state of the world.

This is one of the first examples of gameplay emerging from accumulated information.

---

# Experiment

Only change one thing.

---

### Experiment A

Increase:

```gdscript
required_objects
```

to:

```gdscript
3
```

Observe.

---

### Experiment B

Push several RigidBodies into the Area.

Observe.

---

### Experiment C

Remove one object.

Observe.

Does the Area deactivate automatically?

---

### Experiment D

Replace:

```gdscript
print("Activated!")
```

with:

```gdscript
$Door.open()
```

(or another gameplay response)

Observe.

The counting logic remains unchanged.

Only the response changes.

---

### Experiment E

Create two independent Areas.

Give each a different:

```gdscript
required_objects
```

Observe.

Each puzzle now has its own activation rule.

---

# Practical Applications

This pattern appears throughout games.

Examples include:

- pressure plates
- weighted elevators
- cooperative switches
- multiplayer objectives
- puzzle rooms
- territory control
- ritual circles
- resource collection

Many gameplay systems depend on the current state of the world rather than a single event.

---

# Common Misconceptions

### "body_entered() should activate the puzzle."

Usually not.

The event updates the count.

The count determines the gameplay.

---

### "Only players should count."

Not necessarily.

Crates, balls, and other physics objects are often part of puzzle mechanics.

---

### "The count never changes."

Objects may leave the Area at any time.

Always update the count on both entry and exit.

---

# Workbench Habit

Whenever gameplay depends on **how many** objects satisfy a condition, think in three steps.

```text
Events

↓

Update State

↓

Evaluate Rule
```

Separating these ideas produces flexible gameplay systems that are easy to expand.

---

# Challenge

Build a simple puzzle room.

The exit door should only open when:

- two crates
- or two players
- or one player and one crate

occupy the pressure plate.

Experiment with different values for:

```gdscript
required_objects
```

Notice that changing a single variable dramatically changes the gameplay without changing the underlying pattern.