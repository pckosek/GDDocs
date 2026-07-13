# Pattern 2.11.8 — Count Objects Inside an Area

## Classification

**Type:** Gameplay Pattern

**Category:** Area Detection

**Difficulty:** Intermediate

**Prerequisites:**

- Area3D
- body_entered()
- body_exited()

---

# Problem

Sometimes gameplay depends not on a single event...

...but on **how many objects are currently inside an Area**.

Examples include:

- pressure plates
- capture zones
- puzzle switches
- enemy detection zones
- healing areas
- multiplayer objectives

Rather than reacting to one object entering or leaving, we want to continuously know:

> **How many objects are currently inside?**

---

# Starter Implementation

Create an **Area3D**.

Attach the following script.

```gdscript
extends Area3D

var occupants := 0

func _on_body_entered(body):

	occupants += 1

	print("Objects Inside:", occupants)

func _on_body_exited(body):

	occupants -= 1

	print("Objects Inside:", occupants)
```

Run the scene.

Walk into the Area.

Walk back out.

Observe.

The count increases when something enters and decreases when something leaves.

---

# How It Works

Every interaction changes the current count.

```text
Enter

↓

+1

↓

Exit

↓

-1
```

Instead of asking:

> "Did something happen?"

we begin asking:

> "What is the current state?"

---

# Anatomy

## body_entered()

Increases the count.

---

## body_exited()

Decreases the count.

---

## occupants

Stores how many objects currently occupy the Area.

---

# Design Principle

## Events change state.

Events are temporary.

State persists.

The signals:

```text
body_entered()

body_exited()
```

occur only once.

The variable:

```gdscript
occupants
```

remembers the result.

---

# Experiment

Only change one thing.

---

### Experiment A

Create two players (or two RigidBodies).

Walk both into the Area.

Observe.

---

### Experiment B

Remove one object.

Observe.

---

### Experiment C

Replace:

```gdscript
print(occupants)
```

with:

```gdscript
if occupants > 0:

	print("Area Occupied")
```

Observe.

---

### Experiment D

Require:

```gdscript
occupants >= 2
```

before printing.

Observe.

How could this become a cooperative puzzle?

---

### Experiment E

Push several RigidBodies into the Area.

Observe.

The Area doesn't care what entered.

It simply counts.

---

# Practical Applications

Counting occupants appears throughout games.

Examples include:

- pressure plates
- capture zones
- elevators
- enemy awareness
- puzzle rooms
- cooperative mechanics
- spawn control
- safe zones

Many gameplay systems care about **how many** objects are present rather than simply **whether** one entered.

---

# Common Misconceptions

### "body_entered() tells me how many objects are inside."

No.

It only reports one event.

You must maintain the count yourself.

---

### "The Area remembers the count."

No.

The Area reports events.

Your script stores the current state.

---

### "This only works for players."

Any compatible physics body can be counted.

---

# Workbench Habit

Whenever gameplay asks:

> **How many objects are inside this region?**

think in two parts.

Events update the count.

The variable stores the state.

Keeping those ideas separate makes gameplay systems much easier to reason about.

---

# Challenge

Build a simple pressure plate.

The door should only open when:

```gdscript
occupants >= 2
```

Experiment with:

- one player
- two crates
- one player and one crate

Notice that the gameplay depends entirely on the current count rather than any individual event.